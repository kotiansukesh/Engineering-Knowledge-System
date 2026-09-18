---
title: "Java 21 LTS , Master"
type: folder-MOC
tags: [MOC, java21, lts, java]
---
# 09 Java 21 lts , Master

> **Java 21 LTS (Sep 2023)** , the LTS before 25. If you ace 21, 25 is a **delta** (ScopedValue final, Structured Concurrency preview, Compact Headers, Primitive Patterns, Flexible Constructors, Module Imports). Part of [[../README|Java MOC]].
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "Java/09_Java-21-LTS"
WHERE file.name != "README"
SORT file.name ASC
```

## Progress

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done", reviewed as "Last Reviewed"
FROM "Java/09_Java-21-LTS"
WHERE category
SORT file.name ASC
```

## The 10 Notes , Java 21 lts (JEPs you Will be Asked)

| # | Note | JEP | Interview 60-sec |
|---|------|-----|------------------|
| 0 | [[00 Java 21 Overview]] | , | 17→21→25 map, what interviewers test |
| 1 | [[01 Virtual Threads]] | 444 | `newVirtualThreadPerTaskExecutor()`, cheap threads, **but pinning on 21** |
| 2 | [[02 Sequenced Collections]] | 431 | `getFirst()/getLast()/reversed()` , unified `List/Set/Map` |
| 3 | [[03 Record Patterns]] | 440 | `case Point(int x,int y)` deconstruction |
| 4 | [[04 Pattern Matching for Switch]] | 441 | Exhaustive `switch` over sealed hierarchy, `when` guards |
| 5 | [[05 String Templates]] | 430 (preview) | `STR."\{x} + \{y}"` , **why it was removed in 23** |
| 6 | [[06 Unnamed Patterns and Variables]] | 443 | `case Point(_, int y)` + `var _ = sideEffect()` |
| 7 | [[07 Unnamed Classes and Instance Main]] | 445 (preview) | `void main(){}` , no `public static` boilerplate |
| 8 | [[08 Generational ZGC]] | 439 | Generational ZGC , `-XX:+UseZGC` now nursery/old |
| 9 | [[09 Foreign Function and Memory API]] | 442 (3rd preview) | `MemorySegment`, `Arena`, `Linker` , safe `sun.misc.Unsafe` successor |

> **Java 25 delta after this folder:** [[../08_Modern-Java/06 ScopedValue|ScopedValue final JEP 506]] vs preview JEP 446, [[../08_Modern-Java/05 Virtual Threads - Loom|JEP 491 no pinning]], [[../08_Modern-Java/08 Compact Object Headers and Performance|Compact Headers JEP 450]], [[../08_Modern-Java/03 Pattern Matching|Primitive Patterns JEP 507]], [[../08_Modern-Java/07 Flexible Constructors and Module Imports|Flexible Constructors JEP 513]].

## How to use

- **New to 21?** Read 00→09 in order , each is Why it matters → When/NOT → runnable `javac --release 21` → How it compares → Q&A.
- **Already know 21?** `00 Overview` then jump to [[../08_Modern-Java/README|08 Modern Java]] for 21→25 delta.
- **Interview?** `grep "Q:" Java/09_Java-21-LTS` , every Q&A is a flashcard.

[[../README|← Back to Java MOC]] • [[../00_Java-25-Overview/Whats New in Java 25|25 , Whats New]] • [[../99_Revision/Study Plan|Study Plan]]

---
*Category: java21*
