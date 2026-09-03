---
title: "Singleton"
category: Design-Patterns
group: Creational
tags: [design-patterns, creational, singleton]
pattern: singleton
source: "https://refactoring.guru/design-patterns/singleton"
created: 2026-09-02
updated: 2026-09-02
---
# Singleton

> Category: Creational • Source: [Refactoring.Guru — Singleton](https://refactoring.guru/design-patterns/singleton) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Ensures a class has one instance and gives global access to it.

## Problem

Logger, config, or pool should not have multiple instances. A global variable does not prevent extra creation.

## Solution

Make the constructor private, keep a single static holder, and expose a static accessor. Enum or holder pattern handles thread safety without manual locking.

## Structure

```
Client → Singleton.getInstance() → single instance. Enum variant is one line and handles serialization.
```

## Trade-offs

Use when exactly one coordinator is needed across the app. Enum is the simplest choice. Holder is good when you need lazy init on a class that cannot be an enum. Prefer injecting a single instance instead of a global getInstance when testability matters. Costs: hides dependencies, harder to test, can be abused as global state.

## Java example

```java

// Purpose: Singleton ensures single instance; enum or holder idiom; global access point
// Participants: AppConfig, Database, H
// Behavior: Factory/creation or delegation without exposing concrete construction
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Singleton | One instance, global access |
| Dependency injection | One instance injected, easier to test |

## Interview Q&A

**Q: Is singleton just a global?**

No. It prevents extra instances, but a plain global does not. Prefer injection for testability and use enum for the simplest correct singleton.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Creational • Tags: design-patterns • Source: refactoring.guru*
