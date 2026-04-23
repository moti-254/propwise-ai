from __future__ import annotations

import uuid
import pandas as pd
from app.integrations.embedding_client import embed_text
from app.vectorstore.chroma_client import property_collection

async def ingest_dataframe(df: pd.DataFrame):
    for _, row in df.iterrows():
        embedding_text = str(row.get("embedding_text", "") or "")
        embedding = await embed_text(embedding_text)
        property_collection.add(
            ids=[str(uuid.uuid4())],
            embeddings=[embedding],
            documents=[embedding_text],
            metadatas=[
                {
                    "location": str(row.get("location", "") or ""),
                    "price": float(row.get("price") or 0),
                    "expected_rent": float(row.get("expected_rent") or 0),
                    "property_type": str(row.get("property_type", "") or ""),
                    "bedrooms": float(row.get("bedrooms") or 0),
                    "bathrooms": float(row.get("bathrooms") or 0),
                    "square_feet": float(row.get("square_feet") or 0),
                    "rental_yield": float(row.get("rental_yield") or 0),
                    "price_per_sqft": float(row.get("price_per_sqft") or 0),
                    "source": str(row.get("source", "") or ""),
                }
            ],
        )
