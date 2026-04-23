from __future__ import annotations

import logging
from statistics import mean
from typing import List, Tuple
from app.vectorstore.query import query_similar_properties



from app.agents.state import ComparableProperty, MarketData, PropertyInput


from app.integrations.embedding_client import embed_text

logger = logging.getLogger(__name__)


async def fetch_market_comparables(
    property_data: PropertyInput,
    top_k: int = 5,
) -> Tuple[MarketData, List[ComparableProperty]]:
    """
    Retrieve comparable properties + market summary.

    Reads:
        - property_data

    Returns:
        market_data
        comparables

    Uses:
        PostgreSQL + pgvector semantic search
    """

    location = property_data["location"]
    property_type = property_data.get("property_type", "apartment")
    bedrooms = property_data.get("bedrooms")
    target_price = property_data["price"]

    query_text = _build_embedding_query(property_data)

    try:
        query_embedding = await embed_text(query_text)
    except Exception as exc:
        logger.exception("Embedding generation failed")
        raise RuntimeError("Failed to generate embedding for market retrieval") from exc

    results = await query_similar_properties(
    query_text=query_text,
    top_k=top_k,
    )

    comparables = []

    if results and results.get("metadatas"):
        metadata_rows = results["metadatas"][0]
        distances = results.get("distances", [[]])[0]

        for idx, row in enumerate(metadata_rows):
            similarity = 1 - distances[idx]

            comparable = {
                "location": row.get("location"),
                "price": float(row.get("price", 0)),
                "rent": float(row.get("expected_rent", 0)),
                "similarity_score": round(similarity, 4),
            }

            comparables.append(comparable)

    if not comparables:
        logger.warning("No comparables found for %s", location)

        fallback_market: MarketData = {
            "average_price": target_price,
            "average_rent": property_data["expected_rent"],
            "neighborhood_growth_rate": 0.0,
            "demand_score": 0.5,
            "vacancy_rate": 0.08,
        }

        return fallback_market, []

    market_summary = _build_market_summary(comparables)

    logger.info(
        "Retrieved %s comparables for %s",
        len(comparables),
        location,
    )

    return market_summary, comparables




def _build_market_summary(
    comparables: List[ComparableProperty],
) -> MarketData:
    """
    Aggregate comparable properties into structured market data.
    """

    avg_price = mean([c["price"] for c in comparables])
    avg_rent = mean([c["rent"] for c in comparables])

    price_growth_proxy = _estimate_growth_rate(comparables)
    demand_score = _estimate_demand_score(comparables)
    vacancy_rate = _estimate_vacancy_rate(comparables)

    market_data: MarketData = {
        "average_price": round(avg_price, 2),
        "average_rent": round(avg_rent, 2),
        "neighborhood_growth_rate": round(price_growth_proxy, 4),
        "demand_score": round(demand_score, 4),
        "vacancy_rate": round(vacancy_rate, 4),
    }

    return market_data



def _build_embedding_query(property_data: PropertyInput) -> str:
    """
    Convert structured property input into semantic embedding query.
    """

    return (
        f"Property investment in {property_data['location']} "
        f"for {property_data.get('property_type', 'apartment')} "
        f"priced at {property_data['price']} with rent {property_data['expected_rent']} "
        f"bedrooms {property_data.get('bedrooms', 'unknown')}"
    )



def _estimate_growth_rate(comparables: List[ComparableProperty]) -> float:
    """
    Placeholder until historical pricing table exists.
    """

    if len(comparables) < 2:
        return 0.03

    return 0.05



def _estimate_demand_score(comparables: List[ComparableProperty]) -> float:
    """
    Simple heuristic demand score.
    """

    average_rent = mean([c["rent"] for c in comparables])

    if average_rent > 100000:
        return 0.90
    elif average_rent > 50000:
        return 0.75

    return 0.60



def _estimate_vacancy_rate(comparables: List[ComparableProperty]) -> float:
    """
    Vacancy proxy until historical occupancy table exists.
    """

    return 0.08
