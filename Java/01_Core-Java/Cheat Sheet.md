---
category: CheatSheet
tags: [java, core-java, cheatsheet]
title: Core Java — Cheat Sheet
---

# Core Java — Cheat Sheet

## JVM vs JDK vs JRE | Primitives vs Wrappers | String vs StringBuilder vs StringBuffer

| Concept | A | B | Key Difference |
|---|---|---|---|
| **JVM / JRE / JDK** | JVM (runtime, interprets bytecode) | JRE = JVM + libs; JDK = JRE + javac/javadoc | JDK to build, JRE to run, JVM to execute |
| **Primitive vs Wrapper** | `int` (stack, no null) | `Integer` (heap, nullable, cached -128..127) | Use `Integer.valueOf()` not `new Integer()`; `==` compares refs for wrappers |
| **String vs StringBuilder vs StringBuffer** | `String` immutable, pool, thread-safe | `StringBuilder` mutable, not sync | `StringBuffer` mutable + synchronized → slower; prefer Builder |
| **== vs .equals()** | `==` ref equality | `.equals()` logical (override!) | For Strings always `.equals()`; for records auto-generated |
| **Checked vs Unchecked** | Checked: `IOException` (compile-time) | Unchecked: `NPE`, `IAE` (RuntimeException) | Don't catch `Error`; use try-with-resources for checked |
| **static vs instance** | `static` = class-level, 1 copy | instance = per-object | static can't access `this`; static blocks run once on class load |

## Core Concepts — Quick Table

| Topic | Must-Know | Interview Trap |
|---|---|---|
| **String Pool** | `new String("a")` creates 2 objects; `"a".intern()` reuses pool | `==` on literals true, on `new String` false |
| **Immutability** | `String`, `Integer`, `LocalDate` immutable; `final class + private final fields + no setters + defensive copy` | Returning mutable field breaks immutability |
| **Autoboxing** | `Integer i=127; i==127` → true (cache); `128==128` → false | Use `.equals()` for wrapper comparison |
| **Generics (PECS)** | `Producer Extends, Consumer Super` | `List<Integer>` ≠ `List<Number>`; use `? extends Number` |
| **Optional** | Never null; `ofNullable`, `orElse` vs `orElseGet` (lazy) | Don't use `Optional` as field/param; `orElse` always executes |
| **Records (Java 16+)** | `record Point(int x,int y){}` auto equals/hashCode | Compact constructor for validation |
| **Sealed Classes (17+)** | `sealed class Shape permits Circle, Square` | `switch` becomes exhaustive — no default needed |
| **Var (`var`)** | Local type inference, not keyword | Can't use for fields/params |

## Time / Space Notes

| Operation | Complexity | Note |
|---|---|---|
| String concat in loop (`+`) | O(n²) | Use `StringBuilder` → O(n) |
| `StringBuilder.append` | Amortized O(1) | Backed by resizable char[] |
| Autoboxing array `int[]` vs `Integer[]` | `Integer[]` 4× memory | Prefer primitives in hot loops |

## Java 25 One-Liners

```java
// Modern Java idioms — records, sealed hierarchies, streams, NIO
record User(String name, int age) {}
if (obj instanceof User(var n, var a) && a >= 18) System.out.println(n);

sealed interface Shape permits Circle, Rect {}
String desc = switch(shape){ case Circle c -> "circle r="+c.r(); case Rect r -> "rect"; };

String json = """
    {"name": "%s", "age": %d}
    """.formatted(name, age);

// Optional and Streams — prefer lazy orElseGet and unmodifiable toList()
var val = Optional.ofNullable(mayBeNull).orElseGet(() -> expensiveDefault());
var evens = list.stream().filter(n -> n%2==0).toList();
var first = list.getFirst(); var last = list.getLast();

try (var br = Files.newBufferedReader(path)) { return br.lines().toList(); }

String hex = HexFormat.of().formatHex(bytes);
```

> **Memory:** Stack (primitives, refs) → Heap (objects) → Metaspace (class metadata) → PC Register + Native Stack. GC: G1 (default), ZGC/Shenandoah (low-latency, Java 21+ Generational ZGC).

*Category: CheatSheet*
