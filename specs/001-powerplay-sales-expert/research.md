# Research: PowerPlay Sales Expert

## Decision: Use Copilot Studio connectors as the integration boundary

**Rationale**: Microsoft documents connector tools in Copilot Studio and supports custom connectors for publicly available external APIs. The parent and specialists can therefore remain Copilot Studio agents while Tokity access is isolated behind a narrowly scoped connector or adapter.

**Evidence**: [Use connectors in Copilot Studio agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-connectors) documents connector tools, custom connectors, maker-provided credentials, and connector limitations.

**Alternatives considered**: Direct undocumented Tokity calls from agent instructions were rejected because they cannot enforce permissions or provide a testable contract. A future standalone app is outside the first-release scope.

## Decision: Keep Tokity behavior behind a capability-gated boundary adapter

**Rationale**: Public DeskDirector material confirms ticketing, automation, custom forms, and live chat capabilities, but no public Tokity contract was found that verifies ticket-created events, tag-change events, field-level read/write operations, internal updates, or a Copilot Studio message exchange. The implementation must validate these capabilities in a DeskDirector/Tokity tenant or sandbox before selecting a concrete connector, flow, or webhook design.

**Evidence**: [DeskDirector public product page](https://deskdirector.com/) describes ticketing, automation, custom forms, and live chat. The public page does not establish the exact Tokity operations required by this feature. No Tokity or DeskDirector API documentation was present in the repository or retrievable from the public documentation URL checked during planning.

**Open dependency and validation step**: Obtain the tenant-specific Tokity integration/API documentation or run a sandbox capability spike that proves: new-ticket detection, `Sales-expert` tag detection, current-ticket context reads, public replies, internal sales-summary updates, event origin metadata, and correlation identifiers. Record request/response examples and permission scopes in the contracts. **Fallback**: use an authorized Tokity automation or export/import queue that invokes the same boundary contract; if public replies or internal updates cannot be supported, stop before implementation or limit release 1 to a validated manual-in-ticket workflow.

## Decision: Use ticket identity plus event/message identity for idempotency

**Rationale**: New-ticket and tag events, agent replies, and retries can otherwise create duplicate responses or summaries. The boundary must persist or derive a correlation key from ticket ID, source event ID, message ID, and processing type, and must ignore events already completed or currently leased.

**Alternatives considered**: Conversation text matching alone was rejected because repeated or edited messages are ambiguous and unsafe for customer-facing automation.

## Decision: Parent-specialist consultation uses a typed finding contract

**Rationale**: The parent owns discovery and recommendation; specialists own approved product expertise. A structured request passes only the current opportunity context needed for evaluation, and a specialist returns fit, evidence, caveats, product status, unanswered questions, and confidence. This supports multiple specialists without leaking unrelated product knowledge or internal context.

**Alternatives considered**: Free-form specialist prose was rejected because it makes claim verification, conflict resolution, and testing difficult.

## Decision: Product knowledge requires ownership and review metadata

**Rationale**: Every specialist must be grounded in an approved source with an owner, effective date, review date, status, and scope. The parent must not treat missing, expired, or conflicting knowledge as confirmed capability.

**Alternatives considered**: A shared unowned knowledge pool was rejected because it cannot establish claim authority or review accountability.

## Decision: Human handoff is explicit-request driven

**Rationale**: The clarified requirement says the agent answers answerable questions unless the participant explicitly requests a human. Reserved commitments, proposals, demonstrations, and unverified claims are flagged for confirmation but do not silently become promises or change the handoff rule.

## Open dependencies

1. Tokity event and connector contract, including authentication and authorization model.
2. Whether Tokity supports a true internal/private update distinct from a customer-visible reply.
3. Whether the agent can receive customer replies as events without reacting to its own posted replies.
4. Durable location for idempotency and conversation correlation state.
5. Copilot Studio connected-agent feature availability and tenant licensing/configuration for eight specialists.
6. Approved knowledge source and named owner/reviewer for each of the eight solutions.
7. Sales-summary formatting or highlighting capabilities available in the Tokity ticket UI.

## Research boundary

No implementation endpoint, webhook name, Tokity field ID, authentication scheme, or Copilot Studio deployment detail is presented as confirmed until the capability spike supplies evidence.
