---
title: What is Architecture
type: concept
category: Architect/01_Architecture-Foundations
difficulty: Beginner
completed: false
reviewed:
sr-due:
tags: [architecture, foundations, decisions]
---

# What Is Software Architecture?

## Core idea

Software architecture is the set of significant structures and decisions that shape a system's qualities, boundaries, cost and ability to change.

The useful test is not "is this high level?" but:

> **Is this decision broad in consequence, expensive to reverse, or materially constraining future choices?**

## Architecture vs design vs implementation

| Level | Main question | Example |
|---|---|---|
| Architecture | What major structure or constraint shapes the system? | Data ownership, service boundary, consistency model |
| Design | How should a component implement that structure? | Repository strategy, caching algorithm |
| Implementation | How is the design expressed? | Java class, SQL query, YAML |

The boundary is contextual. A local choice can become architectural when it creates a system-wide dependency.

## Architecture is a decision system

~~~text
Business outcome
      ↓
Constraints + assumptions
      ↓
Architectural drivers
      ↓
Structures + decisions
      ↓
Quality attributes
      ↓
Evidence
      ↓
Evolution
~~~

## Common architectural drivers

- business capabilities;
- scale and growth;
- latency;
- availability and recovery;
- consistency and correctness;
- security/compliance;
- organizational ownership;
- delivery speed;
- cost;
- technology constraints;
- migration requirements.

## Significant-decision test

Ask:

1. Is it expensive to reverse?
2. Does it affect multiple components or teams?
3. Does it materially affect a quality attribute?
4. Does it constrain future choices?
5. Would changing it require migration or coordination?

## What architecture is not

- a technology shopping list;
- a microservices diagram;
- infrastructure alone;
- a document produced once;
- a prediction of every future requirement.

## Practice

Classify these decisions as architecture/design/implementation and defend each classification:

- package naming;
- module boundaries;
- database ownership;
- REST vs events;
- connection-pool size;
- deployment boundary;
- SQL index;
- multi-region strategy.

## Senior interview answer

> Software architecture is the set of significant structures and decisions that shape system qualities, boundaries, cost and evolution. It focuses attention on decisions whose consequences are broad or expensive to reverse.

## Practice tasks

- [ ] Classify ten engineering decisions
- [ ] Explain the definition in under 30 seconds
- [ ] Record one architectural decision from a real project and its consequence
