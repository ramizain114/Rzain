# Contributing to Amana-GRC

We welcome contributions to Amana-GRC! This document provides guidelines for contributing.

## Development Setup

### Backend Development

1. **Setup Python environment:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Start MongoDB and Redis:**
```bash
docker-compose up -d mongodb redis
```

3. **Run development server:**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Development

1. **Install dependencies:**
```bash
cd frontend
npm install
```

2. **Start development server:**
```bash
npm run dev
```

## Code Standards

### Backend (Python)

- Follow PEP 8 style guide
- Use type hints
- Document all public functions and classes
- Write tests for new features
- Use async/await for I/O operations

### Frontend (TypeScript/React)

- Follow React best practices
- Use TypeScript strict mode
- Use functional components and hooks
- Follow component file structure
- Implement proper error boundaries

## Commit Messages

Follow conventional commits format:

```
feat: add risk matrix visualization
fix: correct RTL layout on Arabic language
docs: update API documentation
test: add tests for auth service
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `refactor`: Code refactoring
- `style`: Formatting changes
- `chore`: Build process or auxiliary tool changes

## Pull Request Process

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Write/update tests
4. Update documentation
5. Commit with conventional commits
6. Push and create a pull request
7. Wait for code review

## Testing

### Backend Tests

```bash
cd backend
pytest
```

### Frontend Tests

```bash
cd frontend
npm test
```

## Questions?

Feel free to open an issue for questions or discussions.
