# Validated Tokity Contract

No Tokity operation is validated yet. This file is intentionally a gate, not an API assumption.

## Required evidence before activation implementation

1. Ticket-created event or supported equivalent.
2. `Sales-expert` tag-added event or supported equivalent.
3. Current-ticket reads for the authorized subject, description, requester, organization, tags, status, and conversation history.
4. Public reply write.
5. Private/internal sales-summary write with distinct visibility.
6. Actor origin, ticket ID, message ID, event ID, and correlation behavior.
7. Authentication and field-level denial for forbidden writes and other-ticket reads.
8. Ticket-to-opportunity association behavior.

Attach tenant-specific request/response examples and permission scopes here before any deployment task is marked complete.
