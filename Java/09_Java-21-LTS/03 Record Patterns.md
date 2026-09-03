---
title: "Record Patterns — JEP 440 (Java 21)"
category: java21
tags: [java21, jep440, record-patterns, interview]
created: 2026-09-03
completed: false
---

# Record Patterns — JEP 440 (Java 21 LTS)

> Deconstruct `record` values in `instanceof` and `switch` — `case Point(int x,int y)` binds components directly.

## Intent

Pattern-match data carriers without manual `p.x()` accessors — concise, type-safe, nestable.

## When to Use / NOT

| Use | Avoid |
|-----|-------|
| `record` DTOs, sealed hierarchy with records | Mutable classes — pattern couples to component order |

## Runnable Java 21

```java
// Point — deconstruction in instanceof/switch
record Point(int x, int y) {}
// Rectangle — deconstruction in instanceof/switch
record Rectangle(Point lo, Point hi) {}

String describe(Object o) {
    if (o instanceof Point(int x, int y) && x == y) return "diag " + x;
    return switch (o) {
        case Point(int x, int y) when x > 0 -> "point " + x + "," + y;
        case Rectangle(Point(int x1,int y1), Point(int x2,int y2)) -> "rect ["+x1+","+y1+"]->["+x2+","+y2+"]";
        case null -> "null";
        default -> "other";
    };
}
void demo21() {
    System.out.println(describe(new Point(3,4)));
    System.out.println(describe(new Rectangle(new Point(0,0), new Point(2,3))));
}
```

## How It Compares — Java 25 adds primitive patterns (JEP 507)

| Java 21 | Java 25 (JEP 507) |
|---------|-------------------|
| `case Integer i` (boxed) | `case int i when i>0` (no boxing) |
| Record patterns | + primitive type patterns |

## Interview Q&A

**Q: Nested record pattern?**  
`case Rectangle(Point(int x1,int y1), Point(int x2,int y2))` — fully nestable; `var` also: `case Point(var x, var y)`.

**Q: `when` guard vs `&&`?**  
`when` is switch guard: `case Point(int x,int y) when x==y`. `if (o instanceof Point(int x,int y) && x==y)` uses `&&`.

## Pitfalls

- Missing `case null` — `switch(null)` NPE unless `case null`.
- Changing record component order breaks patterns — treat as API.

## Related

- [[04 Pattern Matching for Switch]] • [[02 Sequenced Collections]] • [[../08_Modern-Java/01 Records|08 — Records]] • [[../08_Modern-Java/03 Pattern Matching|08 — Primitive Patterns]]

---
*Category: java21*
