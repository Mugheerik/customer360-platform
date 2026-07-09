# Repository Pattern

## Purpose

The Repository Pattern separates business logic from database access.

Instead of allowing services to interact directly with SQLAlchemy, all persistence operations are delegated to repositories.

## Benefits

- Separation of concerns
- Easier testing
- Centralized data access
- Easier maintenance
- Flexibility to change persistence implementation

## Customer360

Customer360 uses one repository per feature module.

Example:

customers/
├── repository.py

Future modules such as Orders and Products will also contain their own repositories.

## Responsibility

Repositories answer:

"How is data stored and retrieved?"

Services answer:

"What business operation should happen?"