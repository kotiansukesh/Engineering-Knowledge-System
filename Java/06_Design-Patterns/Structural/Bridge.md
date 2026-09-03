---
title: "Bridge"
category: Design-Patterns
group: Structural
tags: [design-patterns, structural, bridge]
pattern: bridge
source: "https://refactoring.guru/design-patterns/bridge"
created: 2026-09-02
updated: 2026-09-02
---
# Bridge

> Category: Structural • Source: [Refactoring.Guru — Bridge](https://refactoring.guru/design-patterns/bridge) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Splits a large class into two hierarchies so they can vary independently.

## Problem

Shape with color variants explodes into RedCircle, BlueCircle, RedSquare and so on.

## Solution

Extract one dimension (color) behind an interface and have the other (shape) hold a reference to it.

## Structure

```
Abstraction (Shape) → Implementor (Color). Shape delegates fill to its Color. Adding a color or shape is independent.
```

## Trade-offs

Use when you have two dimensions that change often and combinatorial subclasses become unmanageable. It reduces subclass count and keeps each hierarchy focused. The extra indirection is the cost.

## Java example

```java

// Purpose: Bridge decouples abstraction from implementation; both vary independently
// Participants: Color, Red, Blue
// Structure: sealed hierarchy + records — exhaustive, immutable composition
// Behavior: wrapping/composition at runtime; no direct new of concrete in client
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Bridge | Two independent dimensions |
| Adapter | One interface translated to another |

## Interview Q&A

**Q: When does bridge pay off?**

When two dimensions both change and combining them would explode subclasses. Otherwise plain composition is enough.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Structural • Tags: design-patterns • Source: refactoring.guru*
