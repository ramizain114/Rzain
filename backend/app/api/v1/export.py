"""Export endpoints for generating reports."""

from fastapi import APIRouter, Depends, Response
from app.services.export_service import ExportService
from app.api.deps import get_current_user
from app.core.exceptions import raise_not_found

router = APIRouter()


@router.get("/risks")
async def export_risks(current_user = Depends(get_current_user)):
    """Export all risks to CSV."""
    csv_data = await ExportService.export_risks_to_csv()

    return Response(
        content=csv_data,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=risks_export.csv"}
    )


@router.get("/controls")
async def export_controls(
    standard_id: str = None,
    current_user = Depends(get_current_user)
):
    """Export controls to CSV."""
    csv_data = await ExportService.export_controls_to_csv(standard_id)

    filename = f"controls_export_{standard_id or 'all'}.csv"
    return Response(
        content=csv_data,
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )


@router.get("/audit/{audit_id}")
async def export_audit_report(
    audit_id: str,
    current_user = Depends(get_current_user)
):
    """Export audit report with findings."""
    try:
        csv_data = await ExportService.export_audit_report(audit_id)

        return Response(
            content=csv_data,
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename=audit_report_{audit_id}.csv"}
        )
    except ValueError as e:
        raise_not_found(str(e))
