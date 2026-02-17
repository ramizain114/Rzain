"""Audit management endpoints."""

from typing import List
from datetime import datetime
from fastapi import APIRouter, Depends, status

from app.schemas.audit import (
    AuditCreate,
    AuditUpdate,
    AuditResponse,
    NonConformityCreate,
    NonConformityUpdate,
    NonConformityResponse,
)
from app.models.audit import Audit, AuditStatus
from app.models.nonconformity import NonConformity, Severity, NonConformityStatus
from app.models.user import User, Role
from app.api.deps import get_current_user, require_role
from app.core.exceptions import raise_not_found, raise_bad_request

router = APIRouter()


@router.get("/", response_model=List[AuditResponse], dependencies=[Depends(get_current_user)])
async def list_audits():
    """List all audits."""
    audits = await Audit.find_all().to_list()
    return [
        AuditResponse(
            id=str(audit.id),
            audit_id=audit.audit_id,
            title_en=audit.title_en,
            title_ar=audit.title_ar,
            scope=audit.scope,
            description_en=audit.description_en,
            description_ar=audit.description_ar,
            status=audit.status.value,
            lead_auditor_id=str(audit.lead_auditor.ref.id),
            auditor_ids=audit.auditor_ids,
            start_date=audit.start_date,
            end_date=audit.end_date,
            findings_summary=audit.findings_summary,
            created_at=audit.created_at,
        )
        for audit in audits
    ]


@router.post("/", response_model=AuditResponse, status_code=status.HTTP_201_CREATED)
async def create_audit(
    audit_data: AuditCreate,
    current_user=Depends(require_role(Role.ADMIN, Role.AUDITOR)),
):
    """Create a new audit."""
    lead_auditor = await User.get(audit_data.lead_auditor_id)
    if not lead_auditor:
        raise_bad_request("Lead auditor not found")

    # Generate audit ID
    count = await Audit.count()
    audit_id = f"AUD-{datetime.now().year}-{count + 1:04d}"

    audit = Audit(
        audit_id=audit_id,
        title_en=audit_data.title_en,
        title_ar=audit_data.title_ar,
        scope=audit_data.scope,
        description_en=audit_data.description_en,
        description_ar=audit_data.description_ar,
        lead_auditor=lead_auditor,
        auditor_ids=audit_data.auditor_ids,
        start_date=audit_data.start_date,
        end_date=audit_data.end_date,
    )

    await audit.insert()

    return AuditResponse(
        id=str(audit.id),
        audit_id=audit.audit_id,
        title_en=audit.title_en,
        title_ar=audit.title_ar,
        scope=audit.scope,
        description_en=audit.description_en,
        description_ar=audit.description_ar,
        status=audit.status.value,
        lead_auditor_id=str(audit.lead_auditor.ref.id),
        auditor_ids=audit.auditor_ids,
        start_date=audit.start_date,
        end_date=audit.end_date,
        findings_summary=audit.findings_summary,
        created_at=audit.created_at,
    )


@router.get("/{audit_id}/findings", response_model=List[NonConformityResponse])
async def list_audit_findings(
    audit_id: str,
    current_user: User = Depends(get_current_user),
):
    """List all findings for an audit."""
    audit = await Audit.get(audit_id)
    if not audit:
        raise_not_found("Audit not found")

    findings = await NonConformity.find(NonConformity.audit.ref.id == audit_id).to_list()

    return [
        NonConformityResponse(
            id=str(nc.id),
            audit_id=str(nc.audit.ref.id),
            control_id=str(nc.control.ref.id) if nc.control else None,
            finding=nc.finding,
            severity=nc.severity.value,
            status=nc.status.value,
            corrective_action=nc.corrective_action,
            assigned_to_id=str(nc.assigned_to.ref.id) if nc.assigned_to else None,
            due_date=nc.due_date,
            resolution_notes=nc.resolution_notes,
            resolved_at=nc.resolved_at,
            created_at=nc.created_at,
        )
        for nc in findings
    ]


@router.post("/{audit_id}/findings", response_model=NonConformityResponse, status_code=status.HTTP_201_CREATED)
async def create_finding(
    audit_id: str,
    finding_data: NonConformityCreate,
    current_user=Depends(require_role(Role.ADMIN, Role.AUDITOR)),
):
    """Add a finding to an audit."""
    audit = await Audit.get(audit_id)
    if not audit:
        raise_not_found("Audit not found")

    nonconformity = NonConformity(
        audit=audit,
        finding=finding_data.finding,
        severity=Severity(finding_data.severity),
        corrective_action=finding_data.corrective_action,
        due_date=finding_data.due_date,
    )

    if finding_data.control_id:
        from app.models.control import Control
        control = await Control.get(finding_data.control_id)
        if control:
            nonconformity.control = control

    if finding_data.assigned_to_id:
        assignee = await User.get(finding_data.assigned_to_id)
        if assignee:
            nonconformity.assigned_to = assignee

    await nonconformity.insert()

    return NonConformityResponse(
        id=str(nonconformity.id),
        audit_id=str(nonconformity.audit.ref.id),
        control_id=str(nonconformity.control.ref.id) if nonconformity.control else None,
        finding=nonconformity.finding,
        severity=nonconformity.severity.value,
        status=nonconformity.status.value,
        corrective_action=nonconformity.corrective_action,
        assigned_to_id=str(nonconformity.assigned_to.ref.id) if nonconformity.assigned_to else None,
        due_date=nonconformity.due_date,
        resolution_notes=nonconformity.resolution_notes,
        resolved_at=nonconformity.resolved_at,
        created_at=nonconformity.created_at,
    )
