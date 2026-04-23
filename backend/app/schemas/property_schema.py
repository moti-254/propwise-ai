from pydantic import BaseModel
from typing import Optional

class UnifiedPropertySchema(BaseModel):
    property_id: Optional[str] = None
    location: Optional[str] = None
    sub_location: Optional[str] = None
    price: Optional[float] = None
    expected_rent: Optional[float] = None
    property_type: Optional[str] = None
    bedrooms: Optional[float] = None
    bathrooms: Optional[float] = None
    square_feet: Optional[float] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    listing_description: Optional[str] = None
    source: Optional[str] = None
    rental_yield: Optional[float] = None
    price_per_sqft: Optional[float] = None
    embedding_text: Optional[str] = None
