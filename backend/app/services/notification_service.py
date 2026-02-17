"""Notification service for sending email alerts."""

import logging
from typing import List, Optional
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

from app.config import settings
from app.models.user import User
from app.models.nonconformity import NonConformity

logger = logging.getLogger(__name__)


class NotificationService:
    """Service for sending email notifications."""

    def __init__(self):
        # Email configuration (would be in settings)
        self.smtp_host = getattr(settings, 'smtp_host', 'localhost')
        self.smtp_port = getattr(settings, 'smtp_port', 587)
        self.smtp_user = getattr(settings, 'smtp_user', '')
        self.smtp_password = getattr(settings, 'smtp_password', '')
        self.from_email = getattr(settings, 'from_email', 'noreply@amana-grc.gov.sa')

    async def send_email(
        self,
        to_email: str,
        subject: str,
        body_html: str,
        body_text: Optional[str] = None
    ) -> bool:
        """Send an email."""
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.from_email
            msg['To'] = to_email

            # Add plain text version
            if body_text:
                msg.attach(MIMEText(body_text, 'plain', 'utf-8'))

            # Add HTML version
            msg.attach(MIMEText(body_html, 'html', 'utf-8'))

            # Send email
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                if self.smtp_user and self.smtp_password:
                    server.starttls()
                    server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)

            logger.info(f"Email sent to {to_email}: {subject}")
            return True

        except Exception as e:
            logger.error(f"Failed to send email to {to_email}: {e}")
            return False

    async def notify_finding_assigned(self, finding: NonConformity):
        """Notify user when a finding is assigned to them."""
        if not finding.assigned_to:
            return

        # Fetch user
        await finding.fetch_all_links()
        user = finding.assigned_to
        audit = finding.audit

        subject_en = f"New Finding Assigned: {audit.audit_id}"
        subject_ar = f"نتيجة جديدة تم تعيينها: {audit.audit_id}"

        body_html = f"""
        <html>
            <body style="font-family: Arial, sans-serif; direction: ltr;">
                <h2>New Finding Assigned</h2>
                <p>Dear {user.full_name_en},</p>
                <p>A new finding has been assigned to you:</p>
                <ul>
                    <li><strong>Audit:</strong> {audit.title_en}</li>
                    <li><strong>Finding:</strong> {finding.finding}</li>
                    <li><strong>Severity:</strong> {finding.severity.value}</li>
                    <li><strong>Due Date:</strong> {finding.due_date.strftime('%Y-%m-%d') if finding.due_date else 'Not set'}</li>
                </ul>
                <p>Please log in to Amana-GRC to review and take action.</p>
                
                <hr style="margin: 20px 0;">
                
                <div style="direction: rtl; font-family: 'IBM Plex Sans Arabic', Arial, sans-serif;">
                    <h2>نتيجة جديدة تم تعيينها</h2>
                    <p>عزيزي {user.full_name_ar}،</p>
                    <p>تم تعيين نتيجة جديدة لك:</p>
                    <ul>
                        <li><strong>التدقيق:</strong> {audit.title_ar}</li>
                        <li><strong>النتيجة:</strong> {finding.finding}</li>
                        <li><strong>الخطورة:</strong> {finding.severity.value}</li>
                        <li><strong>تاريخ الاستحقاق:</strong> {finding.due_date.strftime('%Y-%m-%d') if finding.due_date else 'غير محدد'}</li>
                    </ul>
                    <p>يرجى تسجيل الدخول إلى أمانة للحوكمة والمخاطر والامتثال للمراجعة واتخاذ الإجراءات.</p>
                </div>
            </body>
        </html>
        """

        await self.send_email(user.email, subject_en, body_html)

    async def notify_finding_overdue(self, finding: NonConformity):
        """Notify when a finding is overdue."""
        if not finding.assigned_to or not finding.due_date:
            return

        await finding.fetch_all_links()
        user = finding.assigned_to
        audit = finding.audit

        subject = f"⚠️ Overdue Finding: {audit.audit_id}"

        body_html = f"""
        <html>
            <body style="font-family: Arial, sans-serif;">
                <h2 style="color: #dc2626;">⚠️ Overdue Finding Alert</h2>
                <p>Dear {user.full_name_en},</p>
                <p>The following finding is <strong>overdue</strong>:</p>
                <ul>
                    <li><strong>Audit:</strong> {audit.title_en}</li>
                    <li><strong>Finding:</strong> {finding.finding}</li>
                    <li><strong>Severity:</strong> {finding.severity.value}</li>
                    <li><strong>Due Date:</strong> {finding.due_date.strftime('%Y-%m-%d')}</li>
                    <li><strong>Days Overdue:</strong> {(datetime.now() - finding.due_date).days}</li>
                </ul>
                <p><strong>Immediate action required.</strong></p>
            </body>
        </html>
        """

        await self.send_email(user.email, subject, body_html)
