"""AI service endpoints."""

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.services.ai_service import AIService, ComplianceSuggestion
from app.models.control import Control
from app.models.user import Role
from app.api.deps import require_role
from app.core.exceptions import raise_not_found, AIServiceError

router = APIRouter()


class AnalyzeEvidenceRequest(BaseModel):
    """Request to analyze evidence."""
    control_id: str
    evidence_text: str


class AnalyzeEvidenceResponse(BaseModel):
    """Response from evidence analysis."""
    compliance_status: str
    confidence: float
    reasoning_en: str
    reasoning_ar: str
    recommendations: list[str]


@router.post("/analyze-evidence", response_model=AnalyzeEvidenceResponse)
async def analyze_evidence(
    request: AnalyzeEvidenceRequest,
    current_user=Depends(require_role(Role.ADMIN, Role.RISK_OFFICER, Role.AUDITOR)),
):
    """
    Analyze evidence against a control using AI.

    This endpoint uses vLLM to assess whether provided evidence
    demonstrates compliance with a specific control requirement.
    """
    # Get control
    control = await Control.get(request.control_id)
    if not control:
        raise_not_found("Control not found")

    # Call AI service
    try:
        ai_service = AIService()
        suggestion = await ai_service.analyze_evidence(
            evidence_text=request.evidence_text,
            control=control
        )

        return AnalyzeEvidenceResponse(
            compliance_status=suggestion.compliance_status,
            confidence=suggestion.confidence,
            reasoning_en=suggestion.reasoning_en,
            reasoning_ar=suggestion.reasoning_ar,
            recommendations=suggestion.recommendations,
        )

    except AIServiceError as e:
        # Return graceful degradation if AI service is unavailable
        return AnalyzeEvidenceResponse(
            compliance_status="UNKNOWN",
            confidence=0.0,
            reasoning_en=f"AI service unavailable: {str(e)}",
            reasoning_ar=f"خدمة الذكاء الاصطناعي غير متاحة: {str(e)}",
            recommendations=[],
        )
