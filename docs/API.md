# API Documentation

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

All authenticated endpoints require a Bearer token in the Authorization header:

```
Authorization: Bearer <access_token>
```

## Endpoints

### Authentication

#### POST /auth/login
Authenticate user and receive JWT tokens.

**Request:**
```json
{
  "username": "admin",
  "password": "password"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer"
}
```

#### GET /auth/me
Get current user profile (requires authentication).

**Response:**
```json
{
  "id": "507f1f77bcf86cd799439011",
  "username": "admin",
  "email": "admin@municipality.gov.sa",
  "full_name_en": "Admin User",
  "full_name_ar": "مستخدم المشرف",
  "role": "ADMIN",
  "is_active": true,
  "is_ldap_user": false
}
```

### Standards

#### GET /standards
List all regulatory standards.

#### GET /standards/{id}
Get standard by ID.

### Controls

#### GET /controls
List controls with optional filters.

**Query Parameters:**
- `standard_id`: Filter by standard
- `priority`: Filter by priority (LOW, MEDIUM, HIGH, CRITICAL)
- `status`: Filter by implementation status
- `skip`: Pagination offset (default: 0)
- `limit`: Pagination limit (default: 20, max: 100)

#### PATCH /controls/{id}
Update control implementation status (requires ADMIN or RISK_OFFICER role).

### Risks

#### GET /risks
List all risks.

#### POST /risks
Create a new risk (requires ADMIN or RISK_OFFICER role).

#### GET /risks/{id}
Get risk by ID.

#### PUT /risks/{id}
Update risk (requires ADMIN or RISK_OFFICER role).

#### DELETE /risks/{id}
Soft delete risk (requires ADMIN role).

## Error Responses

All error responses follow this format:

```json
{
  "detail": "Error message"
}
```

Common status codes:
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
