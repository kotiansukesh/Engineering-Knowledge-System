---
title: 30-Day Study Plan
category: Revision
tags: [plan, revision]
created: 2026-09-02
updated: 2026-09-02
---

# 30-Day Study Plan

> Interview prep — Core → OOP → Collections → Concurrency → Spring → Design Patterns → DSA + Coding Patterns. Java 25 throughout. Check off each day as you go.

```dataview
TABLE WITHOUT ID
  length(filter(file.tasks, (t) => t.completed)) as "Done",
  length(file.tasks) as "Total",
  round(length(filter(file.tasks, (t) => t.completed)) / length(file.tasks) * 100) + "%" as "Progress"
FROM "Java/99_Revision/30-Day Plan"
```

```dataview
TASK
FROM "Java/99_Revision/30-Day Plan"
GROUP BY file.link
```

---

## Week 1 — Core Java (Day 1–5) · Lambdas, Streams, Optional, Date/Time, IO/NIO + String/JVM

- [ ] **Day 1 — Lambdas & Functional Interfaces** (⏱ 60–90 min)
  - Notes: [[Lambdas and Functional Interfaces]] · [[Interface]] · [[Generics]]
  - Goal: Explain SAM, `@FunctionalInterface`, method refs, captures, and the 4 core FIs (Predicate/Function/Consumer/Supplier).
  - Review: spaced repetition queue

- [ ] **Day 2 — Streams API** (⏱ 60–90 min)
  - Notes: [[Streams API]] · [[Lambdas and Functional Interfaces]] · [[Optional]]
  - Goal: Intermediate vs terminal ops, lazy evaluation, collectors, parallel streams & pitfalls.
  - Review: spaced repetition queue

- [ ] **Day 3 — Optional & Exception Handling** (⏱ 60–90 min)
  - Notes: [[Optional]] · [[Exception Handling]] · [[Generics]]
  - Goal: `Optional` idioms (map/flatMap/orElseThrow), avoid `get()`/`null`, try-with-resources and exception hierarchy.
  - Review: spaced repetition queue

- [ ] **Day 4 — Date/Time API** (⏱ 60–90 min)
  - Notes: [[Date and Time API]] · [[Enums]] · [[Serialization]]
  - Goal: `java.time` immutability, `Instant`/`LocalDate`/`ZonedDateTime`, `DateTimeFormatter`, legacy `Date` migration.
  - Review: spaced repetition queue

- [ ] **Day 5 — IO/NIO + String & JVM** (⏱ 60–90 min)
  - Notes: [[IO and NIO]] · [[String Handling]] · [[JVM Memory Model]] · [[Annotations]]
  - Goal: Byte vs char streams, NIO `Path`/`Files`/`Channel`/`Buffer`, `String`/`StringBuilder`/`StringBuffer`, string pool, JVM heap/metaspace/GC basics.
  - Review: spaced repetition queue

---

## Week 2 — OOP + Collections (Day 6–10)

- [ ] **Day 6 — OOP Pillars** (⏱ 60–90 min)
  - Notes: [[00 - OOP Overview]] · [[Abstraction]] · [[Encapsulation]] · [[Polymorphism]]
  - Goal: 4 pillars with Java examples; abstract class vs interface, overloading vs overriding.
  - Review: spaced repetition queue

- [ ] **Day 7 — Inheritance & Types** (⏱ 60–90 min)
  - Notes: [[Inheritance]] · [[Single Inheritance]] · [[Multilevel Inheritance]] · [[Hierarchical Inheritance]] · [[Multiple Inheritance]] · [[Hybrid Inheritance]] · [[Classes]] · [[Interface]] · [[Abstract Class]] · [[Object Class]] · [[POJO Class]] · [[Immutable Class]]
  - Goal: All 5 inheritance types, why Java forbids multiple class inheritance, diamond via interfaces, `Types/` taxonomy.
  - Review: spaced repetition queue

- [ ] **Day 8 — Collections: List & Collection** (⏱ 60–90 min)
  - Notes: [[Collection]] · [[List]] · [[ArrayList]] · [[LinkedList]] · [[Vector]] · [[Stack]]
  - Goal: `ArrayList` vs `LinkedList` vs `Vector`/`Stack`, `SequencedCollection` (Java 21/25), fail-fast iterators.
  - Review: spaced repetition queue

- [ ] **Day 9 — Collections: Set & Map** (⏱ 60–90 min)
  - Notes: [[Set]] · [[HashSet]] · [[TreeSet]] · [[Sorted Set]] · [[Map]]
  - Goal: `HashSet`/`TreeSet`/`LinkedHashSet`, `HashMap` internals, `TreeMap` ordering, `Set` vs `Map`.
  - Review: spaced repetition queue

- [ ] **Day 10 — Collections: Queue + Types Deep-Dive** (⏱ 60–90 min)
  - Notes: [[Queue]] · [[Wrapper Class]] · [[Singleton Class]] · [[Static Class]] · [[Nested Classes Overview|Nested Classes Overview]] · [[Generics]]
  - Goal: `Queue`/`Deque`/`PriorityQueue`, Wrapper caching, Singleton/Static/Nested variants, generics PECS.
  - Review: spaced repetition queue

---

## Week 3 — Concurrency (Day 11–15)

- [ ] **Day 11 — Threads** (⏱ 60–90 min)
  - Notes: [[Threads]] · [[Atomics and Volatile]]
  - Goal: Thread lifecycle, 4 creation ways (Thread/Runnable/Callable/Future), race/deadlock/starvation/livelock.
  - Review: spaced repetition queue

- [ ] **Day 12 — Executor Framework** (⏱ 60–90 min)
  - Notes: [[Executor Framework]] · [[Threads]] · [[Concurrent Collections]]
  - Goal: `Executor`/`ExecutorService`/`ThreadPoolExecutor`, pool sizing, `Future`, `ScheduledExecutor`, concurrent collections overview.
  - Review: spaced repetition queue

- [ ] **Day 13 — CompletableFuture** (⏱ 60–90 min)
  - Notes: [[CompletableFuture]] · [[Executor Framework]]
  - Goal: Async chains (`thenApply`/`thenCompose`/`exceptionally`), combining futures, custom executors, Java 25 structured concurrency context.
  - Review: spaced repetition queue

- [ ] **Day 14 — Locks & Synchronizers** (⏱ 60–90 min)
  - Notes: [[Locks and Synchronizers]] · [[Threads]]
  - Goal: `synchronized` vs `ReentrantLock`, `ReadWriteLock`, `CountDownLatch`/`CyclicBarrier`/`Semaphore`/`Phaser`.
  - Review: spaced repetition queue

- [ ] **Day 15 — Atomics, Volatile & Concurrent Collections** (⏱ 60–90 min)
  - Notes: [[Atomics and Volatile]] · [[Concurrent Collections]] · [[Locks and Synchronizers]]
  - Goal: `volatile` visibility, `AtomicInteger`/`LongAdder`, CAS, `ConcurrentHashMap`/`CopyOnWriteArrayList`/`BlockingQueue`.
  - Review: spaced repetition queue

---

## Week 4 — Spring + Design Patterns (Day 16–22)

- [ ] **Day 16 — Spring Boot & Core** (⏱ 60–90 min)
  - Notes: [[Spring Boot]] · [[Spring Framework]] · [[Spring Core]]
  - Goal: Boot auto-config, starters, `Spring Core` IoC container, beans lifecycle, `@SpringBootApplication`.
  - Review: spaced repetition queue

- [ ] **Day 17 — Spring MVC & DI** (⏱ 60–90 min)
  - Notes: [[Spring MVC]] · [[Dependency Injection]] · [[Spring Framework]]
  - Goal: MVC dispatch flow, controllers/`@RequestMapping`, DI (constructor vs setter), AOP basics. Extra: [[Dependency Injection Pattern]]
  - Review: spaced repetition queue

- [ ] **Day 18 — Spring Data JPA** (⏱ 60–90 min)
  - Notes: [[Spring Data JPA]] · [[Spring Framework]]
  - Goal: JPA/`Hibernate`, repositories, `@Entity` lifecycle, `record` entities (Java 25), query methods, N+1.
  - Review: spaced repetition queue

- [ ] **Day 19 — Spring Security & Transaction** (⏱ 60–90 min)
  - Notes: [[Spring Security]] · [[Spring Transaction]]
  - Goal: Security filter chain, auth/RBAC/JWT, `@Transactional` propagation/isolation, rollback rules.
  - Review: spaced repetition queue

- [ ] **Day 20 — Design Patterns: Creational (5)** (⏱ 60–90 min)
  - Notes: [[Singleton]] · [[Factory Method]] · [[Abstract Factory]] · [[Builder]] · [[Prototype]]
  - Goal: Problem → solution → trade-offs for all 5 GoF creational patterns. Compare Factory Method vs Abstract Factory.
  - Review: spaced repetition queue

- [ ] **Day 21 — Design Patterns: Structural (7)** (⏱ 60–90 min)
  - Notes: [[Adapter]] · [[Bridge]] · [[Composite]] · [[Decorator]] · [[Facade]] · [[Flyweight]] · [[Proxy]]
  - Goal: All 7 structural patterns; Decorator vs Proxy vs Adapter; where Spring uses them.
  - Review: spaced repetition queue

- [ ] **Day 22 — Design Patterns: Behavioral (10)** (⏱ 60–90 min)
  - Notes: [[Chain of Responsibility]] · [[Command]] · [[Iterator]] · [[Mediator]] · [[Memento]] · [[Observer]] · [[State]] · [[Strategy]] · [[Template Method]] · [[Visitor]]
  - Goal: All 10 behavioral patterns; Observer vs Mediator, Strategy vs State vs Template Method.
  - Review: spaced repetition queue

---

## Week 5 — DSA + Coding Patterns + Mocks (Day 23–30)

- [ ] **Day 23 — DSA: Array & Heap** (⏱ 60–90 min)
  - Notes: [[Array]] · [[Heap]] · [[HashMap]]
  - Goal: Array two-pointer/sliding window basics, `Heap`/`PriorityQueue`, heap sort, `HashMap` (Java 25 Compact Object Headers note).
  - Review: spaced repetition queue

- [ ] **Day 24 — DSA: Graph, Trees & Linked Lists** (⏱ 60–90 min)
  - Notes: [[Graph]] · [[Trees]] · [[Linked List]] · [[Singly Linked List]] · [[Doubly Linked List]] · [[Stack]] · [[Queue]]
  - Goal: Graph BFS/DFS, tree traversals/height, singly vs doubly LL, `Stack`/`Queue` implementations.
  - Review: spaced repetition queue

- [ ] **Day 25 — Coding Patterns: Array (4)** (⏱ 60–90 min)
  - Notes: [[01 - Prefix Sum]] · [[02 - Two Pointers]] · [[03 - Sliding Window]] · [[04 - Frequency Counting]]
  - Goal: Master 4 array patterns — prefix sums, two pointers, sliding window, frequency counting; 2 problems each.
  - Review: spaced repetition queue

- [ ] **Day 26 — Coding Patterns: LinkedList + Stack/Heap (4)** (⏱ 60–90 min)
  - Notes: [[01 - Fast and Slow Pointers]] · [[02 - LinkedList In-place Reversal]] · [[01 - Monotonic Stack]] · [[02 - Top K Elements]]
  - Goal: Fast & slow, in-place reversal, monotonic stack, top-K heap; cross-drill with [[Linked List]]/[[Heap]].
  - Review: spaced repetition queue

- [ ] **Day 27 — Coding Patterns: Intervals/Search + Trees/Graphs (7)** (⏱ 60–90 min)
  - Notes: [[01 - Overlapping Intervals]] · [[02 - Modified Binary Search]] · [[01 - Binary Tree Traversal]] · [[02 - DFS]] · [[03 - BFS]] · [[04 - Shortest Path]] · [[05 - Trie]]
  - Goal: Intervals merging, modified binary search, tree DFS/BFS, shortest path (Dijkstra), trie.
  - Review: spaced repetition queue

- [ ] **Day 28 — Coding Patterns: Matrix + Backtracking/DP + Bit (5)** (⏱ 60–90 min)
  - Notes: [[01 - Matrix Traversal]] · [[01 - Backtracking]] · [[02 - Dynamic Programming]] · [[03 - Greedy]] · [[01 - Bit Manipulation]]
  - Goal: Matrix traversal, backtracking template, DP (memo vs tabulation), greedy, bit tricks.
  - Review: spaced repetition queue

- [ ] **Day 29 — Mock Interview 1 + DSA Drill** (⏱ 60–90 min)
  - Notes: [[Interview Questions]] · [[Array]] · [[Heap]] · [[Graph]] · [[03 - Sliding Window]] · [[02 - DFS]]
  - Goal: Timed mock (45 min coding + 15 min review), weak-area patch from Days 1–28.
  - Review: spaced repetition queue

- [ ] **Day 30 — Mock Interview 2 + Final Review** (⏱ 60–90 min)
  - Notes: [[Interview Questions]] · [[Lambdas and Functional Interfaces]] · [[CompletableFuture]] · [[Spring Boot]] · [[Strategy]] · [[02 - Dynamic Programming]]
  - Goal: Full-stack mock (Core + Concurrency + Spring + Pattern + DSA), fill spaced-repetition queue, set `reviewed:` dates.
  - Review: spaced repetition queue

---

## How to use

1. Check `- [ ]` → `- [x]` as you complete each day.
2. Progress bar at top is live Dataview (tasks ratio).
3. Set `reviewed: 2026-09-XX` in each note's frontmatter when done — enables `99_Revision` dataview tracking.
4. Missed a day? Shift by one — keep the spaced-repetition line honest.

*Java 25: notes reference `record`, `SequencedCollection`, pattern matching, Compact Object Headers (JEP 450) — search `Java 25` across vault.*
