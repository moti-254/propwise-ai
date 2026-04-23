"""
Request schema for property analysis.
"""
from pydantic import BaseModel, Field
from typing import Optional

class PropertyAnalysisRequest(BaseModel):
    """
    Request model for analyzing a property investment opportunity.
    """
    price: float = Field(..., gt=0, description="Property price in local currency.")
    expected_rent: float = Field(..., gt=0, description="Expected monthly rent.")
    location: str = Field(..., description="Property location (city or area).")
    property_type: Optional[str] = Field("apartment", description="Type of property.")
    bedrooms: Optional[int] = Field(None, description="Number of bedrooms.")
