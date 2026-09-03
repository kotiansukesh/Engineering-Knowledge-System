---
title: "Sealed Classes"
category: Modern-Java
tags: [java25, sealed, modern-java, interview]
created: 2026-09-03
completed: false
---

# Sealed Classes — Java 17/25

> `sealed` restricts which classes may extend/implement a type (`permits` clause). Compiler knows the exhaustive set → exhaustive `switch` without `default`, safer hierarchies.

## Why it matters

Model **closed** hierarchies (Result `Success|Failure`, `Shape` `Circle|Rect|Triangle`) with compile-time exhaustiveness, replacing `enum` when variants carry different data.

## When to use / NOT

| Use | Avoid |
|-----|-------|
| Fixed variants with different fields/behavior, want exhaustive pattern switch | Open plugin hierarchies — use non-sealed abstract class/interface |
| Domain types: `Payment = Card | Upi | Netbanking` | Need deep inheritance — sealed is shallow by design |

## Runnable Java 25

```java
// Shape — closed hierarchy, exhaustive switch
sealed interface Shape permits Circle, Rect, Triangle {}
// Circle — closed hierarchy, exhaustive switch
record Circle(double r) implements Shape {}
// Rect — closed hierarchy, exhaustive switch
record Rect(double w, double h) implements Shape {}
// Triangle — closed hierarchy, exhaustive switch
final class Triangle implements Shape { double a,b,c; Triangle(double a,double b,double c){this.a=a;this.b=b;this.c=c;} }

double area(Shape s) {
    return switch (s) {
        case Circle(double r) -> Math.PI * r * r;
        case Rect(double w, double h) -> w * h;
        case Triangle t -> {
            double p = (t.a + t.b + t.c) / 2;
            yield Math.sqrt(p*(p-t.a)*(p-t.b)*(p-t.c));
        }
    };
}
// Expr — closed hierarchy, exhaustive switch

sealed interface Expr permits Literal, Add, Mul {}
// Literal — closed hierarchy, exhaustive switch
record Literal(int v) implements Expr {}
// Add — closed hierarchy, exhaustive switch
record Add(Expr l, Expr r) implements Expr {}
non-sealed interface Mul extends Expr {}
```

## How it compares

|  | `sealed` | `enum` | `abstract class` |
|--|----------|--------|------------------|
| Variants carry data | yes (different records/classes) | no (same fields) | yes but open |
| Exhaustive switch | yes, no default | yes | no |
| Extensibility | closed (`permits`) | closed | open |

## Interview Q&A

**Q: `sealed` vs `final`?**  
`final` = no subclasses. `sealed` = only `permits` subclasses, each must be `final`/`sealed`/`non-sealed`.

**Q: Do you need `default` in switch over sealed?**  
No if you cover all `permits`. Compiler errors if you miss one — great for refactoring.

**Q: `non-sealed` use?**  
Opens a branch: `sealed A permits B,C; non-sealed B` → `B` can have arbitrary subclasses while `A` stays sealed via `C`.

## Pitfalls

- Forgetting `permits` subclass must be in same module/package (or named module).
- Using `sealed` for truly open hierarchies — forces artificial `non-sealed` everywhere.

## Related

- [[01 Records]] • [[03 Pattern Matching]] • [[../02_OOP/Inheritance/Multiple Inheritance|Multiple Inheritance]] (interfaces)

---
*Category: Modern-Java • java25*
