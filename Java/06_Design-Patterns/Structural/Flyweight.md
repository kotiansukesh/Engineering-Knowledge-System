---
title: "Flyweight"
category: Design-Patterns
group: Structural
tags: [design-patterns, structural, flyweight]
pattern: flyweight
source: "https://refactoring.guru/design-patterns/flyweight"
created: 2026-09-02
updated: 2026-09-02
---
# Flyweight

> Category: Structural • Source: [Refactoring.Guru — Flyweight](https://refactoring.guru/design-patterns/flyweight) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Shares common state among many objects instead of keeping it in each object.

## Problem

A forest with thousands of trees repeats the same type data in every tree and wastes memory.

## Solution

Split intrinsic shared state (type) from extrinsic varying state (position). Store intrinsic once in a factory and pass extrinsic at draw time.

## Structure

```
Factory holds canonical TreeType records. Tree holds position plus a reference to a shared TreeType. Clients get types from the factory.
```

## Trade-offs

Use when you have many similar objects and memory matters. Records and ConcurrentHashMap make the cache concise. Only do this when you have measured duplication; otherwise the factory adds indirection for little gain.

## Java example

```java

// Purpose: Flyweight shares intrinsic state; factory pools instances to reduce memory
// Participants: TreeType, TreeFactory, Tree
// Behavior: Factory/creation or delegation without exposing concrete construction
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Flyweight | Share intrinsic state, many objects |
| Singleton | One object |
| Prototype | Clone instead of sharing |

## Interview Q&A

**Q: What can go wrong?**

Mixing intrinsic and extrinsic state makes bugs. Keep shared state immutable and pass the rest in.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Structural • Tags: design-patterns • Source: refactoring.guru*
