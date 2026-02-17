"""Risk schemas."""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class RiskCreate(BaseModel):
    """Risk creation schema."""
    title_en: str
    title_ar: str
    description_en: str
    description_ar: str
    asset: str
    threat: str
    vulnerability: str
    impact_score: int = Field(ge=1, le=5)
    likelihood_score: int = Field(ge=1, le=5)
    treatment: str = "MITIGATE"
    treatment_plan: Optional[str] = None
    owner_id: str
    review_date: Optional[datetime] = None


class RiskUpdate(BaseModel):
    """Risk update schema."""
    title_en: Optional[str] = None
    title_ar: Optional[str] = None
    description_en: Optional[str] = None
    description_ar: Optional[str] = None
    asset: Optional[str] = None
    threat: Optional[str] = None
    vulnerability: Optional[str] = None
    impact_score: Optional[int] = Field(None, ge=1, le=5)
    likelihood_score: Optional[int] = Field(None, ge=1, le=5)
    treatment: Optional[str] = None
    treatment_plan: Optional[str] = None
    status: Optional[str] = None
    review_date: Optional[datetime] = None


class RiskResponse(BaseModel):
    """Risk response schema."""
    id: str
    risk_id: str
    title_en: str
    title_ar: str
    description_en: str
    description_ar: str
    asset: str
    threat: str
    vulnerability: str
    impact_score: int
    likelihood_score: int
    risk_score: int
    risk_level: str
    treatment: str
    treatment_plan: Optional[str] = None
    status: str
    owner_id: str
    review_date: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
