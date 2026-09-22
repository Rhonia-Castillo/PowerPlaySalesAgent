# Access Matrix

| Resource or operation | Allowed | Boundary |
|---|---|---|
| Current ticket subject | Read | Authorized current ticket only |
| Current ticket description | Read | Authorized current ticket only |
| Current requester and organization | Read | Authorized current ticket only |
| Current ticket tags and status | Read | Context only; no status mutation |
| Current conversation history | Read | Authorized current ticket only |
| Other tickets | Deny | Separate authorization required |
| Customer-facing reply | Write | Current ticket only; public-safe content |
| Clearly identified internal sales summary | Create/update | Current ticket only; internal visibility required |
| Ticket status | Deny write | Must not change |
| Assignment | Deny write | Must not change |
| Priority | Deny write | Must not change |
| Unrelated fields | Deny write | Must not change |

Every denied operation must produce an audit record without exposing unnecessary customer content.
