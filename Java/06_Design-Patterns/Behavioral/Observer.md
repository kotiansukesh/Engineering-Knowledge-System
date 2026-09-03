---
title: "Observer"
category: Design-Patterns
group: Behavioral
tags: [design-patterns, behavioral, observer]
pattern: observer
source: "https://refactoring.guru/design-patterns/observer"
created: 2026-09-02
updated: 2026-09-02
---
# Observer *Also known as: Pub-Sub*

> Category: Behavioral • Source: [Refactoring.Guru — Observer](https://refactoring.guru/design-patterns/observer) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Defines a subscription so observers react when the publisher changes.

## Problem

A store should notify customers about new products without hard-coding who listens.

## Solution

Keep a thread-safe list of observers. Add subscribe and unsubscribe plus a notify loop. Sealed events with switch keep handling exhaustive.

## Structure

```
Publisher holds List<Observer>. ConcretePublisher calls update on each. Customer implements update.
```

## Trade-offs

Use when one change needs many reactions or subscribers come and go at runtime. CopyOnWriteArrayList handles concurrent subscribe and notify. Remember to unsubscribe or you keep objects alive longer than intended.

## Java example

```java

// Purpose: Observer notifies dependents on state change; pub-sub via subject-observer contract
// Participants: Evt, NewProd, Store
// Structure: sealed hierarchy + records — exhaustive, immutable composition
// Behavior: wrapping/composition at runtime; no direct new of concrete in client
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Observer | One publisher, many subscribers |
| Mediator | Central hub for peers |
| Flow | Back-pressured async pub-sub |

## Interview Q&A

**Q: What is the common bug?**

Forgetting to unsubscribe. Stale observers keep objects alive and duplicate work.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Behavioral • Tags: design-patterns • Source: refactoring.guru*
