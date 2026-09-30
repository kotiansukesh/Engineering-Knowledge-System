---
title: Generational ZGC , JEP 439 (Java 21)
category: Java/09_Java-21-LTS
tags:
- java21
- jep439
- zgc
- gc
- interview
created: 2026-09-03
completed: false
pattern: 9
difficulty: Medium
reviewed: "2026-09-29"
sr-due: "2026-10-06"
excalidraw: ''
source: ''
type: concept
---

## Why it Matters

Make ZGC viable as **default low-latency GC** without giving up throughput , young GC cheap, old GC rare.

## Diagram

```mermaid
flowchart TD
 O["new objects"] --> YOUNG["young generation<br/>cheap, frequent GC"]
 YOUNG -->|survivors| OLD["old generation<br/>rare GC, scans less"]
 YOUNG -->|die young (most)| DEAD["immediately reclaimable<br/>why generational pays off"]
 Z["-XX:+UseZGC on 21"] --> GEN["generational by default (JEP 439)<br/>sub-ms pauses, +30-50% throughput"]
 GEN --> CH["Java 25: compact headers (450)<br/>denser heap complements ZGC"]
```

## Code

```bash
java -XX:+UseZGC -Xmx4g -Xlog:gc* App
```

```java
// Java 25: programmatic ZGC config via command-line flags (no API yet)
// Compact Object Headers (JEP 450) complements ZGC: denser heap = fewer GC cycles
// Usage: java -XX:+UseZGC -XX:+ZGenerational -XX:+UseCompactObjectHeaders -Xmx4g App
public class ZgcConfigDemo {
    public static void main(String[] args) {
        var runtime = Runtime.getRuntime();
        long heap = runtime.maxMemory() / (1024 * 1024);
        System.out.println("Max heap: " + heap + " MB");
        System.out.println("ZGC Generational: " + isZgcGenerational());
    }
    static boolean isZgcGenerational() {
        String gc = java.lang.management.ManagementFactory.getGarbageCollectorMXBeans()
            .stream().map(b -> b.getName()).filter(n -> n.contains("ZGC")).findFirst().orElse("none");
        return gc.contains("Generational");
    }
}
```

## When to use / NOT

| Use | Avoid |
|-----|-------|
| Low-latency services, <10ms pause SLO, 8GB+ heap | Tiny heaps (<1GB) , Serial/G1 simpler |

## Trade-offs

- ✅ Sub-ms pauses **and** +30-50% throughput over non-generational ZGC - the low-latency default on 21+.
- ✅ Young GC scans far less heap (most objects die young); old GC runs rarely.
- ❌ Overkill on small heaps (<1GB): Serial or G1 are simpler and cheaper.
- ❌ Needs heap sizing (`-Xmx`) and `ZAllocationSpikeTolerance` tuning for bursty allocation.

## Vs

| GC | Pause | Throughput | Use |
|----|-------|------------|-----|
| **G1** | ~50-200ms | high | default, balanced |
| **ZGC non-gen (pre-21)** | ~1ms | lower (scan all) | latency only |
| **Generational ZGC (21)** | ~1ms | +30-50% vs non-gen | **default for low-latency on 21+** |
| **Shenandoah** | ~1ms | similar | alternative low-latency |

## Pitfalls

- Expecting generational flag on 17 , it's 21+ only.
- Not sizing `Xmx` + `ZAllocationSpikeTolerance` for burst.

## Interview Q&A

**Q: Why generational?**
Most objects die young , young-gen GC scans less, promotes survivors, old GC rarely.

**Q: Flag on 21 vs 25?**
21: `-XX:+UseZGC` enables generational by default (JEP 439). 25: same; compact headers (JEP 450) complements ZGC by denser heap.

**Q: How to pick G1 vs ZGC?**
SLO: need <10ms → ZGC; need max throughput → G1; >32GB + low pause → ZGC.

: Why generational?:: Most objects die young , young-gen GC scans less, promotes survivors, old GC rarely. **Q: Flag on 21 vs 25?** 21: `-XX:+UseZGC` enables generational by default (JEP 439). 25: same; compact headers (JEP 450) complements ZGC by denser heap. **Q: How to pick G1 vs ZGC?** SLO: need <10ms → ZGC; need max throughput → G1; >32GB + low pause → ZGC. #flashcard

## Related

- 01 Virtual Threads • 09 Foreign Function and Memory API • [[Java/01_Core-Java/JVM Memory Model|JVM Memory Model]]

---
*Category: java21*

# Generational ZGC , JEP 439 (Java 21 LTS)

> ZGC gains **generations** (young/old) , keeps sub-ms pauses while doubling throughput for generational workloads.

# 21 generational is default when UseZGC on; disable via -XX:-ZGenerational (if need non-generational)

java -XX:+UseZGC -XX:+ZGenerational -XX:+ZUncommit -Xlog:gc,gc+heap=info App
```