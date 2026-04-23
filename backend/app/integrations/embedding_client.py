from __future__ import annotations

from typing import List
from sentence_transformers import SentenceTransformer

class EmbeddingClient:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    async def embed(self, text: str) -> List[float]:
        if not text or not str(text).strip():
            raise ValueError("Cannot embed empty text")
        return self.model.encode(str(text)).tolist()

embedding_client = EmbeddingClient()

async def embed_text(text: str) -> List[float]:
    return await embedding_client.embed(text)