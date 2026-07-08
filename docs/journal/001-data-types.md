# Journal 007 — Database Data Types

**Date:** 2026-07-08

---

# Lecture Summary

Today's lecture introduced database data types and their role in designing reliable database schemas.

Rather than viewing a database as a place to store arbitrary values, we explored how each column represents a specific business concept and therefore requires an appropriate data type.

---

# What Changed Today

We shifted our focus from API architecture to database engineering.

The Customer module now has an initial design document describing its purpose, planned API endpoints, and core data fields.

---

# Important Concepts

- Database data types
- Business entities
- UUID identifiers
- TIMESTAMPTZ
- JSONB
- Data integrity
- Enterprise schema design

---

# Architect's Perspective

A database should never trust the application.

Even if the API validates incoming requests, the database must still enforce correctness through appropriate data types and constraints.

Protecting data at multiple layers increases reliability and reduces the risk of inconsistent or invalid records.

---

# Customer360 Impact

The Customer module is now formally defined as the foundational domain of the platform.

Future modules such as Orders, Payments, Analytics, AI, and Notifications will reference customers rather than storing duplicate customer information.

---

# Next Steps

The next lecture will introduce database constraints, including:

- NOT NULL
- UNIQUE
- PRIMARY KEY
- FOREIGN KEY
- CHECK constraints

These constraints will be applied to the Customer schema before implementation begins.