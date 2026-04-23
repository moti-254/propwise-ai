from __future__ import annotations

from typing import Dict, Any, List


def calculate_risk(
    property_data: Dict[str, Any],
    metrics: Dict[str, Any],
    market_data: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Structured risk computation layer.

    Returns:
        {
            "risk_score": float,
            "risk_level": str,
            "risks": list[str],
            "signals": dict
        }
    """

    risks: List[str] = []
    score = 0.0

    property_price = float(property_data.get("price", 0))
    expected_rent = float(property_data.get("expected_rent", 0))

    market_avg_price = float(market_data.get("average_price", property_price))
    vacancy_rate = float(market_data.get("vacancy_rate", 0.08))
    demand_score = float(market_data.get("demand_score", 0.5))
    growth_rate = float(
        market_data.get("neighborhood_growth_rate", 0.03)
    )

    roi = float(metrics.get("roi", 0))
    cap_rate = float(metrics.get("cap_rate", 0))

    # ---------------------------------------------------
    # PRICE RISK
    # ---------------------------------------------------

    if property_price > market_avg_price * 1.20:
        score += 2.0
        risks.append("Property price significantly exceeds market average")

    elif property_price > market_avg_price * 1.10:
        score += 1.0
        risks.append("Property price slightly above market average")

    # ---------------------------------------------------
    # ROI RISK
    # ---------------------------------------------------

    if roi < 5:
        score += 2.5
        risks.append("Low ROI projection")

    elif roi < 8:
        score += 1.0
        risks.append("Moderate ROI")

    # ---------------------------------------------------
    # CAP RATE RISK
    # ---------------------------------------------------

    if cap_rate < 4:
        score += 2.0
        risks.append("Weak cap rate")

    # ---------------------------------------------------
    # VACANCY RISK
    # ---------------------------------------------------

    if vacancy_rate > 0.12:
        score += 2.0
        risks.append("High vacancy area")

    elif vacancy_rate > 0.08:
        score += 1.0
        risks.append("Moderate vacancy exposure")

    # ---------------------------------------------------
    # DEMAND RISK
    # ---------------------------------------------------

    if demand_score < 0.4:
        score += 2.0
        risks.append("Weak rental demand")

    elif demand_score < 0.6:
        score += 1.0
        risks.append("Average rental demand")

    # ---------------------------------------------------
    # MARKET GROWTH RISK
    # ---------------------------------------------------

    if growth_rate < 0.02:
        score += 1.5
        risks.append("Low neighborhood appreciation potential")

    # ---------------------------------------------------
    # NORMALIZE
    # ---------------------------------------------------

    risk_score = min(round(score, 2), 10)

    if risk_score <= 3:
        risk_level = "Low"
    elif risk_score <= 6:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "risks": risks,
        "signals": {
            "roi": roi,
            "cap_rate": cap_rate,
            "vacancy_rate": vacancy_rate,
            "demand_score": demand_score,
            "growth_rate": growth_rate,
        },
    }