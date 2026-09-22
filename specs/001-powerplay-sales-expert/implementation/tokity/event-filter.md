# Inbound Event Filter

Ignore an event when its idempotency key is completed, its origin is the agent, its ticket is unauthorized, or classification says unrelated/uncertain without explicit `Sales-expert` activation. Concurrent delivery requires a lease on the same key.

Implementation status: design complete; runtime implementation is blocked pending Tokity event identity and origin metadata.
