from typing import Dict, Any
import logging

from app.agents.state import AgentState
from app.services.market_service import fetch_market_comparables

logger = logging.getLogger(__name__)

import asyncio

async def market_node(state: AgentState) -> Dict[str, Any]:
    """
    Market intelligence node.
    """

    property_data = state.get("property")
    if not property_data:
        raise ValueError("Market node requires property data.")

    logger.info(f"[Market Node] Retrieving comparables for {property_data.get('location')}")

    market_summary, comparables = await fetch_market_comparables(property_data)

    return {
        "market": market_summary,
        "comparables": comparables,
    }
