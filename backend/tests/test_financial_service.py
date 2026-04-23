from app.services.financial_service import calculate_metrics

def test_calculate_metrics():
	price = 1000000
	expected_rent = 10000
	metrics = calculate_metrics(price, expected_rent)
	assert metrics["annual_rent"] == 120000
	assert metrics["annual_profit"] == 120000
	assert metrics["roi"] == 12.0
	assert metrics["rental_yield"] == 1.0
