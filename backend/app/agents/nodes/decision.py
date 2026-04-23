from typing import Dict, Any
import logging

from app.agents.state import AgentState
from app.agents.prompts import DECISION_PROMPT
from app.integrations.openrouter_client import openrouter_client

logger = logging.getLogger(__name__)

def decision_node(state: AgentState) -> Dict[str, Any]:
	"""
	Makes final investment decision using:
	- Financial metrics
	- Market insights
	- Risk profile
	"""

	metrics = state.get("metrics")
	risk = state.get("risk")
	market = state.get("market")

	if not metrics:
		raise ValueError("Decision node requires financial metrics.")

	prompt = f"""
{DECISION_PROMPT}

PROPERTY DATA:
{state.get('property')}

FINANCIAL METRICS:
{metrics}

MARKET DATA:
{market}

RISK PROFILE:
{risk}

Return STRICT JSON only.
"""

	logger.info("[Decision Node] Starting investment decision generation")

	result = openrouter_client.complete_json(prompt)

	if not result:
		raise ValueError("Decision node failed to generate decision.")

	required_fields = ["verdict", "score", "confidence"]

	for field in required_fields:
		if field not in result:
			raise ValueError(f"Missing field in decision output: {field}")

	logger.info("[Decision Node] Decision successfully generated")

	return {"decision": result}
