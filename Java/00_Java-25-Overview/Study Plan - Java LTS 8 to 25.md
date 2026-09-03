---
title: "Study Plan - Java LTS 8 to 25"
category: overview
tags: [lts, plan, study, java8, java11, java17, java21, java25]
created: 2026-09-03
completed: false
---

# Study Plan — Java LTS 8 → 25 (10 Weeks, 8–12h/week)

> Interview-ready across any LTS. **Path:** `/Users/sukesh/documents/github/obsidian/Java` • Daily checkboxes are live `TASK` — tick them, Dataview counts at top. Each day links to its `--release` runnable. Mark notes `completed: true` + `reviewed: YYYY-MM-DD` as you go. **Previous 6-week plan kept as [[Study Plan - Java 25|Study Plan - Java 25 (legacy)]] — this restructured plan subsumes it.**

```dataview
TABLE WITHOUT ID
  length(filter(file.tasks, (t) => t.completed)) as "Done",
  length(file.tasks) as "Total",
  round(length(filter(file.tasks, (t) => t.completed)) / length(file.tasks) * 100) + "%" as "Progress"
FROM "Java/00_Java-25-Overview/Study Plan - Java LTS 8 to 25"
```

```dataview
TASK
FROM "Java/00_Java-25-Overview/Study Plan - Java LTS 8 to 25"
GROUP BY file.link
```

---

## How to use

1. **Each checkbox = 60–90 min**. 5 days/week, buffer weekends for review.
2. Follow **LTS order**: 8 → 11 → 17 → 21 → 25 — each day's notes list the `--release` to run.
3. After each day: set `reviewed: YYYY-MM-DD` + `completed: true` in that note's frontmatter.
4. End of week: open [[Dashboard]] → fix Overdue (>7d) + SR Due.

## Phase 1 — Java 8 Foundations (Weeks 1–2) — *The 90% interview*

- [ ] **Day 1 — Java 8: Lambdas & Functional Interfaces** (60–90m) `--release 8`
  - Notes: [[Java 8 LTS Overview|Java 8 Overview]] § Lambdas · [[../01_Core-Java/Lambdas and Functional Interfaces|Lambdas]] · [[../01_Core-Java/Interface|Interface]] · [[../01_Core-Java/Generics|Generics]]
  - Goal: SAM, `@FunctionalInterface`, captures effectively final, method refs
  - Drill: `Function<String,Integer> f = String::length`

- [ ] **Day 2 — Streams & Optional** (60–90m) `--release 8`
  - Notes: [[Java 8 LTS Overview|Java 8]] § Streams · [[../01_Core-Java/Streams API|Streams API]] · [[../01_Core-Java/Optional|Optional]]
  - Goal: lazy intermediate vs terminal, collectors, `map/flatMap/orElseThrow` — never `Optional.get()`

- [ ] **Day 3 — java.time & Metaspace** (60–90m) `--release 8`
  - Notes: [[Java 8 LTS Overview|Java 8]] § java.time · [[../01_Core-Java/Date and Time API|Date/Time]] · [[../01_Core-Java/JVM Memory Model|JVM - Metaspace]] · [[../01_Core-Java/String Handling|String Handling]]
  - Goal: `Instant/LocalDate/ZonedDateTime` immutable vs `SimpleDateFormat` race; PermGen → Metaspace

- [ ] **Day 4 — Default Methods & Types Deep Dive** (60–90m) `--release 8`
  - Notes: [[Java 8 LTS Overview|Java 8]] § Default · [[../01_Core-Java/Types/Immutable Class|Immutable]] · [[../01_Core-Java/Types/Singleton Class|Singleton]] · [[../01_Core-Java/Types/Wrapper Class|Wrapper]]
  - Goal: evolve interfaces without breaking; immutable防, singleton DCL vs enum

- [ ] **Day 5 — Date/Time + IO/NIO + Exceptions Buffer** (60–90m)
  - Notes: [[../01_Core-Java/IO and NIO|IO/NIO]] · [[../01_Core-Java/Exception Handling|Exceptions]] · [[LTS Evolution 8 to 25|LTS Evolution]]
  - Buffer: flashcards from [[Java 8 LTS Overview|Java 8]] Quick Check

## Phase 2 — Java 11 Expansion (Week 3) — *The quiet LTS*

- [ ] **Day 6 — var & String/Collection Sugar** (60–90m) `--release 11`
  - Notes: [[Java 11 LTS Overview|Java 11]] § var/String · [[../01_Core-Java/Generics|Generics]] § var limits
  - Goal: where `var` NOT allowed (field/param/no init), `isBlank/strip/lines/repeat`, `List.of` immutable

- [ ] **Day 7 — HttpClient & Single-File Launch** (60–90m) `--release 11`
  - Notes: [[Java 11 LTS Overview|Java 11]] § HttpClient · [[../01_Core-Java/IO and NIO|IO/NIO]]
  - Goal: `HttpClient.send` vs `HttpURLConnection`; `java Hello.java` without `javac`; JAXB removal → `jakarta.xml.bind`

## Phase 3 — Java 17 Modern Baseline (Weeks 4–5) — *Sealed + Records*

- [ ] **Day 8 — Records, Sealed, Text Blocks** (60–90m) `--release 17`
  - Notes: [[Java 17 LTS Overview|Java 17]] § sealed/record · [[../08_Modern-Java/01 Records|Records]] · [[../08_Modern-Java/02 Sealed Classes|Sealed]] · [[../01_Core-Java/Types/POJO Class|POJO]]
  - Goal: `record` compact constructor; `sealed permits` exhaustive switch

- [ ] **Day 9 — Pattern instanceof & Switch Expressions** (60–90m) `--release 17`
  - Notes: [[Java 17 LTS Overview|Java 17]] § pattern/switch · [[../02_OOP/00 - OOP Overview|OOP Overview]] · [[../02_OOP/Polymorphism|Polymorphism]]
  - Goal: `if (o instanceof String s)`, `switch` expr with `->` and `yield`, flow scoping

- [ ] **Day 10 — OOP Pillars + Inheritance Types** (60–90m) `--release 17`
  - Notes: [[../02_OOP/Inheritance|Inheritance]] · [[../02_OOP/Inheritance/Single Inheritance|Single]] · [[../02_OOP/Inheritance/Multiple Inheritance|Multiple]] · [[../01_Core-Java/Classes|Classes]]
  - Goal: 5 inheritance types, diamond via interfaces, `non-sealed`

- [ ] **Day 11 — Collections 11→17 Deep Dive** (60–90m) `--release 17`
  - Notes: [[../03_Collections/Collection|Collection]] · [[../03_Collections/List/ArrayList|ArrayList]] · [[../03_Collections/Set/HashSet|HashSet]] · [[../03_Collections/Map|Map]]
  - Goal: `ArrayList` 1.5×, `HashSet` via `HashMap`, `TreeSet` ordering

## Phase 4 — Java 21 LTS Leap (Weeks 6–7) — *The concurrency LTS*

- [ ] **Day 12 — Sequenced Collections & Record/Switch Patterns** (60–90m) `--release 21`
  - Notes: [[../09_Java-21-LTS/02 Sequenced Collections|Sequenced 431]] · [[../09_Java-21-LTS/03 Record Patterns|Record Patterns 440]] · [[../09_Java-21-LTS/04 Pattern Matching for Switch|Switch Patterns 441]] · [[../08_Modern-Java/03 Pattern Matching|Pattern Matching]]
  - Goal: `getFirst()/reversed()`, `case Point(int x,int y)`, exhaustive sealed switch

- [ ] **Day 13 — Virtual Threads (JEP 444) — pinning trap on 21** (60–90m) `--release 21`
  - Notes: [[../09_Java-21-LTS/01 Virtual Threads|Virtual Threads 444]] · [[../04_Concurrency/Threads|Threads]] · [[../04_Concurrency/Executor Framework|Executor]]
  - Goal: `newVirtualThreadPerTaskExecutor()`, **synchronized pins on 21** → use `ReentrantLock`; `spring.threads.virtual.enabled=true`

- [ ] **Day 14 — Unnamed Patterns, String Templates (removed!), Instance Main** (60–90m) `--release 21`
  - Notes: [[../09_Java-21-LTS/06 Unnamed Patterns and Variables|Unnamed 443]] · [[../09_Java-21-LTS/05 String Templates|String Templates 430]] · [[../09_Java-21-LTS/07 Unnamed Classes and Instance Main|Instance Main 445]]
  - Goal: `Point(_, int y)`, `STR."\{x}"` **preview removed in 23** — say `formatted()`

- [ ] **Day 15 — Generational ZGC + FFM** (60–90m) `--release 21`
  - Notes: [[../09_Java-21-LTS/08 Generational ZGC|ZGC 439]] · [[../09_Java-21-LTS/09 Foreign Function and Memory API|FFM 442]] · [[../01_Core-Java/JVM Memory Model|JVM]]
  - Goal: `-XX:+UseZGC` generational by default on 21; `Arena`/`MemorySegment` safe `Unsafe`

- [ ] **Day 16 — Queue/Concurrent Collections + Review** (60–90m) `--release 21`
  - Notes: [[../03_Collections/Queue|Queue]] · [[../04_Concurrency/Concurrent Collections|Concurrent Collections]] · [[LTS Evolution 8 to 25|LTS Evolution]]
  - Buffer: 17→21 delta flashcards; `find Java/09_Java-21-LTS -name "*.md" | xargs grep -l "Q:"`

## Phase 5 — Java 25 Delta (Week 8) — *What changed since 21*

- [ ] **Day 17 — ScopedValue Final (506) vs ThreadLocal** (60–90m) `--release 25`
  - Notes: [[Whats New in Java 25|Whats New - ScopedValue]] §1 · [[../08_Modern-Java/06 ScopedValue|ScopedValue]] · [[../04_Concurrency/Locks and Synchronizers|Locks]]
  - Goal: `ScopedValue.where(...).run()` immutable, auto-inherit to virtual forks

- [ ] **Day 18 — Compact Headers + Flexible Constructors + Module Imports** (60–90m) `--release 25`
  - Notes: [[Whats New in Java 25|Whats New]] §3,5,6 · [[../08_Modern-Java/08 Compact Object Headers and Performance|Compact Headers 450]] · [[../08_Modern-Java/07 Flexible Constructors and Module Imports|Flexible 513/511]] · [[../01_Core-Java/JVM Memory Model|JVM]]
  - Goal: `-XX:+UseCompactObjectHeaders` 128→64 bits; statements before `super()`; `import module java.base`

- [ ] **Day 19 — Structured Concurrency Preview (505) + JEP 491 Fix** (60–90m) `--release 25 --enable-preview`
  - Notes: [[Whats New in Java 25|Whats New]] §2 · [[../08_Modern-Java/05 Virtual Threads - Loom|Virtual Threads - JEP 491]] · [[../04_Concurrency/Threads|Threads]] § StructuredTaskScope
  - Goal: `ShutdownOnFailure` vs `ShutdownOnSuccess`, **`synchronized` no longer pins since 24/25**

- [ ] **Day 20 — Spring Boot 3.5 + Virtual Threads + Performance** (60–90m) `--release 25`
  - Notes: [[../05_Spring/Spring Framework|Spring]] · [[../05_Spring/Spring Boot|Boot]] · [[../05_Spring/Spring Transaction|TX]] · [[Whats New in Java 25|Whats New]] § JEP 491
  - Goal: Boot 3.5 auto-config, JPA N+1, `@Transactional` self-invocation pitfall, headers + ZGC

## Phase 6 — Backend, Patterns, DSA, Mocks (Weeks 9–10)

- [ ] **Day 21 — Spring Core/MVC/DI** (60–90m)
  - Notes: [[../05_Spring/Spring Core|Spring Core]] · [[../05_Spring/Spring MVC|MVC]] · [[../05_Spring/Dependency Injection|DI]]
  - Goal: IoC lifecycle, dispatch flow, constructor vs setter DI

- [ ] **Day 22 — Spring Data JPA + Security** (60–90m)
  - Notes: [[../05_Spring/Spring Data JPA|Data JPA]] · [[../05_Spring/Spring Transaction|TX]] · [[../05_Spring/Spring Security|Security]]
  - Goal: query methods, `Propagation`, filter chain, JWT

- [ ] **Day 23 — Design Patterns Creational + Structural** (60–90m)
  - Notes: [[../06_Design-Patterns/Creational/Singleton|Singleton]] · [[../06_Design-Patterns/Creational/Factory Method|Factory]] · [[../06_Design-Patterns/Structural/Adapter|Adapter]] · [[../06_Design-Patterns/Structural/Proxy|Proxy]]
  - Goal: Factory vs Abstract Factory; where Spring uses Proxy/Decorator

- [ ] **Day 24 — Design Patterns Behavioral** (60–90m)
  - Notes: [[../06_Design-Patterns/Behavioral/Observer|Observer]] · [[../06_Design-Patterns/Behavioral/Strategy|Strategy]] · [[../06_Design-Patterns/Behavioral/Command|Command]]
  - Goal: Strategy vs State vs Template; whiteboard 3 patterns

- [ ] **Day 25 — DSA Core** (60–90m)
  - Notes: [[../07_DSA/Array|Array]] · [[../07_DSA/Heap|Heap]] · [[../07_DSA/HashMap|HashMap]] · [[../07_DSA/Trees|Trees]] · [[../07_DSA/Graph|Graph]]
  - Goal: heap, HashMap internals + compact headers, BFS/DFS

- [ ] **Day 26 — Coding Patterns: Array + LinkedList** (60–90m)
  - Notes: [[../../Coding Patterns/01_Array/01 - Prefix Sum|Prefix Sum]] · [[../../Coding Patterns/01_Array/02 - Two Pointers|Two Pointers]] · [[../../Coding Patterns/02_LinkedList/01 - Fast and Slow Pointers|Fast/Slow]]
  - Goal: 2 problems per pattern

- [ ] **Day 27 — Coding Patterns: Trees/Graphs + DP + Mock 1** (90m)
  - Notes: [[../../Coding Patterns/05_Trees_Graphs/02 - DFS|DFS]] · [[../../Coding Patterns/05_Trees_Graphs/03 - BFS|BFS]] · [[../../Coding Patterns/07_Backtracking_DP/02 - Dynamic Programming|DP]] · [[../99_Revision/Interview Questions|Interview Qs]]
  - Goal: Dijkstra, memo vs tabulation; timed mock 45+15

- [ ] **Day 28 — Mock 2 + SR Sweep** (90m)
  - Notes: [[../99_Revision/Interview Questions|Interview Qs]] · [[Whats New in Java 25|Whats New]] · [[Interview Strategy|Strategy]] · [[LTS Evolution 8 to 25|LTS Evolution]]
  - Goal: Full-stack mock (Core + 17 + 21 + 25 + Spring + DSA), fill SR queue

- [ ] **Buffer — Overdue sweep** (anytime)
  - Open [[Dashboard]] → fix all `>7d` stale + SR Due, set `reviewed: 2026-09-XX`

---

## Tracker — How to know you're done

- Each day's checkbox → `TASK` progress bar at top.
- Each note's `completed: true` → [[../README|Java MOC]] folder bars + [[Dashboard]].
- `reviewed: 2026-09-XX` → [[Dashboard]] urgency (🟢 ≤7d, 🟡 7–14d, 🔴 >14d/never).
- LTS coverage: search `lts` tag — `WHERE contains(file.tags, "lts")` across vault.

*Category: overview • lts*
