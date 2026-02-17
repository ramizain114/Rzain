# Amana-GRC Testing Guide

This guide will help you run and test the Amana-GRC platform locally.

## Prerequisites

Ensure you have installed:
- Docker & Docker Compose (for backend services)
- Node.js 20+ (for frontend development)
- Python 3.12+ (optional, for local backend development)

## Quick Start (Docker)

### 1. Start All Services

```bash
# Start MongoDB, Redis, Backend, and Frontend
docker-compose up -d

# View logs
docker-compose logs -f
```

This will start:
- **MongoDB** on port 27017
- **Redis** on port 6379
- **Backend API** on port 8000
- **Frontend** on port 3000

### 2. Create Admin User

```bash
docker-compose exec backend python -m app.seeders.create_admin
```

**Default Credentials:**
- Username: `admin`
- Password: `Admin@123456`
- Email: `admin@municipality.gov.sa`

### 3. Load Saudi Standards

```bash
# Load all 4 standards (267 controls)
docker-compose exec backend python -m app.seeders.run_seeders --all
```

This will seed:
- NCA-ECC (114 controls)
- NCA-CSCC (73 controls)
- NDMO (50 controls)
- SDAIA (30 controls)

### 4. Access the Application

**Frontend:** http://localhost:3000
- Login with admin credentials
- Switch language (English ↔ Arabic)
- Explore all modules

**Backend API Docs:** http://localhost:8000/docs
- Interactive OpenAPI documentation
- Try endpoints directly
- View request/response schemas

**Backend Alternative Docs:** http://localhost:8000/redoc
- ReDoc documentation interface

## Testing Checklist

### ✅ Authentication
- [ ] Login with admin credentials
- [ ] Verify JWT token is stored
- [ ] Access protected routes
- [ ] Logout and verify redirect to login

### ✅ Language & RTL
- [ ] Click language toggle (top-right)
- [ ] Verify UI switches to Arabic with RTL layout
- [ ] Check sidebar navigation mirrors
- [ ] Verify text alignment changes
- [ ] Switch back to English (LTR)

### ✅ Dashboard
- [ ] View compliance score percentage
- [ ] Check risk summary card
- [ ] View audit summary card
- [ ] Verify metrics update from database

### ✅ Compliance Module
- [ ] Navigate to Compliance page
- [ ] View loaded standards
- [ ] Browse controls by standard
- [ ] Check bilingual control descriptions

### ✅ Risk Register
- [ ] Navigate to Risk Register
- [ ] Switch view modes: Table → Matrix → Heatmap
- [ ] Click "Add Risk" button
- [ ] Fill risk form (bilingual)
- [ ] Verify risk score auto-calculation
- [ ] Save risk (requires owner_id - use admin user ID)
- [ ] View risk in matrix and heatmap

### ✅ Audit Module
- [ ] Navigate to Audits page
- [ ] View audit status statistics
- [ ] Check bilingual labels

### ✅ Backend API
- [ ] Visit http://localhost:8000/docs
- [ ] Test health endpoint: `GET /health`
- [ ] Test login: `POST /api/v1/auth/login`
- [ ] Test standards list: `GET /api/v1/standards`
- [ ] Test risks list: `GET /api/v1/risks`
- [ ] Verify OpenAPI schema

## Manual Testing Scenarios

### Scenario 1: Create a Risk

1. Login as admin
2. Go to Risk Register
3. Click "Add Risk"
4. Fill in the form:
   - **Title (EN):** "Unauthorized Database Access"
   - **Title (AR):** "وصول غير مصرح به إلى قاعدة البيانات"
   - **Description (EN):** "Risk of unauthorized access to production database"
   - **Description (AR):** "مخاطر الوصول غير المصرح به إلى قاعدة الإنتاج"
   - **Asset:** "Production Database"
   - **Threat:** "External Attacker"
   - **Vulnerability:** "Weak Authentication"
   - **Impact:** 5
   - **Likelihood:** 4
   - **Treatment:** Mitigate
5. Verify risk score = 20, level = HIGH
6. Save and verify in table/matrix

### Scenario 2: Test Bilingual UI

1. Login and go to Dashboard
2. Note current language (English)
3. Click language toggle (top-right)
4. Verify:
   - UI switches to Arabic
   - Text aligns right
   - Navigation items flip
   - All text translated
5. Click toggle again → back to English

### Scenario 3: Browse Saudi Standards

1. Go to Compliance page
2. API call: `GET http://localhost:8000/api/v1/standards`
3. Select NCA-ECC standard
4. View controls: `GET http://localhost:8000/api/v1/controls?standard_id=<id>`
5. Check bilingual control descriptions
6. Note priority levels (CRITICAL, HIGH, etc.)

## Development Mode Testing

### Backend (Python)

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest -v

# Run development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Access:** http://localhost:8000

### Frontend (React)

```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

**Access:** http://localhost:5173 (Vite dev server)

## API Testing with curl

### Login
```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "Admin@123456"}'
```

Copy the `access_token` from the response.

### Get User Profile
```bash
curl http://localhost:8000/api/v1/auth/me \
  -H "Authorization: Bearer <your_access_token>"
```

### List Standards
```bash
curl http://localhost:8000/api/v1/standards \
  -H "Authorization: Bearer <your_access_token>"
```

### List Risks
```bash
curl http://localhost:8000/api/v1/risks \
  -H "Authorization: Bearer <your_access_token>"
```

### Get Dashboard Summary
```bash
curl http://localhost:8000/api/v1/dashboard/summary \
  -H "Authorization: Bearer <your_access_token>"
```

## Database Verification

### Check MongoDB Data

```bash
# Connect to MongoDB
docker-compose exec mongodb mongosh amana_grc

# List standards
db.standards.find()

# Count controls
db.controls.countDocuments()

# List users
db.users.find()
```

Expected:
- 4 standards (NCA-ECC, NCA-CSCC, NDMO, SDAIA)
- 267 controls total
- 1 admin user

## Troubleshooting

### Backend Won't Start

**Check logs:**
```bash
docker-compose logs backend
```

**Common issues:**
- MongoDB not ready → Wait a few seconds and restart
- Port 8000 in use → Change port in docker-compose.yml
- Missing dependencies → Rebuild: `docker-compose build backend`

### Frontend Won't Start

**Check logs:**
```bash
docker-compose logs frontend
```

**Common issues:**
- Backend not available → Check backend is running on port 8000
- Port 3000 in use → Change port in docker-compose.yml
- Build errors → See TypeScript errors (expected in Docker until npm install runs locally)

### Can't Login

**Verify admin user exists:**
```bash
docker-compose exec backend python -m app.seeders.create_admin
```

**Check MongoDB:**
```bash
docker-compose exec mongodb mongosh amana_grc --eval "db.users.find()"
```

### No Standards/Controls

**Run seeders:**
```bash
docker-compose exec backend python -m app.seeders.run_seeders --all
```

**Verify:**
```bash
docker-compose exec mongodb mongosh amana_grc --eval "db.standards.countDocuments()"
docker-compose exec mongodb mongosh amana_grc --eval "db.controls.countDocuments()"
```

## Performance Testing

### Load Test with Apache Bench

```bash
# Test health endpoint
ab -n 1000 -c 10 http://localhost:8000/health

# Test authenticated endpoint (requires valid token)
ab -n 100 -c 5 -H "Authorization: Bearer <token>" \
  http://localhost:8000/api/v1/standards
```

## Clean Up

### Stop Services
```bash
docker-compose down
```

### Remove All Data
```bash
docker-compose down -v
```

### Reset Database
```bash
docker-compose exec mongodb mongosh amana_grc --eval "db.dropDatabase()"
docker-compose exec backend python -m app.seeders.run_seeders --all --reset
```

## Expected Test Results

After setup, you should see:

✅ **Backend API:** http://localhost:8000
- OpenAPI docs functional
- Health check returns `{"status": "healthy"}`
- 40+ endpoints documented

✅ **Frontend:** http://localhost:3000
- Login page displays
- Admin login successful
- Dashboard shows metrics
- Language toggle works (EN ↔ AR)
- All navigation links functional

✅ **Database:**
- 4 standards
- 267 controls
- 1 admin user
- Collections properly indexed

✅ **Features Working:**
- Authentication (login/logout)
- Dashboard metrics
- Risk register (table/matrix/heatmap views)
- Bilingual support with RTL
- API endpoints responding

## Known Limitations (Development Mode)

1. **vLLM AI Service:** Not included in docker-compose (requires GPU hardware)
   - AI features will show graceful degradation
   - Core functionality works without AI

2. **LDAP Server:** Not included in docker-compose
   - Use local admin account for testing
   - LDAP can be added separately if needed

3. **Email Service:** Requires SMTP configuration
   - Notifications will log errors if not configured
   - Optional feature

## Next Steps After Testing

1. Review all modules and features
2. Test with your own data
3. Configure LDAP for your Active Directory
4. Set up vLLM server for AI features
5. Configure email notifications
6. Deploy to production environment

## Support

- **Documentation:** See `docs/` directory
- **API Reference:** http://localhost:8000/docs
- **Issues:** Create GitHub issue in repository
