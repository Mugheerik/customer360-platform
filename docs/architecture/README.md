# Customer360 Architecture

## Overview

Customer360 is currently implemented as a **Modular Monolith** following **Clean Architecture** principles.

Business domains are organized into independent modules while sharing a single application and database. This approach keeps the platform simple during early development while providing clear architectural boundaries for future growth.

The architecture emphasizes:

* Separation of concerns
* Maintainability
* Testability
* Extensibility

---

# Project Structure

```text
apps/
└── api/
    ├── app/
    │   ├── core/
    │   ├── database/
    │   ├── entrypoints/
    │   └── modules/
    │       ├── auth/
    │       ├── users/
    │       └── customers/
    │
    └── tests/
```

### Responsibilities

| Directory      | Responsibility                        |
| -------------- | ------------------------------------- |
| `core/`        | Shared application components         |
| `database/`    | Database configuration and migrations |
| `entrypoints/` | API routers                           |
| `modules/`     | Business domains                      |
| `tests/`       | Automated tests                       |

---

# Layered Architecture

Customer360 separates business logic from infrastructure through a layered architecture.

```text
HTTP Request
      │
      ▼
FastAPI Router
      │
      ▼
Application Service
      │
      ▼
Repository
      │
      ▼
SQLAlchemy ORM
      │
      ▼
PostgreSQL
```

Each layer has a single responsibility.

| Layer      | Responsibility               |
| ---------- | ---------------------------- |
| Router     | HTTP requests and responses  |
| Service    | Business logic and use cases |
| Repository | Data access                  |
| Database   | Persistence                  |

---

# Request Lifecycle

A typical API request follows this flow:

```text
Client
   │
   ▼
Router
   │
   ▼
Authentication
   │
   ▼
Service
   │
   ▼
Repository
   │
   ▼
Database
   │
   ▼
Response
```

Business rules remain inside the Service Layer, while persistence logic remains inside the Repository Layer.

---

# Module Organization

Business functionality is organized into independent modules.

Current modules include:

* Authentication
* Users
* Customers

Each module owns its routers, services, repositories, schemas, and models where applicable.

This organization minimizes coupling between business domains and simplifies future expansion.

---

# Security Architecture

Authentication is implemented using JSON Web Tokens (JWT).

Protected endpoints authenticate the current user through dependency injection before executing business logic.

Current security capabilities include:

* User authentication
* JWT access tokens
* Current user resolution
* Role-based authorization
* Superuser authorization

---

# Database Architecture

Customer360 uses PostgreSQL as its primary data store.

Database access is implemented through SQLAlchemy ORM, while schema evolution is managed with Alembic migrations.

Current database responsibilities include:

* ORM mapping
* Transaction management
* Schema versioning
* Data persistence

---

# Future Evolution

The current architecture provides the foundation for additional platform capabilities.

Future architectural additions include:

* Platform Services
* Event Bus
* Workflow Engine
* Audit Service
* Notification Service
* Analytics Services
* AI Services

These capabilities will be introduced incrementally while preserving the existing architectural boundaries.

---

# Related Documentation

* Repository Overview: `README.md`
* Platform Roadmap: `docs/roadmap/platform-roadmap.md`
* Architecture Decision Records: `docs/adr/`
* Release History: `CHANGELOG.md`
