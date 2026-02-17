"""User model."""

from datetime import datetime
from enum import Enum
from typing import Optional
from beanie import Document, Indexed
from pydantic import EmailStr, Field


class Role(str, Enum):
    """User roles for RBAC."""
    ADMIN = "ADMIN"
    RISK_OFFICER = "RISK_OFFICER"
    AUDITOR = "AUDITOR"
    VIEWER = "VIEWER"


class User(Document):
    """User document model."""

    username: Indexed(str, unique=True)  # type: ignore
    email: Indexed(EmailStr, unique=True)  # type: ignore
    full_name_en: str
    full_name_ar: str
    hashed_password: Optional[str] = None  # Only for local accounts
    role: Role = Role.VIEWER
    is_active: bool = True
    is_ldap_user: bool = False
    last_login: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "users"
        indexes = [
            "username",
            "email",
            "role",
        ]

    class Config:
        json_schema_extra = {
            "example": {
                "username": "jdoe",
                "email": "jdoe@municipality.gov.sa",
                "full_name_en": "John Doe",
                "full_name_ar": "جون دو",
                "role": "VIEWER",
                "is_active": True,
                "is_ldap_user": True,
            }
        }
