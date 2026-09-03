---
title: "Interview Strategy — Java 25"
category: overview
tags: [java25, interview, strategy]
created: 2026-09-03
completed: false
---

# Interview Strategy — Java 25

> Part of [[README|00 Overview]] • `overview` • How to answer Java 25 questions and crack backend interviews

## The 60-second "What's new in Java 25?" answer

> "Java 25 is the LTS after 21. On top of 21's **virtual threads, SequencedCollection, record/pattern switch**, Java 25 finalizes **ScopedValue (JEP 506)** as the ThreadLocal replacement for Loom, introduces **Structured Concurrency (JEP 505 preview)** via `StructuredTaskScope` for scoped fan-out, **compact object headers (JEP 450)** for memory, **flexible constructor bodies (JEP 513)**, **primitive patterns (JEP 507)**, and **module imports (JEP 511)**. Crucially, since Java 24 (JEP 491) `synchronized` no longer pins virtual threads, so you can use `synchronized` around IO safely."

Deliver in **STAR + code**: name JEP, show 5-line snippet, state tradeoff.

## Answer template (Intent → When/NOT → Code → Vs)

Every vault note follows this. In interview, use it:

1. **Intent** (10s): one-sentence definition.
2. **When / When NOT** (15s): 1 good, 1 bad case.
3. **Code** (20s): runnable Java 25 snippet.
4. **Vs** (15s): compare to alternative (`record` vs `class`, `ScopedValue` vs `ThreadLocal`).

## Topic → Killer question → One-liner

| Topic | Killer Q | One-liner |
|-------|----------|-----------|
| Virtual threads | Does `synchronized` pin? | No since 24 (JEP 491); on 21 it did |
| ScopedValue | Why not ThreadLocal with Loom? | TL leaks at millions of threads; SV is immutable + scope-bound + cheap |
| Records | When NOT to use record? | Mutable / JPA entity with lazy proxies / need inheritance |
| SequencedCollection | vs `list.get(0)`? | Works for List/Deque/LinkedHashSet; `.reversed()` too |
| Compact Headers | Heap saving? | 128→64 bit header, `-XX:+UseCompactObjectHeaders`, ~10–20% |
| Pattern matching | Primitive patterns? | JEP 507 — `case int i when i>0` without boxing |
| Flexible constructors | Before 24? | `super()` had to be first; now validate before super |
| Spring + Loom | Boot 3.5 + virtual threads? | `spring.threads.virtual.enabled=true`, Tomcat uses virtual threads |

## 30 Java 25 flashcards (tap to reveal in Dashboard.html)

Covered in `08_Modern-Java` + `04_Concurrency` — set `completed: true` per note to track.

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done"
FROM "Java/08_Modern-Java"
WHERE category
SORT file.name ASC
```

## Mock loop (weekly, 90 min)

1. **15 min** — pick 5 random `## Interview Q&A` via `99_Revision` dashboard.
2. **45 min** — code 1 DSA (Coding Patterns) + 1 concurrency snippet on paper.
3. **15 min** — explain a Java 25 feature whiteboard-style (record/Virtual/ScopedValue).
4. **15 min** — review pitfalls + mark `reviewed: YYYY-MM-DD`.

## Pitfalls interviewers hunt

- `new T()` / `T.class` with generics — erasure, won't compile.
- `- [ ]` tasks unchecked but claiming `completed: true` — dashboard exposes it.
- Claiming virtual threads for CPU-bound — use platform threads for CPU/JNI.
- `ThreadLocal` in virtual thread code — leak + JEP 506 question trap.

## Related

- [[Whats New in Java 25]] • [[../08_Modern-Java/README|08 Modern Java]] • [[Study Plan - Java 25]] • [[../99_Revision/README|99 Revision MOC]]

---
*Category: overview • java25*
