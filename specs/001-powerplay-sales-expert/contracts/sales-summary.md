# Contract: Sales Summary and Customer Reply

## Customer-facing reply

The reply is written in the current Tokity ticket and contains only customer-appropriate
content: acknowledgement of known context, focused discovery questions, verified value,
recommendations and reasons, explicit product-status caveats, objections answered, and
an appropriate next step. Internal sales notes, confidence metadata, routing details,
and confidential information are excluded.

## Internal sales summary

The internal update is clearly labeled and contains:

- Customer organization and contact details when authorized and appropriate.
- Stated needs, current process, desired outcomes, and buying signals.
- Recommended solutions and the distinct reason for each.
- Questions answered, objections, limitations, gaps, and open qualification questions.
- Claims or commitments requiring human confirmation.
- Suggested next action and explicit human-request handoff state.
- Ticket ID, summary version, generated-at time, and source conversation correlation.

The summary is upserted for the current ticket only. It is not appended as a duplicate on
retry. Public reply and internal summary writes are separate operations with independent
visibility checks and audit records.
