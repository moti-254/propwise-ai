from typing import Dict, Any
import logging

from app.agents.state import AgentState
from app.agents.prompts import EXPLANATION_PROMPT
from app.integrations.openrouter_client import openrouter_client

logger = logging.getLogger(__name__)


def explanation_node(state: AgentState) -> Dict[str, Any]:
    """
    Final explanation node.

    Converts structured investment decision into a
    clean user-facing explanation.

    Reads:
        - property
        - metrics
        - market
        - risk
        - decision

    Writes:
        - explanation
    """

    decision = state.get("decision")
    metrics = state.get("metrics")

    if not decision:
        raise ValueError("Explanation node requires decision data.")

    prompt = f"""
{EXPLANATION_PROMPT}

PROPERTY:
{state.get('property')}

FINANCIAL METRICS:
{metrics}

MARKET:
{state.get('market')}

RISK:
{state.get('risk')}

DECISION:
{decision}

Return plain text only.
"""

    logger.info("[Explanation Node] Generating explanation")

    response = openrouter_client.complete_text(prompt)

    if not response:
        raise ValueError("Explanation node failed to produce text.")

    explanation = response.strip()

    logger.info("[Explanation Node] Explanation generated successfully")

    return {
        "explanation": explanation
    }