---
title: Stakeholders and Concerns
category: architect
tags: [architecture, stakeholders]
created: 2026-09-03
completed: false
---

# Stakeholders and Concerns

## Intent
Map who cares about what so views and priorities target real concerns, not generic diagrams.

## When / NOT
- Use at phase start and before any review.
- NOT a one-time list — revisit when scope or compliance shifts.

## Example
```text
Why matrix: Product cares time-to-market, SRE cares MTTR, Security cares PCI,
Finance cares cost — same system, conflicting pulls → drives tradeoff ADRs
```

## Pros / Cons
- Pros: right view per audience; fewer re-reviews.
- Cons: analysis paralysis if you chase every stakeholder.

## Vs
| Stakeholder | Top concern | View that satisfies |
|-------------|-------------|---------------------|
| Product | Features/speed | Roadmap + runtime view |
| SRE/Ops | Availability/MTTR | Deployment + observability |
| Security | Confidentiality/compliance | Threat model + data flow |

## Q&A
1. **Minimum viable list?** User, dev, ops, security, sponsor — plus regulator if PII/payment.
2. **Hidden stakeholders?** Support, finance (cost), auditors — ask "who pays / who gets paged."
3. **How to record?** Table: stakeholder → concern → quality → scenario link.

## Pitfalls
- Only technical stakeholders; missing business/compliance.
- One diagram for everyone.

## Related
- [[Views-and-Viewpoints-4-plus-1|Views 4+1]], [[../02_Requirements-Quality-Attributes/Quality-Scenarios|Quality Scenarios]]
