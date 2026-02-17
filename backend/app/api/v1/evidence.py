"""Evidence management endpoints."""

from typing import List
from fastapi import APIRouter, Depends, UploadFile, File, status
from datetime import datetime
import os
import aiofiles

from app.schemas.evidence import EvidenceCreate, EvidenceResponse, EvidenceReview
from app.models.evidence import Evidence, EvidenceStatus
from app.models.control import Control
from app.models.user import User, Role
from app.api.deps import get_current_user, require_role
from app.core.exceptions import raise_not_found, raise_bad_request
from app.config import settings

router = APIRouter()

# Evidence upload directory
UPLOAD_DIR = "uploads/evidence"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload", response_model=EvidenceResponse, status_code=status.HTTP_201_CREATED)
async def upload_evidence(
    control_id: str,
    title: str,
    description: str = "",
    file: UploadFile = File(...),
    current_user=Depends(require_role(Role.ADMIN, Role.RISK_OFFICER, Role.AUDITOR)),
):
    """Upload evidence file for a control."""
    # Validate control exists
    control = await Control.get(control_id)
    if not control:
        raise_bad_request("Control not found")

    # Validate file size (max 50MB)
    max_size = 50 * 1024 * 1024
    file.file.seek(0, 2)  # Seek to end
    file_size = file.file.tell()
    file.file.seek(0)  # Reset to start

    if file_size > max_size:
        raise_bad_request("File size exceeds 50MB limit")

    # Generate unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    # Save file
    async with aiofiles.open(file_path, 'wb') as f:
        content = await file.read()
        await f.write(content)

    # Create evidence record
    evidence = Evidence(
        control=control,
        uploaded_by=current_user,
        title=title,
        description=description,
        file_path=file_path,
        file_type=file.content_type,
        file_size=file_size,
        status=EvidenceStatus.PENDING,
    )
    await evidence.insert()

    return EvidenceResponse(
        id=str(evidence.id),
        control_id=str(evidence.control.ref.id),
        uploaded_by_id=str(evidence.uploaded_by.ref.id),
        title=evidence.title,
        description=evidence.description,
        file_path=evidence.file_path,
        file_type=evidence.file_type,
        file_size=evidence.file_size,
        status=evidence.status.value,
        reviewer_notes=evidence.reviewer_notes,
        ai_assessment=evidence.ai_assessment,
        ai_confidence=evidence.ai_confidence,
        created_at=evidence.created_at,
    )


@router.get("/", response_model=List[EvidenceResponse], dependencies=[Depends(get_current_user)])
async def list_evidence(control_id: str = None):
    """List evidence, optionally filtered by control."""
    query = Evidence.find()
    
    if control_id:
        query = query.find(Evidence.control.ref.id == control_id)
    
    evidence_list = await query.to_list()

    return [
        EvidenceResponse(
            id=str(e.id),
            control_id=str(e.control.ref.id),
            uploaded_by_id=str(e.uploaded_by.ref.id),
            title=e.title,
            description=e.description,
            file_path=e.file_path,
            file_type=e.file_type,
            file_size=e.file_size,
            status=e.status.value,
            reviewer_notes=e.reviewer_notes,
            ai_assessment=e.ai_assessment,
            ai_confidence=e.ai_confidence,
            created_at=e.created_at,
        )
        for e in evidence_list
    ]


@router.patch("/{evidence_id}/review", response_model=EvidenceResponse)
async def review_evidence(
    evidence_id: str,
    review: EvidenceReview,
    current_user=Depends(require_role(Role.ADMIN, Role.AUDITOR)),
):
    """Review evidence (approve or reject)."""
    evidence = await Evidence.get(evidence_id)
    if not evidence:
        raise_not_found("Evidence not found")

    evidence.status = EvidenceStatus(review.status)
    evidence.reviewer_notes = review.reviewer_notes
    evidence.updated_at = datetime.utcnow()
    await evidence.save()

    return EvidenceResponse(
        id=str(evidence.id),
        control_id=str(evidence.control.ref.id),
        uploaded_by_id=str(evidence.uploaded_by.ref.id),
        title=evidence.title,
        description=evidence.description,
        file_path=evidence.file_path,
        file_type=evidence.file_type,
        file_size=evidence.file_size,
        status=evidence.status.value,
        reviewer_notes=evidence.reviewer_notes,
        ai_assessment=evidence.ai_assessment,
        ai_confidence=evidence.ai_confidence,
        created_at=evidence.created_at,
    )
