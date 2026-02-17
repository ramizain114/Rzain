"""Export service for generating reports."""

import csv
import io
from typing import List
from datetime import datetime

from app.models.risk import Risk
from app.models.control import Control
from app.models.audit import Audit


class ExportService:
    """Service for exporting data to various formats."""

    @staticmethod
    async def export_risks_to_csv() -> str:
        """Export all risks to CSV format."""
        risks = await Risk.find_all().to_list()

        output = io.StringIO()
        writer = csv.writer(output)

        # Header
        writer.writerow([
            'Risk ID', 'Title (EN)', 'Title (AR)', 'Asset', 'Threat',
            'Vulnerability', 'Impact', 'Likelihood', 'Risk Score',
            'Risk Level', 'Treatment', 'Status', 'Created At'
        ])

        # Data rows
        for risk in risks:
            writer.writerow([
                risk.risk_id,
                risk.title_en,
                risk.title_ar,
                risk.asset,
                risk.threat,
                risk.vulnerability,
                risk.impact_score,
                risk.likelihood_score,
                risk.risk_score,
                risk.risk_level.value,
                risk.treatment.value,
                risk.status,
                risk.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            ])

        return output.getvalue()

    @staticmethod
    async def export_controls_to_csv(standard_id: str = None) -> str:
        """Export controls to CSV format."""
        query = Control.find()
        if standard_id:
            query = query.find(Control.standard.ref.id == standard_id)

        controls = await query.to_list()

        output = io.StringIO()
        writer = csv.writer(output)

        # Header
        writer.writerow([
            'Control ID', 'Domain (EN)', 'Domain (AR)', 'Title (EN)',
            'Title (AR)', 'Priority', 'Implementation Status', 'Created At'
        ])

        # Data rows
        for control in controls:
            writer.writerow([
                control.control_id,
                control.domain_en,
                control.domain_ar,
                control.title_en,
                control.title_ar,
                control.priority,
                control.implementation_status.value,
                control.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            ])

        return output.getvalue()

    @staticmethod
    async def export_audit_report(audit_id: str) -> str:
        """Export audit report with findings."""
        from app.models.nonconformity import NonConformity

        audit = await Audit.get(audit_id)
        if not audit:
            raise ValueError("Audit not found")

        findings = await NonConformity.find(
            NonConformity.audit.ref.id == audit_id
        ).to_list()

        output = io.StringIO()
        writer = csv.writer(output)

        # Header
        writer.writerow(['Audit Report'])
        writer.writerow(['Audit ID:', audit.audit_id])
        writer.writerow(['Title:', audit.title_en])
        writer.writerow(['Status:', audit.status.value])
        writer.writerow(['Start Date:', audit.start_date.strftime('%Y-%m-%d')])
        writer.writerow([])
        writer.writerow(['Findings'])
        writer.writerow([
            'Finding', 'Severity', 'Status', 'Corrective Action', 'Due Date'
        ])

        # Findings
        for finding in findings:
            writer.writerow([
                finding.finding,
                finding.severity.value,
                finding.status.value,
                finding.corrective_action or 'N/A',
                finding.due_date.strftime('%Y-%m-%d') if finding.due_date else 'N/A',
            ])

        return output.getvalue()
