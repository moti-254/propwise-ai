from __future__ import annotations

import os
from typing import List
from openai import AsyncOpenAI


class EmbeddingClient:
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
        )

        # Lightweight embedding model
        self.embedding_model = os.getenv(
            "EMBEDDING_MODEL",
            "openai/text-embedding-3-small"
        )

    async def embed(self, text: str) -> List[float]:
        if not text or not str(text).strip():
            raise ValueError("Cannot embed empty text")

        response = await self.client.embeddings.create(
            model=self.embedding_model,
            input=str(text)
        )

        return response.data[0].embedding


embedding_client = EmbeddingClient()


async def embed_text(text: str) -> List[float]:
    return await embedding_client.embed(text)