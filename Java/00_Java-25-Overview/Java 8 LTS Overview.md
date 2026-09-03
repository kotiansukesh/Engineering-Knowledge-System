---
title: "Java 8 LTS Overview"
category: overview
tags: [java8, lts, overview, jep, interview]
created: 2026-09-03
completed: false
---

# Java 8 LTS Overview (Mar 2014) — The Foundation

> Part of [[README|00 Overview]] • `overview` • **The LTS every interview assumes you know cold.** If you nail 8, everything else is a delta.

## TL;DR for interviews

> **Java 8** brought **lambdas + functional interfaces, Streams, `java.time`, default methods, `Optional`, `CompletableFuture`, Nashorn + PermGen → Metaspace**. 90% of "Core Java" interview Qs are still Java 8 Qs.

## Must-Know Features (JEPs you will be asked)

| Feature | JEP / API | 60-sec answer |
|---------|-----------|---------------|
| **Lambdas & Functional Interfaces** | JEP 126 | `(a,b)->a+b`, `@FunctionalInterface` SAM, capture *effectively final* |
| **Streams** | JEP 107 | `filter/map/collect` — lazy intermediate vs eager terminal, **not reusable** |
| **`java.time` (JSR-310)** | JEP 150 | `Instant/LocalDate/ZonedDateTime` — **immutable, thread-safe** vs `Date/Calendar` |
| **Default + Static in Interfaces** | JEP 126 | `default void forEach` — evolve interfaces without breaking impls |
| **`Optional`** | JEP 122 | `map/flatMap/orElseThrow` — **not for fields/params**, never `get()` without check |
| **`CompletableFuture`** |  | `supplyAsync/thenApply/thenCompose` — async without raw `Future.get()` |
| **Method References** | JEP 126 | `String::valueOf`, `this::handle`, `ArrayList::new` |
| **Metaspace** | JEP 122 | PermGen removed → Metaspace (`-XX:MaxMetaspaceSize`) — `OOM: Metaspace` now |

## When to Use / NOT

| Use | Avoid |
|-----|-------|
| Streams for filter/map/groupBy | `parallelStream()` blindly — fork-join overhead, non-threadsafe collectors |
| `Optional` as return type for nullable | `Optional` field/param or `Optional.get()` |
| `java.time` everywhere | `Date`/`Calendar`/`SimpleDateFormat` (not thread-safe) |

## Runnable Java 8 (`--release 8`)

```java
import java.time.*;
import java.util.*;
import java.util.stream.*;
import java.util.concurrent.CompletableFuture;

void demo8() {
    // Lambda + Stream: lazy vs terminal
    List<String> names = List.of("ava","bob","ava");
    Map<String,Long> freq = names.stream()
        .filter(s -> s.length()==3)
        .collect(Collectors.groupingBy(s->s, Collectors.counting())); // {ava=2, bob=1}

    // java.time — immutable
    LocalDate d = LocalDate.of(2024,3,14);
    ZonedDateTime z = d.atStartOfDay(ZoneId.of("Asia/Kolkata"));

    // CompletableFuture
    CompletableFuture<String> cf = CompletableFuture.supplyAsync(() -> "hello")
        .thenApply(String::toUpperCase);
    System.out.println(cf.join()); // HELLO

    // Optional — orElseThrow
    Optional<String> opt = Optional.ofNullable(null);
    System.out.println(opt.orElse("fallback"));
}

@FunctionalInterface interface TriFn<A,B,C,R>{ R apply(A a,B b,C c); }
default interface MyList<E> { default void forEachDo(java.util.function.Consumer<E> c){} }
```

## Vs Tables

**Stream vs Loop**

|  | Loop | Stream |
|--|------|--------|
| Readability | imperative | declarative `filter/map/collect` |
| Laziness | eager | intermediate lazy, terminal triggers |
| Reuse | reusable | **single-use** — `stream.forEach(...); stream.filter(...)` throws |

**`Optional` vs `null`**

|  | `null` | `Optional` |
|--|--------|------------|
| NPE risk | yes | `orElseThrow` forces handling |
| Overuse | — | Don't store as field — serialize cost |

## Quick Check — Can you answer?

- [ ] Why must lambda captures be *effectively final*?
- [ ] Intermediate vs terminal — when does stream execute?
- [ ] `map` vs `flatMap` on `Optional`/`Stream`?
- [ ] Why `SimpleDateFormat` is unsafe vs `DateTimeFormatter`?
- [ ] `CompletableFuture.thenApply` vs `thenCompose`?

## Pitfalls

- `parallelStream()` on small lists + blocking IO → slower.
- `Optional.of(null)` → NPE; use `ofNullable`.
- `Date` mutability + `SimpleDateFormat` shared static → race.

## Related

- [[Java 11 LTS Overview]] → next delta • [[Whats New in Java 25]] (timeline) • [[../01_Core-Java/Streams API|Streams API]] • [[../01_Core-Java/JVM Memory Model|JVM - Metaspace]] • [[LTS Evolution 8 to 25]]

---
*Category: overview • java8*
