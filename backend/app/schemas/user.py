"""User schemas."""

from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """User creation schema."""
    username: str
    email: EmailStr
    full_name_en: str
    full_name_ar: str
    password: Optional[str] = None
    role: str = "VIEWER"
    is_ldap_user: bool = False


class UserUpdate(BaseModel):
    """User update schema."""
    full_name_en: Optional[str] = None
    full_name_ar: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None


class UserResponse(BaseModel):
    """User response schema."""
    id: str
    username: str
    email: EmailStr
    full_name_en: str
    full_name_ar: str
    role: str
    is_active: bool
    is_ldap_user: bool

    class Config:
        from_attributes = True
