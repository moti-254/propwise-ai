from pydantic import BaseModel
from typing import List, Optional

class AnalyzeRequest(BaseModel):
    price: float
    expected_rent: float
    location: str

class ComparablePropertyModel(BaseModel):
    location: str
    price: float
    rent: float
    similarity_score: float

class MarketDataModel(BaseModel):
    average_price: float
    average_rent: float
    neighborhood_growth_rate: float
    demand_score: float
    vacancy_rate: float

class FinancialMetricsModel(BaseModel):
    annual_rent_income: float
    annual_expenses: float
    net_cash_flow: float
    roi_percent: float
    rental_yield_percent: float
    cap_rate_percent: float
    payback_period_years: float

class RiskProfileModel(BaseModel):
    risk_score: float
    risks: List[str]
    confidence: float

class InvestmentDecisionModel(BaseModel):
    verdict: str
    score: float
    confidence: float

class AnalyzeResponse(BaseModel):
    property: Optional[dict]
    metrics: Optional[FinancialMetricsModel]
    market: Optional[MarketDataModel]
    comparables: Optional[List[ComparablePropertyModel]]
    risk: Optional[RiskProfileModel]
    decision: Optional[InvestmentDecisionModel]
    explanation: Optional[str]
