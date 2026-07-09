# ADR-003: Soft Delete Strategy

## Status

Accepted

## Context

Customer records represent long-lived business entities. Permanently deleting customer records would remove historical information and make auditing difficult.

## Decision

Customer360 will use a soft delete strategy by changing the customer's `status` from `active` to `inactive` instead of physically deleting database records.

## Consequences

### Advantages

- Preserves historical data.
- Supports auditing.
- Allows future account restoration.
- Prevents accidental data loss.

### Disadvantages

- Queries must account for inactive records.
- Additional filtering is required.

## Future Considerations

As Customer360 evolves, soft deletion may be enhanced with fields such as:

- deleted_at
- deleted_by
- deletion_reason