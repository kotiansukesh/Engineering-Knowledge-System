---
title: "Virtual Threads — JEP 444 (Java 21)"
category: java21
tags: [java21, jep444, loom, virtual-threads, interview]
created: 2026-09-03
completed: false
---

# Virtual Threads — JEP 444 (Java 21 LTS)

> Lightweight user-mode threads — `Thread.ofVirtual()` / `newVirtualThreadPerTaskExecutor()` — millions per JVM. **Java 21 caveat: `synchronized` still pins the carrier** (fixed in 24/25 by JEP 491).

## Intent

Scale IO-bound servers without pool tuning or reactive rewrite — block in virtual thread, carrier reused.

## When to Use / NOT

| Use | Avoid |
|-----|-------|
| HTTP/DB fan-out, 10k+ concurrent blocking tasks | CPU-bound tight loops — platform threads faster |
| `ReentrantLock` around IO (never pins) | `synchronized` around IO on 21 — pins → throughput collapse |

## Runnable Java 21 (`--release 21`)

```java
import java.util.concurrent.*;
import java.time.Duration;

void fanOut21() throws Exception {
    try (var exec = Executors.newVirtualThreadPerTaskExecutor()) {
        var f1 = exec.submit(() -> fetch("user"));
        var f2 = exec.submit(() -> fetch("order"));
        System.out.println(f1.get() + " " + f2.get());
    }
}
String fetch(String k) throws InterruptedException {
    Thread.sleep(Duration.ofMillis(100));
    return k;
}

ThreadFactory vf = Thread.ofVirtual().name("v-", 0).factory();
try (var exec = Executors.newThreadPerTaskExecutor(vf)) { /* ... */ }
// Counter21 — pinning caveat, ReentrantLock fix

class Counter21 {
    synchronized void incAndIO() throws InterruptedException {
        Thread.sleep(Duration.ofMillis(50));
    }
}
import java.util.concurrent.locks.ReentrantLock;
// CounterFixed21 — pinning caveat, ReentrantLock fix
class CounterFixed21 {
    private final ReentrantLock lock = new ReentrantLock();
    void incAndIO() throws InterruptedException {
        lock.lock(); try { Thread.sleep(Duration.ofMillis(50)); } finally { lock.unlock(); }
    }
}
```

## How It Compares — 21 vs 25

|  | Java 21 | Java 25 (with JEP 491) |
|--|---------|------------------------|
| `synchronized` + sleep/IO | **Pins** carrier | **Not pinned** (unmounts) |
| `ReentrantLock` + sleep/IO | Never pins | Never pins |
| `StructuredTaskScope` | Incubator (JEP 453) | Preview JEP 505 (`ShutdownOnFailure/Success`) |
| `ScopedValue` | Preview JEP 446 | Final JEP 506 |

## Interview Q&A

**Q: Does `synchronized` pin on Java 21?**  
Yes — virtual thread cannot unmount inside `synchronized`/`native` on 21. Use `ReentrantLock` for IO.

**Q: `ThreadLocal` with virtual threads on 21?**  
Expensive (millions × ThreadLocalMap) and leaks without `remove()`. 21 preview is `ScopedValue`; 25 final replaces it.

**Q: Spring Boot 3.2 + Java 21 virtual threads?**  
`spring.threads.virtual.enabled=true` (Boot 3.2+), Tomcat uses `newVirtualThreadPerTaskExecutor()`.

## Pitfalls

- Not closing executor — `try-with-resources` required (21).
- Copying `newFixedThreadPool(200)` mental model — virtual is `newVirtualThreadPerTaskExecutor()` (no size).

## Related

- [[02 Sequenced Collections]] • [[08 Generational ZGC]] • [[../08_Modern-Java/05 Virtual Threads - Loom|08 — 25 delta JEP 491]] • [[../04_Concurrency/Threads|04 Concurrency]]

---
*Category: java21*
