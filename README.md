# Amana-GRC: Governance, Risk, and Compliance Platform

Enterprise-grade GRC platform built for Saudi municipal government use, featuring bilingual Arabic/English support with full RTL, local AI capabilities, and pre-loaded Saudi regulatory standards.

## 🏗️ Architecture

- **Backend:** FastAPI (Python 3.12+) with Beanie ODM
- **Database:** MongoDB 7+
- **Cache:** Redis 7
- **Frontend:** React 18 + Vite + TypeScript
- **UI:** shadcn/ui + Tailwind CSS v4 (RTL-ready)
- **State:** TanStack Query + Zustand
- **Auth:** JWT + LDAP (Active Directory integration)
- **AI:** vLLM serving Qwen3-Coder-MoE FP8 (OpenAI-compatible API)
- **Icons:** Lucide React

## 📋 Features

### Core Modules
- **Compliance Management:** Control mapping, evidence collection, status tracking
- **Risk Register:** ISO 31000-aligned risk assessment with 5x5 matrix visualization
- **Audit Workflow:** Planning, execution, findings, corrective actions
- **AI Auditor:** Automated evidence analysis and compliance suggestions
- **Dashboard:** Real-time compliance scores, risk heatmaps, audit metrics

### Saudi Regulatory Standards (Pre-loaded)
- ✅ **NCA-ECC:** Essential Cybersecurity Controls (~114 controls)
- ✅ **NCA-CSCC:** Cloud Security Controls (~73 controls)
- ✅ **NDMO:** Data Management Standards (~50 controls)
- ✅ **SDAIA:** AI Ethics Guidelines (~30 controls)

### Internationalization
- **Dual-language:** Arabic (RTL) and English (LTR)
- **Dynamic switching:** Instant language toggle with layout mirroring
- **Font:** IBM Plex Sans Arabic for optimal Arabic rendering

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 20+ (for local frontend development)
- Python 3.12+ (for local backend development)
- vLLM server running separately (for AI features)

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/ramizain114/Rzain.git
cd Rzain
```

2. **Configure environment:**
```bash
cp .env.example .env
# Edit .env with your LDAP, vLLM, and other settings
```

3. **Start services:**
```bash
docker-compose up -d
```

4. **Run database seeders:**
```bash
docker-compose exec backend python -m app.seeders.run_seeders --all
```

5. **Create initial admin user:**
```bash
docker-compose exec backend python -m app.seeders.create_admin
```

6. **Access the application:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 🔧 Development

### Backend Development
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Development
```bash
cd frontend
npm install
npm run dev
```

### Run Tests
```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## 📦 Project Structure

```
amana-grc/
├── backend/                # FastAPI application
│   ├── app/
│   │   ├── models/        # Beanie document models
│   │   ├── schemas/       # Pydantic request/response schemas
│   │   ├── api/           # Route handlers
│   │   ├── services/      # Business logic
│   │   ├── core/          # Security, middleware, exceptions
│   │   └── seeders/       # Data seeders for Saudi standards
│   └── tests/
├── frontend/              # React SPA
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Page components
│   │   ├── api/           # TanStack Query hooks
│   │   ├── stores/        # Zustand state stores
│   │   └── lib/           # Utilities
│   └── public/locales/    # i18n translation files
└── docs/                  # Documentation
```

## 🔐 Authentication

The platform supports dual authentication:
1. **LDAP/Active Directory:** Primary authentication for municipal users
2. **Local Admin Fallback:** MongoDB-stored admin accounts for emergency access

## 🤖 AI Integration

The AI Auditor uses vLLM (OpenAI-compatible API) to:
- Analyze uploaded evidence against control requirements
- Generate compliance suggestions in both Arabic and English
- Provide confidence scores and recommendations

**Note:** vLLM must be running separately on GPU hardware. Configure `VLLM_BASE_URL` in `.env`.

## 🌍 Internationalization (i18n)

The platform fully supports:
- **Arabic (ar):** RTL layout with proper text rendering
- **English (en):** LTR layout

Language can be switched instantly via the UI toggle. All user-facing content, including data from the database, is bilingual.

## 📊 RBAC Roles

| Role | Permissions |
|------|-------------|
| **Admin** | Full system access, user management, settings |
| **Risk Officer** | Risk register CRUD, evidence upload, compliance updates |
| **Auditor** | Audit workflow, evidence review, findings management |
| **Viewer** | Read-only access to all modules |

## 🛠️ Technology Stack

### Backend
- FastAPI 0.115+
- Beanie ODM 1.27+
- Motor (async MongoDB driver)
- ldap3 (LDAP/AD integration)
- PyJWT (JWT tokens)
- Redis-py
- httpx (vLLM client)

### Frontend
- React 18.3+
- Vite 6+
- TypeScript 5.7+
- TanStack Query 5+
- Zustand 5+
- shadcn/ui
- Tailwind CSS 4+
- i18next
- Lucide React
- Recharts

## 📝 License

[Add your license here]

## 🤝 Contributing

[Add contribution guidelines]

## 📧 Support

For issues and questions, please contact the development team.
