---
title: "Prototype"
category: Design-Patterns
group: Creational
tags: [design-patterns, creational, prototype]
pattern: prototype
source: "https://refactoring.guru/design-patterns/prototype"
created: 2026-09-02
updated: 2026-09-02
---
# Prototype

> Category: Creational • Source: [Refactoring.Guru — Prototype](https://refactoring.guru/design-patterns/prototype) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Lets you copy existing objects without depending on their classes.

## Problem

Copying an object that may have private fields or subclasses requires knowing its concrete type.

## Solution

Declare a copy method on a prototype interface. Records give a shallow copy for free; for deep copy, implement copy that duplicates mutable parts.

## Structure

```
Prototype declares copy. Concrete prototypes return new instances with same state. Client clones instead of constructing.
```

## Trade-offs

Use when object creation is costly or you need to avoid subclassing a creator. Clone is simple for immutable records; be careful with deep copy on mutable graphs. It avoids constructors but shared mutable state can surprise you.

## Java example

```java

// Purpose: Prototype clones existing instance; avoids costly construction
// Participants: Shape, Circle, Rectangle
// Structure: sealed hierarchy + records — exhaustive, immutable composition
// Behavior: wrapping/composition at runtime; no direct new of concrete in client
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Prototype | Clone existing object |
| Factory | Create from scratch via factory method |

## Interview Q&A

**Q: When does clone beat new?**

When setup is expensive or you need a copy without knowing the exact type. Be careful with mutable fields and deep copy.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Creational • Tags: design-patterns • Source: refactoring.guru*
