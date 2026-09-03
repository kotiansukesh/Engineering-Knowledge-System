---
title: "Study Plan - Java 25"
category: overview
tags: [java25, plan, study]
created: 2026-09-03
completed: false
---

# Study Plan — Java 25 LTS (6 Weeks, 8–12h/week)

> Interview-ready in 6 weeks. **Path:** `/Users/sukesh/documents/github/obsidian/Java` • Daily checkboxes are live `TASK` — tick them, Dataview counts at top. Mark notes `completed: true` + `reviewed: YYYY-MM-DD` as you go.

```dataview
TABLE WITHOUT ID
  length(filter(file.tasks, (t) => t.completed)) as "Done",
  length(file.tasks) as "Total",
  round(length(filter(file.tasks, (t) => t.completed)) / length(file.tasks) * 100) + "%" as "Progress"
FROM "Java/00_Java-25-Overview/Study Plan - Java 25"
```

```dataview
TASK
FROM "Java/00_Java-25-Overview/Study Plan - Java 25"
GROUP BY file.link
```

---

## How to use

1. **Each checkbox = 60–90 min**. 5 days/week, 2 days buffer/review.
2. Notes linked via `[[wikilink]]` — open + run the runnable snippet.
3. After each day: set `reviewed: YYYY-MM-DD` + `completed: true` in that note's frontmatter.
4. End of week: sweep `[[Dashboard]]` → Overdue (>7d) + SR Due.

## Week 1 — Core Java Foundations

- [ ] **Day 1 — Lambdas & Functional Interfaces** (60–90m)
  - Notes: [[../01_Core-Java/Lambdas and Functional Interfaces|Lambdas]] · [[../01_Core-Java/Interface|Interface]] · [[../01_Core-Java/Generics|Generics]]
  - Goal: SAM, `@FunctionalInterface`, method refs, captures, `Predicate/Function/Consumer/Supplier`
  - Drill: write `Function<String,Integer>` without IDE hint

- [ ] **Day 2 — Streams & Optional** (60–90m)
  - Notes: [[../01_Core-Java/Streams API|Streams API]] · [[../01_Core-Java/Optional|Optional]] · [[../01_Core-Java/Lambdas and Functional Interfaces|Lambdas]]
  - Goal: intermediate vs terminal, lazy, collectors, `Optional` map/flatMap/orElseThrow
  - Pitfall: never `Optional.get()` without `isPresent()`

- [ ] **Day 3 — String, JVM, Annotations** (60–90m)
  - Notes: [[../01_Core-Java/String Handling|String Handling]] · [[../01_Core-Java/JVM Memory Model|JVM Memory Model]] · [[../01_Core-Java/Annotations|Annotations]]
  - Goal: pool, `StringBuilder` vs `StringBuffer`, heap/metaspace/GC basics, `StackOverflow` vs `OOM`

- [ ] **Day 4 — Types Deep Dive** (60–90m)
  - Notes: [[../01_Core-Java/Types/Immutable Class|Immutable Class]] · [[../01_Core-Java/Types/Singleton Class|Singleton Class]] · [[../01_Core-Java/Types/Wrapper Class|Wrapper Class]] · [[../01_Core-Java/Types/Nested Classes Overview|Nested Overview]]
  - Goal: immutable防, singleton DCL vs enum, wrapper caching (`Integer` -128..127)

- [ ] **Day 5 — Date/Time + IO/NIO + Exception** (60–90m)
  - Notes: [[../01_Core-Java/Date and Time API|Date/Time]] · [[../01_Core-Java/IO and NIO|IO/NIO]] · [[../01_Core-Java/Exception Handling|Exceptions]]
  - Goal: `java.time` immutability, `Path/Files/Channel`, try-with-resources
  - Buffer: review flashcards from [[Whats New in Java 25|Whats New]] Q

## Week 2 — OOP + Collections + Modern Start

- [ ] **Day 6 — OOP Pillars** (60–90m)
  - Notes: [[../02_OOP/00 - OOP Overview|OOP Overview]] · [[../02_OOP/Abstraction|Abstraction]] · [[../02_OOP/Encapsulation|Encapsulation]] · [[../02_OOP/Polymorphism|Polymorphism]]
  - Goal: 4 pillars with code; abstract vs interface, overloading vs overriding

- [ ] **Day 7 — Inheritance & Types** (60–90m)
  - Notes: [[../02_OOP/Inheritance|Inheritance]] · [[../02_OOP/Inheritance/Single Inheritance|Single]] · [[../02_OOP/Inheritance/Multiple Inheritance|Multiple]] · [[../02_OOP/Inheritance/Hybrid Inheritance|Hybrid]] · [[../01_Core-Java/Classes|Classes]]
  - Goal: 5 types, diamond via interfaces, sealed preview

- [ ] **Day 8 — Records & Sealed** (60–90m)
  - Notes: [[../08_Modern-Java/01 Records|01 Records]] · [[../08_Modern-Java/02 Sealed Classes|02 Sealed]] · [[../01_Core-Java/Types/POJO Class|POJO]]
  - Goal: `record` compact constructor, `sealed permits`, exhaustive switch
  - Code: `record Point(int x,int y){public Point{if(x<0)throw...}}`

- [ ] **Day 9 — Collections List/Set/Map** (60–90m)
  - Notes: [[../03_Collections/Collection|Collection]] · [[../03_Collections/List/ArrayList|ArrayList]] · [[../03_Collections/Set/HashSet|HashSet]] · [[../03_Collections/Map|Map]]
  - Goal: `ArrayList` 1.5× growth, `HashSet` via `HashMap`, `TreeSet` ordering

- [ ] **Day 10 — Sequenced + Pattern Matching** (60–90m)
  - Notes: [[../08_Modern-Java/04 Sequenced Collections|Sequenced]] · [[../08_Modern-Java/03 Pattern Matching|Pattern Matching]] · [[../03_Collections/Queue|Queue]]
  - Goal: `getFirst()/getLast()/reversed()`, record patterns, primitive patterns (JEP 507)

## Week 3 — Concurrency (Loom is the interview)

- [ ] **Day 11 — Threads Lifecycle** (60–90m)
  - Notes: [[../04_Concurrency/Threads|Threads]] · [[../04_Concurrency/Atomics and Volatile|Atomics]]
  - Goal: 7 states, 4 creation ways, race/deadlock/starvation

- [ ] **Day 12 — Virtual Threads (JEP 491!)** (60–90m)
  - Notes: [[../08_Modern-Java/05 Virtual Threads - Loom|Virtual Threads]] · [[../04_Concurrency/Executor Framework|Executor]]
  - Goal: `newVirtualThreadPerTaskExecutor()`, `synchronized` no longer pins (JEP 491), carrier vs virtual
  - Code: `try(var exec = Executors.newVirtualThreadPerTaskExecutor()){ exec.submit(...) }`

- [ ] **Day 13 — ScopedValue** (60–90m)
  - Notes: [[../08_Modern-Java/06 ScopedValue|ScopedValue]] · [[../04_Concurrency/Locks and Synchronizers|Locks]]
  - Goal: `ScopedValue` vs `ThreadLocal`, `where().run()`, auto-inherit to forks

- [ ] **Day 14 — Structured Concurrency (preview)** (60–90m)
  - Notes: [[../04_Concurrency/Threads|Threads]] § StructuredTaskScope · [[../08_Modern-Java/06 ScopedValue|ScopedValue]]
  - Goal: `StructuredTaskScope.ShutdownOnFailure` vs `ShutdownOnSuccess`, `--enable-preview`
  - Flag: `javac --enable-preview --release 25`

- [ ] **Day 15 — CompletableFuture + Locks + Concurrent Collections** (60–90m)
  - Notes: [[../04_Concurrency/CompletableFuture|CompletableFuture]] · [[../04_Concurrency/Locks and Synchronizers|Locks]] · [[../04_Concurrency/Concurrent Collections|Concurrent Collections]]
  - Goal: `thenApply/thenCompose/exceptionally`, `CountDownLatch/Semaphore`, `ConcurrentHashMap`

## Week 4 — Spring Boot 3.5 + Virtual Threads

- [ ] **Day 16 — Spring Core & Boot** (60–90m)
  - Notes: [[../05_Spring/Spring Framework|Spring Framework]] · [[../05_Spring/Spring Core|Spring Core]] · [[../05_Spring/Spring Boot|Spring Boot]]
  - Goal: IoC, beans lifecycle, auto-config, `spring.threads.virtual.enabled=true`

- [ ] **Day 17 — Spring MVC + DI** (60–90m)
  - Notes: [[../05_Spring/Spring MVC|Spring MVC]] · [[../05_Spring/Dependency Injection|DI]]
  - Goal: dispatch flow, `@RequestMapping`, constructor vs setter DI

- [ ] **Day 18 — Data JPA + Transactions** (60–90m)
  - Notes: [[../05_Spring/Spring Data JPA|Data JPA]] · [[../05_Spring/Spring Transaction|Transaction]]
  - Goal: JPA lifecycle, query methods, N+1, `@Transactional` propagation

- [ ] **Day 19 — Security + Flexible Constructors** (60–90m)
  - Notes: [[../05_Spring/Spring Security|Security]] · [[../08_Modern-Java/07 Flexible Constructors and Module Imports|Flexible Constructors]]
  - Goal: filter chain, JWT, statements before `super()` (JEP 513)

- [ ] **Day 20 — Performance** (60–90m)
  - Notes: [[../08_Modern-Java/08 Compact Object Headers and Performance|Compact Headers]] · [[../01_Core-Java/JVM Memory Model|JVM]]
  - Goal: `-XX:+UseCompactObjectHeaders`, ZGC/G1, header 128→64 bits

## Week 5 — Design Patterns as Spring Uses Them

- [ ] **Day 21 — Creational (5)** (60–90m)
  - Notes: [[../06_Design-Patterns/Creational/Singleton|Singleton]] · [[../06_Design-Patterns/Creational/Factory Method|Factory Method]] · [[../06_Design-Patterns/Creational/Abstract Factory|Abstract Factory]] · [[../06_Design-Patterns/Creational/Builder|Builder]] · [[../06_Design-Patterns/Creational/Prototype|Prototype]]
  - Goal: Factory Method vs Abstract Factory, where Spring uses them

- [ ] **Day 22 — Structural (7)** (60–90m)
  - Notes: [[../06_Design-Patterns/Structural/Adapter|Adapter]] · [[../06_Design-Patterns/Structural/Decorator|Decorator]] · [[../06_Design-Patterns/Structural/Proxy|Proxy]] · [[../06_Design-Patterns/Structural/Facade|Facade]]
  - Goal: Decorator vs Proxy vs Adapter; Spring AOP = Proxy

- [ ] **Day 23 — Behavioral (10)** (60–90m)
  - Notes: [[../06_Design-Patterns/Behavioral/Observer|Observer]] · [[../06_Design-Patterns/Behavioral/Strategy|Strategy]] · [[../06_Design-Patterns/Behavioral/Command|Command]] · [[../06_Design-Patterns/Behavioral/Template Method|Template Method]]
  - Goal: Observer vs Mediator, Strategy vs State vs Template

## Week 6 — DSA + Mocks + SR Sweep

- [ ] **Day 24 — DSA Core** (60–90m)
  - Notes: [[../07_DSA/Array|Array]] · [[../07_DSA/Heap|Heap]] · [[../07_DSA/HashMap|HashMap]] · [[../07_DSA/Trees|Trees]] · [[../07_DSA/Graph|Graph]]
  - Goal: Array patterns, heap, HashMap internals + compact headers, BFS/DFS

- [ ] **Day 25 — Coding Patterns: Array + LinkedList** (60–90m)
  - Notes: [[../../Coding Patterns/01_Array/01 - Prefix Sum|Prefix Sum]] · [[../../Coding Patterns/01_Array/02 - Two Pointers|Two Pointers]] · [[../../Coding Patterns/02_LinkedList/01 - Fast and Slow Pointers|Fast/Slow]]
  - Goal: 2 problems per pattern

- [ ] **Day 26 — Coding Patterns: Trees/Graphs + DP** (60–90m)
  - Notes: [[../../Coding Patterns/05_Trees_Graphs/02 - DFS|DFS]] · [[../../Coding Patterns/05_Trees_Graphs/03 - BFS|BFS]] · [[../../Coding Patterns/07_Backtracking_DP/02 - Dynamic Programming|DP]]
  - Goal: Dijkstra, memo vs tabulation

- [ ] **Day 27 — Mock 1 (timed 45+15)** (90m)
  - Notes: [[../99_Revision/Interview Questions|Interview Questions]] · [[../08_Modern-Java/01 Records|Records]] · [[../08_Modern-Java/05 Virtual Threads - Loom|Virtual Threads]]
  - Goal: 45m coding + 15m review; weakest folder revisit

- [ ] **Day 28 — Mock 2 + Final SR** (90m)
  - Notes: [[../99_Revision/Interview Questions|Interview Questions]] · [[Whats New in Java 25|Whats New]] · [[Interview Strategy|Interview Strategy]]
  - Goal: Full-stack mock (Core + Concurrency + Spring + Pattern + DSA), fill SR queue

- [ ] **Buffer — Overdue sweep** (anytime)
  - Open [[Dashboard]] → fix all `>7d` stale + SR Due, set `reviewed: 2026-09-XX`

---

## Tracker — How to know you're done

- Each day's checkbox → `TASK` progress bar at top.
- Each note's `completed: true` → [[../README|Java MOC]] folder bars + [[Dashboard]].
- `reviewed: 2026-09-XX` → [[Dashboard]] urgency (🟢 ≤7d, 🟡 7–14d, 🔴 >14d/never).

*Java 25 flag:* notes with `Java 25` in text: `WHERE contains(file.text, "Java 25")`

---
*Category: overview • java25*
