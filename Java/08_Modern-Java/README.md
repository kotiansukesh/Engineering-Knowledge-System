---
title: "Modern Java"
category: "Modern-Java"
tags: [java, java25, modern-java, records, virtual-threads]
created: 2026-09-03
pattern: 0
difficulty: Medium
completed: false
reviewed:
sr-due:
---# 08 Modern Java , Java 8 → 25

> What's new from lambdas to Loom, SequencedCollection, records, sealed, pattern matching, ScopedValue, compact headers. All runnable on **Java 25 LTS**. Part of [[../README|Java MOC]].
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "Java/08_Modern-Java"
WHERE file.name != "README"
SORT file.name ASC
```

## Progress

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done", reviewed as "Last Reviewed"
FROM "Java/08_Modern-Java"
WHERE category
SORT file.name ASC
```

## The 8 Notes

| # | Note | Version | Interview must-know |
|---|------|---------|---------------------|
| 1 | [[01 Records]] | 16/21 | `record` vs class, compact constructor, JPA gotcha |
| 2 | [[02 Sealed Classes]] | 17 | `sealed permits`, exhaustive `switch` |
| 3 | [[03 Pattern Matching]] | 21/25 | `instanceof` pattern, record patterns, **primitive patterns (JEP 507)** |
| 4 | [[04 Sequenced Collections]] | 21 | `getFirst()/getLast()/reversed()` |
| 5 | [[05 Virtual Threads - Loom]] | 21/25 | `newVirtualThreadPerTaskExecutor`, **JEP 491** no pinning |
| 6 | [[06 ScopedValue]] | 25 (JEP 506) | `ScopedValue` vs `ThreadLocal` |
| 7 | [[07 Flexible Constructors and Module Imports]] | 25 (JEP 513, 511) | statements before `super()` |
| 8 | [[08 Compact Object Headers and Performance]] | 25 (JEP 450) | `-XX:+UseCompactObjectHeaders` |

## How to use

- Need the 60-sec answer? → [[../00_Java-25-Overview/Whats New in Java 25|Whats New]].
- Deep dive? → open 01→08 in order (each is Intent → When/NOT → Code → Vs → Q&A).
- Interview? → Q&A at bottom of each note + [[../00_Java-25-Overview/Interview Strategy|Interview Strategy]].

[[../README|← Back to Java MOC]] • [[../99_Revision/Study Plan|Study Plan]] • [[../99_Revision/README|Revision]]

---
*Category: modern-java*
