---
title: "Study Plan - Java"
category: "Java/99_Revision"
tags: [study-plan, java, interview-prep]
created: "2026-09-30"
completed: false
difficulty: "Medium"
reviewed: "2026-09-30"
sr-due: "2026-10-07"
type: "study-plan"
---

# Study Plan — Java

> **12-week senior Java engineering plan.** The goal is not to read every note. The goal is to build enough fluency to implement, diagnose, explain and design with Java 25.

## Weekly Loop

**Learn → Code → Break → Test → Explain → Review**

Each week should produce one tangible artifact: code, benchmark, test suite, diagram, or timed solution.

---

## Weeks 1–2 — Core Java

Focus:

- [[../01_Core-Java/Classes|Classes]]
- [[../01_Core-Java/Interface|Interfaces]]
- [[../01_Core-Java/Generics|Generics]]
- [[../01_Core-Java/Exception Handling|Exceptions]]
- [[../01_Core-Java/String Handling|Strings]]
- [[../01_Core-Java/Streams API|Streams]]
- [[../01_Core-Java/Optional|Optional]]
- [[../01_Core-Java/Date and Time API|Date/Time]]
- [[../01_Core-Java/IO and NIO|I/O and NIO]]
- [[../01_Core-Java/JVM Memory Model|JVM memory model]]

**Build:** a small Java 25 command-line application with parsing, validation, collections, streams and file I/O.

**Exit:** explain generics/PECS, equality, immutability, exception boundaries, stream semantics and memory basics.

---

## Week 3 — OOP and SOLID

Focus:

- [[../02_OOP/00 - OOP Overview|OOP]]
- [[../02_OOP/Abstraction|Abstraction]]
- [[../02_OOP/Encapsulation|Encapsulation]]
- [[../02_OOP/Inheritance|Inheritance]]
- [[../02_OOP/Polymorphism|Polymorphism]]
- [[../02_OOP/Class-Relationships|Class Relationships]]
- [[../02_OOP/SOLID-Summary|SOLID]]

**Build:** refactor a deliberately coupled service into composition + dependency inversion.

**Exit:** explain why a design changes when requirements change.

---

## Week 4 — Collections + DSA

Focus:

- [[../03_Collections/Collection|Collection contracts]]
- [[../03_Collections/List/List|List]]
- [[../03_Collections/Map|Map]]
- [[../03_Collections/Set/Set|Set]]
- [[../03_Collections/Queue|Queue]]
- [[../07_DSA/Array|Arrays]]
- [[../07_DSA/Linked List|Linked Lists]]
- [[../07_DSA/Trees|Trees]]
- [[../07_DSA/Graph|Graphs]]
- [[../07_DSA/Heap|Heap]]

Pair with the repository's [[../../Coding Patterns/README|Coding Patterns]].

**Exit:** choose a data structure from ordering, uniqueness, lookup, mutation and complexity constraints.

---

## Week 5 — Concurrency

Focus:

- [[../04_Concurrency/Threads|Threads]]
- [[../04_Concurrency/Executor Framework|Executors]]
- [[../04_Concurrency/CompletableFuture|CompletableFuture]]
- [[../04_Concurrency/Locks and Synchronizers|Locks]]
- [[../04_Concurrency/Atomics and Volatile|Atomics]]
- [[../04_Concurrency/Concurrent Collections|Concurrent Collections]]

Then study [[../01_Core-Java/Structured Concurrency|Structured Concurrency]] and virtual threads.

**Build:** a fan-out service that compares platform threads, virtual threads and CompletableFuture.

**Exit:** explain ownership, cancellation, contention, backpressure and when virtual threads are not useful.

---

## Week 6 — JVM and Performance

Focus:

- [[../11_JVM-Performance/JVM Diagnostics|Diagnostics]]
- [[../11_JVM-Performance/Garbage Collection|GC]]
- [[../11_JVM-Performance/JIT and Profiling|JIT and Profiling]]
- [[../01_Core-Java/JVM Memory Model|Memory model]]

**Build:** reproduce one allocation/GC or contention problem and diagnose it with JFR/JDK tooling.

**Exit:** distinguish CPU, allocation, GC, lock contention and I/O bottlenecks before changing configuration.

---

## Weeks 7–8 — Spring Backend

Read in order:

1. [[../05_Spring/Spring Framework|Spring Framework]]
2. [[../05_Spring/Dependency Injection|Dependency Injection]]
3. [[../05_Spring/Spring Boot|Spring Boot]]
4. [[../05_Spring/Spring MVC|Spring MVC]]
5. [[../05_Spring/Spring Data JPA|Spring Data JPA]]
6. [[../05_Spring/Spring Transaction|Transactions]]
7. [[../05_Spring/Spring Security|Security]]

**Build:** controller → service → repository with validation, consistent error handling, persistence and one explicit transaction boundary.

**Exit:** explain proxies, self-invocation, transaction propagation/isolation and the security filter chain.

---

## Week 9 — Testing and Build Engineering

Focus:

- [[../12_Testing-Tooling/JUnit 5|JUnit 5]]
- [[../12_Testing-Tooling/Testcontainers|Testcontainers]]
- [[../12_Testing-Tooling/Maven and Gradle|Maven and Gradle]]

**Build:** unit tests plus database integration tests against a disposable container.

**Exit:** know which behavior belongs in a unit test, integration test or end-to-end test; understand reproducible Java builds.

---

## Week 10 — Modern Java and Patterns

Focus:

- [[../00_Java-25-Overview/Java 25 Roadmap|Java 25 roadmap]]
- [[../00_Java-25-Overview/Whats New in Java 25|Java 25 changes]]
- [[../08_Modern-Java/01 Records|Records]]
- [[../08_Modern-Java/02 Sealed Classes|Sealed Classes]]
- [[../08_Modern-Java/03 Pattern Matching|Pattern Matching]]
- [[../08_Modern-Java/05 Virtual Threads - Loom|Virtual Threads]]
- [[../08_Modern-Java/06 ScopedValue|Scoped Values]]
- [[../06_Design-Patterns/Creational/Builder|Builder]]
- [[../06_Design-Patterns/Structural/Proxy|Proxy]]
- [[../06_Design-Patterns/Structural/Decorator|Decorator]]
- [[../06_Design-Patterns/Behavioral/Strategy|Strategy]]
- [[../06_Design-Patterns/Behavioral/Observer|Observer]]

**Rule:** learn a pattern from the change pressure it handles, not from its class diagram.

---

## Week 11 — LLD and Machine Coding

Start with:

- [[../10_LLD-Machine-Coding/00_Method-How-to-Answer-LLD|LLD method]]
- [[../10_LLD-Machine-Coding/00_UML-Class-and-Sequence-Diagrams|UML]]
- [[../10_LLD-Machine-Coding/01_Parking-Lot|Parking Lot]]
- [[../10_LLD-Machine-Coding/06_LRU-Cache|LRU Cache]]
- [[../10_LLD-Machine-Coding/05_ATM|ATM]]
- [[../10_LLD-Machine-Coding/11_Splitwise|Splitwise]]

**Exit:** solve one problem in 35–45 minutes with requirements, classes, state, concurrency and test strategy.

---

## Week 12 — Revision and Interview Simulation

Use [[Interview Questions]] plus random notes from every domain.

### Weekly simulation

- 2 Java coding problems.
- 1 concurrency explanation.
- 1 JVM diagnosis exercise.
- 1 Spring debugging question.
- 1 LLD problem.
- 10 spaced-repetition questions.
- 1 written architecture/trade-off decision.

### Final gate

You should be able to:

- write Java 25 code without syntax lookup;
- explain the JVM at a useful operational level;
- design thread-safe backend components;
- diagnose common Spring proxy/transaction problems;
- write meaningful integration tests;
- choose patterns only when they reduce change cost;
- complete a machine-coding problem under time pressure.

---

## Fast Tracks

### Backend interview in 4 weeks

1. Core Java + OOP.
2. Collections + DSA patterns.
3. Concurrency + Spring.
4. Testing + LLD + mocks.

### Java 25 delta

Read [[../00_Java-25-Overview/Whats New in Java 25|What is New in Java 25]], then [[../01_Core-Java/Structured Concurrency|Structured Concurrency]] and [[../08_Modern-Java/06 ScopedValue|Scoped Values]]. Do not relearn Java 8–21 if those foundations are already fluent.

### Senior/architect track

Spend extra time on JVM diagnosis, transaction boundaries, security, integration testing, concurrency ownership and LLD trade-offs.

---

## Review Ritual

**Monday:** choose three focus notes.

**Wednesday:** implement one concept without copying.

**Friday:** solve one DSA problem and one debugging problem.

**Sunday:** update completed/reviewed/sr-due and record one lesson learned.

---

## Related

- [[../00_Java-25-Overview/README|Java Overview]]
- [[../11_JVM-Performance/README|JVM & Performance]]
- [[../12_Testing-Tooling/README|Testing & Tooling]]
- [[../05_Spring/README|Spring]]
- [[../10_LLD-Machine-Coding/README|LLD]]
