"""Standard schemas."""

from typing import Optional
from pydantic import BaseModel


class StandardResponse(BaseModel):
    """Standard response schema."""
    id: str
    code: str
    name_en: str
    name_ar: str
    description_en: Optional[str] = None
    description_ar: Optional[str] = None
    version: str
    category: str
    is_active: bool

    class Config:
        from_attributes = True
