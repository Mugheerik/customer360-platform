# Application Logging

## Purpose

Customer360 uses Python's built-in `logging` module to record application events.

Logging helps engineers understand application behavior during development and troubleshoot issues in production.

## Logging Principles

- Log business events, not implementation details.
- Include enough context to understand what happened.
- Avoid logging sensitive information.
- Keep messages concise and meaningful.

## Current Usage

Application logs are configured centrally in `app/core/logging.py`.

Business services use module-specific loggers created with:

```python
logger = logging.getLogger(__name__)
```

This allows logs to identify the source module automatically.