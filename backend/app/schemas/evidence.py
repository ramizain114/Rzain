"""Evidence schemas."""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class EvidenceCreate(BaseModel):
    """Evidence creation schema."""
    control_id: str
    title: str
    description: Optional[str] = None


class EvidenceResponse(BaseModel):
    """Evidence response schema."""
    id: str
    control_id: str
    uploaded_by_id: str
    title: str
    description: Optional[str] = None
    file_path: Optional[str] = None
    file_type: Optional[str] = None
    file_size: Optional[int] = None
    status: str
    reviewer_notes: Optional[str] = None
    ai_assessment: Optional[str] = None
    ai_confidence: Optional[float] = None
    created_at: datetime

    class Config:
        from_attributes = True


class EvidenceReview(BaseModel):
    """Evidence review schema."""
    status: str
    reviewer_notes: Optional[str] = None
