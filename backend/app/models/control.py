"""Control model for compliance requirements."""

from datetime import datetime
from enum import Enum
from typing import Optional
from beanie import Document, Indexed, Link
from pydantic import Field

from app.models.standard import Standard


class ImplementationStatus(str, Enum):
    """Control implementation status."""
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
    PARTIALLY_IMPLEMENTED = "PARTIALLY_IMPLEMENTED"
    IMPLEMENTED = "IMPLEMENTED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class Control(Document):
    """Control/requirement from a standard."""

    standard: Link[Standard]
    control_id: Indexed(str)  # type: ignore
    domain_en: str
    domain_ar: str
    title_en: str
    title_ar: str
    description_en: str
    description_ar: str
    priority: str = "MEDIUM"  # LOW, MEDIUM, HIGH, CRITICAL
    implementation_status: ImplementationStatus = ImplementationStatus.NOT_IMPLEMENTED
    implementation_notes: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "controls"
        indexes = [
            "control_id",
            "priority",
            "implementation_status",
        ]

    class Config:
        json_schema_extra = {
            "example": {
                "control_id": "ECC-1-1-1",
                "domain_en": "Cybersecurity Governance",
                "domain_ar": "حوكمة الأمن السيبراني",
                "title_en": "Cybersecurity Strategy",
                "title_ar": "استراتيجية الأمن السيبراني",
                "description_en": "The organization shall define...",
                "description_ar": "يجب على الجهة تحديد...",
                "priority": "HIGH",
                "implementation_status": "PARTIALLY_IMPLEMENTED",
            }
        }
