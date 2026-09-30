---
title: Architecture Principles
type: note
category: Architect/01_Architecture-Foundations
difficulty: Intermediate
completed: false
reviewed:
sr-due:
tags: [architecture, foundations, principles, governance]
---

# Architecture Principles

## Purpose

A principle is a durable decision rule that narrows choices without pretending every context is identical.

## Anatomy

**Statement → Rationale → Implications → Exceptions → Evidence → Owner**

Example:

> **Prefer explicit ownership over shared mutable state.**

Rationale: shared state increases coordination and change coupling.

Implication: define a clear owner and expose behavior through contracts.

Exception: shared state can be justified when atomic cross-boundary behavior is a hard requirement.

Evidence: dependency/change metrics and incident history.

## Good vs bad principles

| Good | Bad |
|---|---|
| Prefer simplest architecture satisfying measured requirements | Always use microservices |
| Make failure boundaries explicit | Use Kubernetes everywhere |
| Automate architectural invariants | Everything must be scalable |
| Record expensive-to-reverse decisions | Cloud-native is better |

## Useful baseline principles

1. Own data where the business capability owns the behavior.
2. Prefer the simplest architecture that satisfies measured requirements.
3. Make failure boundaries explicit.
4. Automate architectural invariants where practical.
5. Treat security and operability as design properties.
6. Record expensive-to-reverse decisions and their assumptions.

## Principle vs ADR

| Principle | ADR |
|---|---|
| General rule | Specific decision |
| Durable | Context-specific |
| Guides many decisions | Records one decision |
| May become a governance rule | Records consequences and alternatives |

## Practice

Create three principles for a fintech platform. For each, state:

- rationale;
- implication;
- exception;
- evidence;
- owner.

## Practice tasks

- [ ] Write three principles
- [ ] Give one exception for each
- [ ] Define evidence for one principle
- [ ] Convert one repeated team debate into a principle
