"""Control schemas."""

from typing import Optional
from pydantic import BaseModel


class ControlResponse(BaseModel):
    """Control response schema."""
    id: str
    control_id: str
    domain_en: str
    domain_ar: str
    title_en: str
    title_ar: str
    description_en: str
    description_ar: str
    priority: str
    implementation_status: str
    implementation_notes: Optional[str] = None

    class Config:
        from_attributes = True


class ControlUpdate(BaseModel):
    """Control update schema."""
    implementation_status: Optional[str] = None
    implementation_notes: Optional[str] = None
