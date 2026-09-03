---
title: "Memento"
category: Design-Patterns
group: Behavioral
tags: [design-patterns, behavioral, memento]
pattern: memento
source: "https://refactoring.guru/design-patterns/memento"
created: 2026-09-02
updated: 2026-09-02
---
# Memento *Also known as: Snapshot*

> Category: Behavioral • Source: [Refactoring.Guru — Memento](https://refactoring.guru/design-patterns/memento) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Captures and restores an object's state without exposing its internals.

## Problem

Editor needs undo but exposing all fields breaks encapsulation.

## Solution

Let the originator create an opaque snapshot record and restore from it. A caretaker holds snapshots.

## Structure

```
Editor creates Snap records and restores from them. Caretaker keeps the stack but cannot read the snapshot internals.
```

## Trade-offs

Use for undo where you must not leak internal state. Records give a compact immutable memento. Storing many large mementos costs memory, so cap history or keep deltas.

## Java example

```java

// Purpose: Memento captures and restores internal state without violating encapsulation
// Participants: Editor, Snap
// Behavior: Factory/creation or delegation without exposing concrete construction
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Memento | Save and restore state, keep encapsulation |
| Command undo | Request object stores reverse action |

## Interview Q&A

**Q: How long do you keep mementos?**

Only as long as undo is needed. Large or many snapshots cost memory, so bound history.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Behavioral • Tags: design-patterns • Source: refactoring.guru*
