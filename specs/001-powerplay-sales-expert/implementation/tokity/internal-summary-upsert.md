# Internal Summary Upsert

Upsert only the clearly identified internal summary on the current ticket. Use the same idempotency key for retries. Deny status, assignment, priority, unrelated-field, and other-ticket writes.

Implementation status: blocked pending proof that Tokity supports a distinct internal/private update.
