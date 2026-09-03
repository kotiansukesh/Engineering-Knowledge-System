---
title: "Template Method"
category: Design-Patterns
group: Behavioral
tags: [design-patterns, behavioral, template-method]
pattern: template-method
source: "https://refactoring.guru/design-patterns/template-method"
created: 2026-09-02
updated: 2026-09-02
---
# Template Method

> Category: Behavioral • Source: [Refactoring.Guru — Template Method](https://refactoring.guru/design-patterns/template-method) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Defines the skeleton of an algorithm and lets subclasses fill in details.

## Problem

Games run the same turn steps (collect, build, fight) with different behavior per race.

## Solution

Write a final template method that calls abstract steps. Subclasses override the steps, not the skeleton.

## Structure

```
GameAI.turn is final and calls collect and attack. OrcAI and others override only the steps.
```

## Trade-offs

Use when you have a fixed sequence with varying parts. It keeps the order in one place and avoids duplication. In Java, a single abstract class is enough; you do not need a deep hierarchy.

## Java example

```java

// Purpose: Template Method defines skeleton in base; subclasses override steps without changing structure
// Participants: GameAI, OrcAI
// Behavior: Factory/creation or delegation without exposing concrete construction
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Template method | Fixed skeleton, subclass steps |
| Strategy | Whole algorithm swapped |
| Factory method | Creation step is the variable part |

## Interview Q&A

**Q: When do you pick composition over template method?**

When steps vary a lot or you want to swap without inheritance. Template method ties you to a class hierarchy.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Behavioral • Tags: design-patterns • Source: refactoring.guru*
