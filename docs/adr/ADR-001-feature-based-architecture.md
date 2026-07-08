# ADR-001: Feature-Based Architecture

**Status:** Accepted

**Date:** 2026-07-08

---

# Context

Customer360 is expected to grow into a large, modular platform supporting multiple business domains such as customers, orders, analytics, AI, and notifications.

A scalable project structure is required to keep related code together and reduce coupling between modules.

---

# Decision

The platform will use a feature-based architecture.

Each business domain will own its routers, services, repositories, models, schemas, and tests.

Example:

modules/
    customers/
    orders/
    payments/

---

# Alternatives Considered

## Layer-Based Architecture

Advantages:
- Simple for small projects.

Disadvantages:
- Features become scattered across multiple folders.
- Difficult to maintain as the codebase grows.

---

# Consequences

Advantages:

- High cohesion
- Better scalability
- Easier onboarding
- Independent feature development
- Improved maintainability

Disadvantages:

- Slightly more structure for very small applications.

---

# Status

Accepted.