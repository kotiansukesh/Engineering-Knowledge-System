---
title: "Java Core Plan — 21 Days"
category: Revision
tags: [plan, java, revision]
created: 2026-09-02
updated: 2026-09-02
---

# Java Core Plan — 21 Days

> Focus: Core Java → OOP → Collections → Concurrency → DSA + Patterns. **No Spring** — do this first, then Spring Plan. Each day 60-90 min + 15 min SR.

```dataview
TABLE WITHOUT ID choice(completed, "✅", "⬜") as "Done", file.link as "Note", category as "Category", reviewed as "Reviewed"
FROM "Java"
WHERE category = "Core-Java" OR category = "DSA" OR category = "Concurrency" OR contains(file.path, "02_OOP") OR contains(file.path, "03_Collections")
SORT file.path ASC
LIMIT 5
```

## Week 1 — Foundations (Core Java)

### Day 1 — Language Basics ⏱ 60 min
- [ ] [[Classes]] • [[Interface]] • [[Method Overload]]
- [ ] [[Object Class]] • [[Wrapper Class]]
- Goal: classes vs interfaces, overload resolution

### Day 2 — Class Types ⏱ 60 min
- [ ] [[Abstract Class]] • [[Final Class]] • [[Immutable Class]] • [[Static Class]]
- [ ] [[Concrete Class]] • [[POJO Class]] • [[Singleton Class]]
- Goal: when to use abstract vs interface vs final

### Day 3 — Nested & Advanced Types ⏱ 60 min
- [ ] [[Nested Classes Overview|Nested Classes Overview]] • [[Nested Inner Class]] • [[Static Nested Class]] • [[Anonymous Inner Class]] • [[Method Local Inner Class]] • [[Anonymous Class]]
- Goal: nested vs inner, capture rules

### Day 4 — String, Annotations, Enums ⏱ 75 min
- [ ] [[String Handling]] • [[Annotations]] • [[Enums]]
- [ ] [[Exception Handling]] • [[Serialization]]
- Goal: pool/intern, retention, enum vs constants

### Day 5 — JVM + Modern Java 8+ ⏱ 75 min
- [ ] [[JVM Memory Model]] • [[Generics]] • [[Lambdas and Functional Interfaces]] • [[Streams API]] • [[Optional]]
- [ ] [[Date and Time API]] • [[IO and NIO]]
- Goal: heap/stack, PECS, streams collectors

### Day 6 — Review + Flashcards ⏱ 45 min
- [ ] Re-do Day 1-5 SR queue (`#flashcard`)
- [ ] 1 mock Q per note

## Week 2 — OOP + Collections

### Day 7 — OOP Pillars ⏱ 60 min
- [ ] [[00 - OOP Overview]] • [[Abstraction]] • [[Encapsulation]] • [[Polymorphism]]
- Goal: 4 pillars + SOLID

### Day 8 — Inheritance ⏱ 60 min
- [ ] [[Inheritance]] • [[Single Inheritance]] • [[Multilevel Inheritance]] • [[Hierarchical Inheritance]] • [[Multiple Inheritance]] • [[Hybrid Inheritance]]
- Goal: diamond via interfaces, sealed

### Day 9 — Collections Core ⏱ 60 min
- [ ] [[Collection]] • [[List]] • [[Map]] • [[Queue]] • [[Set]]
- Goal: hierarchy, ordered/duplicate/null

### Day 10 — List & Set Impl ⏱ 75 min
- [ ] [[ArrayList]] • [[LinkedList]] • [[Vector]] • [[Stack]] • [[HashSet]] • [[TreeSet]] • [[Sorted Set]]
- Goal: ArrayList 1.5× vs Vector 2×, Sequenced

### Day 11 — Review + Cheat Sheet ⏱ 45 min
- [ ] [[01_Core-Java/Cheat Sheet|Core Cheat Sheet]] • [[02_OOP/Cheat Sheet|OOP Cheat Sheet]] • [[03_Collections/Cheat Sheet|Collections Cheat Sheet]]

## Week 3 — Concurrency + DSA

### Day 12 — Threads (Java 25) ⏱ 75 min
- [ ] [[Threads]] — lifecycle, 4 ways, JEP 491 (pinning fix)
- Goal: platform vs virtual

### Day 13 — Executors & Futures ⏱ 75 min
- [ ] [[Executor Framework]] • [[CompletableFuture]]
- Goal: `newVirtualThreadPerTaskExecutor()` + structured

### Day 14 — Locks & Atomics ⏱ 60 min
- [ ] [[Locks and Synchronizers]] • [[Atomics and Volatile]] • [[Concurrent Collections]]
- Goal: `ScopedValue` vs `ThreadLocal`

### Day 15 — DSA Fundamentals ⏱ 75 min
- [ ] [[Array]] • [[Linked List]] • [[Singly Linked List]] • [[Doubly Linked List]] • [[Stack]] • [[Queue]] • [[HashMap]] • [[Trees]] • [[Heap]] • [[Graph]]
- Goal: complexities, record Node, Compact Headers

### Day 16-18 — Coding Patterns (20) ⏱ 90 min/day
- [ ] Day 16: [[01 - Prefix Sum]] • [[02 - Two Pointers]] • [[03 - Sliding Window]] • [[04 - Frequency Counting]] • [[01 - Fast and Slow Pointers]] • [[02 - LinkedList In-place Reversal]]
- [ ] Day 17: [[01 - Monotonic Stack]] • [[02 - Top K Elements]] • [[01 - Overlapping Intervals]] • [[02 - Modified Binary Search]] • [[01 - Binary Tree Traversal]] • [[02 - DFS]] • [[03 - BFS]]
- [ ] Day 18: [[04 - Shortest Path]] • [[05 - Trie]] • [[01 - Matrix Traversal]] • [[01 - Backtracking]] • [[02 - Dynamic Programming]] • [[03 - Greedy]] • [[01 - Bit Manipulation]]

### Day 19 — Mock 1 ⏱ 90 min
- [ ] Random 10 from `Interview Questions.md`
- [ ] [[07_DSA/Cheat Sheet|DSA Cheat Sheet]] • [[Coding Patterns/Cheat Sheet|Patterns Cheat Sheet]]

### Day 20 — Mock 2 ⏱ 90 min
- [ ] Timed: 2 DSA patterns + 2 Core Q

### Day 21 — Final Review ⏱ 60 min
- [ ] SR overdue queue • weak folders

---
*Part of [[README|Java MOC]] • [[Spring Plan|Spring Plan →]] • [[30-Day Plan|Legacy Combined Plan]]*
