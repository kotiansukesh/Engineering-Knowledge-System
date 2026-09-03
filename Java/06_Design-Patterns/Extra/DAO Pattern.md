---
title: "DAO Pattern"
category: Design-Patterns
tags: [design-patterns, dao, extra]
created: 2026-01-18
updated: 2026-09-02
---
# DAO Pattern

> Category: Extra • Source: [Refactoring.Guru — DAO Pattern](https://refactoring.guru/design-patterns/dao-pattern) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Isolates business code from persistence details behind an interface.

## Problem

Business logic mixed with jdbc calls is hard to test and hard to move from jdbc to jpa.

## Solution

Define a DAO interface with find, save, and delete. Concrete DAOs hide jdbc or in-memory detail. Services depend only on the interface.

## Structure

```
Service → UserDao → MemDao or JdbcDao. User is a record. Tests swap in the memory DAO.
```

## Trade-offs

Use to keep persistence swappable and testable. Records make entities concise. In Spring Data, JpaRepository already plays this role, so a hand-rolled DAO is mainly for plain jdbc or test isolation.

## Java example

```java

// Purpose: DAO abstracts persistence; separates domain from data-access mechanics
// Participants: User, UserDao, MemDao
// Structure: sealed hierarchy + records — exhaustive, immutable composition
// Behavior: wrapping/composition at runtime; no direct new of concrete in client
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| DAO | CRUD for one entity |
| Repository | Collection-like, broader queries |
| Active record | Entity persists itself |

## Interview Q&A

**Q: DAO vs repository?**

DAO is plain crud for one entity. Repository feels like a collection with broader queries and specs.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Extra • Tags: design-patterns • Source: refactoring.guru*
