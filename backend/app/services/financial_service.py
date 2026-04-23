
def calculate_metrics(price: float, expected_rent: float) -> dict:
	# ROI = (Annual Profit / Price) * 100
	annual_rent = expected_rent * 12
	annual_profit = annual_rent  # Assume no costs for simplicity; extend as needed
	roi = (annual_profit / price) * 100 if price else 0
	rental_yield = (expected_rent / price) * 100 if price else 0
	return {
		"annual_rent": annual_rent,
		"annual_profit": annual_profit,
		"roi": round(roi, 2),
		"rental_yield": round(rental_yield, 2),
	}
