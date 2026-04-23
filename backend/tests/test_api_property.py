import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_property_success():
    payload = {
        "price": 10000000,
        "expected_rent": 80000,
        "location": "Nairobi",
        "property_type": "apartment",
        "bedrooms": 3
    }
    response = client.post("/api/v1/property/analyze", json=payload)
    print("API Response:", response.json()) 
    assert response.status_code == 200
    data = response.json()
    assert "metrics" in data
    assert "decision" in data
    assert "explanation" in data
    assert data["property"]["location"] == "Nairobi"

def test_analyze_property_invalid_price():
    payload = {
        "price": 1e12,  # Too high
        "expected_rent": 80000,
        "location": "Nairobi"
    }
    response = client.post("/api/v1/property/analyze", json=payload)
    print("API Response:", response.json()) 
    assert response.status_code == 400
    assert "unreasonably high" in response.text
