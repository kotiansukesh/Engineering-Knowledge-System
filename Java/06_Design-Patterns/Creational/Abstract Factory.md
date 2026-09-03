---
title: "Abstract Factory"
category: Design-Patterns
group: Creational
tags: [design-patterns, creational, abstract-factory]
pattern: abstract-factory
source: "https://refactoring.guru/design-patterns/abstract-factory"
created: 2026-09-02
updated: 2026-09-02
---
# Abstract Factory

> Category: Creational • Source: [Refactoring.Guru — Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Produces families of related objects without naming concrete classes.

## Problem

Building matching furniture sets (modern vs victorian chair + sofa) should not mix styles.

## Solution

Define a factory interface with a method per product in the family. Each concrete factory creates a consistent set.

## Structure

```
Client → FurnitureFactory → Chair + Sofa. ModernFactory makes ModernChair and ModernSofa, VictorianFactory makes the other pair.
```

## Trade-offs

Use when you work with families and need compatibility within a family. You get consistency and the client never touches concrete names. Adding a new family is easy; adding a new product kind touches every factory.

## Java example

```java

// Purpose: Abstract Factory creates families of related objects without specifying concrete classes
// Participants: Chair, ModernChair, VictChair
// Structure: sealed hierarchy + records — exhaustive, immutable composition
// Behavior: wrapping/composition at runtime; no direct new of concrete in client
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Abstract factory | Family of products |
| Factory method | Single product |
| Builder | Step-by-step assembly |

## Interview Q&A

**Q: When do you need abstract factory at all?**

When you must create matching families. If you only make one product, factory method is enough.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Creational • Tags: design-patterns • Source: refactoring.guru*
