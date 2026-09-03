---
title: "Generational ZGC — JEP 439 (Java 21)"
category: java21
tags: [java21, jep439, zgc, gc, interview]
created: 2026-09-03
completed: false
---

# Generational ZGC — JEP 439 (Java 21 LTS)

> ZGC gains **generations** (young/old) — keeps sub-ms pauses while doubling throughput for generational workloads.

## Intent

Make ZGC viable as **default low-latency GC** without giving up throughput — young GC cheap, old GC rare.

## When to Use / NOT

| Use | Avoid |
|-----|-------|
| Low-latency services, <10ms pause SLO, 8GB+ heap | Tiny heaps (<1GB) — Serial/G1 simpler |

## Runnable Java 21

```bash
java -XX:+UseZGC -Xmx4g -Xlog:gc* App
# 21 generational is default when UseZGC on; disable via -XX:-ZGenerational (if need non-generational)
java -XX:+UseZGC -XX:+ZGenerational -XX:+ZUncommit -Xlog:gc,gc+heap=info App
```

```java

```

## How It Compares

| GC | Pause | Throughput | Use |
|----|-------|------------|-----|
| **G1** | ~50–200ms | high | default, balanced |
| **ZGC non-gen (pre-21)** | ~1ms | lower (scan all) | latency only |
| **Generational ZGC (21)** | ~1ms | +30–50% vs non-gen | **default for low-latency on 21+** |
| **Shenandoah** | ~1ms | similar | alternative low-latency |

## Interview Q&A

**Q: Why generational?**  
Most objects die young — young-gen GC scans less, promotes survivors, old GC rarely.

**Q: Flag on 21 vs 25?**  
21: `-XX:+UseZGC` enables generational by default (JEP 439). 25: same; compact headers (JEP 450) complements ZGC by denser heap.

**Q: How to pick G1 vs ZGC?**  
SLO: need <10ms → ZGC; need max throughput → G1; >32GB + low pause → ZGC.

## Pitfalls

- Expecting generational flag on 17 — it's 21+ only.
- Not sizing `Xmx` + `ZAllocationSpikeTolerance` for burst.

## Related

- [[01 Virtual Threads]] • [[09 Foreign Function and Memory API]] • [[../01_Core-Java/JVM Memory Model|JVM Memory Model]]

---
*Category: java21*
