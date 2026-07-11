# Customer360 API

The Customer360 API is the backend service powering the Customer360 Platform.

It exposes RESTful endpoints for customer management and provides the engineering foundation for future analytics, event processing, and customer intelligence modules.

---

# Prerequisites

Install the following before running the project:

* Python 3.13+
* Docker Desktop
* Git
* uv

Install **uv** if needed:

https://docs.astral.sh/uv/

---

# Clone the Repository

```bash
git clone https://github.com/Mugheerik/customer360-platform.git

cd customer360-platform
```

---

# Install Dependencies

Move into the API project:

```bash
cd apps/api
```

Install dependencies:

```bash
uv sync
```

---

# Environment Variables

Create a `.env` file inside `apps/api`.

Example:

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/customer360
DEBUG=true
```

---

# Start PostgreSQL

From the repository root:

```bash
cd infra

docker compose up -d
```

Verify:

```bash
docker ps
```

---

# Database Migrations

Apply the latest migration:

```bash
uv run alembic upgrade head
```

Create a migration after changing SQLAlchemy models:

```bash
uv run alembic revision --autogenerate -m "describe your change"
```

---

# Run the API

From `apps/api`:

```bash
uv run uvicorn app.main:app --reload
```

API URL:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

OpenAPI Specification:

```
http://localhost:8000/openapi.json
```

---

# Running Tests

From the repository root:

```bash
uv run pytest
```

Run with coverage:

```bash
uv run pytest --cov=apps/api/app
```

---

# Code Quality

Run Ruff checks:

```bash
uv run ruff check apps/api
```

Automatically format the project:

```bash
uv run ruff format apps/api
```

---

# Continuous Integration

Every push and pull request automatically:

* Installs project dependencies
* Runs Ruff linting
* Verifies formatting
* Executes the automated test suite
* Generates code coverage

---

# Project Structure

```text
apps/api/

├── app/
│   ├── core/
│   ├── database/
│   ├── entrypoints/
│   └── modules/
│
├── migrations/
│
├── pyproject.toml
│
├── uv.lock
│
└── README.md
```

---

# Architecture

```text
Client
   │
   ▼
FastAPI Router
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
SQLAlchemy
   │
   ▼
PostgreSQL
```

---

# Current Modules

### Health

* API health endpoint

### Customers

* Create customer
* Retrieve customer
* List customers
* Update customer
* Deactivate customer

---

# Development Standards

The project follows these engineering standards:

* Clean Architecture
* Layered Design
* Dependency Injection
* SQLAlchemy ORM
* Alembic Migrations
* Pydantic Validation
* Automated Testing
* Ruff Code Quality
* GitHub Actions CI

---

# Useful Commands

## Install dependencies

```bash
uv sync
```

## Run the API

```bash
uv run uvicorn app.main:app --reload
```

## Run tests

```bash
uv run pytest
```

## Coverage

```bash
uv run pytest --cov=apps/api/app
```

## Lint

```bash
uv run ruff check apps/api
```

## Format

```bash
uv run ruff format apps/api
```

## Apply migrations

```bash
uv run alembic upgrade head
```

## Create migration

```bash
uv run alembic revision --autogenerate -m "migration description"
```
