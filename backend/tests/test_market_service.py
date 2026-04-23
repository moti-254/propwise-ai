import pytest
import asyncio
from app.services.market_service import fetch_market_comparables

@pytest.mark.asyncio
async def test_fetch_market_comparables():
    # Example property input (adjust values as needed for your test data)
    property_data = {
        "price": 180.0,
        "expected_rent": 10.0,
        "location": "Albany",
        "property_type": "Entire home",
        "bedrooms": 3,
        "bathrooms": 1,
        "square_feet": 100.0,
    }
    market, comparables = await fetch_market_comparables(property_data, top_k=3)
    assert isinstance(market, dict)
    assert "average_price" in market
    assert isinstance(comparables, list)
    assert len(comparables) > 0
    assert "price" in comparables[0]
    assert "location" in comparables[0]
    print("Market summary:", market)
    print("Comparables:", comparables)
