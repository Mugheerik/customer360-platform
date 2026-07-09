# Global Exception Handling

## Purpose

Business logic should not depend on the web framework.

Instead of raising HTTP-specific exceptions inside services, Customer360 raises business exceptions (for example, `CustomerNotFoundError`). Global exception handlers convert those exceptions into consistent HTTP responses.

## Benefits

- Keeps the service layer framework-independent.
- Centralizes HTTP error formatting.
- Produces consistent API responses.
- Makes future frameworks or interfaces easier to support.

## Flow

HTTP Request

↓

Router

↓

Service

↓

Business Exception

↓

Global Exception Handler

↓

HTTP Response