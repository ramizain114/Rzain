"""Audit model for audit workflow management."""

from datetime import datetime
from enum import Enum
from typing import List, Optional
from beanie import Document, Indexed, Link
from pydantic import Field

from app.models.user import User


class AuditStatus(str, Enum):
    """Audit workflow status."""
    PLANNED = "PLANNED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CLOSED = "CLOSED"


class Audit(Document):
    """Audit engagement document."""

    audit_id: Indexed(str, unique=True)  # type: ignore
    title_en: str
    title_ar: str
    scope: str
    description_en: Optional[str] = None
    description_ar: Optional[str] = None
    status: AuditStatus = AuditStatus.PLANNED
    lead_auditor: Link[User]
    auditor_ids: List[str] = Field(default_factory=list)  # User IDs
    start_date: datetime
    end_date: Optional[datetime] = None
    findings_summary: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "audits"
        indexes = [
            "audit_id",
            "status",
            "start_date",
        ]

    class Config:
        json_schema_extra = {
            "example": {
                "audit_id": "AUD-2024-Q1",
                "title_en": "Q1 Cybersecurity Audit",
                "title_ar": "تدقيق الأمن السيبراني للربع الأول",
                "scope": "NCA-ECC controls",
                "status": "IN_PROGRESS",
                "start_date": "2024-01-15T00:00:00Z",
            }
        }
