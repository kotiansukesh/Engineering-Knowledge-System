---
title: "State"
category: Design-Patterns
group: Behavioral
tags: [design-patterns, behavioral, state]
pattern: state
source: "https://refactoring.guru/design-patterns/state"
created: 2026-09-02
updated: 2026-09-02
---
# State

> Category: Behavioral • Source: [Refactoring.Guru — State](https://refactoring.guru/design-patterns/state) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Lets an object change behavior when its internal state changes.

## Problem

A document behaves differently as draft vs published vs archived, with conditionals everywhere.

## Solution

Extract each state into its own type with the same interface. The context holds the current state and delegates. Switching state changes behavior.

## Structure

```
Document holds State. Draft and Published implement State. Client calls publish and delegation does the rest.
```

## Trade-offs

Use when behavior branches on state and states have distinct rules. It removes conditionals and groups state logic together. Creating a type per state is overkill when differences are minor.

## Java example

```java

// Purpose: State lets object alter behavior when internal state changes; state-specific implementations
// Participants: State, Draft, Published
// Structure: sealed hierarchy + records — exhaustive, immutable composition
// Behavior: wrapping/composition at runtime; no direct new of concrete in client
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| State | Object changes behavior with state, delegates |
| Strategy | Algorithm chosen externally |
| Template method | Steps fixed, details vary |

## Interview Q&A

**Q: State vs strategy choice?**

State switches internally when the object's own state changes. Strategy is picked by the caller.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Behavioral • Tags: design-patterns • Source: refactoring.guru*
