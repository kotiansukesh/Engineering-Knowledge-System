---
title: "Compact Object Headers and Performance"
category: Modern-Java
tags: [java25, jep450, performance, jvm]
created: 2026-09-03
completed: false
---

# Compact Object Headers & Performance — Java 25 (JEP 450)

> **JEP 450 — Compact Object Headers (Lilliput)**: shrinks 64-bit object header from **128 → 64 bits** (16→8 bytes). Enabled via `-XX:+UseCompactObjectHeaders` in Java 25 (default in future). More objects per cache line, ~10–20% heap reduction on object-heavy workloads.

## Why it matters

Heap is often header-heavy (small objects, `HashMap` nodes, `record` instances). Halving header doubles object density, improves GC and cache.

## When to use / NOT

| Use | Avoid |
|-----|-------|
| Object-heavy heaps (caches, graphs, DTO records) | Need `UseLargePages` tricks that conflict — test first |
| Latency-sensitive with ZGC/G1 | JNI that assumes header layout (rare) |

## Runnable / Flags — Java 25

```bash
# Run with compact headers (Java 25 opt-in)
java -XX:+UseCompactObjectHeaders -Xlog:gc* -jar app.jar

# Compare heap
java -XX:-UseCompactObjectHeaders -XX:+PrintCompressedOopsMode -jar app.jar
# vs
java -XX:+UseCompactObjectHeaders -jar app.jar

# Verify
java -XX:+UseCompactObjectHeaders -Xlog:gc+heap=info -version
```

```java
// Compact headers (JEP 450) — 64-bit headers, cache locality
record Node(int id, String label) {}
void manyNodes() {
    var nodes = new java.util.ArrayList<Node>();
    for (int i=0;i<1_000_000;i++) nodes.add(new Node(i, "n"+i));
}
```

## How it compares

| Headers | Size | Heap | Status |
|---------|------|------|--------|
| Classic | 128 bits (16B) + klass | baseline | default ≤24 |
| Compact (JEP 450) | 64 bits (8B) | -8B/object → 10–20% | opt-in 25, default future |
| + CompressedOops / Compressed Class Pointers | on | on | keep on |

## Interview Q&A

**Q: What does `-XX:+UseCompactObjectHeaders` do?**  
Halves object header, more objects per line, lower heap/GC.

**Q: Does it change GC choice?**  
No — works with G1, ZGC, Shenandoah; measure with `-Xlog:gc*`.

**Q: Record + compact headers why paired?**  
Records are small, immutable — header dominates size; compaction helps most there.

## Pitfalls

- Not default in 25 — you must opt in; future LTS will default. Don't claim it's auto.
- Native agents assuming header size — rare but test.

## Related

- [[05 Virtual Threads - Loom|Virtual Threads]] • [[06 ScopedValue]] • [[../01_Core-Java/JVM Memory Model|JVM Memory Model]] • [[04 Sequenced Collections]]

---
*Category: Modern-Java • java25*
