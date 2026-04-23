
"""
Production Data Ingestion Pipeline Orchestrator for PropWise AI (ChromaDB version)
"""

import logging
import asyncio
from app.ingestion.preprocess import DatasetPreprocessor
from app.vectorstore.ingestion import ingest_dataframe

logger = logging.getLogger(__name__)

RAW_DATASETS = [
    {
        "path": "backend/data/raw/nairobi.csv",
        "source": "nairobi",
    },
    {
        "path": "backend/data/raw/airbnb.csv",
        "source": "airbnb",
    },
    {
        "path": "backend/data/raw/usa_real_estate.csv",
        "source": "usa_real_estate",
    },
]

async def run_full_ingestion_pipeline():
    logger.info("Starting full ingestion pipeline (ChromaDB)...")
    preprocessor = DatasetPreprocessor()
    for dataset in RAW_DATASETS:
        df = preprocessor.preprocess(
            dataset["path"],
            dataset["source"],
        )
        await ingest_dataframe(df)
    logger.info("Ingestion pipeline completed successfully.")

# Optionally, schedule this pipeline
# from app.ingestion.scheduler import schedule_ingestion
# schedule_ingestion(lambda: asyncio.run(run_full_ingestion_pipeline()))
