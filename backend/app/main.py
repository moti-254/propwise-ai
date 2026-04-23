from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.settings import settings
from app.api.v1.routes import api_router


app = FastAPI(
    title="Property Investment Analyzer API",
    debug=settings.debug,
)

# CORS for frontend-backend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # local frontend
        "https://your-vercel-domain.vercel.app",  # production frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Vector DB bootstrap disabled: ChromaDB is now committed and persistent ---
# from app.services.vector_bootstrap import initialize_vector_db
#
# @app.on_event("startup")
# async def startup_event():
#     try:
#         await initialize_vector_db()
#         print("Vector DB initialized successfully")
#     except Exception as e:
#         print(f"Startup initialization failed: {e}")

# Health endpoint for Render
@app.get("/")
async def health_check():
    return {
        "status": "healthy",
        "service": "Property Investment Analyzer API"
    }

# API routes
app.include_router(api_router, prefix=settings.api_prefix)
