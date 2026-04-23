from __future__ import annotations

from app.integrations.embedding_client import embed_text
from app.vectorstore.chroma_client import property_collection

async def query_similar_properties(
    query_text: str,
    top_k: int = 5,
):
    embedding = await embed_text(query_text)
    results = property_collection.query(
        query_embeddings=[embedding],
        n_results=top_k,
    )
    return results
