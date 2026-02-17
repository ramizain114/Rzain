"""Evidence model for compliance documentation."""

from datetime import datetime
from enum import Enum
from typing import Optional
from beanie import Document, Indexed, Link
from pydantic import Field

from app.models.control import Control
from app.models.user import User


class EvidenceStatus(str, Enum):
    """Evidence review status."""
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class Evidence(Document):
    """Evidence document supporting control implementation."""

    control: Link[Control]
    uploaded_by: Link[User]
    title: str
    description: Optional[str] = None
    file_path: Optional[str] = None
    file_type: Optional[str] = None
    file_size: Optional[int] = None
    status: EvidenceStatus = EvidenceStatus.PENDING
    reviewer_notes: Optional[str] = None
    ai_assessment: Optional[str] = None
    ai_confidence: Optional[float] = Field(None, ge=0.0, le=1.0)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "evidence"
        indexes = [
            "status",
            "created_at",
        ]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Security Policy Document",
                "description": "Organization security policy v2.1",
                "file_path": "/uploads/security-policy-v2.1.pdf",
                "file_type": "application/pdf",
                "status": "PENDING",
            }
        }
