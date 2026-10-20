# Customer360

### Production-Oriented Customer Management Platform & Engineering Laboratory

[![CI](https://github.com/Mugheerik/customer360-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/Mugheerik/customer360-platform/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.139-009688.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-336791.svg)
![React](https://img.shields.io/badge/React-19-61DAFB.svg)
![TypeScript](https://img.shields.io/badge/TypeScript-6-3178C6.svg)
![Ruff](https://img.shields.io/badge/code%20quality-Ruff-blue.svg)
![License](https://img.shields.io/github/license/Mugheerik/customer360-platform)

Customer360 is a full-stack customer management platform and engineering laboratory built to practice backend engineering, software architecture, database engineering, automated testing, and modern web application development.

The platform combines a **FastAPI backend, React/TypeScript frontend, and PostgreSQL database** within a modular application architecture.

The focus is not simply on implementing features. It is on understanding the engineering practices behind maintainable, testable, and reliable business software.

## Table of Contents

- [Overview](#overview)
- [Core Capabilities](#core-capabilities)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Running the Backend](#running-the-backend)
- [Running the Frontend](#running-the-frontend)
- [Testing](#testing)
- [Code Quality and Security](#code-quality-and-security)
- [Database Migrations](#database-migrations)
- [Engineering Workflow](#engineering-workflow)
- [Current Status](#current-status)
- [Future Direction](#future-direction)
- [License](#license)

---

## Overview

Customer360 provides an authenticated environment for managing customer information and related business activity.

The project is used to explore:

- Backend application architecture
- REST API design and validation
- Authentication and authorization
- Relational database design
- Database transactions and rollback behavior
- Repository and service patterns
- Automated testing
- Code quality and dependency auditing
- Docker-based development environments
- Continuous integration with GitHub Actions

The application follows a **modular monolith** approach. This keeps deployment and local development manageable without introducing distributed-system complexity before it is justified.

## Core Capabilities

### Customer Management

The customer domain supports customer records and associated management workflows, including:

- Customer creation and retrieval
- Customer updates
- Customer activation and deactivation
- Search and filtering
- Sorting and pagination
- Input validation
- Customer detail views

### Notes and Tasks

The application includes customer-related notes and task-management functionality.

Notes support recording contextual information associated with customers. Tasks provide a lightweight way to organize customer-related work, including status, priority, and due-date information.

### Activity Timeline

The activity timeline provides a history of relevant customer-related actions. It establishes a foundation for understanding customer activity and developing more comprehensive audit capabilities.

### Authentication and Authorization

Identity and access control are implemented as shared backend capabilities.

The documented functionality includes:

- User registration and authentication
- JWT access tokens
- Password hashing
- Current-user information
- Protected routes
- Role-based authorization
- Superuser authorization

The frontend integrates with the authentication API and maintains authentication state across browser refreshes.

---

## Architecture

Customer360 uses a layered backend architecture with a feature-oriented frontend.

```text
                     Customer360
                          |
             +------------+------------+
             |                         |
             v                         v
       React / TypeScript         FastAPI / Python
             |                         |
             |                         v
             |                    Application
             |                      Services
             |                         |
             |                         v
             |                     Repositories
             |                         |
             +-------------------------+
                                       |
                                       v
                                  SQLAlchemy
                                       |
                                       v
                                  PostgreSQL
```

### Backend request flow

```text
HTTP Request
     |
     v
FastAPI Router
     |
     v
Authentication / Authorization
     |
     v
Application Service
     |
     v
Repository
     |
     v
SQLAlchemy
     |
     v
PostgreSQL
```

### Architectural principles

**Separation of concerns**

HTTP handling, application logic, persistence, and infrastructure are kept in separate responsibilities.

**Service layer**

Application services coordinate use cases and business operations.

**Repository pattern**

Database operations are organized behind repository components rather than being scattered throughout HTTP handlers.

**Dependency injection**

FastAPI dependencies provide access to services, database sessions, and authentication context. This also supports isolated testing.

**Explicit transaction boundaries**

Database changes must have predictable commit and rollback behavior. Transaction-related behavior is included in the backend test suite.

**Modular monolith**

The application remains a single deployable backend. Additional services or infrastructure should be introduced only when supported by concrete requirements.

---

## Technology Stack

### Backend

| Category | Technology |
|---|---|
| Language | Python 3.13 |
| API framework | FastAPI |
| Database | PostgreSQL 17 |
| ORM | SQLAlchemy 2.0 |
| Migrations | Alembic |
| Validation | Pydantic |
| Authentication | JWT |
| Dependency management | uv |
| Testing | Pytest |
| Coverage | pytest-cov |
| Formatting | Ruff |
| Linting | Ruff |
| Dependency auditing | pip-audit |
| Containerization | Docker |
| CI/CD | GitHub Actions |

### Frontend

| Category | Technology |
|---|---|
| Language | TypeScript |
| Framework | React 19 |
| Build tool | Vite |
| Routing | React Router |
| Server state | TanStack Query |
| Forms | React Hook Form |
| Validation | Zod |
| Client state | Zustand |
| HTTP client | Axios |
| Styling | Tailwind CSS |
| Linting | ESLint |
| Formatting | Prettier |

---

## Repository Structure

```text
customer360-platform/
├── .github/
│   └── workflows/
├── apps/
│   ├── api/
│   │   ├── app/
│   │   ├── migrations/
│   │   ├── tests/
│   │   ├── pyproject.toml
│   │   └── README.md
│   └── web/
├── docs/
├── infra/
├── scripts/
├── tests/
├── CHANGELOG.md
├── LICENSE
├── pytest.ini
└── README.md
```

The API implementation, web application, infrastructure, documentation, and tests are organized into separate areas of the repository.

The exact contents of individual directories may evolve as the implementation develops.

---

## Getting Started

### Prerequisites

Install the following tools:

- Git
- Python 3.13
- uv
- Node.js and npm
- Docker Desktop

### 1. Clone the repository

Using HTTPS:

```powershell
git clone https://github.com/Mugheerik/customer360-platform.git
cd customer360-platform
```

Or using SSH:

```powershell
git clone git@github.com:Mugheerik/customer360-platform.git
cd customer360-platform
```

### 2. Start PostgreSQL

The local Docker Compose configuration uses PostgreSQL 17.

From the repository root:

```powershell
docker compose up -d postgres
docker compose ps
```

In the current local development configuration, PostgreSQL is published on host port **5433**, mapped to port 5432 inside the container.

For tools and processes running directly on the Windows host, use:

```text
127.0.0.1:5433
```

For an application running inside the same Docker Compose network, use the PostgreSQL service name and container port:

```text
postgres:5432
```

These connection addresses serve different environments and should not be interchanged.

### 3. Configure the backend environment

Navigate to the API directory:

```powershell
cd apps/api
```

Install the project dependencies:

```powershell
uv sync
```

Create or update the local `.env` file according to the application's settings.

Example for a local Windows-host connection:

```dotenv
DATABASE_URL=postgresql+psycopg://postgres:postgres@127.0.0.1:5433/customer360

JWT_SECRET_KEY=replace-with-a-long-local-secret
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30

APP_NAME=Customer360 API
APP_VERSION=0.4.0
DEBUG=true
```

This is an example configuration, not a replacement for checking the settings expected by the current application.

Use a strong local secret, keep credentials private, and never commit a real `.env` file.

If you use different database credentials, update the connection URL to match your local PostgreSQL configuration.

---

## Running the Backend

From `apps/api`, apply the database migrations:

```powershell
uv run alembic upgrade head
```

Start the development server:

```powershell
uv run uvicorn app.main:app --reload
```

The API is available at:

- API root: `http://localhost:8000`
- Interactive API documentation: `http://localhost:8000/docs`

The API uses the database connection specified in the local environment.

---

## Running the Frontend

Open a second terminal and navigate to the frontend:

```powershell
cd D:\customer360_platform\apps\web
```

Install dependencies:

```powershell
npm install
```

Start the Vite development server:

```powershell
npm run dev
```

The frontend is normally available at:

```text
http://localhost:5173
```

The browser communicates with the backend through the API base URL configured for the frontend.

---

## Testing

The backend uses Pytest and pytest-cov.

The repository-root `pytest.ini` configures test discovery and coverage reporting. Run the tests from the repository root:

```powershell
cd D:\customer360_platform
uv run --project apps/api pytest
```

The equivalent command from the API directory is:

```powershell
cd D:\customer360_platform\apps\api
uv run pytest
```

The suite covers backend behavior such as API operations, authentication, authorization, database interactions, and transaction handling.

### Current local test result

The latest local run reported:

**48 tests passed.**

This is a local verification result, not a claim that the same revision has already passed GitHub Actions.

The test count and coverage can change as the codebase evolves. Use the current test output as the source of truth.

---

## Code Quality and Security

### Ruff formatting

Check formatting without modifying files:

```powershell
cd D:\customer360_platform
uv run --project apps/api ruff format --check apps/api
```

The latest local result was:

```text
64 files already formatted
```

### Ruff linting

```powershell
uv run --project apps/api ruff check apps/api
```

A successful run should report:

```text
All checks passed!
```

### Dependency security audit

```powershell
uv run --project apps/api pip-audit
```

The latest reported audit result was:

```text
No known vulnerabilities found
```

This describes the dependency versions checked at that time; it is not a guarantee that future versions will have no vulnerabilities.

### Git whitespace checks

From the repository root:

```powershell
git diff --check
git status --short
```

Review the changes before committing.

---

## Database Migrations

Alembic manages database schema changes.

Run these commands from the API directory:

```powershell
cd D:\customer360_platform\apps\api
```

Show the current migration revision:

```powershell
uv run alembic current
```

Check for differences between SQLAlchemy metadata and the database schema:

```powershell
uv run alembic check
```

Apply pending migrations:

```powershell
uv run alembic upgrade head
```

The latest local verification reported:

```text
0001_initial_schema (head)
No new upgrade operations detected.
```

This result applies to the local database and migration state that were checked.

---

## Continuous Integration

The repository includes GitHub Actions workflow configuration.

The CI badge at the top links to the repository's workflow status. A badge alone should not be interpreted as proof that every current local change has passed CI.

After committing and pushing changes, inspect the workflow run associated with that commit to verify its actual result.

Local checks and CI checks are related but distinct: a successful local run does not establish that the remote workflow passed.

---

## Engineering Workflow

The intended workflow is:

```text
Define the requirement
         |
         v
Review the design
         |
         v
Implement the change
         |
         v
Run automated tests
         |
         v
Check Ruff formatting
         |
         v
Run Ruff linting
         |
         v
Audit dependencies
         |
         v
Validate migrations
         |
         v
Review Git changes
         |
         v
Commit and verify CI
```

The objective is to keep changes understandable, reproducible, and verifiable instead of relying on manual checks alone.

---

## Current Status

Customer360 is an evolving engineering project focused on backend and platform engineering foundations.

The current work includes:

- A FastAPI backend and React/TypeScript frontend
- PostgreSQL persistence and Alembic migrations
- Authentication and authorization
- Customer management and related workflows
- Automated backend testing
- Ruff formatting and linting
- Python dependency auditing
- Docker-based PostgreSQL development
- GitHub Actions configuration

### Latest local verification

| Check | Reported result |
|---|---|
| Backend tests | 48 passed |
| Ruff formatting | 64 files already formatted |
| Dependency audit | No known vulnerabilities found |
| Alembic current revision | `0001_initial_schema (head)` |
| Alembic consistency check | No new upgrade operations detected |

These results describe the latest local checks reported during development. They are not a substitute for running the checks against a new checkout or verifying the corresponding remote CI run.

---

## Future Engineering Direction

Future work should be guided by application requirements and engineering value rather than technology accumulation.

Potential areas for further development include:

### Backend and platform engineering

- More comprehensive error handling
- Improved observability
- Background processing where justified
- Deployment automation
- Configuration and secret-management improvements

### Database engineering

- Stronger data-integrity guarantees
- Query and transaction analysis
- Migration testing
- Performance measurement where needed

### Testing and reliability

- Additional edge-case and failure-path tests
- Stronger integration testing
- CI verification for changes
- Better coverage of critical application behavior

### Data and intelligent systems

- Customer analytics
- Operational reporting
- Data pipelines
- AI-assisted workflows where a concrete use case justifies them

These are potential directions, not claims that the capabilities have already been implemented.

---

## Project Philosophy

Customer360 is intended to be an engineering laboratory rather than a showcase of tools.

The project prioritizes:

- Correctness over unnecessary complexity
- Maintainability over premature optimization
- Clear boundaries over excessive abstraction
- Tested behavior over feature volume
- Reproducibility over manual configuration
- Engineering reasoning over technology accumulation

The goal is to build software that can be understood, tested, and extended as real requirements emerge.

---

## License

Customer360 is licensed under the Apache License 2.0.

See [LICENSE](LICENSE) for the full license text.

---

### Customer360

**Production-Oriented Customer Management Platform & Engineering Laboratory**

*Built to practice backend engineering, software architecture, database engineering, and platform engineering.*
