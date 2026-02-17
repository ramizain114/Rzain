"""Risk management endpoints."""

from typing import List
from fastapi import APIRouter, Depends, status
from datetime import datetime

from app.schemas.risk import RiskCreate, RiskUpdate, RiskResponse
from app.models.risk import Risk
from app.models.user import User, Role
from app.api.deps import get_current_user, require_role
from app.core.exceptions import raise_not_found, raise_bad_request

router = APIRouter()


@router.get("/", response_model=List[RiskResponse], dependencies=[Depends(get_current_user)])
async def list_risks():
    """List all risks."""
    risks = await Risk.find_all().to_list()
    return [
        RiskResponse(
            id=str(risk.id),
            risk_id=risk.risk_id,
            title_en=risk.title_en,
            title_ar=risk.title_ar,
            description_en=risk.description_en,
            description_ar=risk.description_ar,
            asset=risk.asset,
            threat=risk.threat,
            vulnerability=risk.vulnerability,
            impact_score=risk.impact_score,
            likelihood_score=risk.likelihood_score,
            risk_score=risk.risk_score,
            risk_level=risk.risk_level.value,
            treatment=risk.treatment.value,
            treatment_plan=risk.treatment_plan,
            status=risk.status,
            owner_id=str(risk.owner.ref.id),
            review_date=risk.review_date,
            created_at=risk.created_at,
            updated_at=risk.updated_at,
        )
        for risk in risks
    ]


@router.post("/", response_model=RiskResponse, status_code=status.HTTP_201_CREATED)
async def create_risk(
    risk_data: RiskCreate,
    current_user = Depends(require_role(Role.ADMIN, Role.RISK_OFFICER)),
):
    """Create a new risk."""
    # Get owner
    owner = await User.get(risk_data.owner_id)
    if not owner:
        raise_bad_request("Owner not found")

    # Generate risk ID
    count = await Risk.count()
    risk_id = f"RISK-{datetime.now().year}-{count + 1:04d}"

    # Create risk
    from app.models.risk import RiskTreatment
    risk = Risk(
        risk_id=risk_id,
        title_en=risk_data.title_en,
        title_ar=risk_data.title_ar,
        description_en=risk_data.description_en,
        description_ar=risk_data.description_ar,
        asset=risk_data.asset,
        threat=risk_data.threat,
        vulnerability=risk_data.vulnerability,
        impact_score=risk_data.impact_score,
        likelihood_score=risk_data.likelihood_score,
        treatment=RiskTreatment(risk_data.treatment),
        treatment_plan=risk_data.treatment_plan,
        owner=owner,
        review_date=risk_data.review_date,
    )

    # Calculate risk score and level
    risk.calculate_risk_score()

    await risk.insert()

    return RiskResponse(
        id=str(risk.id),
        risk_id=risk.risk_id,
        title_en=risk.title_en,
        title_ar=risk.title_ar,
        description_en=risk.description_en,
        description_ar=risk.description_ar,
        asset=risk.asset,
        threat=risk.threat,
        vulnerability=risk.vulnerability,
        impact_score=risk.impact_score,
        likelihood_score=risk.likelihood_score,
        risk_score=risk.risk_score,
        risk_level=risk.risk_level.value,
        treatment=risk.treatment.value,
        treatment_plan=risk.treatment_plan,
        status=risk.status,
        owner_id=str(risk.owner.ref.id),
        review_date=risk.review_date,
        created_at=risk.created_at,
        updated_at=risk.updated_at,
    )


@router.get("/{risk_id}", response_model=RiskResponse, dependencies=[Depends(get_current_user)])
async def get_risk(risk_id: str):
    """Get risk by ID."""
    risk = await Risk.get(risk_id)
    if not risk:
        raise_not_found("Risk not found")

    return RiskResponse(
        id=str(risk.id),
        risk_id=risk.risk_id,
        title_en=risk.title_en,
        title_ar=risk.title_ar,
        description_en=risk.description_en,
        description_ar=risk.description_ar,
        asset=risk.asset,
        threat=risk.threat,
        vulnerability=risk.vulnerability,
        impact_score=risk.impact_score,
        likelihood_score=risk.likelihood_score,
        risk_score=risk.risk_score,
        risk_level=risk.risk_level.value,
        treatment=risk.treatment.value,
        treatment_plan=risk.treatment_plan,
        status=risk.status,
        owner_id=str(risk.owner.ref.id),
        review_date=risk.review_date,
        created_at=risk.created_at,
        updated_at=risk.updated_at,
    )


@router.put("/{risk_id}", response_model=RiskResponse)
async def update_risk(
    risk_id: str,
    update_data: RiskUpdate,
    current_user = Depends(require_role(Role.ADMIN, Role.RISK_OFFICER)),
):
    """Update a risk."""
    risk = await Risk.get(risk_id)
    if not risk:
        raise_not_found("Risk not found")

    # Update fields
    update_dict = update_data.model_dump(exclude_unset=True)

    for field, value in update_dict.items():
        if field == "treatment" and value:
            from app.models.risk import RiskTreatment
            setattr(risk, field, RiskTreatment(value))
        else:
            setattr(risk, field, value)

    # Recalculate if impact or likelihood changed
    if "impact_score" in update_dict or "likelihood_score" in update_dict:
        risk.calculate_risk_score()

    risk.updated_at = datetime.utcnow()
    await risk.save()

    return RiskResponse(
        id=str(risk.id),
        risk_id=risk.risk_id,
        title_en=risk.title_en,
        title_ar=risk.title_ar,
        description_en=risk.description_en,
        description_ar=risk.description_ar,
        asset=risk.asset,
        threat=risk.threat,
        vulnerability=risk.vulnerability,
        impact_score=risk.impact_score,
        likelihood_score=risk.likelihood_score,
        risk_score=risk.risk_score,
        risk_level=risk.risk_level.value,
        treatment=risk.treatment.value,
        treatment_plan=risk.treatment_plan,
        status=risk.status,
        owner_id=str(risk.owner.ref.id),
        review_date=risk.review_date,
        created_at=risk.created_at,
        updated_at=risk.updated_at,
    )


@router.delete("/{risk_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_risk(
    risk_id: str,
    current_user = Depends(require_role(Role.ADMIN)),
):
    """Soft delete a risk."""
    risk = await Risk.get(risk_id)
    if not risk:
        raise_not_found("Risk not found")

    risk.status = "CLOSED"
    await risk.save()
