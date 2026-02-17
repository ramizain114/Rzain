# Amana-GRC Quick Start Guide

Get Amana-GRC running in 5 minutes!

## Option 1: Automated Setup (Recommended)

```bash
./START_TESTING.sh
```

This script will:
1. Start all Docker services
2. Create the admin user
3. Load all Saudi standards
4. Display access URLs and credentials

Then open http://localhost:3000 and login!

## Option 2: Manual Setup

### Step 1: Start Services
```bash
docker-compose up -d
```

### Step 2: Initialize Database
```bash
# Create admin user
docker-compose exec backend python -m app.seeders.create_admin

# Load Saudi standards (267 controls)
docker-compose exec backend python -m app.seeders.run_seeders --all
```

### Step 3: Access Application
- **Frontend:** http://localhost:3000
- **Backend:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs

### Step 4: Login
- **Username:** `admin`
- **Password:** `Admin@123456`

## What You'll See

### Dashboard
- Compliance score percentage
- Open risks count
- Pending audits count
- Quick overview statistics

### Compliance Module
- 4 Saudi regulatory standards
- 267 bilingual controls
- Implementation status tracking
- Evidence upload capability

### Risk Register
- Risk entry form with ISO 31000 fields
- Interactive 5×5 risk matrix
- Risk heatmap visualization
- Three view modes

### Audit Module
- Audit workflow management
- Status tracking
- Findings management

## Test the Bilingual UI

1. Click the language toggle (top-right corner)
2. UI switches from English → Arabic (RTL)
3. Notice:
   - Text aligns right
   - Sidebar mirrors to right side
   - All content in Arabic
4. Click again → back to English (LTR)

## Verify Saudi Standards Loaded

### Via API:
```bash
curl http://localhost:8000/api/v1/standards
```

### Via MongoDB:
```bash
docker-compose exec mongodb mongosh amana_grc --eval "db.standards.find().pretty()"
```

### Via Frontend:
Navigate to Compliance page and select a standard.

## Create Your First Risk

1. Go to Risk Register
2. Click "Add Risk" button
3. Fill the form (both English and Arabic fields)
4. Set Impact: 4, Likelihood: 3
5. Watch risk score calculate automatically (4 × 3 = 12)
6. Risk level will be "MEDIUM"
7. Click Save
8. View in Matrix and Heatmap

## Check Backend Health

```bash
# Simple health check
curl http://localhost:8000/health

# Should return:
# {"status":"healthy","version":"0.1.0"}
```

## View Logs

```bash
# All services
docker-compose logs -f

# Just backend
docker-compose logs -f backend

# Just frontend  
docker-compose logs -f frontend
```

## Stop Services

```bash
# Stop but keep data
docker-compose down

# Stop and remove all data
docker-compose down -v
```

## Troubleshooting

### Services won't start
```bash
# Rebuild containers
docker-compose build
docker-compose up -d
```

### Can't login
```bash
# Recreate admin user
docker-compose exec backend python -m app.seeders.create_admin
```

### No standards showing
```bash
# Re-run seeders
docker-compose exec backend python -m app.seeders.run_seeders --all
```

### Port conflicts
Edit `docker-compose.yml` and change port mappings:
- Backend: `"8001:8000"` instead of `"8000:8000"`
- Frontend: `"3001:3000"` instead of `"3000:3000"`

## Next Steps

After basic testing:
1. Read [`TESTING_GUIDE.md`](TESTING_GUIDE.md) for detailed test scenarios
2. Review [`docs/USER_GUIDE.md`](docs/USER_GUIDE.md) for feature documentation
3. Check [`docs/API.md`](docs/API.md) for API reference
4. See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for technical details

## Support

- **Documentation:** `docs/` directory
- **Interactive API:** http://localhost:8000/docs
- **Issues:** GitHub repository issues

Enjoy testing Amana-GRC! 🎉
