---
title: "Decorator"
category: Design-Patterns
group: Structural
tags: [design-patterns, structural, decorator]
pattern: decorator
source: "https://refactoring.guru/design-patterns/decorator"
created: 2026-09-02
updated: 2026-09-02
---
# Decorator *Also known as: Wrapper*

> Category: Structural • Source: [Refactoring.Guru — Decorator](https://refactoring.guru/design-patterns/decorator) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Adds behavior by wrapping an object in another with the same interface.

## Problem

Notifier needs email, then sms, then slack, in any mix. Subclassing every combination does not scale.

## Solution

Wrap the component in a decorator that does work before or after delegating. Decorators stack.

## Structure

```
Notifier is sealed to Email and decorators. Decorator holds a Notifier and forwards send. Client nests wrappers to compose behavior.
```

## Trade-offs

Use when you need to add responsibilities at runtime without touching existing code. It is more flexible than inheritance and keeps each addition focused. Deep stacks are harder to debug and order matters.

## Java example

```java

// Purpose: Decorator adds behavior by wrapping; sealed interface + record wrapper; composes at runtime
// Participants: Notifier, Email, SMSDec
// Structure: sealed hierarchy + records — exhaustive, immutable composition
// Behavior: wrapping/composition at runtime; no direct new of concrete in client
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Decorator | Same interface, stackable |
| Proxy | Same interface, controls access |
| Adapter | Different interface |

## Interview Q&A

**Q: Decorator vs proxy?**

Both share the interface. Decorator adds behavior and stacks. Proxy controls access and usually does not stack.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Structural • Tags: design-patterns • Source: refactoring.guru*
