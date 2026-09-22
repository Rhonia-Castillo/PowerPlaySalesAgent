# Implementation Plan: PowerPlay Sales Expert

**Branch**: `001-powerplay-sales-expert` | **Date**: 2026-09-23 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/001-powerplay-sales-expert/spec.md`

## Summary

Deliver a parent Copilot Studio agent that conducts a sales conversation in the
current Tokity ticket, delegates product-fit questions to eight connected
specialist agents, and writes a customer-facing answer plus an internal sales
summary without exceeding the ticket permissions in the spec. The design uses a
Tokity boundary adapter and idempotent conversation state; exact Tokity event and
message capabilities remain a validation gate.

## Technical Context

**Language/Version**: Copilot Studio authored agent behavior and declarative integration configuration; adapter implementation language is an open delivery choice.

**Primary Dependencies**: Microsoft Copilot Studio, Power Platform connector/custom connector capability, Tokity/DeskDirector supported integration surface, approved PowerPlay product knowledge.

**Storage**: Tokity ticket and internal sales summary are the system of record; minimal idempotency and conversation correlation state requires an approved durable store or Tokity-supported marker.

**Testing**: Copilot Studio test conversations, connector/contract tests against a Tokity sandbox or stub, end-to-end ticket scenarios, security and prompt-evaluation scenarios.

**Target Platform**: Copilot Studio parent and connected specialist agents, surfaced through replies in the Tokity ticket; standalone app is out of scope for release 1.

**Project Type**: Multi-agent sales automation integrated with a ticketing system.

**Performance Goals**: Acknowledge eligible ticket events once, produce a useful response within the agreed Tokity/Copilot interaction window, and avoid duplicate replies or summaries; exact service-level targets require Tokity testing.

**Constraints**: Least privilege; current-ticket-only access; no status, assignment, priority, or unrelated-field changes; no unrelated-ticket reads; public replies must exclude internal summary content; no invented product claims; explicit human request triggers handoff; all unsupported Tokity capabilities remain open dependencies.

**Scale/Scope**: One parent, eight specialists, one current ticket per conversation, and first-release discovery/recommendation/handoff behavior for the named PowerPlay portfolio.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Pass. The design preserves discovery before recommendation, routes product expertise to specialists, grounds claims in approved knowledge, limits Tokity access, preserves opportunity context, escalates only on explicit human request while flagging reserved commitments, and includes realistic quality scenarios. No constitution violation requires an exception.

## Project Structure

### Documentation (this feature)

```text
specs/001-powerplay-sales-expert/
├── plan.md              # This file (/speckit-plan command output)
├── research.md          # Phase 0 output (/speckit-plan command)
├── data-model.md        # Phase 1 output (/speckit-plan command)
├── quickstart.md        # Phase 1 output (/speckit-plan command)
├── contracts/           # Phase 1 output (/speckit-plan command)
└── tasks.md             # Phase 2 output (/speckit-tasks command - NOT created by /speckit-plan)
```

### Source Code (repository root)

```text
specs/001-powerplay-sales-expert/
├── plan.md
├── research.md
├── data-model.md
├── contracts/
│   ├── tokity-ticket-boundary.md
│   ├── specialist-consultation.md
│   └── sales-summary.md
└── quickstart.md
```

**Structure Decision**: This is an agent-and-integration design rather than a
local application source tree. The feature directory contains the executable
design contracts, validation guide, and research record. Copilot Studio agents,
knowledge sources, connector configuration, and Tokity-side automation are
deployment artifacts to be created during implementation after the Tokity
capability gate passes.

## Complexity Tracking

No constitution violations. The parent-plus-specialist topology is required by the
confirmed project direction, and the boundary adapter is required to enforce the
current-ticket permission model and isolate unverified Tokity details.

## Post-Design Constitution Check

Pass. The design keeps discovery before recommendations, assigns product expertise to
specialists, requires approved knowledge and explicit uncertainty, limits data to the
authorized current ticket, separates public replies from internal summaries, prevents
duplicate or misleading updates, and supports realistic quality review. The explicit
human-request handoff and all reserved commitments remain governed by the constitution.
