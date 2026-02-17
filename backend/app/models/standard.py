"""Standard model for regulatory frameworks."""

from datetime import datetime
from typing import Optional
from beanie import Document, Indexed
from pydantic import Field


class Standard(Document):
    """Regulatory standard/framework document."""

    code: Indexed(str, unique=True)  # type: ignore
    name_en: str
    name_ar: str
    description_en: Optional[str] = None
    description_ar: Optional[str] = None
    version: str = "1.0"
    category: str  # e.g., "cybersecurity", "data_management", "ai_ethics"
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "standards"
        indexes = [
            "code",
            "category",
            "is_active",
        ]

    class Config:
        json_schema_extra = {
            "example": {
                "code": "NCA-ECC",
                "name_en": "Essential Cybersecurity Controls",
                "name_ar": "الضوابط الأساسية للأمن السيبراني",
                "version": "2.0",
                "category": "cybersecurity",
                "is_active": True,
            }
        }
