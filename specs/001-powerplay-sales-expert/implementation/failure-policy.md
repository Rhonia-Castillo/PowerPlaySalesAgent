# Failure Policy

- **Unauthorized read/write**: deny, audit, and produce no partial write.
- **Unrelated new ticket**: classify and stop without a public reply or summary.
- **Unknown Tokity capability**: mark blocked and use no unverified operation.
- **Timeout or transient connector failure**: retry with the same idempotency key and correlation ID.
- **Duplicate event**: return the stored result without repeating output.
- **Public reply succeeds but summary fails**: record the partial outcome, retry the summary only, and never duplicate the public reply.
- **Summary succeeds but public reply fails**: record the partial outcome and retry the public reply only when the contract permits; preserve the summary state.
- **Retry exhaustion**: mark failed, alert the owner, and leave the ticket unchanged beyond any already-audited permitted operation.

No fallback may change status, assignment, priority, unrelated fields, or another ticket.
