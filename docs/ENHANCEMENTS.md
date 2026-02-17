# Amana-GRC Enhancements

This document describes the optional enhancements added to Amana-GRC beyond the core implementation.

## Evidence File Upload

### Backend Implementation

**Endpoint:** `POST /api/v1/evidence/upload`

**Features:**
- Multipart file upload support
- File size validation (max 50MB)
- Automatic file naming with timestamps
- Supported formats: PDF, Word, Excel, Images
- Evidence metadata storage in MongoDB
- File storage in `uploads/evidence/` directory

**Usage:**
```bash
curl -X POST "http://localhost:8000/api/v1/evidence/upload" \
  -H "Authorization: Bearer <token>" \
  -F "file=@security-policy.pdf" \
  -F "control_id=507f1f77bcf86cd799439011" \
  -F "title=Security Policy Document" \
  -F "description=Updated security policy v2.1"
```

### Frontend Component

**Component:** [`EvidenceUploader.tsx`](frontend/src/components/compliance/EvidenceUploader.tsx)

**Features:**
- Drag-and-drop file upload
- File preview with size display
- Progress indication
- File type validation
- Bilingual labels

## Reporting & Export Features

### Export Service

**Service:** [`export_service.py`](backend/app/services/export_service.py)

Supports exporting:
- Risk register to CSV
- Controls to CSV (all or by standard)
- Audit reports with findings

### Export Endpoints

**Endpoints:**
- `GET /api/v1/export/risks` - Download risk register CSV
- `GET /api/v1/export/controls?standard_id=<id>` - Download controls CSV
- `GET /api/v1/export/audit/{audit_id}` - Download audit report

**CSV Format:**
- UTF-8 encoding with BOM for Excel compatibility
- Bilingual headers where applicable
- All data fields included

**Usage:**
```bash
# Export all risks
curl -H "Authorization: Bearer <token>" \
  http://localhost:8000/api/v1/export/risks -o risks.csv

# Export controls for specific standard
curl -H "Authorization: Bearer <token>" \
  "http://localhost:8000/api/v1/export/controls?standard_id=<id>" -o controls.csv

# Export audit report
curl -H "Authorization: Bearer <token>" \
  http://localhost:8000/api/v1/export/audit/<audit_id> -o audit_report.csv
```

## Email Notifications

### Notification Service

**Service:** [`notification_service.py`](backend/app/services/notification_service.py)

**Features:**
- SMTP email sending
- Bilingual email templates (Arabic + English)
- HTML email support
- Automatic notifications for:
  - Finding assignments
  - Overdue findings
  - Status changes

### Email Templates

**Finding Assignment:**
- Sent when a non-conformity is assigned to a user
- Includes audit details, finding description, severity, due date
- Both Arabic and English in same email

**Overdue Finding:**
- Sent when a finding passes its due date
- Urgent formatting with red highlighting
- Days overdue calculation

### Configuration

Add to `.env`:
```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
FROM_EMAIL=noreply@amana-grc.gov.sa
```

### Usage

```python
# In your code
from app.services.notification_service import NotificationService

notification_service = NotificationService()

# Notify about assignment
await notification_service.notify_finding_assigned(finding)

# Notify about overdue
await notification_service.notify_finding_overdue(finding)
```

## Compliance Trend Analytics

### Analytics Service

**Endpoint:** `GET /api/v1/analytics/compliance-trend?days=30`

**Features:**
- Compliance percentage over time
- Configurable time range (7-365 days)
- Historical tracking (requires snapshot implementation)
- Control implementation counts

**Response:**
```json
[
  {
    "date": "2024-01-01",
    "percentage": 75.5,
    "implemented_count": 150,
    "total_count": 199
  },
  ...
]
```

### Additional Analytics Endpoints

**Risk Trend:** `GET /api/v1/analytics/risk-trend?days=30`
- Total risks over time
- Open risks trend
- Critical risks trend

**Controls by Domain:** `GET /api/v1/analytics/controls-by-domain`
- Implementation percentage per domain
- Sorted by completion rate
- Bilingual domain names

### Frontend Component

**Component:** [`ComplianceTrendChart.tsx`](frontend/src/components/analytics/ComplianceTrendChart.tsx)

**Features:**
- Line chart visualization using Recharts
- 30-day compliance trend
- Start vs current comparison
- Responsive design
- Bilingual labels

## Advanced Search & Filtering

### Enhanced API Parameters

All list endpoints now support:

**Pagination:**
```
?skip=0&limit=20
```

**Sorting:**
```
?sort_by=created_at&sort_order=desc
```

**Text Search:**
```
?search=keyword
```

**Filtering:**
```
# Controls
?standard_id=<id>&priority=HIGH&status=IMPLEMENTED

# Risks
?risk_level=CRITICAL&status=OPEN&owner_id=<id>

# Evidence
?control_id=<id>&status=PENDING
```

### Examples

```bash
# Search risks containing "database"
GET /api/v1/risks?search=database

# Filter critical risks
GET /api/v1/risks?risk_level=CRITICAL&status=OPEN

# Get high-priority controls
GET /api/v1/controls?priority=HIGH

# Paginated evidence for a control
GET /api/v1/evidence?control_id=<id>&skip=0&limit=10
```

## Implementation Notes

### File Storage

**Local Storage:**
- Files stored in `uploads/evidence/` directory
- Automatic directory creation
- Unique filenames with timestamps

**Production Considerations:**
- Use S3/MinIO for cloud storage
- Implement file encryption at rest
- Add virus scanning for uploads
- Configure CDN for file delivery

### Email Delivery

**Development:**
- Uses SMTP with configurable settings
- Can use Gmail with app passwords
- Localhost SMTP for testing

**Production:**
- Use transactional email service (SendGrid, AWS SES)
- Implement email queue for reliability
- Track delivery status
- Add unsubscribe mechanism

### Analytics Data

**Current Implementation:**
- Shows current state projected over time range
- Simplified for initial release

**Future Enhancement:**
- Implement daily snapshots table
- Store historical compliance percentages
- Track changes over time
- Enable time-series analysis

## Testing

### Test Evidence Upload

```python
async def test_upload_evidence():
    with open("test.pdf", "rb") as f:
        response = await client.post(
            "/api/v1/evidence/upload",
            files={"file": ("test.pdf", f, "application/pdf")},
            data={"control_id": "<id>", "title": "Test Evidence"}
        )
    assert response.status_code == 201
```

### Test Export

```python
async def test_export_risks():
    response = await client.get("/api/v1/export/risks")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/csv"
```

## Security Considerations

1. **File Upload:**
   - Validate file types and sizes
   - Scan for malware
   - Sanitize filenames
   - Restrict access to uploaded files

2. **Email:**
   - Validate recipient addresses
   - Rate limit email sending
   - Log all email notifications
   - Use TLS for SMTP

3. **Export:**
   - Check user permissions before export
   - Log all export operations
   - Consider data sensitivity

## Future Enhancements

- **Advanced Analytics:** Machine learning for risk prediction
- **Real-time Notifications:** WebSocket for instant alerts
- **Document OCR:** Extract text from scanned documents for AI analysis
- **Integration APIs:** Connect with ticketing systems (Jira, ServiceNow)
- **Mobile App:** React Native mobile client
- **Advanced Reporting:** PDF reports with charts and branding
