---
title: "Dependency Injection Pattern"
category: Design-Patterns
tags: [design-patterns, di, extra]
created: 2026-01-18
updated: 2026-09-02
---
# Dependency Injection Pattern

> Category: Extra • Source: [Refactoring.Guru — Dependency Injection Pattern](https://refactoring.guru/design-patterns/dependency-injection-pattern) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Gives a class what it needs instead of letting it create dependencies itself.

## Problem

A notifier that news up EmailSender directly cannot be tested or switched to sms without editing.

## Solution

Pass dependencies through the constructor or framework. Code against an interface and inject the concrete sender at composition time.

## Structure

```
Notifier holds Sender. EmailSender and FakeSender implement it. Client builds Notifier with the sender it wants.
```

## Trade-offs

Use to make code testable and wiring explicit. It removes hard creation from business code. Over-injecting many tiny dependencies is a sign the class does too much.

## Java example

```java

// Purpose: DI injects dependencies via container; depends on abstraction, not construction
// Participants: Sender, EmailSender, FakeSender
// Structure: sealed hierarchy + records — exhaustive, immutable composition
// Behavior: wrapping/composition at runtime; no direct new of concrete in client
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Dependency injection | Give, do not create |
| Service locator | Ask a registry for it |
| Factory | Create without injecting |

## Interview Q&A

**Q: Why not just use a factory inside the class?**

Creating inside hides the dependency and blocks testing. Injection makes wiring visible at construction time.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Extra • Tags: design-patterns • Source: refactoring.guru*
