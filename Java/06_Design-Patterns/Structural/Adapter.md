---
title: "Adapter"
category: Design-Patterns
group: Structural
tags: [design-patterns, structural, adapter]
pattern: adapter
source: "https://refactoring.guru/design-patterns/adapter"
created: 2026-09-02
updated: 2026-09-02
---
# Adapter *Also known as: Wrapper*

> Category: Structural • Source: [Refactoring.Guru — Adapter](https://refactoring.guru/design-patterns/adapter) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Lets objects with incompatible interfaces work together.

## Problem

RoundHole expects RoundPeg but you have SquarePeg with a different interface.

## Solution

Wrap the adaptee in an adapter that implements the target interface and translates the call.

## Structure

```
Client → Target (RoundPeg). Adapter implements Target and holds SquarePeg. RoundHole uses Target without knowing the adaptee.
```

## Trade-offs

Use when you must reuse an existing class whose interface does not match. Prefer composition-based adapter. It adds a layer but avoids changing working code. This is translation, not redesign.

## Java example

```java

// Purpose: Adapter bridges incompatible interfaces; wraps adaptee to match target
// Participants: SquarePeg, RoundPeg, SquareAdapter
// Behavior: Factory/creation or delegation without exposing concrete construction
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Adapter | Translate existing interface after the fact |
| Bridge | Split abstraction and implementation by design |

## Interview Q&A

**Q: Adapter vs decorator?**

Adapter changes the interface. Decorator keeps the same interface and stacks behavior.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Structural • Tags: design-patterns • Source: refactoring.guru*
