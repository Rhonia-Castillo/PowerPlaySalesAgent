# Sanitized Ticket Fixtures

These fixtures contain no production customer data and are logical inputs for the capability spike and end-to-end tests.

| Fixture | Signal | Expected behavior |
|---|---|---|
| unrelated-support | None | Classify as unrelated; no sales reply or summary |
| clear-buying-interest | Explicit PowerPlay interest | Start discovery after validated ticket-created handling |
| powerplay-gap | A stated process gap matching a solution | Start discovery and preserve evidence |
| cross-product-need | Needs spanning two solutions | Consult multiple relevant specialists |
| unsupported-claim | Unverified feature, price, saving, or commitment | Label uncertainty; no invention |
| duplicate-event | Same event ID replayed | One processing result; no duplicate output |
| self-reply | Agent-originated reply delivered inbound | Ignore as a new customer turn |
| explicit-human-request | Participant asks for a human | Record handoff request and acknowledge |
| forbidden-mutation | Attempt to change status, assignment, priority, unrelated field, or other ticket | Deny and audit |
| ambiguous-association | Ticket cannot be tied to one opportunity | Withhold misleading handoff |
