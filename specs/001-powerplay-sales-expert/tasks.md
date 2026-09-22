---

description: "Dependency-ordered implementation tasks for PowerPlay Sales Expert"
---

# Tasks: PowerPlay Sales Expert

**Input**: Design documents from `/specs/001-powerplay-sales-expert/`

**Prerequisites**: [plan.md](plan.md), [spec.md](spec.md), [research.md](research.md), [data-model.md](data-model.md), [contracts/](contracts/), and [quickstart.md](quickstart.md)

**Implementation boundary**: Copilot Studio agents and Tokity integration are external deployment artifacts. The paths below are the repository record of configuration, evidence, and validation; no task assumes an undocumented Tokity endpoint or trigger.

## Phase 1: Setup

**Purpose**: Establish implementation records, environment prerequisites, and approved product-knowledge ownership.

- [ ] T001 [P] Create `specs/001-powerplay-sales-expert/implementation/README.md` with environment owners, deployment boundaries, and links to the approved design contracts; verify every required artifact has an owner.
- [ ] T002 [P] Create `specs/001-powerplay-sales-expert/implementation/prerequisites.md` with Copilot Studio tenant, connected-agent, licensing, Tokity sandbox, identity, and approved-knowledge prerequisites; verify each prerequisite is marked confirmed, blocked, or owner-assigned.
- [ ] T003 [P] Create `specs/001-powerplay-sales-expert/implementation/knowledge/knowledge-register.md` listing the eight specialists, source owner, reviewer, version, effective date, review date, and lifecycle status; verify no specialist is marked available without an approved source.
- [ ] T004 Create `specs/001-powerplay-sales-expert/implementation/test-fixtures/tickets.md` with sanitized fixtures for unrelated support, clear buying interest, PowerPlay gap, cross-product need, unsupported claim, duplicate event, and explicit human request; verify no production customer data is included.

---

## Phase 2: Foundational

**Purpose**: Prove Tokity capabilities and establish the security, contract, correlation, and observability foundations that block all stories.

**CRITICAL**: Do not implement event triggers or writes until the capability gate produces evidence.

- [ ] T005 Create `specs/001-powerplay-sales-expert/implementation/evidence/tokity-capability-matrix.md` by running a Tokity sandbox or tenant spike for ticket-created detection, `Sales-expert` tag detection, current-ticket reads, customer-facing replies, internal/private summary writes, actor origin metadata, stable IDs, authentication, and field-level denial; verify each capability has request/response evidence or is explicitly marked blocked with its fallback.
- [ ] T006 [P] Create `specs/001-powerplay-sales-expert/implementation/security/access-matrix.md` mapping the authorized current-ticket fields to read permissions and the only allowed writes to public replies and the identified internal sales summary; verify status, assignment, priority, unrelated fields, and other-ticket reads are denied.
- [ ] T007 [P] Create `specs/001-powerplay-sales-expert/implementation/state/idempotency-design.md` defining the `(ticket_id, source_event_id, message_id, operation_type)` key, lease/retry states, agent-origin loop prevention, and correlation storage; verify duplicate and replayed events resolve to one processing result.
- [ ] T008 [P] Configure `specs/001-powerplay-sales-expert/implementation/observability/audit-schema.md` for actor identity, connector scope, request ID, ticket ID, source event ID, operation, result, timestamps, retry state, and redaction rules; verify logs exclude unnecessary customer content.
- [ ] T009 Create `specs/001-powerplay-sales-expert/implementation/contracts/validated-tokity-contract.md` from the capability matrix, recording only verified operations and versioned payload examples; verify no undocumented endpoint, webhook, field ID, or authentication scheme appears as fact.
- [ ] T010 Create `specs/001-powerplay-sales-expert/implementation/failure-policy.md` defining retryable errors, blocked capability behavior, partial-write prevention, retry exhaustion, and the approved fallback from `research.md`; verify each failure path leaves no duplicate reply or misleading summary.

**Checkpoint**: The Tokity capability gate, least-privilege matrix, idempotency design, audit schema, and failure policy are approved before user-story work begins.

---

## Phase 3: User Story 1 - Discover an Opportunity (Priority: P1) MVP

**Goal**: Start only on a verified sales signal or explicit `Sales-expert` tag, read the authorized current ticket, and conduct focused discovery through the same ticket.

**Independent Test**: Run the fixture set for unrelated support, clear sales signal, tag activation, known context, duplicate/self-reply, and permission boundaries; verify the agent starts only when allowed, avoids repetition, and performs no forbidden mutation.

- [ ] T011 [US1] Configure the parent Copilot Studio agent `PowerPlay Sales Expert` and record its approved behavior in `specs/001-powerplay-sales-expert/implementation/copilot/parent/agent-definition.md`; verify it owns discovery, the overall conversation, portfolio recommendations, and handoff without product-specific claims.
- [ ] T012 [US1] Implement the verified current-ticket context read in `specs/001-powerplay-sales-expert/implementation/tokity/current-ticket-read.md` for subject, description, requester, organization details, tags, status, and conversation history; verify the parent cannot read another ticket or an unauthorized field.
- [ ] T013 [US1] Implement new-ticket sales-signal assessment in `specs/001-powerplay-sales-expert/implementation/tokity/activation/ticket-created.md` using only the validated contract; verify unrelated support is classified without a public sales reply and a clear interest or PowerPlay gap can activate discovery.
- [ ] T014 [US1] Implement explicit `Sales-expert` tag activation in `specs/001-powerplay-sales-expert/implementation/tokity/activation/sales-expert-tag.md`; verify the tag starts the sales experience once even when ticket creation was already processed.
- [ ] T015 [US1] Implement focused discovery behavior in `specs/001-powerplay-sales-expert/implementation/copilot/parent/discovery.md` for current process, pain points, desired outcomes, Microsoft environment, and constraints; verify known ticket facts are not asked again and missing facts produce only useful questions.
- [ ] T016 [US1] Implement inbound reply correlation and agent-self-reply filtering in `specs/001-powerplay-sales-expert/implementation/tokity/event-filter.md`; verify replayed events, agent-originated replies, and concurrent deliveries produce no duplicate response.
- [ ] T017 [US1] Implement customer-facing reply formatting in `specs/001-powerplay-sales-expert/implementation/copilot/parent/public-reply.md` so detailed sales-focused answers are prominent in the same ticket; verify internal notes, routing metadata, and confidential information cannot appear in the public reply.
- [ ] T018 [US1] Implement the User Story 1 sandbox runbook in `specs/001-powerplay-sales-expert/implementation/verification/us1-discovery.md` using `quickstart.md` scenarios 1-4, 9, and 10; verify the story independently against the capability evidence and access matrix.

**Checkpoint**: A new or tagged ticket can safely begin discovery, preserve ticket context, answer in the ticket, and avoid duplicate or unrelated support responses.

---

## Phase 4: User Story 2 - Evaluate and Explain Product Fit (Priority: P1)

**Goal**: Ground eight product specialists in approved knowledge, route only relevant needs, and combine typed findings into one accurate sales recommendation.

**Independent Test**: Run single-product, cross-product, incorrect-routing, unsupported-claim, planned/custom, conflicting-finding, and no-fit scenarios; verify specialist scope, evidence status, and parent synthesis.

- [ ] T019 [P] [US2] Create the specialist contract configuration in `specs/001-powerplay-sales-expert/implementation/copilot/specialists/specialist-contract.md` from `contracts/specialist-consultation.md`; verify every response includes fit, need addressed, verified capabilities, caveats, product status, source metadata, and human-confirmation state.
- [ ] T020 [P] [US2] Create and ground the Asset Manager specialist in `specs/001-powerplay-sales-expert/implementation/copilot/specialists/asset-manager.md` using its approved knowledge source; verify it refuses claims outside Asset Manager scope.
- [ ] T021 [P] [US2] Create and ground the Asset Procurement specialist in `specs/001-powerplay-sales-expert/implementation/copilot/specialists/asset-procurement.md` using its approved knowledge source; verify it refuses claims outside Asset Procurement scope.
- [ ] T022 [P] [US2] Create and ground the Change Management specialist in `specs/001-powerplay-sales-expert/implementation/copilot/specialists/change-management.md` using its approved knowledge source; verify it refuses claims outside Change Management scope.
- [ ] T023 [P] [US2] Create and ground the Problem Management specialist in `specs/001-powerplay-sales-expert/implementation/copilot/specialists/problem-management.md` using its approved knowledge source; verify it refuses claims outside Problem Management scope.
- [ ] T024 [P] [US2] Create and ground the HR Joiners specialist in `specs/001-powerplay-sales-expert/implementation/copilot/specialists/hr-joiners.md` using its approved knowledge source; verify it refuses claims outside HR Joiners scope.
- [ ] T025 [P] [US2] Create and ground the HR Leavers specialist in `specs/001-powerplay-sales-expert/implementation/copilot/specialists/hr-leavers.md` using its approved knowledge source; verify it refuses claims outside HR Leavers scope.
- [ ] T026 [P] [US2] Create and ground the Entra Group specialist in `specs/001-powerplay-sales-expert/implementation/copilot/specialists/entra-group.md` using its approved knowledge source; verify it refuses claims outside the Entra Group solution scope.
- [ ] T027 [P] [US2] Create and ground the Data Hub specialist in `specs/001-powerplay-sales-expert/implementation/copilot/specialists/data-hub.md` using its approved knowledge source; verify it refuses claims outside Data Hub scope.
- [ ] T028 [US2] Configure parent routing in `specs/001-powerplay-sales-expert/implementation/copilot/parent/routing-matrix.md` from stated needs to specialists; verify single-product needs route only to relevant specialists and unsupported needs route to insufficient-information.
- [ ] T029 [US2] Implement typed parent-specialist consultation in `specs/001-powerplay-sales-expert/implementation/copilot/parent/specialist-consultation.md`; verify only current-ticket context and the stated need are passed, and each finding is correlated to the parent conversation.
- [ ] T030 [US2] Implement multi-specialist reconciliation in `specs/001-powerplay-sales-expert/implementation/copilot/parent/recommendation-synthesis.md`; verify each recommended solution has a distinct role, conflicts remain visible, and no-fit outcomes are allowed.
- [ ] T031 [US2] Implement product-claim status handling in `specs/001-powerplay-sales-expert/implementation/copilot/parent/claim-guard.md`; verify available, planned, custom-candidate, unverified, and retired statuses are never presented interchangeably and unsupported claims require confirmation.
- [ ] T032 [US2] Implement the User Story 2 verification runbook in `specs/001-powerplay-sales-expert/implementation/verification/us2-product-fit.md` using `quickstart.md` scenarios 5-8; verify incorrect routing, unsupported claims, multiple specialists, and no-fit responses independently.

**Checkpoint**: Product-fit recommendations are specialist-grounded, traceable to stated needs, safe for cross-product opportunities, and honest about uncertainty.

---

## Phase 5: User Story 3 - Prepare the Sales Next Step (Priority: P1)

**Goal**: Keep public replies separate from internal summaries, preserve the current-ticket association, and handle explicit human requests and next actions.

**Independent Test**: Complete a discovery and recommendation conversation, then verify a salesperson can act from the internal summary; test human request, reserved commitments, ambiguous association, retry, and internal/public separation.

- [ ] T033 [US3] Implement the internal sales-summary schema and visibility rules in `specs/001-powerplay-sales-expert/implementation/copilot/parent/internal-summary.md` from `contracts/sales-summary.md`; verify it contains needs, recommendations, reasons, objections, open questions, limitations, buying signals, confirmation needs, next action, ticket ID, and correlation ID.
- [ ] T034 [US3] Implement current-ticket-only summary upsert in `specs/001-powerplay-sales-expert/implementation/tokity/internal-summary-upsert.md`; verify retries update one clearly identified summary and never alter status, assignment, priority, unrelated fields, or another ticket.
- [ ] T035 [US3] Implement explicit human-request handling in `specs/001-powerplay-sales-expert/implementation/copilot/parent/human-request.md`; verify an explicit request produces a handoff state and concise acknowledgement, while answerable questions continue without automatic takeover.
- [ ] T036 [US3] Implement reserved-commitment and verification flags in `specs/001-powerplay-sales-expert/implementation/copilot/parent/sales-escalation-flags.md`; verify proposals, demonstrations, commercial commitments, and unverified claims are flagged without being presented as settled commitments.
- [ ] T037 [US3] Implement next-action selection and incomplete-qualification handling in `specs/001-powerplay-sales-expert/implementation/copilot/parent/next-action.md`; verify the summary records a suitable action and labels missing qualification instead of inferring it.
- [ ] T038 [US3] Implement the User Story 3 verification runbook in `specs/001-powerplay-sales-expert/implementation/verification/us3-handoff.md` using `quickstart.md` scenarios 10-13; verify summary readability, public/internal separation, explicit human request, retries, and correct ticket association.

**Checkpoint**: A salesperson receives a trustworthy internal summary and next action, while customer-facing replies remain safe and human requests are honored.

---

## Phase 6: Polish and Cross-Cutting Evaluation

**Purpose**: Validate the full first release against constitution, security, product quality, and operational readiness.

- [ ] T039 [P] Create `specs/001-powerplay-sales-expert/implementation/verification/security-boundary.md` with unauthorized identity, other-ticket access, forbidden-field mutation, and public/internal leakage tests; verify every denial is audited and leaves no partial write.
- [ ] T040 [P] Create `specs/001-powerplay-sales-expert/implementation/verification/knowledge-review.md` with owner approval records for all eight specialist sources and representative available/planned/custom/unverified claims; verify every customer-facing claim maps to approved evidence.
- [ ] T041 Create `specs/001-powerplay-sales-expert/implementation/verification/end-to-end-release.md` by executing all `quickstart.md` scenarios against a Tokity sandbox or validated stub; verify duplicate-event prevention, unrelated-ticket silence, incorrect routing, unsupported claims, internal/public separation, human requests, retries, and forbidden writes.
- [ ] T042 Create `specs/001-powerplay-sales-expert/implementation/operations/release-readiness.md` with deployment, rollback, monitoring, audit review, owner handoff, and open-dependency status; verify no blocked Tokity capability is shipped as an assumed integration.
- [ ] T043 [P] Update `specs/001-powerplay-sales-expert/implementation/README.md` with the final verified deployment surfaces and evidence links; verify the implementation record remains consistent with `plan.md`, `data-model.md`, and all contracts.

---

## Dependencies and Execution Order

### Phase dependencies

- **Phase 1 Setup**: Can begin immediately.
- **Phase 2 Foundational**: Depends on Phase 1 and blocks all user-story implementation.
- **Phase 3 User Story 1**: Depends on the validated Tokity boundary, access matrix, idempotency design, and failure policy.
- **Phase 4 User Story 2**: Depends on the parent agent baseline from US1 and approved specialist knowledge sources; specialist grounding tasks T020-T027 can run in parallel after T019.
- **Phase 5 User Story 3**: Depends on US1 public reply behavior, US2 typed findings, and the validated internal-update capability.
- **Phase 6 Polish**: Depends on all desired user stories and the capability gate passing.

### User-story order

1. US1 establishes the safe ticket conversation and is the MVP.
2. US2 adds product-fit routing and recommendations.
3. US3 adds trustworthy sales summaries and human-request handling.

### Parallel opportunities

- T001-T004 can run in parallel.
- T006-T008 can run in parallel after T005 begins, provided each uses the same capability evidence format.
- T020-T027 can run in parallel after T019 and the corresponding approved knowledge sources exist.
- T039-T040 and T043 can run in parallel after the story checkpoints.

## Implementation Strategy

### MVP first

1. Complete Phase 1 and the Tokity capability gate in Phase 2.
2. Complete US1 only: safe activation, discovery, public reply, correlation, and permission boundaries.
3. Execute T018 and stop for independent validation/demo.

### Incremental delivery

1. Add US2 specialist grounding and fit synthesis; execute T032.
2. Add US3 summaries, next actions, and explicit human requests; execute T038.
3. Run full release evaluation and readiness tasks T039-T043.

### Task format validation

All implementation tasks use `- [ ] T###`, include `[P]` only where parallel execution is safe, include `[US#]` on user-story tasks, and name a concrete repository path plus a verification step. No task assumes an unverified Tokity API, webhook, field ID, or authentication scheme.
