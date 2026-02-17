# Deployment Guide

## Production Deployment with Docker

### Prerequisites

- Docker Engine 20.10+
- Docker Compose 2.0+
- vLLM server (for AI features)
- LDAP/Active Directory server (for authentication)

### Environment Configuration

1. Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

2. Configure environment variables:

**Required:**
- `JWT_SECRET_KEY`: Generate a secure 256-bit key
- `LDAP_SERVER`: Your LDAP server address
- `LDAP_BIND_DN`: Service account DN
- `LDAP_BIND_PASSWORD`: Service account password
- `VLLM_BASE_URL`: Your vLLM server URL

**Optional:**
- `MONGODB_URL`: Default is `mongodb://mongodb:27017`
- `REDIS_URL`: Default is `redis://redis:6379/0`
- `CORS_ORIGINS`: Frontend URLs (comma-separated)

### Deployment Steps

1. **Build containers:**
```bash
docker-compose build
```

2. **Start services:**
```bash
docker-compose up -d
```

3. **Run database migrations (if needed):**
```bash
docker-compose exec backend python -m app.seeders.create_admin
```

4. **Seed Saudi standards:**
```bash
docker-compose exec backend python -m app.seeders.run_seeders --all
```

5. **Verify deployment:**
```bash
# Check backend health
curl http://localhost:8000/health

# Check frontend
curl http://localhost:3000
```

### Post-Deployment

1. **Change default admin password** immediately after first login
2. **Configure LDAP groups** for role mapping
3. **Set up backup** for MongoDB
4. **Configure SSL/TLS** with reverse proxy (nginx/traefik)

### Monitoring

View logs:
```bash
# All services
docker-compose logs -f

# Backend only
docker-compose logs -f backend

# Frontend only
docker-compose logs -f frontend
```

### Scaling

To scale the backend:
```bash
docker-compose up -d --scale backend=3
```

### Backup

Backup MongoDB:
```bash
docker-compose exec mongodb mongodump --out=/data/backup
docker cp $(docker-compose ps -q mongodb):/data/backup ./mongodb-backup
```

### Updates

1. Pull latest changes
2. Rebuild containers: `docker-compose build`
3. Restart services: `docker-compose up -d`
4. Run any new migrations if applicable

## Kubernetes Deployment

For Kubernetes deployment, see `kubernetes/` directory (coming soon).
