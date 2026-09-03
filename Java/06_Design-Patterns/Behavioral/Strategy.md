---
title: "Strategy"
category: Design-Patterns
group: Behavioral
tags: [design-patterns, behavioral, strategy]
pattern: strategy
source: "https://refactoring.guru/design-patterns/strategy"
created: 2026-09-02
updated: 2026-09-02
---
# Strategy *Also known as: Policy*

> Category: Behavioral • Source: [Refactoring.Guru — Strategy](https://refactoring.guru/design-patterns/strategy) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Defines a family of algorithms, puts each in its own class, and makes them interchangeable.

## Problem

Navigator picks road vs walking vs transit. Adding an algorithm should not edit the navigator.

## Solution

Put each algorithm behind a sealed interface. Context holds the chosen strategy and delegates. Switching strategy changes the result.

## Structure

```
Context holds Strategy. Concrete strategies are records. Navigator switches strategy at runtime.
```

## Trade-offs

Use when you swap algorithms at runtime or want to isolate variant logic. It keeps the context closed for change. The client must still choose a strategy, so defaults help.

## Java example

```java

// Purpose: Strategy encapsulates interchangeable algorithms; context delegates to strategy
// Participants: Pt, RouteS, Road
// Structure: sealed hierarchy + records — exhaustive, immutable composition
// Behavior: wrapping/composition at runtime; no direct new of concrete in client
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Strategy | Swap algorithms on one object |
| Command | Encapsulate a request to queue or undo |
| State | Internal state drives behavior |

## Interview Q&A

**Q: Strategy vs state pattern?**

Strategy is chosen externally and swapped at will. State changes itself based on internal transitions.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Behavioral • Tags: design-patterns • Source: refactoring.guru*
