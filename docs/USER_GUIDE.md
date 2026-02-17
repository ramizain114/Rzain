# Amana-GRC User Guide

## Getting Started

### First Login

1. Navigate to `http://localhost:3000`
2. Login with default admin credentials:
   - Username: `admin`
   - Password: (from `.env` - default is `changeme`)
3. **Important:** Change the default password immediately

### Language Switching

Click the language toggle in the top-right corner to switch between Arabic and English. The entire interface, including layout direction, will update instantly.

## Modules

### 📊 Dashboard

The dashboard provides an at-a-glance view of your organization's GRC posture:

- **Compliance Score:** Percentage of implemented controls
- **Open Risks:** Number and severity of active risks
- **Pending Audits:** Active audit engagements
- **Quick Overview:** Summary statistics

### 🛡️ Compliance Management

Track compliance with Saudi regulatory standards:

**Features:**
- View all loaded standards (NCA-ECC, NCA-CSCC, NDMO, SDAIA)
- Browse controls by standard and domain
- Update implementation status
- Upload evidence documents
- Track evidence review status

**Workflow:**
1. Select a standard to view its controls
2. Update implementation status for each control
3. Upload supporting evidence
4. Submit for auditor review

### ⚠️ Risk Register

Manage organizational risks using ISO 31000 methodology:

**Features:**
- Create, view, update, and delete risks
- 5×5 risk matrix visualization
- Risk heatmap by severity level
- Three view modes: Table, Matrix, Heatmap

**Risk Assessment:**
- Define asset, threat, and vulnerability
- Rate impact and likelihood (1-5 scale)
- System auto-calculates risk score (Impact × Likelihood)
- Assign risk level (Very Low → Critical)
- Select treatment strategy (Accept, Mitigate, Transfer, Avoid)

**Risk Matrix:**
- Visual representation of all risks
- Color-coded by severity
- Interactive cells show risk count

### ✅ Audit Management

Conduct compliance audits:

**Features:**
- Create audit engagements
- Assign lead auditor and team
- Track audit status (Planned → In Progress → Completed → Closed)
- Record findings as non-conformities
- Manage corrective actions

**Audit Workflow:**
1. Plan audit (scope, dates, team)
2. Conduct audit activities
3. Document findings
4. Track corrective actions
5. Close audit

### 🤖 AI Auditor (vLLM Integration)

Leverage AI to assist with evidence analysis:

**Features:**
- Upload evidence text
- Select control to check compliance against
- Receive AI assessment in both languages
- View confidence score
- Get recommendations

**How It Works:**
1. The AI analyzes evidence against control requirements
2. Returns compliance status (Compliant, Partial, Non-Compliant)
3. Provides reasoning in Arabic and English
4. Suggests improvements if needed

**Note:** Requires vLLM server to be running and configured.

## User Roles

### Admin
- Full system access
- User management
- System configuration
- All CRUD operations

### Risk Officer
- Full risk register access
- Upload evidence
- Update control implementation status
- Use AI auditor

### Auditor
- Conduct audits
- Review evidence
- Create findings
- Manage non-conformities
- Use AI auditor

### Viewer
- Read-only access to all modules
- View dashboards and reports
- No edit or create permissions

## Best Practices

### Compliance Management
1. Start by seeding Saudi standards
2. Review all controls relevant to your organization
3. Mark non-applicable controls as such
4. Prioritize CRITICAL and HIGH priority controls
5. Upload evidence for all implemented controls

### Risk Management
1. Conduct regular risk assessments
2. Keep risk register up to date
3. Review risks quarterly
4. Track risk treatment progress
5. Escalate CRITICAL risks immediately

### Audit Workflow
1. Plan audits annually or per regulatory requirements
2. Assign qualified auditors
3. Document all findings with evidence
4. Set realistic due dates for corrective actions
5. Follow up on action completion

## Troubleshooting

### Cannot Login
- **LDAP users:** Contact IT for Active Directory access
- **Local users:** Contact admin for account creation
- **Locked account:** Contact admin to reactivate

### Missing Data
- Run seeders: `docker-compose exec backend python -m app.seeders.run_seeders --all`
- Check database connection in backend logs

### AI Features Not Working
- Verify `VLLM_BASE_URL` in `.env`
- Check vLLM server is running
- Review backend logs for connection errors

### RTL Layout Issues
- Clear browser cache
- Ensure you're using a modern browser (Chrome, Firefox, Edge, Safari)
- Check `tailwindcss-rtl` plugin is installed

## Support

For technical issues or questions:
- Check documentation in `docs/` directory
- Review API documentation at `http://localhost:8000/docs`
- Contact system administrator
