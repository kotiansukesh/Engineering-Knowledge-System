---
title: Architecture Review Checklist
category: Architect/99_Revision
tags: [architecture, checklist, design-review]
created: 2026-09-30
type: gate
---

# Architecture Review Checklist

> This is the architecture-domain review gate. It is not a second learning plan and not the AI capstone checklist.

## Scope and quality

- [ ] Functional scope and explicit exclusions are documented.
- [ ] Top quality attributes have measurable scenarios.
- [ ] Scale assumptions are recorded.
- [ ] The simplest viable architecture is identified.

## Data and integration

- [ ] Source of truth is identified for important entities.
- [ ] Consistency model is explicit.
- [ ] API/event contracts are versioned.
- [ ] Idempotency and delivery semantics are explicit.
- [ ] Migration and rollback paths exist where data changes.

## Reliability and operations

- [ ] Timeout, retry and backpressure behavior is defined.
- [ ] Degraded mode is documented.
- [ ] SLOs and key alerts are defined.
- [ ] Backup/recovery expectations are documented.
- [ ] The highest-risk failure has a test or failure experiment.

## Security and governance

- [ ] Trust boundaries are explicit.
- [ ] Authentication and authorization boundaries are explicit.
- [ ] Sensitive data handling is documented.
- [ ] Audit requirements are identified.
- [ ] Compliance requirements are scoped rather than assumed.

## Cost and change

- [ ] Major cost drivers are identified.
- [ ] At least one viable alternative is compared.
- [ ] The decision and rejected alternative are recorded.
- [ ] A redesign trigger is defined.

## Review rule

An unchecked item is either:
1. intentionally out of scope with a recorded reason, or
2. a follow-up task/ADR.

Do not mark this gate complete from memory. Link the supporting diagram, ADR, test, dashboard or runbook.

## Related

- [[Architect/README|Architecture MOC]]
- [[Architect/Decisions/README|Architecture Decisions]]
- [[Architect/10_System-Design-Interviews/README|System Design]]
- [[Evidence/README|Evidence]]
- [[AI/99_Revision/Capstone Checklist|AI Capstone Checklist]]
