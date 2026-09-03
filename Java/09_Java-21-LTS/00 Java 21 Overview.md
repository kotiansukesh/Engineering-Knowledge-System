---
title: "Java 21 Overview — LTS Map"
category: java21
tags: [java21, lts, overview, jep, interview]
created: 2026-09-03
completed: false
---

# Java 21 Overview — LTS Map (17 → 21 → 25)

> Part of [[README|09 Java 21 LTS]] • `java21` • The LTS interviewers actually test — 17→21 is the leap, 21→25 is the delta.

## Intent

Place Java 21 in context: **Java 17 LTS → 21 LTS → 25 LTS**. Know what became **final** in 21 so you can answer "what's new in 21?" and "what's new in 25 vs 21?" crisply.

## JEP Map — What ships by LTS

| LTS | Final (must know) | Preview/Incubator in 21 (know it exists) | Removed/Changed in 25 |
|-----|-------------------|------------------------------------------|-----------------------|
| **17** | `sealed` (409), `record` final, text blocks | pattern switch preview | — |
| **21** | **Virtual Threads 444**, **Sequenced Collections 431**, **Record Patterns 440**, **Pattern Switch 441**, **Generational ZGC 439** | String Templates 430, Unnamed Classes 445, Scoped Values 446, Foreign Memory 442 (3rd preview) | String Templates **removed** in 23, replaced by Template processors |
| **25** | **ScopedValue 506 final**, **Compact Headers 450** (opt-in), plus Primitive Patterns 507, Flexible Constructors 513, Module Imports 511, **JEP 491** no pinning (24) | Structured Concurrency 505 | — |

## 60-sec answer — "What's new in Java 21?"

> "Java 21 as LTS finalizes **virtual threads** (JEP 444) for million-thread concurrency, **Sequenced Collections** for uniform `getFirst/getLast/reversed`, **record patterns** and **pattern matching for switch** for exhaustive sealed hierarchies, and **generational ZGC**. Previews to mention: String Templates, unnamed classes, scoped values, and Foreign Memory API — and note that **on 21, `synchronized` still pins virtual threads** (fixed in 24/25 by JEP 491)."

## When to use 21 knowledge

| Use | Avoid |
|-----|-------|
| Whiteboard virtual thread vs platform, pinning caveat | Claiming scoped values final — in 21 it's preview JEP 446, final in 25 |
| Sequenced `List.getFirst()` in live code | Using `STR."\{x}"` in prod — it never shipped; mention it as preview |

## Runnable — verify you are on 21

```bash
java --version   # → 21.x
javac --release 21 Main.java && java Main
# Virtual thread hello on 21:
```

```java
// Java 21 LTS — virtual threads, sequenced collections, record patterns
try (var exec = java.util.concurrent.Executors.newVirtualThreadPerTaskExecutor()) {
    var f = exec.submit(() -> "hello virtual on 21");
    System.out.println(f.get());
}
```

## Interview Q&A

**Q: 21 vs 25 for ScopedValue?**  
21: `ScopedValue` preview (446), `ThreadLocal` still common. 25: `ScopedValue` final (506) — `ThreadLocal` anti-pattern for Loom.

**Q: Pinning?**  
21: `synchronized` + blocking IO pins carrier → use `ReentrantLock`. 25: JEP 491 removed pinning — `synchronized` safe.

**Q: Biggest trap?**  
String Templates — interviewers ask `STR."..."` ; answer: preview in 21, **withdrawn in 23**, don't ship it. Mention `StringBuilder`/`format` instead.

## Pitfalls

- Mixing 21 preview APIs (`--enable-preview`) in production code without flag.
- Claiming compact headers final in 21 — it's JEP 450, **25 opt-in**.

## Related

- [[01 Virtual Threads]] • [[02 Sequenced Collections]] • [[03 Record Patterns]] • [[08 Generational ZGC]] • [[../08_Modern-Java/README|08 Modern 21→25 delta]]

---
*Category: java21*
