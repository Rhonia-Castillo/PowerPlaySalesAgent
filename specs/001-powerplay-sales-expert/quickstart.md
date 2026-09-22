# Quickstart Validation: PowerPlay Sales Expert

This guide validates the design against a Tokity sandbox, approved stub, or recorded
connector contract. Do not use production customer data for initial tests.

## Prerequisites

1. A Copilot Studio parent agent named `PowerPlay Sales Expert`.
2. Eight specialist agents with approved knowledge sources and named owners.
3. A Tokity test ticket environment or boundary stub implementing the logical contract in
   `contracts/tokity-ticket-boundary.md`.
4. Test identities for an authorized participant, an unauthorized participant, and the
   agent/service connection.
5. Test tickets representing an unrelated support request, a clear PowerPlay signal, a
   cross-product need, an unsupported claim, and an explicit human request.

## Capability gate

Before functional tests, prove and record evidence for ticket creation detection, tag
change detection, current-ticket reads, public replies, private/internal summary writes,
agent-origin metadata, stable ticket/message IDs, authentication, and field-level
permission failures. If any item cannot be proven, mark the corresponding implementation
work blocked and use the fallback documented in `research.md`.

## Scenarios

1. **New unrelated ticket**: create a support ticket without a PowerPlay signal. Expect
   classification as `unrelated-support`, no public reply, and no summary.
2. **New sales-signal ticket**: create a ticket with a clear PowerPlay buying signal.
   Expect one detailed sales-focused reply and one internal summary tied to the ticket.
3. **Explicit tag activation**: add `Sales-expert` to a ticket without relying on ticket
   creation. Expect the sales conversation to start once.
4. **Known context**: include subject, description, requester, organization, tags,
   status, and history. Expect no unnecessary repetition.
5. **Single specialist**: state a need for one solution. Expect only the matching
   specialist to be consulted and its approved evidence reflected in the reply.
6. **Multiple specialists**: state needs spanning two solutions. Expect both specialists
   to return findings and the parent to produce one reconciled recommendation.
7. **Unsupported claim**: ask for an unverified feature, price, saving, or commitment.
   Expect a clear uncertainty label and human-confirmation note, with no invention.
8. **Incorrect routing**: ask a specialist about another product. Expect the specialist
   not to answer outside its scope and the parent to route or mark insufficient data.
9. **Duplicate events and self-replies**: replay the same event and deliver the agent's
   own reply as an inbound event. Expect no duplicate public reply or summary update.
10. **Permission boundaries**: attempt status, assignment, priority, unrelated-field, or
    other-ticket operations. Expect authorization failure and no mutation.
11. **Internal/public separation**: put confidential routing or internal notes in the
    generated state. Expect them only in the internal summary, never in the public reply.
12. **Human request**: ask explicitly for a human agent. Expect a handoff request and no
    further automated sales reply beyond a concise acknowledgement.
13. **Retry/failure**: force a timeout during each write. Expect retry with the same key,
    no duplicate result, audit visibility, and a retry-exhausted state after the limit.

## Exit criteria

All scenarios pass in the sandbox or stub, capability evidence is attached to the
implementation work, no forbidden field changes occur, and the specialist knowledge
owners approve representative claims for all eight solutions.
