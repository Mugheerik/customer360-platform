# Customer360

### Production-Oriented Customer Management Platform & Engineering Laboratory

[![CI](https://github.com/Mugheerik/customer360-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/Mugheerik/customer360-platform/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.139-009688.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-336791.svg)
![React](https://img.shields.io/badge/React-19-61DAFB.svg)
![TypeScript](https://img.shields.io/badge/TypeScript-6-3178C6.svg)
![License](https://img.shields.io/github/license/Mugheerik/customer360-platform)
![Release](https://img.shields.io/github/v/release/Mugheerik/customer360-platform)
![Coverage](https://img.shields.io/badge/coverage-91%25-brightgreen.svg)
![Ruff](https://img.shields.io/badge/lint-Ruff-blue.svg)
![pip-audit](https://img.shields.io/badge/security-passing-brightgreen.svg)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)

---

> **A production-oriented customer management platform built to demonstrate backend engineering, software architecture, database engineering, testing, and modern web application development.**

Customer360 is a full-stack customer management platform and engineering laboratory focused on building software with production-oriented engineering practices.

The project combines a **FastAPI backend, React/TypeScript web application, and PostgreSQL database** using a modular architecture designed for maintainability, testability, and future evolution.

Rather than focusing only on application features, Customer360 is used to practice the engineering foundations behind reliable business systems:

* Backend architecture
* API design
* Authentication and authorization
* Database engineering
* Transaction management
* Automated testing
* Frontend architecture
* CI/CD
* Code quality
* Containerized infrastructure
* Versioned releases

The result is both a functional customer management application and a practical engineering laboratory for exploring how production-oriented software systems are designed and built.

---

# Project at a Glance

| Category          | Technology                              |
| ----------------- | --------------------------------------- |
| Project Type      | Full-Stack Customer Management Platform |
| Engineering Focus | Backend & Platform Engineering          |
| Architecture      | Clean Architecture principles           |
| Design Style      | Modular Monolith                        |
| Backend           | FastAPI / Python                        |
| Frontend          | React / TypeScript                      |
| Database          | PostgreSQL 17                           |
| ORM               | SQLAlchemy 2.0                          |
| Migrations        | Alembic                                 |
| Authentication    | JWT                                     |
| Authorization     | Role-Based Access Control               |
| API Client        | Axios                                   |
| Server State      | TanStack Query                          |
| Client State      | Zustand                                 |
| Testing           | Pytest + Coverage                       |
| Backend Quality   | Ruff                                    |
| Frontend Quality  | ESLint + Prettier                       |
| Dependency Audit  | pip-audit                               |
| Git Hooks         | pre-commit                              |
| Package Manager   | uv                                      |
| Infrastructure    | Docker                                  |
| CI/CD             | GitHub Actions                          |
| Versioning        | Semantic Versioning                     |
| Current Release   | v0.3.0                                  |

---

# Platform Overview

Customer360 provides an authenticated customer management environment for managing customer information, notes, tasks, and activity history.

The system is organized around a modular backend and feature-oriented frontend.

```text
                         Customer360
                              │
             ┌────────────────┴────────────────┐
             │                                 │
             ▼                                 ▼
       React Web App                       FastAPI API
       TypeScript                          Python
             │                                 │
             │                                 ▼
             │                           SQLAlchemy
             │                                 │
             │                                 ▼
             └────────────────────────── PostgreSQL
```

The architecture intentionally remains a **modular monolith** rather than prematurely distributing the system into multiple services.

This provides a simpler operational model while establishing architectural boundaries that can evolve if future requirements justify additional infrastructure.

---

# Core Capabilities

## Customer Management

The Customer domain provides the primary business functionality of the platform.

Current capabilities include:

* Customer creation
* Customer retrieval
* Customer updates
* Customer activation/deactivation
* Customer search
* Status filtering
* Sorting
* Pagination
* Customer detail views
* Input validation

---

## Notes

Customers can have associated notes that provide contextual information about interactions and business activity.

Current capabilities include:

* Create notes
* View notes
* Update notes
* Delete notes
* Associate notes with customers

---

## Tasks

Tasks provide a lightweight workflow capability around customer activity.

Current capabilities include:

* Create tasks
* Update tasks
* Delete tasks
* Task descriptions
* Task status
* Task priority
* Due dates
* Task assignment
* Customer-specific task management

---

## Activity Timeline

Customer activity is recorded through an activity timeline.

The timeline provides an auditable history of important customer-related actions and associates activities with the responsible actor where applicable.

This establishes a foundation for future audit and operational observability capabilities.

---

# Authentication & Authorization

Identity and access control are implemented as shared backend capabilities rather than being embedded directly inside the Customer domain.

Current capabilities include:

* User registration
* User authentication
* JWT access tokens
* Password hashing
* Current-user endpoint
* Protected routes
* Role-based authorization
* Superuser authorization
* Authenticated user context

The frontend integrates with the authentication API and maintains the authenticated session across browser refreshes.

---

# Frontend Application

The web application is built with React and TypeScript and communicates with the FastAPI backend through a centralized API layer.

## Frontend Capabilities

* React 19
* TypeScript
* Vite
* React Router
* TanStack Query
* React Hook Form
* Zod validation
* Zustand
* Axios
* Tailwind CSS
* Shared UI components
* Protected routes
* Persistent authentication state
* Loading and error states
* Customer search
* Filtering
* Sorting
* Pagination
* Customer management
* Notes
* Tasks
* Activity Timeline

---

## Frontend Architecture

The frontend follows a feature-oriented structure:

```text
apps/web/src/
│
├── app/
│   ├── providers/
│   ├── router/
│   └── styles/
│
├── components/
│   ├── navigation/
│   └── ui/
│
├── features/
│   ├── auth/
│   ├── customer/
│   │   ├── api/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── types/
│   │   └── index.ts
│   ├── dashboard/
│   └── home/
│
├── hooks/
├── layouts/
├── lib/
├── services/
└── store/
```

The customer feature owns customer-specific UI, API integration, types, Notes, Tasks, and Activity Timeline functionality.

Shared concerns remain outside the feature boundary.

---

# Authentication Flow

The frontend authentication flow integrates directly with the FastAPI authentication endpoints.

```text
Login Form
    │
    ▼
Client Validation
    │
    ▼
POST /api/v1/auth/login
    │
    ▼
JWT Access Token
    │
    ▼
Authentication State
    │
    ▼
Authenticated API Client
    │
    ▼
GET /api/v1/auth/me
    │
    ▼
Authenticated User
    │
    ▼
Protected Application
```

The access token is persisted locally so that the authenticated session can survive a browser refresh.

---

# System Architecture

Customer360 follows a layered backend architecture with clear separation between HTTP concerns, application logic, persistence, and infrastructure.

```text
HTTP Request
      │
      ▼
FastAPI Router
      │
      ▼
Authentication / Authorization
      │
      ▼
Application Service
      │
      ▼
Repository
      │
      ▼
SQLAlchemy
      │
      ▼
PostgreSQL
```

The modular monolith structure allows business domains and platform capabilities to remain separated while sharing a single deployable backend.

---

# Architectural Layers

## API Layer

Responsible for:

* HTTP routing
* Request handling
* Request validation
* Response serialization
* Dependency injection

---

## Identity Layer

Responsible for:

* Authentication
* Authorization
* User context
* Access control

---

## Application Layer

Responsible for:

* Business rules
* Use cases
* Domain coordination
* Transaction boundaries

---

## Repository Layer

Responsible for:

* Database access
* Query encapsulation
* Persistence operations

---

## Database Layer

Responsible for:

* Persistent storage
* Relational integrity
* Schema evolution
* Database transactions

---

# Engineering Patterns

Customer360 applies several established backend engineering patterns.

## Clean Architecture

Application responsibilities are separated so that business logic is not tightly coupled to infrastructure or HTTP concerns.

---

## Repository Pattern

Database access is encapsulated behind repository interfaces and implementations.

This keeps persistence concerns separate from application-level business logic.

---

## Service Layer

Application services coordinate business operations and enforce application-level rules.

---

## Dependency Injection

FastAPI dependency injection is used to provide application services, repositories, authentication context, and other dependencies.

This also makes components easier to isolate during testing.

---

## Transaction Boundaries

Database operations are coordinated through explicit transaction boundaries.

Repositories stage database changes while the application/service layer controls commit and rollback behavior.

This provides predictable transaction semantics and improves testability.

---

# Database Engineering

Customer360 uses PostgreSQL as its relational persistence layer.

Current database practices include:

* PostgreSQL 17
* SQLAlchemy 2.0
* Alembic migrations
* Version-controlled schema changes
* Transaction management
* Relational constraints
* Automated migration validation

Current domain entities include:

```text
users
customers
notes
tasks
activity_logs
```

Database schema changes are managed through Alembic rather than manual database modification.

---

# Testing Strategy

Testing is treated as a first-class engineering activity.

The backend test suite covers areas including:

* API behavior
* Authentication
* Authorization
* Database operations
* Customer functionality
* Notes
* Tasks
* Transaction behavior
* Rollback behavior
* Dependency overrides

The project uses:

* Pytest
* pytest-cov
* FastAPI test clients
* Database test fixtures
* Transaction rollback fixtures

The goal is not simply to maximize coverage, but to verify important application behavior and transaction semantics.

---

# Code Quality

Backend quality is enforced through automated tooling.

Current practices include:

* Ruff formatting
* Ruff linting
* Type-aware Python development
* pre-commit hooks
* Dependency auditing with pip-audit

Frontend quality is maintained through:

* TypeScript
* ESLint
* Prettier
* Production build validation

---

# Continuous Integration

GitHub Actions automatically validates backend changes through the CI pipeline.

The pipeline verifies important engineering gates including:

* Dependency installation
* Ruff formatting
* Ruff linting
* Database migration validation
* Automated tests
* Build integrity

The goal is to prevent changes that do not satisfy the project's engineering standards from reaching the main branch.

---

# Containerization

Docker is currently used to provide a reproducible PostgreSQL development environment.

The current local infrastructure is:

```text
Docker
└── PostgreSQL 17
        │
        ▼
   Customer360 API
        │
        ▼
   React Web App
```

The API and web application can be run directly through their respective development environments while PostgreSQL runs inside Docker.

The infrastructure configuration is intentionally kept simple while the application architecture is established.

---

# Technology Stack

## Backend

| Category         | Technology     |
| ---------------- | -------------- |
| Language         | Python 3.13    |
| Framework        | FastAPI        |
| ORM              | SQLAlchemy 2.0 |
| Database         | PostgreSQL 17  |
| Migrations       | Alembic        |
| Validation       | Pydantic v2    |
| Authentication   | JWT            |
| Password Hashing | Argon2         |
| Package Manager  | uv             |
| Testing          | Pytest         |
| Coverage         | pytest-cov     |
| Formatting       | Ruff           |
| Linting          | Ruff           |
| Dependency Audit | pip-audit      |
| Git Hooks        | pre-commit     |
| Infrastructure   | Docker         |
| CI/CD            | GitHub Actions |

## Frontend

| Category     | Technology      |
| ------------ | --------------- |
| Language     | TypeScript      |
| Framework    | React 19        |
| Build Tool   | Vite            |
| Routing      | React Router    |
| Server State | TanStack Query  |
| Forms        | React Hook Form |
| Validation   | Zod             |
| Client State | Zustand         |
| HTTP Client  | Axios           |
| Styling      | Tailwind CSS    |
| Linting      | ESLint          |
| Formatting   | Prettier        |

---

# Repository Structure

Customer360 is organized as a multi-application engineering repository.

```text
customer360-platform/
│
├── apps/
│   ├── api/                 # FastAPI backend
│   └── web/                 # React frontend
│
├── docs/                    # Architecture and project documentation
├── infra/                   # Infrastructure configuration
├── scripts/                 # Development and automation scripts
├── tests/                   # Repository-level tests
│
├── .github/                 # GitHub Actions
├── CHANGELOG.md
├── README.md
└── LICENSE
```

The repository separates application code, infrastructure, testing, documentation, and automation concerns.

---

# Backend Structure

The backend follows modular and layered organization.

```text
apps/api/
│
├── app/
│   ├── core/
│   ├── domain/
│   ├── application/
│   ├── infrastructure/
│   └── entrypoints/
│
├── migrations/
├── tests/
├── pyproject.toml
├── alembic.ini
└── README.md
```

The exact implementation may evolve, but the architectural goal remains separation of business logic, application orchestration, infrastructure, and transport concerns.

---

# Getting Started

## Prerequisites

Install the following locally:

* Python 3.13
* Node.js
* npm
* Docker Desktop
* Git

The backend uses **uv** for Python dependency management.

---

## 1. Clone the Repository

Using HTTPS:

```bash
git clone https://github.com/Mugheerik/customer360-platform.git
```

Or using SSH:

```bash
git clone git@github.com:Mugheerik/customer360-platform.git
```

Navigate into the project:

```bash
cd customer360-platform
```

---

# 2. Start PostgreSQL

Customer360 currently uses Docker for the PostgreSQL development database.

Start PostgreSQL from the repository root:

```bash
docker compose up -d postgres
```

Verify that the container is running:

```bash
docker compose ps
```

The database is exposed locally on:

```text
localhost:5432
```

The development database configuration should point to the local PostgreSQL instance.

Example:

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/customer360
```

Use your local `.env` file for environment-specific configuration.

Do not commit real secrets to the repository.

---

# 3. Start the Backend

Navigate to the API application:

```bash
cd apps/api
```

Install dependencies with uv:

```bash
uv sync
```

Create your local environment configuration if it does not already exist.

Example:

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/customer360

JWT_SECRET_KEY=replace-with-a-long-local-secret
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30

APP_NAME=Customer360 API
APP_VERSION=0.4.0
DEBUG=true
```

Run database migrations:

```bash
uv run alembic upgrade head
```

Start the FastAPI development server:

```bash
uv run uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

FastAPI interactive API documentation is available at:

```text
http://localhost:8000/docs
```

---

# 4. Start the Frontend

Open a second terminal.

From the repository root:

```bash
cd apps/web
```

Install frontend dependencies:

```bash
npm install
```

Start the Vite development server:

```bash
npm run dev
```

The web application will normally be available at:

```text
http://localhost:5173
```

---

# 5. Local Development Architecture

After starting all three components, the local development environment looks like this:

```text
Browser
   │
   ▼
React / Vite
localhost:5173
   │
   │ HTTP
   ▼
FastAPI
localhost:8000
   │
   │ PostgreSQL
   ▼
Docker PostgreSQL
localhost:5432
```

The browser communicates with the API through `localhost:8000`.

The API communicates with PostgreSQL through the local database connection configured in `DATABASE_URL`.

---

# 6. Run Tests

From the API directory:

```bash
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov=app --cov-report=term-missing
```

---

# 7. Run Code Quality Checks

Format the backend:

```bash
uv run ruff format .
```

Check formatting:

```bash
uv run ruff format --check .
```

Run linting:

```bash
uv run ruff check .
```

Run dependency auditing:

```bash
uv run pip-audit
```

---

# 8. Run Pre-Commit

Install the configured hooks:

```bash
uv run pre-commit install
```

Run all hooks:

```bash
uv run pre-commit run --all-files
```

---

# 9. Database Migration Checks

Check whether the database schema is synchronized with the migration history:

```bash
uv run alembic check
```

Apply pending migrations:

```bash
uv run alembic upgrade head
```

---

# Engineering Workflow

Customer360 follows a repeatable engineering workflow:

```text
Problem
   │
   ▼
Design
   │
   ▼
Implementation
   │
   ▼
Automated Tests
   │
   ▼
Formatting / Linting
   │
   ▼
Dependency Audit
   │
   ▼
Migration Validation
   │
   ▼
CI
   │
   ▼
Versioned Release
```

Architectural decisions are recorded when they have long-term consequences, allowing the project to preserve both implementation knowledge and architectural reasoning.

---

# Engineering Standards

Customer360 emphasizes engineering quality over feature volume.

The project currently demonstrates:

| Capability                    | Status |
| ----------------------------- | ------ |
| Modular Monolith              | ✅      |
| Clean Architecture Principles | ✅      |
| Dependency Injection          | ✅      |
| Repository Pattern            | ✅      |
| Service Layer                 | ✅      |
| Transaction Boundaries        | ✅      |
| JWT Authentication            | ✅      |
| Role-Based Authorization      | ✅      |
| Customer CRUD                 | ✅      |
| Search                        | ✅      |
| Filtering                     | ✅      |
| Sorting                       | ✅      |
| Pagination                    | ✅      |
| Notes                         | ✅      |
| Tasks                         | ✅      |
| Activity Timeline             | ✅      |
| Automated Testing             | ✅      |
| Transaction Rollback Testing  | ✅      |
| Database Migrations           | ✅      |
| Ruff                          | ✅      |
| Dependency Auditing           | ✅      |
| pre-commit                    | ✅      |
| GitHub Actions CI             | ✅      |
| Semantic Versioning           | ✅      |
| Verified Commits              | ✅      |
| Dockerized PostgreSQL         | ✅      |

---

# Release History

Customer360 evolves through versioned engineering milestones.

| Version | Milestone                          | Status              |
| ------- | ---------------------------------- | ------------------- |
| v0.1.0  | Platform Foundation                | ✅ Complete          |
| v0.2.0  | Identity & Security                | ✅ Complete          |
| v0.3.0  | Customer Management Platform       | ✅ Complete          |
| v0.4.x  | Engineering & Deployment Evolution | 🔄 Current          |
| v1.0.0  | Production-Oriented Platform       | 🎯 Long-Term Target |

Each release represents a meaningful engineering milestone rather than simply an accumulation of UI features.

---

# Current System

The current Customer360 platform provides:

```text
Identity
   │
   ▼
Authentication & Authorization
   │
   ▼
Customer Management
   │
   ├── Customer Information
   │
   ├── Notes
   │
   ├── Tasks
   │
   └── Activity Timeline
```

The system is now sufficiently complete to demonstrate the core engineering foundations of a full-stack business application.

---

# Future Engineering Direction

Future development may explore additional platform capabilities where they provide a clear engineering or product justification.

Potential areas include:

### Platform Engineering

* Background processing
* Scheduled jobs
* Notifications
* Audit capabilities
* External integrations
* Cloud deployment

### Distributed Systems

* Event-driven processing
* Messaging infrastructure
* Asynchronous workflows
* Service integration patterns

### Data & Analytics

* Operational analytics
* Customer analytics
* Reporting
* Data pipelines
* Analytical data models

### Intelligence

* Customer segmentation
* Recommendation systems
* Predictive analytics
* AI-assisted workflows
* Intelligent customer operations

Future technologies will be introduced where they solve a concrete system requirement rather than being added solely for technology coverage.

---

# Documentation

Architecture and engineering documentation lives alongside the implementation.

```text
docs/
│
├── architecture/
│   ├── README.md
│   └── adr/
│
├── roadmap/
│
└── ...
```

Documentation focuses on:

* System architecture
* Architectural decisions
* Engineering practices
* Project evolution
* Development guidance

Architecture Decision Records are used for significant decisions where documenting the reasoning is valuable.

---

# What This Project Demonstrates

Customer360 is designed to demonstrate practical engineering capability across several areas.

## Backend Engineering

* Python
* FastAPI
* REST API design
* Authentication
* Authorization
* Application services
* Repository pattern
* Dependency injection
* Transaction management

## Database Engineering

* PostgreSQL
* SQLAlchemy
* Alembic
* Relational modeling
* Schema evolution
* Transaction behavior

## Frontend Engineering

* React
* TypeScript
* Feature-oriented architecture
* API integration
* Server-state management
* Form validation
* Protected application flows

## Software Engineering

* Automated testing
* Code quality
* Dependency auditing
* CI/CD
* Version control
* Semantic versioning
* Release management

## Platform Engineering Foundations

* Modular architecture
* Infrastructure configuration
* Containerized development environments
* CI automation
* Reproducible database environments
* Architectural evolution

---

# Project Philosophy

Customer360 is intentionally developed as an engineering laboratory rather than a framework showcase.

The project values:

* Correctness over unnecessary complexity
* Maintainability over premature optimization
* Clear architecture over excessive abstraction
* Tested behavior over feature volume
* Reproducibility over manual configuration
* Engineering reasoning over technology accumulation

The goal is to build a system that is understandable, testable, and capable of evolving when real requirements justify that evolution.

---

# Contributing

Customer360 is currently maintained as a personal engineering project, but it follows professional development practices.

Contributions should:

* Follow the established architecture.
* Include appropriate automated tests.
* Maintain code quality standards.
* Preserve database migration integrity.
* Pass CI checks.
* Update documentation when necessary.

---

# License

Licensed under the Apache License 2.0.

See the [LICENSE](LICENSE) file for details.

---

<div align="center">

### Customer360

**Production-Oriented Customer Management Platform**

*Built as an engineering laboratory for backend, architecture, database, and platform engineering.*

</div>
