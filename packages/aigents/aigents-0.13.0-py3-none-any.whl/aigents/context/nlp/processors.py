import gc
import logging
import asyncio
from typing import List

import spacy
import numpy as np
import pandas as pd

import google.generativeai as genai
from aigents import (
    OpenAIChatter,
    AsyncOpenAIChatter,
    GoogleChatter
)
from aigents.constants import (
    MODELS,
    MODELS_EMBEDDING,
    EMBEDDINGS_COLUMNS,
)
from aigents.utils import get_encoding, run_async

from .base import BaseTextProcessor
from .utils import clean_text, deep_clean
from .errors import ProcessingError


logger = logging.getLogger('aigents')


class TextProcessor(BaseTextProcessor):
    def __init__(self, *args, pipeline: str = None, **kwargs):
        """
        A text processing class that inherits from BaseTextProcessor.

        Parameters:
        - *args: Variable length argument list.
        - pipeline (str, optional): The spaCy pipeline to use for text
            processing.

        Attributes:
        - text (str): The input text.
        - sequences (list): A list of sentences obtained by splitting the text.
        - chunks (list): A list of chunks obtained by grouping sentences
            based on the maximum number of tokens.
        - n_tokens (list): A list of token counts for each chunk.
        - segments (list): A list of semantically grouped segments.
        - dataframe (pd.DataFrame): A DataFrame containing chunks and their
        corresponding token counts.

        Methods:
        - split(self, text) -> np.ndarray:
            Split the input text into sentences.

        - to_chunks(self, text: str = None, model: str = MODELS[1],
            max_tokens: int = 100) -> List[str]:
            Group sentences semantically with a maximum number of tokens.

        - group_by_semantics(self, data: str | List[str] = None,
                            model: str = MODELS[1], max_tokens: int = 100,
                            threshold: float = 0.8) -> List[str]:
            Group chunks by semantics based on spaCy similarity.

        - to_dataframe(self, data: str | List[str] = None,
                        model: str = MODELS[1], max_tokens: int = 120,
                        threshold: float = 0.8) -> pd.DataFrame:
            Convert chunks and token counts to a pandas DataFrame.

        - embeddings(self, data: str | List[str] | pd.DataFrame = None,
                    model: str = MODELS[1], max_tokens: int = 120,
                    threshold: float = .8, openai_key=None,
                    openai_organization=None) -> pd.DataFrame:
            Obtain embeddings for chunks using OpenAI API.

        - async_embeddings(self, data: str | List[str] | pd.DataFrame = None,
                            model: str = MODELS[1], max_tokens: int = 120,
                            threshold: float = .8,
                            openai_key=None,
                            openai_organization=None,
                            **kwargs) -> pd.DataFrame:
            Asynchronously obtain embeddings for chunks using OpenAI API.

        """
        super().__init__(*args, pipeline=pipeline, **kwargs)

    def split(self,
              text,
              clean=True,
              deep_clean_=True,
              language="english",
              n_grams_number=20,
              n_grams_tolerance=2) -> List[str]:
        self.text = text
        if clean:
            self.text = clean_text(self.text)
            if deep_clean_:
                self.text = deep_clean(
                    self.text,
                    language=language,
                    n_grams_number=n_grams_number,
                    n_grams_tolerance=n_grams_tolerance
                )
        self.doc = self.nlp(self.text)
        self.sequences = [sent.text for sent in self.doc.sents]
        return self.sequences

    def to_chunks(self,
                  text: str = None,
                  model: str = MODELS[0],
                  max_tokens: int = 100,
                  clean=True,
                  deep_clean_=True,
                  language="english",
                  n_grams_number=20,
                  n_grams_tolerance=2) -> List[str]:
        if text is not None:
            self.split(
                text,
                clean=clean,
                deep_clean_=deep_clean_,
                language=language,
                n_grams_number=n_grams_number,
                n_grams_tolerance=n_grams_tolerance,
            )
        # group sentences semantically with a maximum number of tokens
        # using tiktoken to compute tokens
        # example maximum number of tokens
        chunks = []
        tokens = []
        current_chunk = []
        current_tokens = 0
        encoding = get_encoding(model)

        def split_sentence_into_chunks(sentence, max_tokens):
            encoded_sentence = encoding.encode(sentence)
            if len(encoded_sentence) <= max_tokens:
                return [sentence]
            else:
                words = sentence.split()
                sub_chunks = []
                current_sub_chunk = []
                current_sub_tokens = 0
                for word in words:
                    encoded_word = encoding.encode(word + ' ')
                    if current_sub_tokens + len(encoded_word) <= max_tokens:
                        current_sub_chunk.append(word)
                        current_sub_tokens += len(encoded_word)
                    else:
                        sub_chunks.append(' '.join(current_sub_chunk))
                        current_sub_chunk = [word]
                        current_sub_tokens = len(encoded_word)
                if current_sub_chunk:
                    sub_chunks.append(' '.join(current_sub_chunk))
                return sub_chunks

        for sentence in self.sequences:
            sentence_chunks = split_sentence_into_chunks(sentence, max_tokens)
            for chunk in sentence_chunks:
                encoded_chunk = encoding.encode(chunk + ' ')
                if current_tokens + len(encoded_chunk) <= max_tokens:
                    current_chunk.append(chunk)
                    current_tokens += len(encoded_chunk)
                else:
                    chunks.append(' '.join(current_chunk))
                    tokens.append(current_tokens)
                    current_chunk = [chunk]
                    current_tokens = len(encoded_chunk)

        if current_chunk:
            chunks.append(' '.join(current_chunk))
            tokens.append(current_tokens)
        self.chunks = chunks
        self.n_tokens = tokens
        return chunks

    def group_by_semantics(self,
                           data: str | List[str] = None,
                           model: str = MODELS[0],
                           max_tokens: int = 100,
                           threshold: float = 0.8,
                           clean=True,
                           deep_clean_=True,
                           language="english",
                           n_grams_number=20,
                           n_grams_tolerance=2) -> List[str]:
        
        if data is not None:
            if isinstance(data, list):
                if not self.n_tokens:
                    encoding = get_encoding(model)
                    self.n_tokens = [
                        len(encoding.encode(chunk)) for chunk in data
                    ]
                self.chunks = data
            else:
                self.to_chunks(
                    text=data,
                    model=model,
                    max_tokens=max_tokens,
                    clean=clean,
                    deep_clean_=deep_clean_,
                    language=language,
                    n_grams_number=n_grams_number,
                    n_grams_tolerance=n_grams_tolerance,
                )
        
        docs = [self.nlp(sentence) for sentence in self.chunks]
        segments = []
        start_idx = 0
        end_idx = 1
        if len(self.chunks) == 0:
            raise ProcessingError(
                "Document can't be processed: content is too short"
            )
        segment = [self.chunks[start_idx]]
        while end_idx < len(docs):
            if docs[start_idx].similarity(docs[end_idx]) >= threshold:
                segment.append(docs[end_idx].text)
            else:
                segments.append(" ".join(segment))
                start_idx = end_idx
                segment = [self.chunks[start_idx]]
            end_idx += 1
        if segment:
            segments.append(" ".join(segment))
        self.segments = segments
        return segments

    def to_dataframe(self,
                     data: str | List[str] = None,
                     model: str = MODELS[0],
                     max_tokens: int = 120,
                     threshold: float = 0.8,
                     clean=True,
                     deep_clean_=True,
                     language="english",
                     n_grams_number=20,
                     n_grams_tolerance=2) -> pd.DataFrame:
        if data is not None:
            self.group_by_semantics(
                data=data,
                model=model,
                max_tokens=max_tokens,
                threshold=threshold,
                clean=clean,
                deep_clean_=deep_clean_,
                language=language,
                n_grams_number=n_grams_number,
                n_grams_tolerance=n_grams_tolerance,
            )

        chunks = self.chunks
        n_tokens = self.n_tokens
        self.dataframe = pd.DataFrame({'chunks': chunks, 'n_tokens': n_tokens})
        return self.dataframe

    def embeddings(self,
                   data: str | List[str] | pd.DataFrame = None,
                   model: str = MODELS[0],
                   max_tokens: int = 120,
                   threshold: float = .8,
                   api_key=None,
                   organization=None,
                   embedding_model='openai',
                   clean=True,
                   deep_clean_=True,
                   language="english",
                   n_grams_number=20,
                   n_grams_tolerance=2) -> pd.DataFrame:
        if data is not None and not isinstance(data, pd.DataFrame):
            self.to_dataframe(
                data=data,
                model=model,
                max_tokens=max_tokens,
                threshold=threshold,
                clean=clean,
                deep_clean_=deep_clean_,
                language=language,
                n_grams_number=n_grams_number,
                n_grams_tolerance=n_grams_tolerance,
            )

        embeddings = []
        def create_embedding(row):
            if 'openai' in embedding_model.lower():
                client = OpenAIChatter(
                    api_key=api_key, organization=organization
                ).client
                embedding = client.embeddings.create(
                    input=row[EMBEDDINGS_COLUMNS[0]],
                    model=MODELS_EMBEDDING[0]
                )
                return embedding.data[0].embedding
            if 'gemini' in embedding_model.lower():
                # NOTE: GoogleChatter is called only for setting credentials 
                GoogleChatter(api_key=api_key)
                embedding = genai.embed_content(
                    model=MODELS_EMBEDDING[-2],
                    content=row[EMBEDDINGS_COLUMNS[0]],
                    task_type='SEMANTIC_SIMILARITY'
                )
                return embedding['embedding']
            raise ValueError(
                "`embeddings` only supports `openai` or `gemini` models"
            )


        for _, row in self.dataframe.iterrows():
            embeddings.append(create_embedding(row))

        self.dataframe[EMBEDDINGS_COLUMNS[2]] = embeddings

        return self.dataframe

    async def async_embeddings(self,
                               data: str | List[str] | pd.DataFrame = None,
                               model: str = MODELS[0],
                               max_tokens: int = 120,
                               threshold: float = .8,
                               api_key=None,
                               organization=None,
                               embedding_model='openai',
                               clean=True,
                               deep_clean_=True,
                               language="english",
                               n_grams_number=20,
                               n_grams_tolerance=2,
                               **kwargs) -> pd.DataFrame:
        if data is not None:
            self.to_dataframe(
                data=data,
                model=model,
                max_tokens=max_tokens,
                threshold=threshold,
                clean=clean,
                deep_clean_=deep_clean_,
                language=language,
                n_grams_number=n_grams_number,
                n_grams_tolerance=n_grams_tolerance,
            )

        if 'gemini' in embedding_model.lower():
            GoogleChatter(api_key=api_key)
        tasks = []
        async def create_embedding_openai(row):
            
            client = AsyncOpenAIChatter(
                api_key=api_key,
                organization=organization,
            ).client
            embedding = await client.embeddings.create(
                input=row[EMBEDDINGS_COLUMNS[0]],
                model=MODELS_EMBEDDING[0]
            )
            return embedding.data[0].embedding
        
        def create_embedding_gemini(row):
            # NOTE: GoogleChatter is called only for setting credentials 
            try:
                embedding = genai.embed_content(
                    model=MODELS_EMBEDDING[-2],
                    content=row[EMBEDDINGS_COLUMNS[0]],
                    task_type='SEMANTIC_SIMILARITY'
                )
            except ValueError as err:
                logger.debug(row[EMBEDDINGS_COLUMNS[0]])
                raise err
            return embedding['embedding']

        for _, row in self.dataframe.iterrows():
            if 'openai' in embedding_model.lower():
                tasks.append(create_embedding_openai(row))
            if 'gemini' in embedding_model.lower():
                tasks.append(
                    asyncio.create_task(
                        asyncio.to_thread(create_embedding_gemini, row)
                    )
                )
            # allow some of the tasks time to start
            await asyncio.sleep(0.1)
        
        self.dataframe[EMBEDDINGS_COLUMNS[2]] = await asyncio.gather(*tasks)

        return self.dataframe


def naive_split(
    text: str, minimal_length: int = 50, separator: str = '. ',
) -> list[str]:
    """
    Split a text into sentences.

    Parameters:
    - text (str): The input text.
    - minimal_length (int, optional): The minimum length of a sentence.

    Returns:
    list[str]: A list of sentences.
    """
    sentences = []
    for sentence in text.split(separator):
        if len(sentence) > minimal_length:
            sentences.append(sentence)
    return sentences

def naive_token_splitter(
    text: str,
    model: str = MODELS[0],
    max_tokens: int = 500,
    minimal_length: int = 50,
    separator: str = '. ',
    simple_split: bool = False,
):
    """
    Split a text into tokens.

    Parameters:
    - text (str): The input text.
    - model (str, optional): The model to use for tokenization.
    - max_tokens (int, optional): The maximum number of tokens per chunk.
    - minimal_length (int, optional): The minimum length of a sentence.

    Returns:
    pd.DataFrame: The tokenized data.
    """
    encoding = get_encoding(model)

    sentences = naive_split(text, minimal_length=minimal_length, separator=separator)
    n_tokens = [
        len(encoding.encode(" " + sentence)) for sentence in sentences
    ]

    total_tokens = 0
    chunks = []
    tokens = []
    chunk = []

    # if model == MODELS[1]:  # note: future models may require this to change
    if True:  # note: future models may require this to change
        for sentence, n_token in zip(sentences, n_tokens):
            if simple_split:
                chunks.append(sentence)
                tokens.append(n_token)
                continue

            if total_tokens + n_token > max_tokens and chunk:
                chunks.append(". ".join(chunk) + ".")
                tokens.append(total_tokens)
                chunk = []
                total_tokens = 0

            if n_token > max_tokens:
                continue

            chunk.append(sentence)
            total_tokens += n_token + 1

        array = np.array([chunks, tokens]).T
        data = pd.DataFrame(array, columns=(
            EMBEDDINGS_COLUMNS[0], EMBEDDINGS_COLUMNS[1],)
        )
        data[EMBEDDINGS_COLUMNS[1]] = data[EMBEDDINGS_COLUMNS[1]].astype('int')
        return data
    
    raise NotImplementedError(  # TODO choose another error
        f"number_of_tokens() is not presently implemented for model {model}. "
        "See https://github.com/openai/openai-python/blob/main/chatml.md for "
        "information on how messages are converted to tokens."
        ""
    )

def naive_text_to_embeddings(
        text: str,
        model: str = MODELS[0],
        max_tokens: int = 500,
        api_key=None,
        organization=None,
        separator: str = '. ',
        minimal_length: int = 50,
        simple_split: bool = False,
        **kwargs
):
    processor = TextProcessor()
    processor.dataframe = naive_token_splitter(
        text, model, max_tokens, minimal_length, separator, simple_split
    )
    return processor.embeddings(
        model=model,
        api_key=api_key,
        organization=organization,
        **kwargs
    )

async def naive_text_to_embeddings_async(
        text: str,
        model: str = MODELS[0],
        max_tokens: int = 500,
        api_key=None,
        organization=None,
        separator: str = '. ',
        minimal_length: int = 50,
        simple_split: bool = False,
        **kwargs
):
    processor = TextProcessor()
    processor.dataframe = naive_token_splitter(
        text, model, max_tokens, minimal_length, separator, simple_split
    )
    embeddings = await processor.async_embeddings(
        model=model,
        api_key=api_key,
        organization=organization,
        **kwargs
    )
    del processor
    gc.collect()
    return embeddings


def create_embeddings(text: str,
                      pipeline: str = "en_core_web_md") -> List[float]:
    """
    Create text embeddings for the given input text.

    NOTE: This uses word vectors model, which are lexical types, meaning that
          if you have a list of terms with no context around them,
          this function suffices for similarity tests, e.g., in test cases.
          But for similarity against a context, such as whole paragraphs or
          texts, the return data will only provide a very rough approximation
          of what the text is about.
          (see https://spacy.io/usage/embeddings-transformers)

    Parameters:
    - text (str): The input text.

    Returns:
    List[float]: A list of floats representing the text embeddings.
    """
    nlp = spacy.load(pipeline)
    doc = nlp(text)
    # Average the word vectors to get the text embedding
    text_embedding = [token.vector for token in doc if token.has_vector]
    if text_embedding:
        return sum(text_embedding) / len(text_embedding)
    return []
