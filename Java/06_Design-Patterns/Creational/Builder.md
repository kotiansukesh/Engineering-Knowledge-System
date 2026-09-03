---
title: "Builder"
category: Design-Patterns
group: Creational
tags: [design-patterns, creational, builder]
pattern: builder
source: "https://refactoring.guru/design-patterns/builder"
created: 2026-09-02
updated: 2026-09-02
---
# Builder

> Category: Creational • Source: [Refactoring.Guru — Builder](https://refactoring.guru/design-patterns/builder) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Constructs complex objects step by step with the same code producing different variants.

## Problem

A House with many optional parts leads to telescoping constructors that are hard to read and error prone.

## Solution

Move construction into a mutable builder with fluent methods. A director can encode preset recipes, but the client can also chain directly.

## Structure

```
Client → Builder → House. Director optionally orchestrates the builder. Product is an immutable record.
```

## Trade-offs

Use when a type has many optional parts or when you need different representations from the same steps. It makes construction readable and keeps the product immutable. For only one or two options the extra builder class is not worth it.

## Java example

```java

// Purpose: Builder constructs complex object step-by-step; fluent API; immutable result
// Participants: House, HouseBuilder
// Behavior: Factory/creation or delegation without exposing concrete construction
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Builder | Stepwise, many options |
| Factory | One-shot creation |

## Interview Q&A

**Q: When can you skip the builder?**

When you have one or two optional fields. A record constructor or copy method is clearer than a full builder.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Creational • Tags: design-patterns • Source: refactoring.guru*
