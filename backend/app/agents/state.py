from typing import TypedDict, List, Optional


# -----------------------------
# INPUT STRUCTURES
# -----------------------------

class PropertyInput(TypedDict):
    price: float
    expected_rent: float
    location: str
    property_type: Optional[str]
    bedrooms: Optional[int]
    bathrooms: Optional[int]
    square_feet: Optional[float]


# -----------------------------
# FINANCIAL METRICS
# -----------------------------

class FinancialMetrics(TypedDict):
    annual_rent_income: float
    annual_expenses: float
    net_cash_flow: float
    roi_percent: float
    rental_yield_percent: float
    cap_rate_percent: float
    payback_period_years: float


# -----------------------------
# MARKET DATA
# -----------------------------

class MarketData(TypedDict):
    average_price: float
    average_rent: float
    neighborhood_growth_rate: float
    demand_score: float
    vacancy_rate: float


class ComparableProperty(TypedDict):
    location: str
    price: float
    rent: float
    similarity_score: float


# -----------------------------
# RISK PROFILE
# -----------------------------

class RiskProfile(TypedDict):
    risk_score: float
    risks: List[str]
    confidence: float


# -----------------------------
# DECISION OUTPUT
# -----------------------------

class InvestmentDecision(TypedDict):
    verdict: str
    score: float
    confidence: float


# -----------------------------
# FULL LANGGRAPH STATE
# -----------------------------

class AgentState(TypedDict, total=False):

    # -------- RAW INPUT --------
    price: float
    expected_rent: float
    location: str

    # -------- NORMALIZED INPUT --------
    property: PropertyInput

    # -------- FINANCIAL --------
    metrics: FinancialMetrics

    # -------- MARKET --------
    market: MarketData
    comparables: List[ComparableProperty]

    # -------- RISK --------
    risk: RiskProfile

    # -------- DECISION --------
    decision: InvestmentDecision

    # -------- FINAL OUTPUT --------
    explanation: str

    # -------- SYSTEM METADATA --------
    request_id: str
    processing_time_ms: float
    retrieval_count: int
    llm_model_used: str
    error_message: Optional[str]