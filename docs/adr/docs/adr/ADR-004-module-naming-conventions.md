# ADR-004: Module Naming Conventions

## Status

Accepted

## Context

As Customer360 grows, each feature module will contain multiple SQLAlchemy models and multiple Pydantic schemas. Using singular filenames such as `model.py` and `schema.py` would eventually become misleading.

## Decision

Adopt the following naming convention for all feature modules:

- `models.py` — SQLAlchemy ORM models
- `schemas.py` — Pydantic request and response schemas
- `repository.py` — Data access layer
- `service.py` — Business logic
- `router.py` — HTTP endpoints

## Consequences

- Consistent naming across all modules.
- Better scalability as modules grow.
- Reduced future refactoring.
- Easier navigation for contributors.