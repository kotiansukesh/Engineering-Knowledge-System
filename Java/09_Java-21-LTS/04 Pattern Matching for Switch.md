---
title: "Pattern Matching for Switch — JEP 441 (Java 21)"
category: java21
tags: [java21, jep441, switch, sealed, interview]
created: 2026-09-03
completed: false
---

# Pattern Matching for Switch — JEP 441 (Java 21 LTS)

> Finalized pattern `switch` — type patterns, guarded patterns (`when`), null-aware, exhaustive for `sealed` hierarchies.

## Intent

Replace `if-else` chains + visitor with exhaustive, type-safe `switch (obj)` over hierarchies.

## When to Use / NOT

| Use | Avoid |
|-----|-------|
| Branch on sealed `Shape`/`Result` with records | Simple constant `switch (status)` — plain `case "OK":` clearer |

## Runnable Java 21

```java
// Shape — sealed + guarded patterns
sealed interface Shape permits Circle, Rect {}
// Circle — sealed + guarded patterns
record Circle(double r) implements Shape {}
// Rect — sealed + guarded patterns
record Rect(double w, double h) implements Shape {}

double area(Shape s) {
    return switch (s) {
        case Circle(double r) when r > 0 -> Math.PI * r * r;
        case Circle _ -> 0;
        case Rect(double w, double h) -> w * h;
    };
}
String fmt(Object o) {
    return switch (o) {
        case null -> "null";
        case String str when str.isBlank() -> "blank";
        case String str -> "str:" + str;
        case Integer i -> "int:" + i;
        default -> "other";
    };
}
```

## Vs — Before 21

| Before 21 | Java 21 JEP 441 |
|-----------|-----------------|
| `if (s instanceof Circle c) ... else if ...` | `switch (s) { case Circle(double r) -> ... }` |
| `switch` only constants + enums | `switch` over types + patterns + guards |
| Manual `null` check | `case null` in switch |

## Interview Q&A

**Q: Exhaustive switch over `sealed`?**  
Compiler enforces coverage — add `Triangle` to `permits` → switch must handle it or add `default`.

**Q: Dominance?**  
Order matters — specific before general: `case Circle _` before `case Shape s` (or compiler error).

**Q: `when` guard?**  
`case String s when s.length()>3 -> ...` — condition tied to pattern.

## Pitfalls

- Forgetting `case null` — NPE.
- Over-large switch — extract to polymorphic `area()` if >4 branches but interview loves switch.

## Related

- [[03 Record Patterns]] • [[06 Unnamed Patterns and Variables]] • [[../02_OOP/Polymorphism|OOP Polymorphism]]

---
*Category: java21*
