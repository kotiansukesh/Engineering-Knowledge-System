---
title: Functional vs Constraints
category: architect
tags: [requirements, constraints]
created: 2026-09-03
completed: false
---

# Functional vs Constraints

## Intent
Separate what the system does (functions) from what limits how (constraints) so estimates and style choices rest on facts.

## When / NOT
- Use during elicitation, before picking styles.
- NOT to bury qualities inside "non-functional" vagueness — promote them to scenarios.

## Example
```text
Why split: "Checkout with UPI" (functional) vs "PCI-DSS, deploy on EKS,
Java 21 only" (constraints) — second kills half the options instantly
```

## Pros / Cons
- Pros: clears hidden assumptions; speeds ADR.
- Cons: constraint creep (every preference becomes "mandatory").

## Vs
| Type | Example | Source |
|------|---------|--------|
| Functional | Place order, refund | Product/users |
| Quality | p99 < 300ms | SLO/SLA |
| Constraint | EKS-only, no new DB | Org/policy |

## Q&A
1. **"Non-functional" term?** Avoid — say quality attribute + scenario.
2. **Constraint or quality?** Fixed = constraint; measurable target = quality.
3. **Where record?** Requirements log → link each to scenario/ADR.

## Pitfalls
- Treating preferences as constraints.
- Functions without qualities (untestable "fast").

## Related
- [[ISO-25010-Qualities|ISO 25010]], [[Quality-Scenarios|Quality Scenarios]]
