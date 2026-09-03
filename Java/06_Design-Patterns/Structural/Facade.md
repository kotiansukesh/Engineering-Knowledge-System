---
title: "Facade"
category: Design-Patterns
group: Structural
tags: [design-patterns, structural, facade]
pattern: facade
source: "https://refactoring.guru/design-patterns/facade"
created: 2026-09-02
updated: 2026-09-02
---
# Facade

> Category: Structural • Source: [Refactoring.Guru — Facade](https://refactoring.guru/design-patterns/facade) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Gives a simple interface to a complex subsystem.

## Problem

Video conversion touches files, codecs, buffers, and bitrates. Calling each part in order is tedious and brittle.

## Solution

Put a single class in front that wires the steps in the right order. Clients call one method.

## Structure

```
Client → Facade → subsystem (File, Codec, Converter). Facade hides the wiring.
```

## Trade-offs

Use when a subsystem is hard to use directly or to decouple clients from it. You hide complexity and make the call site readable. It can become overly large if it absorbs too many responsibilities.

## Java example

```java

// Purpose: Facade provides simplified interface over subsystem; hides complexity
// Participants: File, Codec, VideoConv
// Behavior: Factory/creation or delegation without exposing concrete construction
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Facade | Simplified front for a subsystem |
| Adapter | Translate one interface |
| Mediator | Peers coordinate through a hub |

## Interview Q&A

**Q: When would you not use a facade?**

When the subsystem is already simple or you need fine-grained control over each step.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Structural • Tags: design-patterns • Source: refactoring.guru*
