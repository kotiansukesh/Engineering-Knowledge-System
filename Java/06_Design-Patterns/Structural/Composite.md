---
title: "Composite"
category: Design-Patterns
group: Structural
tags: [design-patterns, structural, composite]
pattern: composite
source: "https://refactoring.guru/design-patterns/composite"
created: 2026-09-02
updated: 2026-09-02
---
# Composite

> Category: Structural • Source: [Refactoring.Guru — Composite](https://refactoring.guru/design-patterns/composite) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Composes objects into trees and treats single objects and groups uniformly.

## Problem

A Box can contain Products or other Boxes. Pricing or drawing should not branch on leaf vs group.

## Solution

Define a shared Component interface. Leaves implement it directly. Composites hold children and delegate, often by summing or iterating.

## Structure

```
Component is sealed to Product and Box. Box holds List<Component>. Client calls price on any Component without caring which it is.
```

## Trade-offs

Use when you have part-whole hierarchies and want uniform handling. It simplifies client code. If the tree rules are strict the shared interface can feel permissive.

## Java example

```java

// Purpose: Composite treats individual and group uniformly; tree structure with recursive composition
// Participants: Component, Product, Box
// Structure: sealed hierarchy + records — exhaustive, immutable composition
// Behavior: wrapping/composition at runtime; no direct new of concrete in client
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Composite | Tree, uniform treatment |
| Decorator | Wrap to add behavior, not contain many |

## Interview Q&A

**Q: What makes composite tricky?**

The shared interface hides whether you have a leaf or a group, so invalid combinations are possible if you do not validate.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Structural • Tags: design-patterns • Source: refactoring.guru*
