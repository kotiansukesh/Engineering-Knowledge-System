---
title: Architecture Evolution and Technical Debt
type: concept
category: Architect/01_Architecture-Foundations
difficulty: Advanced
completed: false
reviewed:
sr-due:
tags: [architecture, foundations, evolution, technical-debt]
---

# Architecture Evolution and Technical Debt

## Purpose

Architecture is a living decision set. Good architects know when to preserve, adapt, migrate or retire a decision.

## Evolution loop

~~~text
Current architecture
      ↓
Observed requirement / failure / bottleneck
      ↓
Evidence
      ↓
Smallest viable change
      ↓
Migration
      ↓
Validation
      ↓
New architecture
~~~

## Technical debt

Technical debt is not simply old code.

A useful debt record contains:

- deferred decision;
- reason for deferral;
- interest/cost created;
- repayment trigger;
- owner;
- consequence if ignored.

## Signals for architectural change

- repeated incidents from the same structural cause;
- measured capacity ceiling;
- unacceptable deployment coupling;
- rising change lead time;
- security/compliance requirement;
- operational cost growing faster than value;
- business strategy changing.

## Avoid premature evolution

Do not redesign because:

- a newer technology exists;
- another company uses it;
- a diagram looks old;
- the architecture is unfashionable.

Require evidence of a constraint or risk.

## Migration questions

- Can old and new paths coexist?
- How is data reconciled?
- How is rollback handled?
- What is migration blast radius?
- What proves success?
- When can the old path be removed?

## Practice tasks

- [ ] Define a redesign trigger for one architecture decision
- [ ] Write one technical-debt record
- [ ] Design a strangler migration for one boundary
- [ ] Define migration success evidence
