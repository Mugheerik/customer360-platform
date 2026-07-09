# ADR-002: PostgreSQL as the Primary Transactional Database

**Status:** Accepted

**Date:** 2026-07-09

---

# Context

Customer360 requires a reliable transactional database to store customer information and support future business capabilities.

The platform is expected to evolve into an enterprise system that includes analytics, automation, AI services, and event-driven components. The primary database must therefore provide strong data integrity, support complex relationships, and scale with increasing application complexity.

---

# Decision

Customer360 will use PostgreSQL as its primary transactional database.

PostgreSQL will be responsible for:

- Persisting application data
- Maintaining relational integrity
- Supporting ACID transactions
- Enforcing constraints
- Providing a foundation for future reporting and analytics

Application access to PostgreSQL will be managed through SQLAlchemy ORM and the Repository Pattern.

---

# Rationale

PostgreSQL was selected because it provides:

- Mature and widely adopted open-source technology
- Excellent support for relational data modeling
- Strong ACID compliance
- Advanced indexing and query optimization
- Rich data types (including JSONB when appropriate)
- Compatibility with modern Python frameworks
- Excellent Docker support
- Strong ecosystem and long-term community support

The database also aligns well with the long-term architecture of Customer360 as an Intelligent Systems platform.

---

# Alternatives Considered

## MySQL

Advantages:

- Mature ecosystem
- Broad adoption
- Good performance

Reasons not selected:

- PostgreSQL provides more advanced SQL capabilities and richer support for complex data models.

---

## MongoDB

Advantages:

- Flexible document model
- Rapid schema evolution

Reasons not selected:

- Customer360 manages highly structured business entities and relationships.
- Relational integrity is a primary requirement.
- PostgreSQL better supports future analytics and reporting workloads.

MongoDB may still be introduced in the future if a document-oriented workload justifies its use.

---

# Consequences

Positive:

- Strong data consistency
- Excellent support for enterprise applications
- Clear relational modeling
- Reliable transaction management
- Seamless integration with SQLAlchemy and Alembic

Trade-offs:

- Schema design requires more planning than document databases.
- Normalization introduces additional design effort.
- Developers must understand SQL and relational modeling.

These trade-offs are acceptable given the platform's long-term goals.

---

# Related Architecture

The persistence layer will evolve as follows:

```
FastAPI

↓

Service Layer

↓

Repository Layer

↓

SQLAlchemy ORM

↓

PostgreSQL
```

---

# Future Impact

This decision establishes the foundation for future capabilities, including:

- Customer lifecycle management
- Order management
- Event-driven processing
- Analytics pipelines
- AI-powered customer insights
- Business intelligence reporting

Any future database technologies must integrate with—not replace—the primary PostgreSQL transactional database unless a new ADR supersedes this decision.