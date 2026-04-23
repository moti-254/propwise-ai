

"""
Property analysis endpoint for Propwise AI.
"""
from fastapi import APIRouter, HTTPException, Depends, status
import logging
from app.schemas.property_request import PropertyAnalysisRequest
from app.schemas.property_response import PropertyAnalysisResponse
from app.agents.graph import run_pipeline
from app.core.settings import get_settings
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/property", tags=["Property Analysis"])

def validate_payload(payload: PropertyAnalysisRequest):
	# Example: Add custom validation for realistic price/rent
	if payload.price > 1e9 or payload.expected_rent > 1e7:
		raise HTTPException(status_code=400, detail="Price or rent is unreasonably high.")
	return payload

@router.post(
	"/analyze",
	response_model=PropertyAnalysisResponse,
	status_code=status.HTTP_200_OK,
)
async def analyze_property(
	payload: PropertyAnalysisRequest = Depends(validate_payload),
	settings=Depends(get_settings)
):
	"""
	Analyze a property investment opportunity.
	"""
	try:
		result = await run_pipeline(payload.model_dump())
		return PropertyAnalysisResponse(
			property=result.get("property", {}),
			metrics=result.get("metrics", {}),
			market=result.get("market", {}),
			comparables=result.get("comparables", []),
			risk=result.get("risk", {}),
			decision=result.get("decision", {}),
			explanation=result.get("explanation", ""),
		)
	except Exception as exc:
		logger.exception("Property analysis failed")
		return JSONResponse(
			status_code=500,
			content={"detail": f"Analysis failed: {str(exc)}"},
		)
