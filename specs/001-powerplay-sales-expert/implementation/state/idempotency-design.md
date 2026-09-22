# Idempotency and Correlation Design

Use `(ticket_id, source_event_id, message_id, operation_type)` as the processing key. Store or derive a stable conversation correlation ID for the current ticket.

## States

`received -> classified -> ignored` for unrelated, unauthorized, duplicate, or self-originated events.

`received -> classified -> active -> awaiting-reply -> active` for sales conversations.

`active -> human-requested -> handoff-pending -> handed-off` for explicit human requests.

Any state may enter `failed -> retryable` or `failed -> retry-exhausted`.

## Rules

- A completed key cannot produce a second public reply or summary update.
- An in-progress lease prevents concurrent processing of the same key.
- Agent-originated replies are ignored as new customer turns.
- Retries reuse the same key and correlation ID.
- Audit records retain identity, operation, outcome, and timestamps, not unnecessary full message content.
