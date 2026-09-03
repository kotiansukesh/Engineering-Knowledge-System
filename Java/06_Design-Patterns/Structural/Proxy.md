---
title: "Proxy"
category: Design-Patterns
group: Structural
tags: [design-patterns, structural, proxy]
pattern: proxy
source: "https://refactoring.guru/design-patterns/proxy"
created: 2026-09-02
updated: 2026-09-02
---
# Proxy

> Category: Structural • Source: [Refactoring.Guru — Proxy](https://refactoring.guru/design-patterns/proxy) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Controls access by placing a stand-in in front of an object.

## Problem

A YouTube client hits the network on every listVideos call. Caching or access checks belong in front.

## Solution

Write a proxy that implements the same interface, holds the real subject, and adds logic before or after delegating.

## Structure

```
YTube is sealed to RealYTube and CachedYTube. CachedYTube holds RealYTube and caches results. Client talks to the interface.
```

## Trade-offs

Use to add lazy init, caching, or access checks without changing the subject. The proxy is interchangeable because the interface is the same. Each proxy does one kind of control; do not mix unrelated checks in one.

## Java example

```java

// Purpose: Proxy controls access to real subject; lazy, protection, or remote indirection
// Participants: YTube, RealYTube, CachedYTube
// Structure: sealed hierarchy + records — exhaustive, immutable composition
// Behavior: Factory/creation or delegation without exposing concrete construction
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Proxy | Controls access, same interface |
| Decorator | Adds behavior, stackable |
| Adapter | Different interface |

## Interview Q&A

**Q: Proxy vs decorator?**

Proxy controls how you reach the object, often one layer for caching or checks. Decorator adds features and often stacks.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Structural • Tags: design-patterns • Source: refactoring.guru*
