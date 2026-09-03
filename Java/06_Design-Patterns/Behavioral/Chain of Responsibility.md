---
title: "Chain of Responsibility"
category: Design-Patterns
group: Behavioral
tags: [design-patterns, behavioral, chain-of-responsibility]
pattern: chain-of-responsibility
source: "https://refactoring.guru/design-patterns/chain-of-responsibility"
created: 2026-09-02
updated: 2026-09-02
---
# Chain of Responsibility

> Category: Behavioral • Source: [Refactoring.Guru — Chain of Responsibility](https://refactoring.guru/design-patterns/chain-of-responsibility) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Passes requests along a chain until one handler deals with it.

## Problem

Authentication then data requests need different handling, but the sender should not pick the handler explicitly.

## Solution

Define a handler interface. Chain them so each tries to handle or forwards. With sealed requests, a single switch can replace the chain when the set is closed.

## Structure

```
Request is sealed to AuthRequest and DataRequest. Handler handles or forwards. Client sends any Request to the first handler.
```

## Trade-offs

Use when multiple objects might handle a request or you want to decouple sender from receiver. A chain makes order explicit; a sealed switch is simpler when handlers are known up front.

## Java example

```java

// Purpose: Chain passes request along handlers until one handles it; decouples sender/receiver
// Participants: Req, AuthReq, DataReq
// Structure: sealed hierarchy + records — exhaustive, immutable composition
// Behavior: wrapping/composition at runtime; no direct new of concrete in client
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Chain of responsibility | Runtime chain, any handler |
| Sealed switch | Closed set, compiler-checked |
| Decorator | Stacks, all run |

## Interview Q&A

**Q: Chain vs sealed switch?**

Chain when handlers are dynamic or order matters at runtime. Sealed switch when the set is closed and compiler-checked exhaustiveness is enough.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Behavioral • Tags: design-patterns • Source: refactoring.guru*
