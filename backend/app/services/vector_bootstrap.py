import os
import logging

# Always use the bootstrap ingestion for deployment
from app.ingestion.ingest_bootstrap import ingest_property_dataset

logger = logging.getLogger(__name__)

CHROMA_PATH = "backend/db/chroma_db"

async def initialize_vector_db():
    """
    Build vector DB if missing.
    """
    if os.path.exists(CHROMA_PATH) and os.listdir(CHROMA_PATH):
        logger.info("ChromaDB already exists.")
        return

    logger.info("ChromaDB missing. Starting ingestion bootstrap...")
    await ingest_property_dataset()
    logger.info("Vector DB bootstrap completed.")
