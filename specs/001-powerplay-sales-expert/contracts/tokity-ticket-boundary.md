# Contract: Tokity Ticket Boundary

This is a logical contract. Concrete Tokity endpoint names, payloads, and authentication
must be supplied by the capability spike before implementation.

## Inputs

- `ticketId` and source event/message identity.
- Event type: `ticket.created`, `ticket.tag_added`, `ticket.reply_received`, or a
  validated equivalent supplied by Tokity.
- Authorized current-ticket context: subject, description, requester, organization,
  tags, status, and conversation history.
- Actor identity and authorization context.

## Outputs

- `ignore`: event is unrelated, unauthorized, duplicate, or an agent-originated reply.
- `reply`: customer-facing message for the current ticket only.
- `internal_summary`: clearly identified internal sales summary for the current ticket.
- `handoff_requested`: participant explicitly requested a human agent.
- `retryable_error` or `blocked_dependency`: no unsafe partial write.

## Write rules

Allowed: post a customer-facing reply in the current ticket and create/update the
clearly identified internal sales summary.

Forbidden: change ticket status, assignment, priority, unrelated fields, or any other
ticket; read other tickets without separate authorization.

## Idempotency and loop prevention

Every operation includes `ticketId`, source event ID, message ID, operation type, and a
stable correlation ID. The boundary rejects completed duplicate keys and ignores replies
whose origin is the agent or whose correlation ID is already processed.

## Security

Use least-privilege credentials scoped to the current-ticket operations. Preserve actor,
connection, scope, request ID, result, and timestamp in audit logs without logging full
sensitive message content by default.
