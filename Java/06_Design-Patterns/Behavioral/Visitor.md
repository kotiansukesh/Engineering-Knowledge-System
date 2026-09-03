---
title: "Visitor"
category: Design-Patterns
group: Behavioral
tags: [design-patterns, behavioral, visitor]
pattern: visitor
source: "https://refactoring.guru/design-patterns/visitor"
created: 2026-09-02
updated: 2026-09-02
---
# Visitor

> Category: Behavioral • Source: [Refactoring.Guru — Visitor](https://refactoring.guru/design-patterns/visitor) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Separates an algorithm from the objects it operates on.

## Problem

Exporting shapes to xml should not add export methods to every shape class.

## Solution

Keep shapes clean and put the operation in a visitor. With sealed shapes, a switch visitor does the same without double dispatch.

## Structure

```
Shape is sealed to Dot and Circle. Visitor method or switch over Shape handles each case. Compiler checks exhaustiveness.
```

## Trade-offs

Use when you add many operations over a stable element set. The sealed switch version is simpler when you own the hierarchy; keep the classic visitor when visitors need mutable accumulation or the set is open.

## Java example

```java

// Purpose: Visitor separates operation from structure; double dispatch over element hierarchy
// Participants: Shape, Dot, Circle
// Structure: sealed hierarchy + records — exhaustive, immutable composition
// Behavior: wrapping/composition at runtime; no direct new of concrete in client
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Visitor | Add operation without touching elements |
| Strategy | Swap one algorithm |
| Switch visitor | Lightweight alternative when sealed |

## Interview Q&A

**Q: Do you still need classic visitor?**

Only when visitors accumulate state or elements are open. For stable sealed hierarchies a switch visitor is shorter.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Behavioral • Tags: design-patterns • Source: refactoring.guru*
