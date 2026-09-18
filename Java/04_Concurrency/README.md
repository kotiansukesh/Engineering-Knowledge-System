---
title: "Concurrency"
type: folder-MOC
tags: [MOC, 04_concurrency]
---
# Concurrency

> Threads, virtual threads (Loom), executors, locks, atomics & concurrent collections , slimmed to gold standard: **Summary → Why it matters → Lifecycle (mermaid) → Runnable Java 25 → How it compares → Q&A → Pitfalls**. | Part of [[README|Java MOC]]
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "Java/04_Concurrency"
WHERE file.name != "README"
SORT file.name ASC
```

## Progress

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done"
FROM "Java/04_Concurrency"
WHERE category
SORT file.name ASC
```

## The 7 Notes , What Lives Here

| # | Note | Core diagram / hook | Interview 60-sec |
|---|------|---------------------|------------------|
| 1 | [[Threads]] | `stateDiagram-v2` thread lifecycle + `StructuredTaskScope` flowchart | Virtual vs platform, **JEP 491 no pinning**, ScopedValue over ThreadLocal |
| 2 | [[Executor Framework]] | Executor-choice flowchart (IO→virtual, CPU→fixed, delayed→scheduled) | `newVirtualThreadPerTaskExecutor()` + try-with-resources |
| 3 | [[CompletableFuture]] | Async pipeline flowchart (`supplyAsync → thenApply → thenCompose → handle`) | `thenApply` vs `thenCompose`, always pass a virtual executor |
| 4 | [[Locks and Synchronizers]] | Lock-choice flowchart (`synchronized` vs `ReentrantLock` vs `ReadWriteLock`) | Timeouts/fairness → `Lock`; simple invariants → `synchronized` (safe since 24) |
| 5 | [[Atomics and Volatile]] | CAS loop, `AtomicLong` vs `LongAdder` | `volatile` = visibility only; high contention → `LongAdder` |
| 6 | [[Concurrent Collections]] | CHM vs synchronizedMap, BlockingQueue variants | `computeIfAbsent`, weakly-consistent iterators, N+1-free caches |
| 7 | [[Cheat Sheet]] | Lifecycle mermaid + JMM happens-before one-liners | Last-night revision |

> **Java 25 defaults:** every note assumes `Executors.newVirtualThreadPerTaskExecutor()` for IO, `StructuredTaskScope` (preview, JEP 505) for scoped fan-out, `ScopedValue` (JEP 506) for context. Deep dives: [[../08_Modern-Java/05 Virtual Threads - Loom|08 , Virtual Threads]] · [[../08_Modern-Java/06 ScopedValue|08 , ScopedValue]].

## How to use

- **New to concurrency?** Read [[Threads]] → [[Executor Framework]] → [[Locks and Synchronizers]] → rest in order.
- **Interview?** `grep "Q:" Java/04_Concurrency` , every Q&A is a flashcard; `Threads` SR block is spaced repetition.
- **Practice:** LeetCode 1114 / 1115 / 1116 / 1226 linked at the bottom of each note.

[[README|← Back to Java MOC]]
