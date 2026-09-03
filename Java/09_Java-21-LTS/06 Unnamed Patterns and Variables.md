---
title: "Unnamed Patterns and Variables — JEP 443 (Java 21)"
category: java21
tags: [java21, jep443, unnamed, interview]
created: 2026-09-03
completed: false
---

# Unnamed Patterns and Variables — JEP 443 (Java 21 LTS)

> `_` for unused patterns and variables — `Point(_, int y)` and `catch (Exception _)` — silences unused warnings, signals intent.

## Intent

Mark intentionally unused components/vars without inventing names like `ignored` or `unused`.

## When to Use / NOT

| Use | Avoid |
|-----|-------|
| Deconstruct record but need only one: `Point(_, int y)` | Need the value — don't use `_`, bind `x` |

## Runnable Java 21

```java
// Unnamed patterns — _ for unused components
record Point(int x, int y) {}

void demo21(Object o) {
    if (o instanceof Point(int x, _)) System.out.println("x=" + x);
    String s = switch (o) {
        case Point(_, int y) when y > 5 -> "high y=" + y;
        case Point _ -> "point";
        case null, default -> "other";
    };
    System.out.println(s);
    try { int _ = risky(); } catch (Exception _) { /* ignore */ }
}
int risky() { return 42; }
```

## How It Compares — Java 25 keeps `_`

| Java 21 | Java 25 |
|---------|---------|
| `_` for patterns + vars + catch | Same, plus pattern matching refinements — no change |

## Interview Q&A

**Q: `var _` vs `_`?**  
`var _ = expr;` binds unnamed variable (still evaluates). `_` alone is placeholder in pattern.

**Q: Can you use `_` twice in same pattern?**  
Yes — `Point(_, _)` both unnamed — no conflict.

## Pitfalls

- Using `_` as identifier — before 21 `_` was identifier; now pattern keyword. Don't name variable `_`.

## Related

- [[03 Record Patterns]] • [[04 Pattern Matching for Switch]] • [[07 Unnamed Classes and Instance Main]]

---
*Category: java21*
