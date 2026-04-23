from __future__ import annotations

import logging
from typing import Dict, Any

from app.agents.state import AgentState
from app.agents.prompts import RISK_PROMPT
from app.integrations.openrouter_client import openrouter_client
from app.services.risk_service import calculate_risk

logger = logging.getLogger(__name__)


def risk_node(state: AgentState) -> Dict[str, Any]:
    """
    Risk Node

    Responsibilities:
    - gather context
    - compute deterministic risk
    - optionally enrich with LLM interpretation
    """

    property_data = state.get("property")
    metrics = state.get("metrics")
    market = state.get("market")

    if not property_data:
        raise ValueError("Missing property data")

    if not metrics:
        raise ValueError("Missing financial metrics")

    if not market:
        raise ValueError("Missing market data")

    logger.info("[Risk Node] Computing structured risk")

    structured_risk = calculate_risk(
        property_data=property_data,
        metrics=metrics,
        market_data=market,
    )

    # --------------------------------------------------
    # Optional LLM enrichment
    # --------------------------------------------------

    prompt = f"""
{RISK_PROMPT}

PROPERTY:
{property_data}

FINANCIALS:
{metrics}

MARKET:
{market}

STRUCTURED RISK:
{structured_risk}

Return STRICT JSON:
{{
    "summary": "...",
    "recommendations": ["..."],
    "risk_factors": ["..."]
}}
"""

    try:
        llm_result = openrouter_client.complete_json(prompt)

        if not llm_result:
            raise ValueError("Empty LLM risk response")

    except Exception as exc:
        logger.warning(
            "LLM enrichment failed in risk node: %s",
            exc,
        )

        llm_result = {
            "summary": "Risk analysis generated from deterministic scoring.",
            "recommendations": [],
            "risk_factors": structured_risk["risks"],
        }

    final_risk = {
        **structured_risk,
        "llm_analysis": llm_result,
    }

    logger.info(
        "[Risk Node] Risk score=%s level=%s",
        final_risk["risk_score"],
        final_risk["risk_level"],
    )

    return {
        "risk": final_risk
    }