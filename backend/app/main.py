from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


from app.core.settings import settings
from app.api.v1.routes import api_router
from app.services.vector_bootstrap import initialize_vector_db

app = FastAPI(
    title="Property Investment Analyzer API",
    debug=settings.debug,
)

# CORS for frontend-backend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",  # Allow all origins for development; restrict in production
        "http://localhost:3000",  # local frontend
        "https://your-vercel-domain.vercel.app",# production frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Conditional Vector DB Bootstrap ---
import os
@app.on_event("startup")
async def startup_event():
    bootstrap_enabled = os.getenv("RUN_VECTOR_BOOTSTRAP", "false").lower()
    if bootstrap_enabled == "true":
        print("[Startup] Running vector DB bootstrap...")
        await initialize_vector_db()
        print("[Startup] Vector DB bootstrap complete.")

# Health endpoint for Render
@app.get("/")
async def health_check():
    return {
        "status": "healthy",
        "service": "Property Investment Analyzer API"
    }

# API routes
app.include_router(api_router, prefix=settings.api_prefix)
