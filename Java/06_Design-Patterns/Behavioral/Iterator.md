---
title: "Iterator"
category: Design-Patterns
group: Behavioral
tags: [design-patterns, behavioral, iterator]
pattern: iterator
source: "https://refactoring.guru/design-patterns/iterator"
created: 2026-09-02
updated: 2026-09-02
---
# Iterator

> Category: Behavioral • Source: [Refactoring.Guru — Iterator](https://refactoring.guru/design-patterns/iterator) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Lets you traverse elements without exposing the collection internals.

## Problem

A social network stores profiles internally. Clients should not depend on list vs set vs map.

## Solution

Expose iteration through Iterable and Iterator. For custom traversals, implement Iterator with next and hasNext. Plain Iterable covers most cases.

## Structure

```
Iterable holds Profiles and returns an Iterator. Client uses for-each without seeing storage.
```

## Trade-offs

Use when you need multiple traversal kinds or want to hide the collection type. Implementing Iterable gives for-each and stream support for free. Only write a custom iterator when built-ins do not fit.

## Java example

```java

// Purpose: Iterator traverses collection without exposing internals; SequencedCollection abstraction
// Participants: Profile, SocialNet
// Behavior: Factory/creation or delegation without exposing concrete construction
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Iterator | Sequential access, hide collection |
| Visitor | Operation across a structure |
| Stream | Pipeline, not step-by-step cursor |

## Interview Q&A

**Q: Do you still write custom iterators?**

Rarely. Implement Iterable and reuse built-in iterators. Only write one for special traversals.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Behavioral • Tags: design-patterns • Source: refactoring.guru*
