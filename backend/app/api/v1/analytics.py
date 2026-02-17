"""Analytics endpoints for trend analysis."""

from typing import List
from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from datetime import datetime, timedelta

from app.models.control import Control, ImplementationStatus
from app.models.risk import Risk, RiskLevel
from app.api.deps import get_current_user

router = APIRouter()


class ComplianceTrendPoint(BaseModel):
    """Single point in compliance trend."""
    date: str
    percentage: float
    implemented_count: int
    total_count: int


class RiskTrendPoint(BaseModel):
    """Single point in risk trend."""
    date: str
    total_risks: int
    open_risks: int
    critical_risks: int


@router.get("/compliance-trend", response_model=List[ComplianceTrendPoint])
async def get_compliance_trend(
    days: int = Query(30, ge=7, le=365),
    current_user = Depends(get_current_user)
):
    """
    Get compliance trend over time.
    
    This is a simplified version that shows current compliance.
    In production, you would track historical snapshots.
    """
    total = await Control.count()
    implemented = await Control.find(
        Control.implementation_status == ImplementationStatus.IMPLEMENTED
    ).count()

    percentage = (implemented / total * 100) if total > 0 else 0

    # Generate trend points (simplified - would use historical data in production)
    trend = []
    for i in range(days):
        date = datetime.now() - timedelta(days=days-i-1)
        # In production, query historical snapshots
        trend.append(ComplianceTrendPoint(
            date=date.strftime('%Y-%m-%d'),
            percentage=round(percentage, 1),
            implemented_count=implemented,
            total_count=total,
        ))

    return trend


@router.get("/risk-trend", response_model=List[RiskTrendPoint])
async def get_risk_trend(
    days: int = Query(30, ge=7, le=365),
    current_user = Depends(get_current_user)
):
    """Get risk trend over time."""
    total = await Risk.count()
    open_risks = await Risk.find(Risk.status == "OPEN").count()
    critical = await Risk.find(Risk.risk_level == RiskLevel.CRITICAL).count()

    # Generate trend points (simplified)
    trend = []
    for i in range(days):
        date = datetime.now() - timedelta(days=days-i-1)
        trend.append(RiskTrendPoint(
            date=date.strftime('%Y-%m-%d'),
            total_risks=total,
            open_risks=open_risks,
            critical_risks=critical,
        ))

    return trend


class ControlsByDomain(BaseModel):
    """Controls grouped by domain."""
    domain_en: str
    domain_ar: str
    total: int
    implemented: int
    percentage: float


@router.get("/controls-by-domain", response_model=List[ControlsByDomain])
async def get_controls_by_domain(current_user = Depends(get_current_user)):
    """Get control implementation statistics by domain."""
    controls = await Control.find_all().to_list()

    # Group by domain
    domains = {}
    for control in controls:
        domain_key = control.domain_en
        if domain_key not in domains:
            domains[domain_key] = {
                'domain_en': control.domain_en,
                'domain_ar': control.domain_ar,
                'total': 0,
                'implemented': 0,
            }

        domains[domain_key]['total'] += 1
        if control.implementation_status == ImplementationStatus.IMPLEMENTED:
            domains[domain_key]['implemented'] += 1

    # Calculate percentages
    result = []
    for domain_data in domains.values():
        percentage = (
            domain_data['implemented'] / domain_data['total'] * 100
            if domain_data['total'] > 0 else 0
        )
        result.append(ControlsByDomain(
            domain_en=domain_data['domain_en'],
            domain_ar=domain_data['domain_ar'],
            total=domain_data['total'],
            implemented=domain_data['implemented'],
            percentage=round(percentage, 1),
        ))

    return sorted(result, key=lambda x: x.percentage, reverse=True)
