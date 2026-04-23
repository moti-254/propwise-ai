"""
API router registration for Propwise AI.
"""
from fastapi import APIRouter
from app.api.v1.endpoints.property import router as property_router

api_router = APIRouter()
api_router.include_router(property_router)
