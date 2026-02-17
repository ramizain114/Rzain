"""Standards endpoints."""

from typing import List
from fastapi import APIRouter, Depends, status

from app.schemas.standard import StandardResponse
from app.models.standard import Standard
from app.api.deps import get_current_user
from app.core.exceptions import raise_not_found

router = APIRouter()


@router.get("/", response_model=List[StandardResponse], dependencies=[Depends(get_current_user)])
async def list_standards():
    """List all standards."""
    standards = await Standard.find(Standard.is_active == True).to_list()
    return [
        StandardResponse(
            id=str(std.id),
            code=std.code,
            name_en=std.name_en,
            name_ar=std.name_ar,
            description_en=std.description_en,
            description_ar=std.description_ar,
            version=std.version,
            category=std.category,
            is_active=std.is_active,
        )
        for std in standards
    ]


@router.get("/{standard_id}", response_model=StandardResponse, dependencies=[Depends(get_current_user)])
async def get_standard(standard_id: str):
    """Get standard by ID."""
    standard = await Standard.get(standard_id)
    if not standard:
        raise_not_found("Standard not found")

    return StandardResponse(
        id=str(standard.id),
        code=standard.code,
        name_en=standard.name_en,
        name_ar=standard.name_ar,
        description_en=standard.description_en,
        description_ar=standard.description_ar,
        version=standard.version,
        category=standard.category,
        is_active=standard.is_active,
    )
