# Ingestion Scripts Overview

This project provides two main ingestion scripts for building your ChromaDB vector store:

## 1. ingest_bootstrap.py
- **Purpose:** Minimal, fast bootstrapping for development, testing, or demo environments.
- **Dataset:** Ingests a small sample dataset (`data/bootstrap/nairobi_sample.csv`).
- **When to use:**
  - You want a quick setup for local development or demos.
  - You do NOT need the full production dataset.
- **How to run:**
  ```sh
  python -m app.ingestion.ingest_bootstrap
  ```

## 2. run_ingestion.py
- **Purpose:** Full ingestion of all real/raw datasets for production or comprehensive local testing.
- **Datasets:** Ingests multiple, larger datasets (e.g., `data/raw/nairobi.csv`, `data/raw/airbnb.csv`, `data/raw/usa_real_estate.csv`).
- **When to use:**
  - You want to build a complete, production-ready vector DB.
  - You want all available data indexed for search/analysis.
- **How to run:**
  ```sh
  python -m app.ingestion.run_ingestion
  ```

---

**Best Practice:**
- Use `ingest_bootstrap.py` for quick dev/test cycles.
- Use `run_ingestion.py` for production or when you need all data.
- Both scripts can be extended or customized as your data sources grow.

---

For more details, see the code in `app/ingestion/ingest_bootstrap.py` and `app/ingestion/run_ingestion.py`.
