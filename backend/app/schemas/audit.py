"""Audit schemas."""

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class AuditCreate(BaseModel):
    """Audit creation schema."""
    title_en: str
    title_ar: str
    scope: str
    description_en: Optional[str] = None
    description_ar: Optional[str] = None
    lead_auditor_id: str
    auditor_ids: List[str] = []
    start_date: datetime
    end_date: Optional[datetime] = None


class AuditUpdate(BaseModel):
    """Audit update schema."""
    title_en: Optional[str] = None
    title_ar: Optional[str] = None
    scope: Optional[str] = None
    description_en: Optional[str] = None
    description_ar: Optional[str] = None
    status: Optional[str] = None
    end_date: Optional[datetime] = None
    findings_summary: Optional[str] = None


class AuditResponse(BaseModel):
    """Audit response schema."""
    id: str
    audit_id: str
    title_en: str
    title_ar: str
    scope: str
    description_en: Optional[str] = None
    description_ar: Optional[str] = None
    status: str
    lead_auditor_id: str
    auditor_ids: List[str]
    start_date: datetime
    end_date: Optional[datetime] = None
    findings_summary: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class NonConformityCreate(BaseModel):
    """Non-conformity creation schema."""
    control_id: Optional[str] = None
    finding: str
    severity: str
    corrective_action: Optional[str] = None
    assigned_to_id: Optional[str] = None
    due_date: Optional[datetime] = None


class NonConformityUpdate(BaseModel):
    """Non-conformity update schema."""
    status: Optional[str] = None
    corrective_action: Optional[str] = None
    assigned_to_id: Optional[str] = None
    due_date: Optional[datetime] = None
    resolution_notes: Optional[str] = None


class NonConformityResponse(BaseModel):
    """Non-conformity response schema."""
    id: str
    audit_id: str
    control_id: Optional[str] = None
    finding: str
    severity: str
    status: str
    corrective_action: Optional[str] = None
    assigned_to_id: Optional[str] = None
    due_date: Optional[datetime] = None
    resolution_notes: Optional[str] = None
    resolved_at: Optional[datetime] = None
    created_at: datetime

    class Config:
        from_attributes = True
