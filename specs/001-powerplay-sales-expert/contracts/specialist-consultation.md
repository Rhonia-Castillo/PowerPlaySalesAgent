# Contract: Specialist Consultation

## Parent request

```text
conversationId: stable parent conversation identifier
ticketId: current authorized ticket identifier
customerNeeds: stated needs, process, goals, constraints, and Microsoft environment
question: the product or objection to evaluate
candidateSolutions: one or more in-scope solution names
knowledgePolicy: approved sources only; mark planned/custom/unverified status
```

The parent passes the minimum context needed for fit evaluation and does not pass other
customers' information or unrelated ticket data.

## Specialist response

```text
solution: one assigned solution
fit: fit | partial-fit | no-fit | insufficient-information
needAddressed: the stated customer need
verifiedCapabilities: approved capability statements with source/version
valueExplanation: connection to stated business or IT outcome
prerequisites: known prerequisites or integrations
limitations: known limitations and gaps
productStatus: available | planned | custom-candidate | unverified
questionsForCustomer: focused missing facts
requiresHumanConfirmation: true | false
confidence: high | medium | low
knowledgeSource: owner, version, effective date, review date
correlationId: specialist response identifier
```

A specialist MUST refuse or mark unsupported claims rather than infer them. The parent
may consult multiple specialists and must reconcile conflicting findings before replying.
