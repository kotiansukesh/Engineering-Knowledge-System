---
title: What is Architecture
category: architect
tags: [architecture, foundations]
created: 2026-09-03
completed: false
---

# What is Architecture

## Intent
Define software architecture as the set of significant decisions + structures that shape qualities, cost, and change.

## When / NOT
- Use when justifying structure to stakeholders or reviewing a design.
- NOT for low-level class design — that's detailed design, not architecture.

## Example (Java/Spring — why, not line-by-line)
```java
// Why modular packages: enforce Order→Payment dependency direction
// ArchUnit test fails on cycles → architecture as executable rule, not diagram
package com.shop.order; // depends on payment API, never impl
```

```text
C4 Context: Shop monolith → Postgres, Stripe, warehouse API
Why C4-L1 first: aligns non-technical stakeholders before containers
```

## Pros / Cons
- Pros: shared vocabulary; defers costly rework.
- Cons: over-documentation; ivory-tower diagrams nobody reads.

## Vs
| A | B | Rule |
|---|---|------|
| Architecture | Design | Architecture = hard-to-reverse decisions |
| Architecture | Infrastructure | Infra is hosting; arch spans structure + behavior |

## Q&A
1. **One-line definition for interviews?** "Structures + significant decisions that enable qualities and constrain change."
2. **How much upfront?** Risk-driven: model the 3 riskiest decisions, slice the rest.
3. **Monolith still architecture?** Yes — modularity and boundaries matter more than service count.

## Pitfalls
- Equating architecture with microservices/K8s.
- Diagrams without decisions (no ADR = no traceability).

## Related
- [[Architect-Roles|Architect Roles]], [[Views-and-Viewpoints-4-plus-1|Views 4+1]], [[Architecture-Principles|Principles]]
