"""Authentication schemas."""

from typing import Optional
from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    """Login request schema."""
    username: str
    password: str


class TokenResponse(BaseModel):
    """Token response schema."""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshTokenRequest(BaseModel):
    """Refresh token request schema."""
    refresh_token: str


class UserProfile(BaseModel):
    """User profile response schema."""
    id: str
    username: str
    email: EmailStr
    full_name_en: str
    full_name_ar: str
    role: str
    is_active: bool
    is_ldap_user: bool
    last_login: Optional[str] = None

    class Config:
        from_attributes = True
