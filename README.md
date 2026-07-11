# Customer360 Platform

> A production-style Customer Data Platform (CDP) built with modern Python technologies and engineering best practices.

Customer360 Platform is a backend-focused engineering project that demonstrates how scalable APIs and data platforms are designed, built, tested, and maintained.

Rather than being a simple CRUD application, the project emphasizes clean architecture, maintainability, automated testing, database versioning, code quality, and continuous integration—mirroring practices commonly used in professional software teams.

---

## Why Customer360?

Customer360 aims to provide a unified view of customer information while serving as a foundation for future analytics, event processing, and customer intelligence capabilities.

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

## Repository Structure

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

## Technology Stack

| Category             | Technologies   |
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

## Architecture

The API follows a layered architecture to encourage separation of concerns and maintainability.

```text
HTTP Request
      │
      ▼
Router
      │
      ▼
Service
      │
      ▼
Repository
      │
      ▼
PostgreSQL
```

Each layer has a single responsibility:

* **Router** – Handles HTTP requests and responses.
* **Service** – Contains business logic.
* **Repository** – Manages database operations.
* **Models** – SQLAlchemy ORM entities.
* **Schemas** – Pydantic request/response models.

---

## Engineering Principles

Customer360 is built around production-oriented engineering practices:

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

## Current Features

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

## Getting Started

Clone the repository:

```bash
git clone https://github.com/Mugheerik/customer360-platform.git
```

Navigate to the project:

```bash
cd customer360-platform
```

Detailed API setup instructions are available in:

```text
apps/api/README.md
```

---

## Roadmap

### Phase 1 — Foundation ✅

* Project structure
* FastAPI
* PostgreSQL
* Customer CRUD
* Testing
* Ruff
* Docker
* GitHub Actions

### Phase 2

* Orders Module
* Products Module
* Customer Relationships
* Pagination
* Filtering
* Search

### Phase 3

* Event Tracking
* Customer Analytics
* Data Pipelines
* Reporting APIs
* Customer Insights

---

## Development Workflow

Every feature follows the same workflow:

1. Update models
2. Generate Alembic migration
3. Apply migration
4. Implement business logic
5. Write tests
6. Run Ruff
7. Execute the test suite
8. Open a Pull Request

---

## License

Licensed under the Apache License 2.0.
