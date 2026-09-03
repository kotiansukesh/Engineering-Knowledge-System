---
title: Architect Roles
category: architect
tags: [architecture, roles]
created: 2026-09-03
completed: false
---

# Architect Roles

## Intent
Distinguish solution / domain / enterprise / platform architect so you operate at the right scope.

## When / NOT
- Use when scoping ownership (who decides what) on a program.
- NOT as a hierarchy excuse — small teams wear multiple hats.

## Example (Spring shop — why, not line-by-line)
```text
Why RACI: Order checkout spans solution (flow), domain (pricing rules),
platform (Kafka/EKS), enterprise (PCI scope) — one owner per decision
```

## Pros / Cons
- Pros: clear escalation; avoids every decision landing on one person.
- Cons: title inflation; silos if roles don't code-review.

## Vs
| Role | Owns | Doesn't own |
|------|------|-------------|
| Solution | End-to-end for one system | Org-wide standards |
| Domain | Bounded context model | Deployment platform |
| Platform | Paved road (CI/K8s/Kafka) | Business rules |
| Enterprise | Portfolio constraints | Sprint-level design |

## Q&A
1. **Backend dev → which first?** Solution/domain — closest to code you know.
2. **Do architects code?** Enough to validate: spikes, ADRs, fitness tests, reviews.
3. **How to show it?** Capstone with C4 + ADRs signed per role.

## Pitfalls
- Becoming a PowerPoint architect; keep a spike per phase.
- Owning implementation details instead of constraints.

## Related
- [[What-is-Architecture|What is Architecture]], [[Stakeholders-Concerns|Stakeholders]]
