---
title: "Java 17 LTS Overview"
category: overview
tags: [java17, lts, overview, jep, interview]
created: 2026-09-03
completed: false
---

# Java 17 LTS Overview (Sep 2021) — The Modern Baseline

> Part of [[README|00 Overview]] • `overview` • **The LTS before 21.** Interviews test **sealed/record final, pattern `instanceof`, text blocks, switch expressions, strong encapsulation** — 70% of "what's new since 8?" answers are 17 answers.

## TL;DR for interviews

> **Java 17 = Java 11 +** `sealed` (409 final) + `record` (395 final) + **pattern `instanceof`** (394) + **switch expressions** (361) + **text blocks** (378) + **records + sealed + patterns together** + `jpackage`, foreign linker incubator, strong encapsulation (JEP 403).

## Must-Know Features

| Feature | JEP | 60-sec answer |
|---------|-----|---------------|
| **`sealed` classes** | 409 | `sealed interface Shape permits Circle,Rect` — compiler enforces exhaustive `switch` |
| **`record`** (final) | 395 | `record Point(int x,int y)` — immutable, `equals/hashCode/toString`, compact constructor |
| **Pattern `instanceof`** | 394 | `if (o instanceof String s && !s.isBlank())` — binding + flow scoping |
| **Switch expressions** | 361 | `var r = switch(day){ case MON -> 1; default -> 0; }` — expression, `yield` in blocks |
| **Text blocks** | 378 | `""" hello {name} """` — JSON/SQL without `\"` soup |
| **New `instanceof` + `switch` synergy** | — | `sealed` + `record` + `switch` = exhaustive without `default` — preview of 21's record patterns |
| **Strong encapsulation** | 403 | `--illegal-access=deny` by default — `setAccessible` on JDK internals fails |
| **`jpackage`** | 343 | Native installer — `jpackage --type dmg` |

## Runnable Java 17 (`--release 17`)

```java
sealed interface Shape permits Circle, Rect {}
record Circle(double r) implements Shape {}
record Rect(double w,double h) implements Shape {}

// Pattern instanceof + switch expression + text block
String describe(Object o) {
    if (o instanceof Circle c && c.r() > 0) return "circle " + c.r();
    return switch (o) {
        case String s when s.isBlank() -> "blank";
        case String s -> "str " + s;
        case Shape sh -> "shape";
        case null -> "null";
        default -> "other";
    };
}
String json = """
    {"name": "%s", "age": %d}
    """.formatted("Ava", 30);

double area(Shape s) {
    return switch (s) { // exhaustive — no default needed (sealed)
        case Circle(double r) -> Math.PI*r*r; // 21 adds record patterns; 17 needs instanceof chain
        case Rect(double w, double h) -> w*h;
    };
}
```

> **17 vs 21 nuance:** In **17** you write `if (s instanceof Circle c) ... else if (s instanceof Rect r) ...`. In **21** you write `case Circle(double r)` (record patterns JEP 440) — interviewers love this diff.

## When to Use / NOT

| Use | Avoid |
|-----|-------|
| `record` for DTOs, events, keys | `record` for mutable entities/JPA entities |
| `sealed` for closed hierarchies (`Result`, `Shape`) | `sealed` for open extension — use `non-sealed` |
| Text blocks for JSON/SQL | Text blocks for single-line strings |

## Vs — 11 → 17

| Before (11) | Java 17 |
|-------------|---------|
| `if (o instanceof String) { String s=(String)o; ...}` | `if (o instanceof String s)` |
| `switch` statement with fall-through | `switch` expression with `->` + `yield` |
| `"{\"name\":\"Ava\"}"` | `""" {"name": "%s"} """.formatted(name)` |
| `enum` for closed set | `sealed interface` + `record` |

## Quick Check

- [ ] `sealed` + `permits` vs `non-sealed`?
- [ ] `record` compact constructor vs canonical?
- [ ] Why `switch` expression needs exhaustive or `default`?
- [ ] When does `instanceof String s` binding go out of scope?

## Pitfalls

- Forgetting `permits` list must be in same package/module — permits must be accessible.
- Using `record` with JPA/Hibernate — bytecode proxy needs no-arg constructor.

## Related

- [[Java 11 LTS Overview]] ← prev • [[../09_Java-21-LTS/00 Java 21 Overview|Java 21 Overview]] → next • [[LTS Evolution 8 to 25]] • [[../08_Modern-Java/01 Records|08 — Records]] • [[../08_Modern-Java/02 Sealed Classes|Sealed]]

---
*Category: overview • java17*
