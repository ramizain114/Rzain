"""Non-conformity model for audit findings."""

from datetime import datetime
from enum import Enum
from typing import Optional
from beanie import Document, Indexed, Link
from pydantic import Field

from app.models.audit import Audit
from app.models.control import Control
from app.models.user import User


class Severity(str, Enum):
    """Finding severity level."""
    OBSERVATION = "OBSERVATION"
    MINOR = "MINOR"
    MAJOR = "MAJOR"
    CRITICAL = "CRITICAL"


class NonConformityStatus(str, Enum):
    """Non-conformity resolution status."""
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"


class NonConformity(Document):
    """Non-conformity/finding from an audit."""

    audit: Link[Audit]
    control: Optional[Link[Control]] = None
    finding: str
    severity: Severity
    status: NonConformityStatus = NonConformityStatus.OPEN
    corrective_action: Optional[str] = None
    assigned_to: Optional[Link[User]] = None
    due_date: Optional[datetime] = None
    resolution_notes: Optional[str] = None
    resolved_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "nonconformities"
        indexes = [
            "severity",
            "status",
            "due_date",
        ]

    class Config:
        json_schema_extra = {
            "example": {
                "finding": "Password policy does not meet minimum complexity requirements",
                "severity": "MAJOR",
                "status": "OPEN",
                "corrective_action": "Update password policy to enforce 12+ characters with complexity",
                "due_date": "2024-02-15T00:00:00Z",
            }
        }
