"""
Response schema for property analysis.
"""
from pydantic import BaseModel, Field
from typing import Dict, List, Any

class PropertyAnalysisResponse(BaseModel):
    """
    Response model for property analysis results.
    """
    property: Dict[str, Any] = Field(..., description="Input property details.")
    metrics: Dict[str, Any] = Field(..., description="Calculated financial metrics.")
    market: Dict[str, Any] = Field(..., description="Market data for the property location.")
    comparables: List[Dict[str, Any]] = Field(..., description="Comparable properties.")
    risk: Dict[str, Any] = Field(..., description="Risk assessment results.")
    decision: Dict[str, Any] = Field(..., description="Investment decision and score.")
    explanation: str = Field(..., description="User-facing explanation of the analysis.")
