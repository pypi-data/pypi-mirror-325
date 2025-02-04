from dataclasses import dataclass
from typing import List

import numpy as np
from numpy.typing import NDArray
from openai import OpenAI

from openaivec.util import map_unique_minibatch

__ALL__ = ["EmbeddingOpenAI"]


@dataclass(frozen=True)
class EmbeddingOpenAI:
    client: OpenAI
    model_name: str

    def embed(self, sentences: List[str]) -> List[NDArray[np.float32]]:
        responses = self.client.embeddings.create(input=sentences, model=self.model_name)
        return [np.array(d.embedding, dtype=np.float32) for d in responses.data]

    def embed_minibatch(self, sentences: List[str], batch_size: int) -> List[NDArray[np.float32]]:
        return map_unique_minibatch(sentences, batch_size, self.embed)
