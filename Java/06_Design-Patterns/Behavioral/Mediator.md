---
title: "Mediator"
category: Design-Patterns
group: Behavioral
tags: [design-patterns, behavioral, mediator]
pattern: mediator
source: "https://refactoring.guru/design-patterns/mediator"
created: 2026-09-02
updated: 2026-09-02
---
# Mediator

> Category: Behavioral • Source: [Refactoring.Guru — Mediator](https://refactoring.guru/design-patterns/mediator) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Lets objects communicate through a central hub instead of directly.

## Problem

Dialog buttons and checkboxes call each other. The code becomes a graph of direct references.

## Solution

Move coordination into a mediator. Components notify the mediator, the mediator decides what happens next.

## Structure

```
UiEvent is sealed to Check and Click. Mediator has a single notify switch. Components only know the mediator.
```

## Trade-offs

Use when many objects interact and direct wiring gets tangled. Centralizing logic makes it easier to follow. The mediator can grow large and needs to stay focused.

## Java example

```java

// Purpose: Mediator centralizes communication; colleagues interact via mediator, not directly
// Participants: Evt, Check, Click
// Structure: sealed hierarchy + records — exhaustive, immutable composition
// Behavior: wrapping/composition at runtime; no direct new of concrete in client
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Mediator | Peers talk via a hub |
| Observer | Broadcast to subscribers from a publisher |

## Interview Q&A

**Q: Mediator vs observer?**

Mediator centralizes many-to-many coordination. Observer broadcasts from one publisher to many subscribers.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Behavioral • Tags: design-patterns • Source: refactoring.guru*
