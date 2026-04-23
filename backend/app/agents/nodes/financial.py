from typing import Dict, Any

from app.agents.state import AgentState
from app.services.financial_service import calculate_metrics


def financial_node(state: AgentState) -> Dict[str, Any]:
	"""
	Pure deterministic financial analysis.
	"""

	property_data = state.get("property")

	if not property_data:
		raise ValueError("Missing property data.")

	price = property_data.get("price")
	expected_rent = property_data.get("expected_rent")

	metrics = calculate_metrics(
		price=price,
		expected_rent=expected_rent,
	)

	return {"metrics": metrics}
