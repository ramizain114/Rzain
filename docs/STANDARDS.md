# Saudi Regulatory Standards

Amana-GRC comes pre-loaded with controls from four major Saudi regulatory frameworks.

## Included Standards

### 1. NCA-ECC: Essential Cybersecurity Controls

**Authority:** National Cybersecurity Authority (NCA)  
**Version:** 2.0  
**Controls:** ~114 across 5 domains  
**Code:** `NCA-ECC`

**Domains:**
1. Cybersecurity Governance
2. Cybersecurity Risk Management
3. Cybersecurity Framework
4. Cybersecurity Operations
5. Third-Party Cybersecurity

**Purpose:** Foundational cybersecurity controls for all Saudi organizations.

**Key Controls:**
- ECC-1-1: Cybersecurity Strategy
- ECC-2-1: Risk Assessment
- ECC-3-2: Access Control
- ECC-4-1: Incident Management
- ECC-5-1: Third-Party Risk Assessment

---

### 2. NCA-CSCC: Cloud Security Controls

**Authority:** National Cybersecurity Authority (NCA)  
**Version:** 1.0  
**Controls:** ~73 cloud-specific controls  
**Code:** `NCA-CSCC`

**Domains:**
1. Cloud Governance
2. Data Security in Cloud
3. Identity and Access Management
4. Cloud Infrastructure Security
5. Cloud Security Monitoring

**Purpose:** Supplementary controls for organizations using cloud services.

**Key Controls:**
- CSCC-1-2: Cloud Service Provider Assessment
- CSCC-2-2: Encryption in Transit and at Rest
- CSCC-2-3: Data Residency
- CSCC-3-1: Cloud Identity Management
- CSCC-5-2: Threat Detection

---

### 3. NDMO: Data Management Standards

**Authority:** National Data Management Office (NDMO)  
**Version:** 1.0  
**Controls:** ~50 data governance controls  
**Code:** `NDMO`

**Domains:**
1. Data Governance
2. Data Classification
3. Data Quality
4. Data Lifecycle Management
5. Data Privacy
6. Data Sharing

**Purpose:** Data governance and management best practices.

**Key Controls:**
- NDMO-1-1: Data Governance Framework
- NDMO-2-1: Data Classification Policy
- NDMO-3-1: Data Quality Standards
- NDMO-4-1: Data Retention Policy
- NDMO-5-1: Privacy Impact Assessment

---

### 4. SDAIA: AI Ethics Guidelines

**Authority:** Saudi Data & AI Authority (SDAIA)  
**Version:** 1.0  
**Controls:** ~30 AI ethics controls  
**Code:** `SDAIA`

**Domains:**
1. AI Governance
2. Fairness and Non-Discrimination
3. Transparency and Explainability
4. Privacy and Data Protection
5. Safety and Security
6. Accountability

**Purpose:** Ethical and responsible AI development and deployment.

**Key Controls:**
- SDAIA-1-1: AI Ethics Framework
- SDAIA-2-1: Bias Detection and Mitigation
- SDAIA-3-2: Explainable AI
- SDAIA-4-1: Privacy by Design
- SDAIA-6-1: Human Oversight

---

## Loading Standards

### Initial Seed

Seed all standards and controls:
```bash
docker-compose exec backend python -m app.seeders.run_seeders --all
```

### Individual Standard

Seed a specific standard:
```bash
docker-compose exec backend python -m app.seeders.run_seeders --standard nca-ecc
docker-compose exec backend python -m app.seeders.run_seeders --standard nca-cscc
docker-compose exec backend python -m app.seeders.run_seeders --standard ndmo
docker-compose exec backend python -m app.seeders.run_seeders --standard sdaia
```

### Reset and Re-seed

Reset all data and re-seed:
```bash
docker-compose exec backend python -m app.seeders.run_seeders --all --reset
```

## Custom Standards

To add custom standards:

1. Create a new seeder file in `backend/app/seeders/`
2. Define `STANDARD_META` dictionary
3. Define `CONTROLS` list with bilingual content
4. Add to `SEEDERS` dict in `run_seeders.py`

Example structure:
```python
STANDARD_META = {
    "code": "CUSTOM-STD",
    "name_en": "Custom Standard",
    "name_ar": "معيار مخصص",
    "version": "1.0",
    "category": "custom",
}

CONTROLS = [
    {
        "control_id": "CUSTOM-1-1",
        "domain_en": "Domain Name",
        "domain_ar": "اسم المجال",
        "title_en": "Control Title",
        "title_ar": "عنوان الضابط",
        "description_en": "Control description...",
        "description_ar": "وصف الضابط...",
        "priority": "HIGH",
    },
]
```

## Control Priority Levels

- **CRITICAL:** Must be implemented, highest priority
- **HIGH:** Should be implemented soon
- **MEDIUM:** Important but can be deferred
- **LOW:** Nice to have

## Implementation Status

Each control tracks implementation status:
- **NOT_IMPLEMENTED:** Not started
- **PARTIALLY_IMPLEMENTED:** Work in progress
- **IMPLEMENTED:** Fully implemented
- **NOT_APPLICABLE:** Does not apply to organization
