# Feature Specification: PowerPlay Sales Expert

**Feature Branch**: `001-powerplay-sales-expert`

**Created**: 2026-09-23

**Status**: Draft

**Input**: User description: "Define the first release of PowerPlay Sales Expert for Tokity-based PowerPlay opportunity discovery, product fit recommendations, value explanation, and sales handoff."

## Clarifications

### Session 2026-09-23

- Q: Where should the potential customer converse directly with PowerPlay Sales Expert? -> A: Directly in the Tokity ticket; a standalone app is a future iteration and out of scope for the first release.
- Q: What Tokity event makes the experience available? -> A: A newly created ticket or a manually added `Sales-expert` ticket tag.
- Q: Which Tokity fields may PowerPlay Sales Expert read and update? -> A: Read ticket context; update the structured sales summary.
- Q: What detailed Tokity access and activation behavior is required? -> A: Read the authorized current ticket's subject, description, requester, organization details, tags, status, and conversation history; post customer-facing replies in that ticket; add or update only a clearly identified internal sales summary; do not change status, assignment, priority, unrelated fields, or read other tickets. A new ticket is assessed for a clear buying-interest or PowerPlay solution-gap signal without interrupting unrelated support, while adding the `Sales-expert` tag explicitly starts the agent.
- Q: When should the human salesperson take ownership of the conversation? -> A: Only when the participant explicitly asks for a human agent; otherwise PowerPlay Sales Expert answers all questions it can answer, while unsupported claims and commitments remain clearly flagged for confirmation.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Discover an Opportunity (Priority: P1)

A potential PowerPlay customer is identified in a Tokity opportunity. The PowerPlay Sales Expert uses relevant information already supplied in that opportunity, asks focused questions only when needed, and builds a shared understanding of the customer's current process, pain points, desired outcomes, Microsoft environment, and constraints.

**Why this priority**: Discovery is required before a trustworthy fit recommendation and prevents the customer from repeating information already available.

**Independent Test**: Provide a Tokity opportunity with partial customer context and verify that the conversation acknowledges known facts, asks only relevant missing questions, and records the resulting discovery context.

**Acceptance Scenarios**:

1. **Given** an eligible Tokity opportunity with customer context, **When** the experience starts, **Then** the parent agent uses available relevant context before asking discovery questions.
2. **Given** discovery information is incomplete, **When** the parent agent needs a detail to assess fit, **Then** it asks a focused question about process, pain point, outcome, Microsoft environment, or constraint.
3. **Given** a customer or salesperson provides information already present in the opportunity, **When** the parent agent receives it, **Then** it does not treat the information as new or create a misleading duplicate.
4. **Given** a conversation is conducted in a Tokity ticket, **When** the parent responds, **Then** it presents a detailed, sales-focused answer prominently in the ticket.
5. **Given** a newly created ticket contains a clear potential buying-interest or PowerPlay solution-gap signal, **When** the ticket is assessed, **Then** the agent may begin the sales conversation; **given** the ticket is unrelated support without that signal, **then** the agent does not interrupt it.
6. **Given** an authorized user adds the `Sales-expert` tag, **When** the ticket is processed, **Then** the agent starts the sales conversation for that ticket.

### User Story 2 - Evaluate and Explain Product Fit (Priority: P1)

The parent agent consults the relevant PowerPlay solution specialists, evaluates one or more solutions against the customer's stated needs, and presents a coherent recommendation with a fair explanation of verified value.

**Why this priority**: The core customer outcome is a recommendation grounded in genuine fit rather than a generic product pitch.

**Independent Test**: Provide discovery context covering one solution and another context crossing two solution boundaries, then verify that the parent consults the relevant specialists and explains each recommendation's distinct role.

**Acceptance Scenarios**:

1. **Given** a stated need that maps to an in-scope solution, **When** the parent evaluates fit, **Then** it consults that solution's specialist and explains the recommendation using approved product information.
2. **Given** a stated need that crosses product boundaries, **When** the parent evaluates fit, **Then** it may consult multiple relevant specialists and presents one reconciled recommendation.
3. **Given** no current solution clearly fits, **When** the parent evaluates the opportunity, **Then** it says so and identifies what would need to change or be validated.
4. **Given** a product question or objection exceeds approved knowledge, **When** the agent responds, **Then** it identifies the unsupported claim or question and marks it for human confirmation.
5. **Given** a capability is planned or may require custom work, **When** the agent discusses it, **Then** it distinguishes that status from available functionality.

### User Story 3 - Prepare the Sales Next Step (Priority: P1)

The experience produces a readable opportunity summary and proposes a suitable next step, such as a discovery call, focused demonstration, technical validation, or discussion with a salesperson.

**Why this priority**: The experience must advance qualified opportunities without making commitments reserved for a human sales owner.

**Independent Test**: Complete a conversation with known needs, recommendations, open questions, and objections, then verify that a salesperson can understand the opportunity and act without reconstructing the conversation.

**Acceptance Scenarios**:

1. **Given** a completed discovery and fit discussion, **When** the experience prepares the next step, **Then** the summary includes known customer context, needs, recommendations, limitations, open qualification information, and a suggested action.
2. **Given** a commercial commitment, formal proposal, demonstration request, or claim requiring verification, **When** it arises, **Then** the experience identifies the appropriate human sales owner as the next decision-maker.
3. **Given** a conversation cannot be safely associated with one Tokity opportunity, **When** a handoff would be prepared, **Then** the experience does not create or apply a misleading update.

### Edge Cases

- A Tokity opportunity has no usable customer context; the experience states the gap and asks only the minimum discovery questions needed to continue.
- A newly created ticket is unrelated to PowerPlay sales; the experience does not interrupt the support request.
- Relevant Tokity information is missing, stale, contradictory, or inaccessible; the experience treats it as unconfirmed and does not invent a replacement.
- No specialist has approved knowledge for the customer's question; the parent identifies the gap and routes it for human confirmation.
- Multiple specialists provide overlapping or conflicting information; the parent does not present an unresolved conflict as fact.
- The customer changes or withdraws a stated need; the parent revisits fit instead of preserving an obsolete recommendation.
- A handoff is attempted more than once for the same opportunity; the experience avoids duplicate or misleading updates.
- The conversation ends before qualification is complete; the summary labels the opportunity as incomplete and records the next information needed.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The experience MUST provide one parent agent named PowerPlay Sales Expert that owns discovery, the overall conversation, portfolio-wide recommendations, and the sales handoff.
- **FR-002**: The first release MUST provide a separate specialist agent for each of Asset Manager, Asset Procurement, Change Management, Problem Management, HR Joiners, HR Leavers, the Entra Group solution, and Data Hub.
- **FR-003**: Each specialist MUST answer questions about only its assigned solution using approved product information and MUST explain how verified capabilities address stated customer needs.
- **FR-004**: The parent MUST use relevant information supplied through the associated Tokity opportunity before asking the customer or salesperson to repeat it.
- **FR-005**: The parent MUST ask focused discovery questions when information needed to assess fit is missing, including current process, pain points, desired outcomes, relevant Microsoft environment, and constraints.
- **FR-006**: The parent MUST select and consult relevant specialists based on the customer's stated needs and MUST be able to consult multiple specialists for cross-product needs.
- **FR-007**: The parent MUST reconcile specialist findings into one coherent recommendation and explain the reason for each recommended solution.
- **FR-008**: The parent MUST state when no current PowerPlay solution clearly fits and MUST identify the change or validation needed before a recommendation can be made.
- **FR-009**: Customer-facing product claims MUST be grounded in approved information. The experience MUST distinguish available functionality from planned functionality, possible custom work, and unverified claims.
- **FR-010**: The experience MUST NOT invent features, pricing, savings, timelines, certifications, references, contractual commitments, or other unsupported claims.
- **FR-011**: The experience MUST respond to questions and objections directly and fairly without high-pressure or exaggerated claims, and MUST present a detailed, sales-focused answer prominently in the Tokity ticket.
- **FR-012**: The experience MUST prepare a structured, readable sales summary associated with the correct Tokity opportunity when the association is confirmed.
- **FR-013**: The sales summary MUST include, when available and appropriate, customer organization and contact details, stated needs, current process, desired outcomes, recommended solutions and reasons, answered questions, objections, limitations, gaps, buying signals, qualification needs, claims requiring confirmation, and the suggested next action.
- **FR-014**: The experience MUST avoid duplicate or misleading Tokity updates and MUST identify information that requires human confirmation.
- **FR-015**: The experience MUST offer a suitable next step, such as a discovery call, focused demonstration, technical validation, or discussion with a salesperson.
- **FR-016**: The experience MUST continue answering questions it can answer without human takeover and MUST transfer the conversation to a human sales agent when the participant explicitly asks for one. Commercial commitments, formal proposals, demonstrations, and claims requiring verification MUST be identified as requiring human confirmation; the agent MUST NOT present them as settled facts or commitments.
- **FR-017**: The first release MUST define who may converse with the agent and where the conversation takes place: an authorized person who has raised potential interest in PowerPlay or identified a gap that PowerPlay may address converses directly in the Tokity ticket. A standalone app is out of scope for this release.
- **FR-018**: When a new Tokity ticket is created, the experience MUST assess whether the ticket contains a clear potential buying-interest signal or a gap that an in-scope PowerPlay solution may address. It MUST begin a sales conversation only when that signal is clear and MUST NOT interrupt an unrelated support request. Adding the `Sales-expert` tag MUST explicitly start the agent for that ticket.
- **FR-019**: The parent MUST be permitted to read only the authorized current ticket's subject, description, requester, organization details, tags, status, and conversation history. It MUST NOT read other tickets unless that access is separately specified and authorized.
- **FR-020**: The parent MUST be permitted to post customer-facing replies in the current ticket and add or update only a clearly identified internal sales summary containing the customer's needs, recommended PowerPlay solutions, reasons, objections, open questions, and next action. It MUST NOT change the ticket's status, assignment, priority, or other unrelated fields.
- **FR-021**: The first release MUST define the takeover point for a human salesperson: the participant's explicit request for a human agent is the takeover trigger.
- **FR-022**: The parent MUST preserve the opportunity context throughout the conversation and MUST label unknown, stale, conflicting, or unverified information rather than presenting it as fact.
- **FR-023**: New PowerPlay solutions MUST be addable through approved product knowledge and a specialist responsibility without weakening the parent's core sales principles.

### Key Entities *(include if feature involves data)*

- **Tokity Opportunity**: The opportunity record that establishes the relevant customer context and remains associated with the conversation and sales summary. It may contain organization, contact, needs, process, outcomes, qualification, and sales ownership information when available and authorized.
- **Customer Conversation**: The interaction in which an authorized participant provides or confirms discovery information, asks product questions, raises objections, and receives recommendations or next-step guidance.
- **PowerPlay Solution**: An in-scope portfolio offering with approved product knowledge and one specialist agent. Initial solutions are Asset Manager, Asset Procurement, Change Management, Problem Management, HR Joiners, HR Leavers, the Entra Group solution, and Data Hub.
- **Specialist Finding**: A product-specific explanation or fit assessment returned by a specialist using approved information and tied to stated customer needs.
- **Sales Handoff**: The structured summary of known context, needs, recommendations, limitations, open questions, buying signals, verification needs, and next action associated with the correct opportunity.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In at least 90% of representative scenarios where relevant opportunity information is available, the first parent response uses that information without asking the participant to repeat it.
- **SC-002**: In at least 90% of representative fit-assessment scenarios, every recommendation is traceable to a stated customer need and an approved specialist finding or approved product fact.
- **SC-003**: In 100% of scenarios involving unsupported, planned, or potentially custom capabilities, the response labels the status accurately and identifies whether human confirmation is required.
- **SC-004**: In at least 90% of completed opportunity scenarios, a salesperson can identify the customer's needs, recommended solutions, open qualification questions, and next action from the sales handoff without rereading the full conversation.
- **SC-005**: In 100% of no-fit scenarios, the experience clearly states that no current solution is confirmed as a fit and does not force a product recommendation.
- **SC-006**: In 100% of scenarios where the participant explicitly requests a human agent, the experience identifies or initiates the human sales handoff; in all other scenarios, it continues answering answerable questions while clearly flagging commitments and claims requiring confirmation.
- **SC-007**: In 100% of handoff scenarios, the summary is associated with the correct Tokity opportunity or is withheld when that association cannot be confirmed.

## Assumptions

- The first release is limited to the eight named PowerPlay solutions; future solutions require approved knowledge before inclusion.
- The first release conducts the conversation directly in the Tokity ticket; a standalone app is deferred to a future iteration.
- Product-specific recommendations depend on approved knowledge being supplied for the relevant specialist; missing knowledge is treated as an explicit gap.
- A newly created Tokity ticket is assessed for a clear buying-interest or PowerPlay solution-gap signal; unrelated support tickets are not interrupted. An authorized `Sales-expert` ticket tag explicitly starts the agent.
- The authorized current ticket context includes subject, description, requester, organization details, tags, status, and conversation history. The parent may post customer-facing replies and add or update only a clearly identified internal sales summary; it cannot change status, assignment, priority, unrelated fields, or read other tickets without separate authorization.
- Customer and internal sales information is available only to authorized participants and agents in the correct opportunity context.
- The detailed integration design, including how an event is detected or how records are updated, is deferred to planning after the unresolved requirements are decided.
- The experience may support a partially complete conversation and must label incomplete qualification rather than infer missing facts.
