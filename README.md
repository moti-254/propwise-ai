# Propwise AI – Property Investment Analyzer

A full-stack, production-ready platform for AI-powered property investment analysis. Combines a modular FastAPI backend (with multi-agent pipeline, vector search, and LLMs) and a premium Next.js/Tailwind frontend dashboard.

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

## Project Structure

```
Propwise_AI/
├── backend/   # FastAPI app, pipeline, vectorstore, agents, tests
├── frontend/  # Next.js app, React components, dashboard UI
├── .gitignore
```

---

## Quickstart

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
cp .env.example .env  # Fill in your keys
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
cp .env.example .env.local  # Fill in your API URL
npm run dev
```

---

## API Example

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

## Contributing

Pull requests welcome! Please open issues for bugs or feature requests.

---

## License

MIT
