# Changelog

All notable changes to **Customer360 Platform Engineering Laboratory** will be documented in this file.

The format is based on **Keep a Changelog**, and this project follows **Semantic Versioning (SemVer)**.

---

# [Unreleased]

## Added

* Upcoming Customer Domain enhancements.

---

# [v0.2.0] - 2026-07-28

## Added

### Identity & Security

* User registration
* User authentication
* JWT access token generation
* Current authenticated user endpoint
* Role-based authorization
* Superuser authorization
* Authentication dependencies

### User Management

* User listing endpoint
* User lookup by ID
* Current user endpoint

### Testing

* Authentication integration tests
* Authorization integration tests
* User endpoint tests
* Shared pytest fixtures
* Transaction rollback test database

### Engineering

* Global exception handling
* Standardized API error responses
* Ruff formatting and linting
* Continuous Integration workflow
* Semantic versioning
* GitHub Releases
* Verified SSH commit signing

## Changed

* Refactored authentication dependencies for improved reusability.
* Standardized unauthorized and forbidden error responses.
* Improved project documentation.
* Updated repository README with Platform Engineering Laboratory positioning.

## Fixed

* Authentication error handling.
* Authorization response consistency.
* CI formatting issues.
* Ruff compliance issues.

---

# [v0.1.0] - 2026-07-11

## Added

### Platform Foundation

* FastAPI application
* PostgreSQL integration
* SQLAlchemy ORM
* Alembic database migrations
* Customer CRUD API
* Health endpoint
* Environment configuration
* Docker development environment

### Engineering

* Clean Architecture
* Modular Monolith structure
* Repository pattern
* Service layer
* Dependency Injection
* Automated testing
* Ruff formatting and linting

## Changed

* Initial repository structure established.

---

## Versioning

Customer360 follows Semantic Versioning.

* **MAJOR** — incompatible architectural or API changes.
* **MINOR** — new platform capabilities.
* **PATCH** — bug fixes, documentation improvements, and maintenance releases.
