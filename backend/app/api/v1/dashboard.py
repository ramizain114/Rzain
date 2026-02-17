"""Dashboard summary endpoints."""

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.models.control import Control, ImplementationStatus
from app.models.risk import Risk, RiskLevel
from app.models.audit import Audit, AuditStatus
from app.models.nonconformity import NonConformity, NonConformityStatus
from app.api.deps import get_current_user

router = APIRouter()


class DashboardSummary(BaseModel):
    """Dashboard summary statistics."""
    total_controls: int
    implemented_controls: int
    compliance_percentage: float
    total_risks: int
    open_risks: int
    critical_risks: int
    total_audits: int
    active_audits: int
    open_findings: int


@router.get("/summary", response_model=DashboardSummary)
async def get_dashboard_summary(current_user = Depends(get_current_user)):
    """Get aggregated dashboard statistics."""
    # Controls stats
    total_controls = await Control.count()
    implemented_controls = await Control.find(
        Control.implementation_status == ImplementationStatus.IMPLEMENTED
    ).count()
    compliance_percentage = (
        (implemented_controls / total_controls * 100) if total_controls > 0 else 0
    )

    # Risk stats
    total_risks = await Risk.count()
    open_risks = await Risk.find(Risk.status == "OPEN").count()
    critical_risks = await Risk.find(Risk.risk_level == RiskLevel.CRITICAL).count()

    # Audit stats
    total_audits = await Audit.count()
    active_audits = await Audit.find(
        Audit.status.in_([AuditStatus.PLANNED, AuditStatus.IN_PROGRESS])
    ).count()

    # Findings stats
    open_findings = await NonConformity.find(
        NonConformity.status.in_([NonConformityStatus.OPEN, NonConformityStatus.IN_PROGRESS])
    ).count()

    return DashboardSummary(
        total_controls=total_controls,
        implemented_controls=implemented_controls,
        compliance_percentage=round(compliance_percentage, 1),
        total_risks=total_risks,
        open_risks=open_risks,
        critical_risks=critical_risks,
        total_audits=total_audits,
        active_audits=active_audits,
        open_findings=open_findings,
    )
