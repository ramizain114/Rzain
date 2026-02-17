"""Controls endpoints."""

from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status

from app.schemas.control import ControlResponse, ControlUpdate
from app.models.control import Control
from app.models.user import Role
from app.api.deps import get_current_user, require_role
from app.core.exceptions import raise_not_found

router = APIRouter()


@router.get("/", response_model=List[ControlResponse], dependencies=[Depends(get_current_user)])
async def list_controls(
    standard_id: Optional[str] = Query(None),
    priority: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
):
    """List controls with optional filters."""
    query = Control.find()

    if standard_id:
        query = query.find(Control.standard.ref.id == standard_id)
    if priority:
        query = query.find(Control.priority == priority)
    if status:
        query = query.find(Control.implementation_status == status)

    controls = await query.skip(skip).limit(limit).to_list()

    return [
        ControlResponse(
            id=str(ctrl.id),
            control_id=ctrl.control_id,
            domain_en=ctrl.domain_en,
            domain_ar=ctrl.domain_ar,
            title_en=ctrl.title_en,
            title_ar=ctrl.title_ar,
            description_en=ctrl.description_en,
            description_ar=ctrl.description_ar,
            priority=ctrl.priority,
            implementation_status=ctrl.implementation_status.value,
            implementation_notes=ctrl.implementation_notes,
        )
        for ctrl in controls
    ]


@router.get("/{control_id}", response_model=ControlResponse, dependencies=[Depends(get_current_user)])
async def get_control(control_id: str):
    """Get control by ID."""
    control = await Control.get(control_id)
    if not control:
        raise_not_found("Control not found")

    return ControlResponse(
        id=str(control.id),
        control_id=control.control_id,
        domain_en=control.domain_en,
        domain_ar=control.domain_ar,
        title_en=control.title_en,
        title_ar=control.title_ar,
        description_en=control.description_en,
        description_ar=control.description_ar,
        priority=control.priority,
        implementation_status=control.implementation_status.value,
        implementation_notes=control.implementation_notes,
    )


@router.patch("/{control_id}", response_model=ControlResponse)
async def update_control(
    control_id: str,
    update_data: ControlUpdate,
    current_user = Depends(require_role(Role.ADMIN, Role.RISK_OFFICER)),
):
    """Update control implementation status."""
    control = await Control.get(control_id)
    if not control:
        raise_not_found("Control not found")

    if update_data.implementation_status:
        from app.models.control import ImplementationStatus
        control.implementation_status = ImplementationStatus(update_data.implementation_status)

    if update_data.implementation_notes is not None:
        control.implementation_notes = update_data.implementation_notes

    await control.save()

    return ControlResponse(
        id=str(control.id),
        control_id=control.control_id,
        domain_en=control.domain_en,
        domain_ar=control.domain_ar,
        title_en=control.title_en,
        title_ar=control.title_ar,
        description_en=control.description_en,
        description_ar=control.description_ar,
        priority=control.priority,
        implementation_status=control.implementation_status.value,
        implementation_notes=control.implementation_notes,
    )
