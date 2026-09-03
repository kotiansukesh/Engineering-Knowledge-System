---
title: Tradeoffs and Tensions
category: architect
tags: [quality, tradeoffs]
created: 2026-09-03
completed: false
---

# Tradeoffs and Tensions

## Intent
Name what you sacrifice (CAP, consistency vs availability, speed vs safety) so decisions are explicit and reversible.

## When / NOT
- Use in every ADR's "Considered options / Consequences" section.
- NOT to avoid deciding — timebox and record the bet.

## Example (Java/Kafka — why, not line-by-line)
```java
// Why async saga over 2PC: availability + throughput beat immediate consistency
// Cost: eventual consistency → compensate + idempotent consumers
// outbox → Kafka → payment consumer (at-least-once + dedupe key)
```

## Pros / Cons
- Pros: honest scope; fewer revisits.
- Cons: tradeoff theater (listing without quantification).

## Vs
| Tension | Pick A when | Pick B when |
|---------|-------------|-------------|
| Consistency vs availability | Payments ledger | Flash-sale cart |
| Cache vs freshness | Catalog reads | Inventory counts |
| Speed vs safety | Prototype | PCI path |

## Q&A
1. **How to quantify?** Scenario measures + cost/latency notes in ADR.
2. **Who breaks ties?** Stakeholder with the top concern (see [[../01_Architecture-Foundations/Stakeholders-Concerns|Stakeholders]]).
3. **Revisit when?** Assumption change or SLO breach — link ADR supersede chain.

## Pitfalls
- Silent tradeoffs discovered in prod.
- Optimizing the easy quality, ignoring the driver.

## Related
- [[Quality-Scenarios|Quality Scenarios]], [[ISO-25010-Qualities|ISO 25010]]
