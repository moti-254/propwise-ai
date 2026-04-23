import pandas as pd
import numpy as np
from app.ingestion.schema_mapper import map_columns

class DatasetPreprocessor:
    def __init__(self):
        pass

    def preprocess(self, file_path: str, source_name: str):
        df = pd.read_csv(file_path)
        df = map_columns(df)
        df = self.standardize_columns(df)
        df = self.create_derived_features(df)
        df["source"] = source_name
        df = self.build_embedding_text(df)
        return df

    def standardize_columns(self, df):
        required_cols = [
            "price",
            "location",
            "bedrooms",
            "bathrooms",
            "square_feet",
            "expected_rent",
            "property_type",
            "latitude",
            "longitude",
            "listing_description",
        ]
        for col in required_cols:
            if col not in df.columns:
                df[col] = None
        return df

    def create_derived_features(self, df):
        df["price"] = pd.to_numeric(df["price"], errors="coerce")
        df["expected_rent"] = pd.to_numeric(df["expected_rent"], errors="coerce")
        df["square_feet"] = pd.to_numeric(df["square_feet"], errors="coerce")
        df["price_per_sqft"] = np.where(
            (df["price"].notna()) & (df["square_feet"].notna()),
            df["price"] / df["square_feet"],
            None,
        )
        df["rental_yield"] = np.where(
            (df["expected_rent"].notna()) & (df["price"].notna()),
            ((df["expected_rent"] * 12) / df["price"]) * 100,
            None,
        )
        return df

    def build_embedding_text(self, df):
        df["embedding_text"] = (
            df["bedrooms"].astype(str)
            + " bedroom "
            + df["property_type"].astype(str)
            + " in "
            + df["location"].astype(str)
            + " priced at "
            + df["price"].astype(str)
        )
        return df
