---
title: Java Domain Syllabus
category: Java/99_Revision
tags: [syllabus, java, backend]
created: 2026-09-30
type: syllabus
---

# Java Domain Syllabus

> **This is a domain syllabus, not a second calendar.**
>
> The repository-wide [[Study Plan]] is the only learning calendar. Because Java/Spring is an existing backend strength, study this domain just-in-time when the baseline or a project exposes a gap.

## Capability map

### Core Java
- generics and PECS
- equality and immutability
- exceptions
- streams and collections
- I/O and NIO
- memory fundamentals

### Concurrency
- threads and executors
- CompletableFuture
- locks and atomics
- concurrent collections
- virtual threads
- structured concurrency concepts

### JVM and performance
- allocation and GC
- JIT
- JFR and profiling
- CPU vs allocation vs contention vs I/O diagnosis

### Spring backend
- dependency injection
- Spring Boot
- MVC
- persistence
- transactions
- security
- testing and Testcontainers

### Design and LLD
- design patterns as responses to change pressure
- object ownership and composition
- machine-coding
- class/sequence diagrams

### Modern Java
Use [[Java/00_Java-25-Overview/Java 25 Roadmap]] for the Java 25 feature map and release context.

## Just-in-time rule

Do not restart a 12-week Java curriculum merely because this domain has one.

Examples:
- Spring transaction issue → study transaction/proxy material.
- concurrency bottleneck → study executors/virtual threads/JFR.
- LLD gap → study the relevant LLD pattern.
- project testability gap → study testing boundaries.

Then return to the current master-plan task.

## Backend baseline

Use Java as a supporting track for the primary path:

**Backend Expert → AI Engineer → AI Platform Engineer → AI Architect**

The objective is production fluency, not completion of every Java note.

## Related

- [[Study Plan]]
- [[Java/README]]
- [[Java/00_Java-25-Overview/Java 25 Roadmap]]
- [[Coding Patterns/README]]
- [[Build Lab/README]]
