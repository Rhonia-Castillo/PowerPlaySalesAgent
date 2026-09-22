# Audit Schema

Each boundary operation records:

- `ticket_id`
- `source_event_id`
- `message_id`
- `conversation_id`
- `actor_id` and actor type
- connector/permission scope
- request ID
- operation type
- result: received, ignored, in-progress, completed, failed, or retry-exhausted
- timestamp and retry count
- safe result reference
- redaction indicator

Full customer message content is excluded by default. Audit access is restricted to authorized project operators.
