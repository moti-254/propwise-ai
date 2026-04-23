import asyncio
from app.ingestion.preprocess import DatasetPreprocessor
from app.vectorstore.ingestion import ingest_dataframe

BOOTSTRAP_DATASETS = [
    {
        "path": "data/bootstrap/nairobi_sample.csv",
        "source": "nairobi_sample",
    },
]

async def ingest_property_dataset():
    preprocessor = DatasetPreprocessor()
    for dataset in BOOTSTRAP_DATASETS:
        df = preprocessor.preprocess(
            dataset["path"],
            dataset["source"],
        )
        await ingest_dataframe(df)

if __name__ == "__main__":
    asyncio.run(ingest_property_dataset())
