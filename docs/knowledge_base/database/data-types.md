# Database Data Types

---

# Definition

A data type defines the kind of information that may be stored inside a database column.

Examples include text, numbers, dates, timestamps, booleans, and JSON documents.

Choosing the correct data type improves data integrity, storage efficiency, and query performance.

---

# Why Data Types Exist

A database should protect data.

Instead of allowing any value to be stored anywhere, each column declares what kind of information it accepts.

Example:

Date of birth should contain a date.

Email should contain text.

Created time should contain a timestamp.

This prevents invalid data from entering the database.

---

# Common PostgreSQL Data Types

## UUID

Used for globally unique identifiers.

Example:

550e8400-e29b-41d4-a716-446655440000

Recommended for distributed systems.

---

## VARCHAR

Stores text with a maximum length.

Example:

First Name

Last Name

Email

---

## TEXT

Stores unlimited text.

Useful for:

- Notes
- Descriptions
- Comments

---

## BOOLEAN

Stores two values.

TRUE

FALSE

---

## DATE

Stores calendar dates.

Example:

1999-05-18

Useful for birthdays.

---

## TIMESTAMP WITH TIME ZONE (TIMESTAMPTZ)

Stores date and time.

Always stored in UTC in production systems.

Example:

2026-07-08 09:45 UTC

---

## INTEGER

Stores whole numbers.

Useful for counters and quantities.

---

## NUMERIC

Stores precise decimal numbers.

Useful for financial calculations because floating point values introduce rounding errors.

---

## JSONB

Stores structured JSON documents.

Useful when data varies between records.

Example:

Customer preferences

Application settings

Metadata

---

# Choosing the Correct Type

The selected data type should represent the business meaning of the data rather than simply making storage possible.

For example:

Email is text.

Birth date is a date.

Price is numeric.

Created time is a timestamp.

---

# Industry Practice

Modern backend systems generally:

- Use UUID for identifiers.
- Store timestamps in UTC.
- Use NUMERIC for financial values.
- Use JSONB only when flexibility is required.
- Prefer explicit data types over generic TEXT.

---

# Customer360 Usage

Customer360 will primarily use:

- UUID
- VARCHAR
- TEXT
- BOOLEAN
- DATE
- TIMESTAMPTZ
- NUMERIC
- JSONB

These types are sufficient for the majority of enterprise backend systems.

---

# Key Takeaways

- Data types define what may be stored.
- Correct data types improve reliability.
- The database should protect data integrity.
- Data modeling begins with choosing appropriate data types.