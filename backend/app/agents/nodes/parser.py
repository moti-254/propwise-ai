from typing import Dict, Any

from app.agents.state import AgentState


REQUIRED_FIELDS = ["price", "expected_rent", "location"]


def parser_node(state: AgentState) -> Dict[str, Any]:
	"""
	Input normalization + validation.
	"""

	missing = [
		field for field in REQUIRED_FIELDS
		if state.get(field) in [None, ""]
	]

	if missing:
		raise ValueError(f"Missing required fields: {', '.join(missing)}")

	try:
		price = float(state["price"])
		expected_rent = float(state["expected_rent"])
		location = str(state["location"]).strip()

		if price <= 0:
			raise ValueError("Price must be positive")

		if expected_rent <= 0:
			raise ValueError("Expected rent must be positive")

	except Exception as e:
		raise ValueError(f"Input validation failed: {e}")

	return {
		"property": {
			"price": price,
			"expected_rent": expected_rent,
			"location": location,
		}
	}
