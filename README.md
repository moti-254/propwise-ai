
# Propwise AI – Property Investment Analyzer

Propwise AI is a full-stack, production-ready platform for AI-powered property investment analysis. It combines a modular FastAPI backend (multi-agent pipeline, vector search, LLMs) with a modern Next.js/Tailwind frontend dashboard.

---

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup & Quickstart](#setup--quickstart)
- [API Usage Example](#api-usage-example)
- [Data Ingestion Pipeline](#data-ingestion-pipeline)
- [Vector Database Bootstrapping](#vector-database-bootstrapping)
- [Testing](#testing)
- [Planned Improvements](#planned-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **AI-powered property analysis**: ROI, risk, market comparison, and investment decision
- **Multi-agent pipeline**: Modular nodes for parsing, financials, market RAG, risk, decision, and explanation
- **Vector search**: ChromaDB/pgvector for real-world property retrieval
- **LLM integration**: OpenRouter/OpenAI for reasoning and explanations
- **Modern SaaS dashboard**: KPI cards, charts, glassmorphism, responsive UI
- **API-first**: Clean REST endpoints, Pydantic schemas, async/await
- **Dockerized**: Easy deployment for backend and frontend
- **Comprehensive tests**: Pytest for backend, React Testing Library for frontend

---

## Architecture

```
┌────────────┐      ┌──────────────┐      ┌──────────────┐
│  Frontend  │ <--> │   FastAPI    │ <--> │ Vector DB    │
│  (Next.js) │      │  Backend     │      │ (ChromaDB)   │
└────────────┘      └──────────────┘      └──────────────┘
        │                  │                     │
        ▼                  ▼                     ▼
   User Input        Multi-Agent           Embeddings,
   Dashboard         Pipeline:             Metadata,
   (React UI)        Parse → Finance →     Search
                     Market → Risk →
                     Decision → Explain
```

---

## Project Structure

```
Propwise_AI/
├── backend/   # FastAPI app, pipeline, vectorstore, agents, tests
├── frontend/  # Next.js app, React components, dashboard UI
├── README.md
├── ...
```

---

## Prerequisites

- Python 3.10+
- Node.js 18+
- npm (or yarn/pnpm/bun)
- [ChromaDB](https://www.trychroma.com/) (auto-managed, no setup needed for dev)
- (Optional) Docker for containerized deployment

---

## Setup & Quickstart

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
cp .env.example .env  # Fill in your keys
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
cp .env.example .env.local  # Fill in your API URL
npm run dev
```

---

## API Usage Example

POST `/api/v1/analyze`

Request:
```json
{
  "price": 5000000,
  "expected_rent": 40000,
  "location": "Nairobi"
}
```

Response:
```json
{
  "metrics": {"roi": 12.0, ...},
  "decision": {"verdict": "Good Investment", ...},
  "explanation": "..."
}
```

---

## Data Ingestion Pipeline

The backend includes a robust ingestion pipeline for transforming raw property datasets into vector embeddings for semantic search and analytics.

**How it works:**
1. Place raw CSVs in `backend/data/raw/` or `backend/data/bootstrap/`.
2. Preprocessing, validation, and enrichment are handled by `preprocess.py` and `validators.py`.
3. Embeddings are generated using the configured model (OpenRouter/OpenAI).
4. Vectors and metadata are stored in ChromaDB for fast search.

**Usage:**
- For quick dev/demo: `python -m app.ingestion.ingest_bootstrap` (small sample dataset)
- For full production ingestion: `python -m app.ingestion.run_ingestion` (all real datasets)
- The main pipeline logic is in `app/ingestion/pipeline.py` and can be scheduled with `app/ingestion/scheduler.py`.

**Best Practices:**
- Use small datasets for local/dev bootstrapping.
- Use full ingestion for production.
- Control vector DB bootstrapping with the `RUN_VECTOR_BOOTSTRAP` environment variable.
- See `backend/app/ingestion/README.md` for more details.

---

## Vector Database Bootstrapping

- **ChromaDB is not stored in Git**. On deployment, the backend automatically rebuilds the vector DB if missing.
- A small, clean sample dataset is tracked in `backend/data/bootstrap/` (e.g. `nairobi_sample.csv`).
- On startup, FastAPI runs a bootstrap routine (`initialize_vector_db`) that:
  - Checks if ChromaDB exists in `backend/db/chroma_db/`
  - If missing, ingests the sample dataset and rebuilds embeddings
- This ensures deployments (e.g. Render, Vercel) always have a working vector DB, even with ephemeral filesystems.
- Large raw datasets and ChromaDB binaries are gitignored for fast, safe deploys.

**To add more data:**
- Place additional small CSVs in `backend/data/bootstrap/` and update `BOOTSTRAP_DATASETS` in `app/ingestion/ingest_bootstrap.py`.
- For production-scale data, migrate to an external object store or production vector DB.

---

## Frontend Features

- Modern dashboard (Next.js, Tailwind, Recharts, Lucide icons)
- Property input form with validation and animated loading
- KPI cards, risk panel, decision verdict, and charts
- Responsive, glassmorphism UI

---

## Backend Features

- FastAPI async API
- LangGraph multi-agent pipeline
- ChromaDB/pgvector vector search
- OpenRouter/OpenAI LLM integration
- Modular, testable nodes
- Centralized prompts
- Logging, error handling, request IDs

---

## Testing

- Backend: `pytest` (unit + integration)
- Frontend: `npm test` (React Testing Library)

---

## Planned Improvements

- User authentication & saved analyses
- Admin dashboard for managing properties
- More granular risk analysis (e.g. location crime, market volatility)
- PDF/CSV export of analysis reports
- Real-time property data ingestion (web scraping, APIs)
- Multi-language support
- Mobile-first UI improvements
- Enhanced charting and analytics
- Integration with real estate APIs (Zillow, local MLS)
- Subscription/paywall for premium features
- AI chat assistant for property Q&A

---

## Deployment Notes

- Use Docker for production deployments. Both backend and frontend have Dockerfiles.
- Environment variables must be set for API keys, DB paths, etc. See `.env.example` files in each app.
- For cloud deploys (Render, Vercel, etc.), ensure persistent storage for ChromaDB or use external DB.

---

## Contributing

Pull requests welcome! Please open issues for bugs or feature requests.

---

## License

MIT

---

## Frontend Features

- Modern dashboard (Next.js, Tailwind, Recharts, Lucide icons)
- Property input form with validation and animated loading
- KPI cards, risk panel, decision verdict, and charts
- Responsive, glassmorphism UI

---

## Backend Features

- FastAPI async API
- LangGraph multi-agent pipeline
- ChromaDB/pgvector vector search
- OpenRouter/OpenAI LLM integration
- Modular, testable nodes
- Centralized prompts
- Logging, error handling, request IDs

---

## Testing

- Backend: `pytest` (unit + integration)
- Frontend: `npm test` (React Testing Library)

---

## Planned Future Improvements

- User authentication & saved analyses
- Admin dashboard for managing properties
- More granular risk analysis (e.g. location crime, market volatility)
- PDF/CSV export of analysis reports
- Real-time property data ingestion (web scraping, APIs)
- Multi-language support
- Mobile-first UI improvements
- Enhanced charting and analytics
- Integration with real estate APIs (Zillow, local MLS)
- Subscription/paywall for premium features
- AI chat assistant for property Q&A

---

## Vector Database Bootstrapping (Deployment-Ready)

- **ChromaDB is not stored in Git**. On deployment, the backend automatically rebuilds the vector DB if missing.
- A small, clean sample dataset is tracked in `backend/data/bootstrap/` (e.g. `nairobi_sample.csv`).
- On startup, FastAPI runs a bootstrap routine (`initialize_vector_db`) that:
  - Checks if ChromaDB exists in `backend/db/chroma_db/`
  - If missing, ingests the sample dataset and rebuilds embeddings
- This ensures deployments (e.g. Render, Vercel) always have a working vector DB, even with ephemeral filesystems.
- Large raw datasets and ChromaDB binaries are gitignored for fast, safe deploys.

**To add more data:**
- Place additional small CSVs in `backend/data/bootstrap/` and update `BOOTSTRAP_DATASETS` in `app/ingestion/ingest_bootstrap.py`.
- For production-scale data, migrate to an external object store or production vector DB (see README for options).

---

## Contributing

Pull requests welcome! Please open issues for bugs or feature requests.

---

## License

MIT
