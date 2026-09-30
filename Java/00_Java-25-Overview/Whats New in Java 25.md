---
title: "What is New in Java 25"
category: "Java/00_Java-25-Overview"
tags: [java25, jep, lts, interview]
created: "2026-09-30"
completed: false
difficulty: "Medium"
reviewed: "2026-09-30"
sr-due: "2026-10-07"
type: concept
---

# What is New in Java 25

> Java 25 is the current LTS. Separate permanent features from previews and from changes that actually landed in earlier releases.

## The important distinction

Java 25 is not a single “Loom release”. Several important items are final, while Structured Concurrency and Stable Values remain preview features.

| JEP | Feature | Java 25 status | Why it matters |
|---|---|---|---|
| 506 | Scoped Values | Final | scoped, one-way context propagation; useful with virtual threads |
| 519 | Compact Object Headers | Product feature | smaller object headers can reduce memory footprint |
| 513 | Flexible Constructor Bodies | Final | allows validation/computation before constructor invocation |
| 511 | Module Import Declarations | Final | concise imports for small programs |
| 512 | Compact Source Files and Instance Main Methods | Final | simpler small programs and teaching examples |
| 507 | Primitive Types in Patterns | Preview | pattern matching involving primitive types |
| 505 | Structured Concurrency | Preview | structured task lifetime, joining and cancellation |
| 502 | Stable Values | Preview | lazily initialized state with at-most-once setting |

## Also know the Java 24 context

JEP 491 changed synchronized behavior for virtual threads in Java 24. It is therefore part of the Java 25 baseline story, but it is not a Java 25 feature.

## Scoped Values

ScopedValue is final in Java 25. It provides dynamically scoped, per-thread bindings that are bounded by the execution of a method and can be inherited by threads created through StructuredTaskScope.

```java
import java.lang.ScopedValue;

class RequestContext {
    static final ScopedValue<String> REQUEST_ID = ScopedValue.newInstance();

    static void handle(String id) {
        ScopedValue.where(REQUEST_ID, id).run(() -> log(REQUEST_ID.get()));
    }

    static void log(String id) {
        System.out.println("request=" + id);
    }
}
```

Use it for bounded, one-way context propagation. Do not describe it as a universal replacement for ThreadLocal: mutable thread-local state, framework compatibility, and unstructured lifetimes are different problems.

## Structured Concurrency

In Java 25, StructuredTaskScope is still a preview API and its API is based on StructuredTaskScope.open(...) and Joiner rather than the older ShutdownOnFailure/ShutdownOnSuccess examples found in earlier previews.

```java
// javac --enable-preview --release 25 Example.java
import java.util.concurrent.StructuredTaskScope;

static String load() throws InterruptedException {
    try (var scope = StructuredTaskScope.open()) {
        var a = scope.fork(() -> fetchA());
        var b = scope.fork(() -> fetchB());
        scope.join();
        return a.get() + b.get();
    }
}
```

Keep the preview label in production documentation and pin the exact JDK used by the application.

## Compact Object Headers

JEP 519 makes compact object headers a product feature in Java 25. On supported 64-bit HotSpot configurations the object header can be reduced from 96/128 bits to 64 bits. Treat any memory-saving percentage as workload-dependent; measure with a representative heap rather than quoting a fixed saving.

## Flexible Constructor Bodies

Validation or computation can occur before the explicit superclass constructor invocation:

```java
class PositivePoint extends Point {
    PositivePoint(int x, int y) {
        if (x < 0 || y < 0) throw new IllegalArgumentException();
        super(x, y);
    }
}
```

## Module Import Declarations

```java
import module java.base;
```

This is mainly useful for small programs. It does not remove the need for deliberate imports in larger codebases.

## Stable Values

StableValue is a Java 25 preview API for values that can be set at most once. It can support lazy initialization and JVM optimizations, but it is not a replacement for every final field or cache.

## Interview Checklist
- [ ] Which Java 25 features are final?
- [ ] Which Java 25 features are preview?
- [ ] Why is ScopedValue different from ThreadLocal?
- [ ] What changed for synchronized and virtual threads in Java 24?
- [ ] Why should StructuredTaskScope examples be version-pinned?
- [ ] Why should compact-header memory claims be measured rather than quoted?

## Related
- Java 25 Roadmap
- LTS Evolution 8 to 25
- [[Java/08_Modern-Java/06 ScopedValue|Scoped Values]]
- [[Java/04_Concurrency/Threads|Threads]]
- [[Java/04_Concurrency/README|Concurrency]]