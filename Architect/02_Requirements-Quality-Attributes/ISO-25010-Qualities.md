---
title: ISO 25010 Qualities
category: architect
tags: [quality, iso-25010]
created: 2026-09-03
completed: false
---

# ISO 25010 Qualities

## Intent
Use the standard quality vocabulary (performance, reliability, security, maintainability…) to stop "scalable/secure" hand-waving.

## When / NOT
- Use to name and prioritize qualities with stakeholders.
- NOT to implement all eight — pick top 3 drivers.

## Example
```text
Why map: "Black Friday 10x" → Performance (throughput) + Reliability (fault tolerance);
"PCI audit" → Security (confidentiality) — naming picks the tactic
```

## Pros / Cons
- Pros: shared checklist; iSAQB-expected language.
- Cons: abstract without scenarios; checkbox compliance.

## Vs
| Quality | Tactic family | Spring example |
|---------|---------------|----------------|
| Performance | Cache/async/scale-out | Redis + virtual threads |
| Reliability | Retry/idempotency | Kafka + outbox |
| Security | AuthN/Z, encrypt | OAuth2/OIDC, KMS |

## Q&A
1. **Must memorize all sub-characteristics?** No — know the 8 + 1 example each.
2. **Top 3 for capstone?** Performance, reliability, security (+ maintainability).
3. **How to prioritize?** Stakeholder impact × risk; timebox the rest.

## Pitfalls
- Listing qualities without owners or measures.
- Optimizing all qualities at once.

## Related
- [[Quality-Scenarios|Quality Scenarios]], [[Tradeoffs-Tensions|Tradeoffs]]
