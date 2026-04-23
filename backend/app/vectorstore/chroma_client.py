from __future__ import annotations

import chromadb
from chromadb.config import Settings

client = chromadb.PersistentClient(
    path="db/chroma_db"
)

property_collection = client.get_or_create_collection(
    name="property_market",
    metadata={"hnsw:space": "cosine"},
)
