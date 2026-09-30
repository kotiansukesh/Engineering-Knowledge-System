---
title: Stakeholders and Concerns
type: concept
category: Architect/01_Architecture-Foundations
difficulty: Beginner
completed: false
reviewed:
sr-due:
tags: [architecture, foundations, stakeholders, requirements]
---

# Stakeholders and Concerns

## Purpose

Architecture exists to satisfy stakeholders under constraints. A stakeholder is anyone who affects, is affected by, or is accountable for the system.

## Typical stakeholders

Product/business, users, engineering, SRE/operations, security, compliance/legal, data teams, finance, support, partners and executives.

## Concern → driver chain

~~~text
Stakeholder
    ↓
Concern
    ↓
Architectural driver
    ↓
Quality attribute
    ↓
Scenario / threshold
    ↓
Decision
    ↓
Evidence
~~~

Example:

**SRE → recovery → low recovery time → resilience → restore service within 15 minutes → multi-zone deployment + recovery drill.**

## Matrix

| Stakeholder | Concern | Risk if ignored | Quality / driver | Evidence |
|---|---|---|---|---|
| Product | conversion | lost revenue | latency | p95/p99 |
| SRE | recovery | prolonged outage | availability | MTTR/RTO |
| Security | exposure | breach | confidentiality | control tests |
| Finance | unit cost | margin pressure | cost | cost/request |
| Support | diagnosability | slow resolution | operability | MTTR |

## Conflicting concerns

Resolve conflicts using:

1. hard constraints;
2. business impact;
3. measurable scenarios;
4. reversibility;
5. explicit trade-off;
6. accountable decision owner.

Do not resolve architecture by stakeholder volume.

## Practice

For checkout:

- identify five stakeholders;
- record their top concern;
- identify one conflict;
- write a measurable scenario;
- identify the architecture decision affected.

## Practice tasks

- [ ] Build a stakeholder matrix
- [ ] Convert three concerns into scenarios
- [ ] Record one conflict and the sacrificed concern
