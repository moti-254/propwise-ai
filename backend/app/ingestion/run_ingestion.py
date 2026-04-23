
import asyncio
from app.ingestion.preprocess import DatasetPreprocessor
from app.vectorstore.ingestion import ingest_dataframe

RAW_DATASETS = [
    {
        "path": "data/raw/nairobi.csv",
        "source": "nairobi",
    },
    {
        "path": "data/raw/airbnb.csv",
        "source": "airbnb",
    },
    {
        "path": "data/raw/usa_real_estate.csv",
        "source": "usa_real_estate",
    },
]


async def run():
    preprocessor = DatasetPreprocessor()
    for dataset in RAW_DATASETS:
        df = preprocessor.preprocess(
            dataset["path"],
            dataset["source"],
        )
        # Limit to first 20 rows for faster dev/test
        df = df.head(20)
        await ingest_dataframe(df)

if __name__ == "__main__":
    asyncio.run(run())
