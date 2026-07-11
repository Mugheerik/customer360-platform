# Customer360 Platform

[![CI](https://github.com/Mugheerik/customer360-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/Mugheerik/customer360-platform/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.139-009688.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-336791.svg)
![License](https://img.shields.io/github/license/Mugheerik/customer360-platform)
![Release](https://img.shields.io/github/v/release/Mugheerik/customer360-platform)
![Status](https://img.shields.io/badge/status-active%20development-brightgreen)

A production-style **Customer Data Platform (CDP)** backend built with modern Python technologies and engineering best practices.

Customer360 Platform demonstrates how scalable backend services, data-centric applications, and analytics platforms are designed, built, tested, and maintained using a production-oriented software engineering workflow.

Rather than being a simple CRUD application, the project emphasizes clean architecture, maintainability, automated testing, database versioning, code quality, and continuous integration—mirroring practices commonly used in professional software teams.

The long-term vision is to evolve Customer360 into a production-grade Customer Data Platform featuring authentication, event ingestion, analytics, and customer intelligence services.

---

# Roadmap

* ✅ **v0.1.0** — Production Backend Foundation
* 🔄 **v0.2.0** — Authentication & Authorization
* ⏳ **v0.3.0** — Orders & Products
* ⏳ **v0.4.0** — Customer Search
* ⏳ **v0.5.0** — Event Tracking
* ⏳ **v0.6.0** — Analytics Engine
* ⏳ **v1.0.0** — Customer360 MVP

---

# Why Customer360?

Customer360 aims to provide a unified view of customer information while serving as the foundation for future analytics, event processing, and customer intelligence capabilities.

The project demonstrates practical backend engineering concepts including:

* Clean Architecture
* Layered Application Design
* REST API Development
* Database Design
* Database Migrations
* Automated Testing
* Code Quality Automation
* Continuous Integration

---

# Repository Structure

```text
customer360-platform/

├── .github/
│   └── workflows/
│       └── ci.yml
│
├── apps/
│   └── api/
│
├── docs/
│
├── infra/
│   └── docker-compose.yml
│
├── scripts/
│
├── tests/
│
├── .gitignore
├── pytest.ini
└── README.md
```

---

# Technology Stack

| Category             | Technology     |
| -------------------- | -------------- |
| Language             | Python 3.13    |
| API Framework        | FastAPI        |
| ORM                  | SQLAlchemy 2.0 |
| Database             | PostgreSQL 17  |
| Database Migrations  | Alembic        |
| Validation           | Pydantic v2    |
| Package Manager      | uv             |
| Testing              | Pytest         |
| Linting & Formatting | Ruff           |
| Infrastructure       | Docker         |
| CI/CD                | GitHub Actions |

---

# Architecture

Customer360 follows a layered architecture that promotes separation of concerns, maintainability, and scalability.

```text
                 HTTP Request
                      │
                      ▼
              FastAPI Router
                      │
                      ▼
          Business Service Layer
                      │
                      ▼
          Repository / Data Access
                      │
                      ▼
        SQLAlchemy ORM + Alembic
                      │
                      ▼
                PostgreSQL
```

Each layer has a single responsibility:

* **Router** — Handles HTTP requests and responses.
* **Service** — Implements business rules and application logic.
* **Repository** — Encapsulates database access.
* **Models** — SQLAlchemy ORM entities.
* **Schemas** — Pydantic request and response models.

---

# Engineering Principles

Customer360 is built around production-oriented engineering practices.

* Modular project structure
* Layered architecture
* Dependency Injection
* Strong typing
* Database version control with Alembic
* Automated testing with Pytest
* Code quality enforcement using Ruff
* Continuous Integration with GitHub Actions
* Docker-based local development

---

# Current Features

* Customer CRUD API
* Health Check Endpoint
* PostgreSQL Integration
* SQLAlchemy ORM
* Alembic Database Migrations
* Docker Development Environment
* Automated Test Suite
* Test Coverage Reporting
* Ruff Linting & Formatting
* GitHub Actions CI Pipeline

---

# Getting Started

Clone the repository.

```bash
git clone https://github.com/Mugheerik/customer360-platform.git
```

Navigate to the project.

```bash
cd customer360-platform
```

Detailed API setup instructions are available in:

```text
apps/api/README.md
```

---

# Development Workflow

Every feature follows the same engineering workflow.

1. Update SQLAlchemy models.
2. Generate an Alembic migration.
3. Apply the migration.
4. Implement business logic.
5. Write automated tests.
6. Run Ruff linting and formatting.
7. Execute the complete test suite.
8. Merge after all CI checks pass.

---

# License

This project is licensed under the Apache License 2.0. See the `LICENSE` file for details.
