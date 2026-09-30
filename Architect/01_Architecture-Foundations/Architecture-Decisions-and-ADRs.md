---
title: Architecture Decisions and ADRs
type: concept
category: Architect/01_Architecture-Foundations
difficulty: Intermediate
completed: false
reviewed:
sr-due:
tags: [architecture, foundations, ADR, decisions]
---

# Architecture Decisions and ADRs

## Purpose

An ADR records **why** a significant decision was made, what alternatives were considered, and what evidence could cause it to change.

## Lifecycle

**Proposed → Accepted → Superseded / Rejected**

## Structure

1. Context
2. Problem
3. Drivers and constraints
4. Decision
5. Alternatives
6. Consequences
7. Validation evidence
8. Review trigger

## Strong decision statement

> Use asynchronous processing for report generation because completion is not user-blocking, workload is bursty, and the latency budget permits eventual completion.

This is stronger than:

> Use Kafka.

## Consequences

Record both benefits and costs:

- operational burden;
- failure modes;
- latency;
- consistency;
- cost;
- migration implications;
- new constraints.

## Reversibility

| Reversibility | Approach |
|---|---|
| Easy | experiment and learn |
| Moderate | document and validate |
| Expensive | prototype, quantify and define migration trigger |

## Anti-patterns

- implementation trivia;
- no alternatives;
- no owner;
- no negative consequence;
- no review trigger;
- recording decisions long after their assumptions are forgotten.

## Practice

Create an ADR for:

**"Should order confirmation be synchronous or asynchronous?"**

Include user experience, consistency, failure behavior, operational cost and review trigger.

## Practice tasks

- [ ] Write one ADR
- [ ] Include two alternatives
- [ ] Record one negative consequence
- [ ] Define one measurable review trigger
