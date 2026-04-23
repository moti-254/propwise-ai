from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.core.settings import settings
from app.api.v1.routes import api_router

app = FastAPI(debug=settings.debug, title="Property Investment Analyzer API")

# CORS for frontend-backend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all versioned routers
app.include_router(api_router, prefix=settings.api_prefix)
