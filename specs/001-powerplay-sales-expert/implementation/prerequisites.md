# Implementation Prerequisites

| Prerequisite | Status | Evidence or owner |
|---|---|---|
| Copilot Studio tenant and authoring access | Blocked | Owner TBD |
| Connected-agent capability and licensing for eight specialists | Unverified | Validate in target tenant; owner TBD |
| Tokity sandbox or tenant integration access | Blocked | Tokity owner TBD |
| Authorized identity and least-privilege connection | Unverified | Validate with Tokity capability spike |
| Approved knowledge source for each specialist | Blocked | See `knowledge/knowledge-register.md` |
| Durable idempotency/correlation storage | Unverified | Decide after Tokity capability spike |
| Private/internal summary operation | Unverified | Must be proven distinct from public reply |
| Test identities and sanitized ticket fixtures | Ready locally | See `test-fixtures/tickets.md` |

Implementation may proceed locally for documentation and evaluation design, but deployment must not proceed while a blocking prerequisite remains unresolved.
