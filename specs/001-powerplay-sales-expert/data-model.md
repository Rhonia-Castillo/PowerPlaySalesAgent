# Data Model: PowerPlay Sales Expert

## Ticket Context

The authorized current Tokity ticket context available to the parent.

| Field | Required | Use | Permission |
|---|---:|---|---|
| Ticket ID | Yes | Correlate every event, reply, summary, and audit record | Read |
| Subject | No | Detect sales signal and frame discovery | Read |
| Description | No | Detect sales signal and seed discovery | Read |
| Requester | No | Address the participant and preserve contact context | Read |
| Organization details | No | Understand account context and handoff | Read |
| Tags | No | Detect or confirm `Sales-expert` activation | Read; tag addition is an external trigger, not an agent write |
| Status | No | Context only; never change | Read |
| Conversation history | No | Avoid repetition, answer contextually, and detect explicit human requests | Read |

The parent MUST NOT read other tickets unless separately authorized.

## Customer Conversation

A sequence of authorized ticket messages and agent turns associated with exactly one
Ticket ID. Each turn records source message ID, actor type, timestamp, visibility,
correlation key, and processing status. Agent-originated messages are marked so they
cannot trigger a new response loop.

## Sales Signal

A classification result for a new ticket: `potential-interest`, `powerplay-gap`,
`unrelated-support`, or `uncertain`. It includes evidence excerpts, classifier
confidence, source event ID, and decision timestamp. `uncertain` must not trigger a
customer-facing sales reply; an authorized `Sales-expert` tag explicitly activates
sales handling.

## Specialist Knowledge Source

The approved source for one PowerPlay solution. It includes solution name, scope,
source reference, owner, reviewer, effective date, review date, lifecycle status
(`available`, `planned`, `custom-candidate`, `unverified`, or `retired`), and known
limitations. A specialist must cite this source in its finding.

## Specialist Finding

A typed response from one specialist:

- Solution and knowledge-source version.
- Fit: `fit`, `partial-fit`, `no-fit`, or `insufficient-information`.
- Stated customer need addressed.
- Verified capabilities and value explanation.
- Prerequisites, limitations, integrations, and product status.
- Unsupported questions or claims requiring confirmation.
- Confidence and specialist correlation ID.

## Sales Recommendation

The parent-owned synthesis of one or more findings. It records recommended solutions,
distinct role of each solution, evidence links, conflicts, assumptions, open questions,
and whether no current solution fits. It must never convert `planned`, `custom-candidate`,
or `unverified` information into `available` functionality.

## Sales Summary

A clearly identified internal update in the current ticket containing customer and
organization context when authorized, needs, current process, desired outcomes,
recommendations and reasons, questions answered, objections, limitations and gaps,
buying signals, open qualification questions, claims requiring confirmation, and next
action. It is separate from customer-facing replies and is the only Tokity content the
agent may create or update beyond public replies.

## Processing Record

An idempotency and audit record keyed by `(ticket_id, source_event_id, message_id,
operation_type)`. It records received, ignored, in-progress, completed, failed, and
retry-exhausted states, plus actor identity, connector scope, timestamps, and a safe
reference to the result. It must not store unnecessary customer content.

## State transitions

`received -> classified -> ignored` for unrelated or unauthorized events.

`received -> classified -> active -> awaiting-reply -> active` for sales conversations.

`active -> human-requested -> handoff-pending -> handed-off` when the participant
explicitly requests a human.

Any state may move to `failed -> retryable` or `failed -> retry-exhausted`; retries must
use the same idempotency key and must not duplicate a public reply or summary update.
