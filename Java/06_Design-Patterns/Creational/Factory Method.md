---
title: "Factory Method"
category: Design-Patterns
group: Creational
tags: [design-patterns, creational, factory-method]
pattern: factory-method
source: "https://refactoring.guru/design-patterns/factory-method"
created: 2026-09-02
updated: 2026-09-02
---
# Factory Method

> Category: Creational • Source: [Refactoring.Guru — Factory Method](https://refactoring.guru/design-patterns/factory-method) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Defines a method for creating objects and lets subclasses decide what to create.

## Problem

You need to create transports without hard-coding Truck vs Ship in client code.

## Solution

Declare a creator with a factory method. Subclasses or a switch override it to return the right product. Sealed product plus switch keeps it exhaustive.

## Structure

```
Creator → factoryMethod() → Product. Concrete creators return Truck or Ship. Client uses only the interface.
```

## Trade-offs

Use when you do not know the exact product type up front or want to keep creation open for extension. It isolates creation from use and removes conditionals from the client, but adds another type per product.

## Java example

```java

// Purpose: Factory Method defers instantiation to subclasses; client depends on abstraction, not concrete new
// Participants: Transport, Truck, Ship
// Structure: sealed hierarchy + records — exhaustive, immutable composition
// Behavior: wrapping/composition at runtime; no direct new of concrete in client
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Factory method | Subclass decides which product to make |
| Abstract factory | Family of related products |

## Interview Q&A

**Q: How is this different from a simple factory function?**

Factory method lets a subclass or registered switch decide the concrete type without the client changing. Simple factory is a single function with a conditional.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Creational • Tags: design-patterns • Source: refactoring.guru*
