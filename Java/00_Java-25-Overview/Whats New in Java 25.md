---
title: "Whats New in Java 25"
category: overview
tags: [java25, jep, interview, whats-new]
created: 2026-09-03
completed: false
---

# Whats New in Java 25 — Interview Cheat Sheet

> Part of [[README|00 Overview]] • `overview` • Every LTS-relevant feature 8 → 25 with interview angle

## TL;DR for interviews

> Java 25 = Java 21 LTS **plus**: **ScopedValue (final)**, **Structured Concurrency (preview JEP 505)**, **compact object headers (JEP 450)**, **primitive types in patterns (JEP 507)**, **flexible constructor bodies (JEP 513)**, **module import declarations (JEP 511)**, plus refinements to virtual threads (JEP 491 — `synchronized` no longer pins). Everything below 8→21 is still asked; 21→25 is the delta.

## Must-Know Timeline (8 → 25)

| Version | Feature | JEP | Interview Q |
|---------|---------|-----|-------------|
| **8** | Lambdas, Streams, Optional, Date/Time | 126,150 | SAM, intermediate vs terminal |
| **9** | Modules, `List.of`, `jshell` | 261 | Module vs package |
| **10** | `var` | 286 | `var` limits |
| **14–16** | `record`, `sealed`, pattern `instanceof` | 359,360,394,397 | `record` vs class vs Lombok |
| **17 LTS** | Sealed final, pattern switch (preview) | 409 | `sealed` permits |
| **21 LTS** | **Virtual threads**, **SequencedCollection**, pattern switch + record patterns (final), String Templates (preview) | 444,431,440,441,430 | virtual vs platform, pinning? |
| **22** | `ScopedValue` (preview), Stream Gatherers (preview), Class-File API | 464,461,447 | ScopedValue vs ThreadLocal |
| **23** | Markdown javadoc, primitive patterns (preview), `ScopedValue` 2nd preview | 467,455,464 | — |
| **24** | **JEP 491** `synchronized` no longer pins virtual threads | 491 | "Does synchronized pin?" → No since 24 |
| **25 LTS** | **ScopedValue final (506)**, **Structured Concurrency preview (505)**, **Compact Headers (450)**, **Primitive patterns (507)**, **Flexible constructors (513)**, **Module imports (511)** | 506,505,450,507,513,511 | See below |

## Java 25 — The 6 You Must Explain Whiteboard-Style

### 1. ScopedValue (JEP 506, final) — replaces ThreadLocal

```java
static final ScopedValue<String> REQ_ID = ScopedValue.newInstance();
void handle(String id) {
    ScopedValue.where(REQ_ID, id).run(() -> {
        // visible to child virtual threads + StructuredTaskScope forks
        log(REQ_ID.get());
    });
    // outside: REQ_ID.isBound()==false — no leak, no remove()
}
```

**Vs:** `ThreadLocal` = mutable, leaks with millions of virtual threads, `remove()` required. `ScopedValue` = immutable, bounded by scope, inherited automatically, cheaper.

### 2. Structured Concurrency — StructuredTaskScope (JEP 505, preview)

```java
// javac --enable-preview --release 25
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
    var u = scope.fork(() -> fetchUser(id));
    var o = scope.fork(() -> fetchOrder(id));
    scope.join(); scope.throwIfFailed();
    return u.get() + o.get();
}
```

Types: `ShutdownOnFailure` (all required) vs `ShutdownOnSuccess<T>` (first wins). Failures propagate, siblings cancelled, scope enforces structure (try-with-resources).

### 3. Flexible Constructor Bodies (JEP 513) — statements before `super()`/`this()`

```java
class PositivePoint extends Point {
    PositivePoint(int x, int y) {
        if (x < 0 || y < 0) throw new IllegalArgumentException(); // allowed in 25!
        super(x, y);
    }
}
```

Before 25: `super()`/`this()` had to be first statement — validation required static helpers. Now: validate/compute before super.

### 4. Primitive Types in Patterns (JEP 507) — `switch` over primitives with patterns

```java
String fmt(Object o) {
    return switch (o) {
        case int i when i > 0 -> "pos " + i;
        case long l -> "long " + l;
        case double d -> "double " + d;
        default -> "other";
    };
}
```

No more boxing to use pattern matching over `int`/`long`/`double`.

### 5. Module Import Declarations (JEP 511) — `import module java.base`

```java
import module java.base; // imports all public types from java.base
// vs import java.util.* per package
```

Concise for small programs/scripts; interview: know it exists, not for large codebases (explicit imports preferred).

### 6. Compact Object Headers (JEP 450) — 64-bit Lilliput

Shrinks object header 128→64 bits (`-XX:+UseCompactObjectHeaders`). More objects per cache line, ~10–20% heap saving on some workloads. Enabled via flag in 25 (default in future LTS). Interview: "How to reduce memory footprint on 25?" → compact headers + records.

### + JEP 491 (since 24, essential for 25 interviews)

`synchronized` **no longer pins** virtual thread carrier. Before 24: `synchronized` + blocking IO pinned carrier → throughput collapse. Since 24: unmounts like `ReentrantLock`. Still prefer `ReentrantLock` when you need timeouts/interrupts.

## Vs Tables

**Virtual Thread vs Platform Thread**

|  | Platform | Virtual (Java 21/25) |
|--|----------|---------------------|
| Cost | OS thread (~1MB) | ~KBs, millions per JVM |
| Creation | `Thread.ofPlatform().start()` | `Thread.ofVirtual().start()` or `newVirtualThreadPerTaskExecutor()` |
| Blocking | Blocks OS thread | Parks virtual thread, carrier reused |
| Pinning (25) | N/A | `synchronized` no longer pins (JEP 491) |
| Use | CPU-bound, JNI | IO-bound servers (default on 25) |

**ScopedValue vs ThreadLocal**

|  | ThreadLocal | ScopedValue (25) |
|--|-------------|------------------|
| Mutability | mutable `set/remove` | immutable binding per scope |
| Inheritance | manual `InheritableThreadLocal` | auto to child virtual/structured tasks |
| Leaks | yes without `remove()` | no — scope exit clears |
| Perf with Loom | expensive | cheap |

## Quick Check — Can you answer?

- [ ] Why does `synchronized` no longer pin in Java 25?
- [ ] ScopedValue vs ThreadLocal — when to use which?
- [ ] `record` vs `class` vs `record` with compact constructor?
- [ ] `SequencedCollection.getFirst()` vs `list.get(0)`?
- [ ] What does `-XX:+UseCompactObjectHeaders` do?

## Related

- [[Java 25 Roadmap]] • [[../08_Modern-Java/README|08 Modern Java]] • [[../04_Concurrency/Threads|Threads]] • [[Interview Strategy]]

---
*Category: overview • java25*
