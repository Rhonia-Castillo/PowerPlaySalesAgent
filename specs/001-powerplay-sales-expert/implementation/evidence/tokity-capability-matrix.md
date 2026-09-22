# Tokity Capability Matrix

Status is intentionally blocked or unverified until tenant-specific evidence is supplied. Public DeskDirector material does not prove these exact Tokity operations.

| Capability | Evidence | Status | Fallback/next step |
|---|---|---|---|
| Detect newly created ticket | No tenant/API evidence | blocked | Run Tokity sandbox spike; otherwise manual `Sales-expert` tag |
| Detect `Sales-expert` tag | No tenant/API evidence | blocked | Validate tag event or use authorized manual launch |
| Read current ticket context | No field-level contract | blocked | Obtain tenant contract and permission test |
| Receive customer replies | No event contract | blocked | Validate inbound event or manual polling/launch |
| Post customer-facing reply | No write contract | blocked | Validate sandbox public-reply operation |
| Write private/internal summary | No visibility contract | blocked | Validate true internal update; stop if only public replies exist |
| Identify agent-originated replies | No origin metadata evidence | unverified | Validate event metadata or use correlation marker |
| Stable ticket/message/event IDs | No contract evidence | unverified | Capture sample payloads from sandbox |
| Authentication and field-level denial | No permission contract | blocked | Validate least-privilege identity and negative tests |
| Ticket-to-opportunity association | No association contract | blocked | Define and prove one-to-one association before handoff |

No implementation task may treat a blocked row as an available endpoint or trigger.
