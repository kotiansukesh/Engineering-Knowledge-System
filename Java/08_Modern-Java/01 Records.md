---
title: "Records"
category: Modern-Java
tags: [java25, record, modern-java, interview]
created: 2026-09-03
completed: false
---

# Records — Java 16/25

> A `record` is a transparent, immutable carrier for data. Compiler generates `equals`, `hashCode`, `toString`, accessors and canonical constructor from the header. Ideal for DTOs, keys, return tuples — not for mutable/JPA entities.

## Why it matters

Reduce boilerplate without Lombok, with built-in immutability and pattern-matching support (`record` patterns in switch). Java 25 adds **primitive patterns** that work cleanly with record components.

## When to use / NOT

| Use | Avoid |
|-----|-------|
| Immutable DTOs, event payloads, cache keys, `Map` return tuples | Mutable entities (JPA lazy proxies need non-final; use class) |
| Value objects where `equals/hashCode` by all components is correct | Need inheritance (`record` is final, implicitly extends `Record`) |
| Pattern matching: `if (o instanceof Point(int x, int y))` | Need to add mutable state after construction |

## Runnable Java 25

```java
// Point — immutable data carrier, compact validation, pattern matching
record Point(int x, int y) {
    public Point {
        if (x < 0 || y < 0) throw new IllegalArgumentException("non-negative");
    }
    double distance() { return Math.hypot(x, y); }
}
// User — immutable data carrier, compact validation, pattern matching

record User(String name, int age) {}

String describe(Object o) {
    if (o instanceof User(String n, int a)) {
        return n + ":" + a;
    }
    return switch (o) {
        case Point(int x, int y) -> "point " + x + "," + y;
        case User u -> "user " + u.name();
        default -> "unknown";
    };
}

void demo() {
    var p = new Point(3, 4);
    System.out.println(p);
    System.out.println(p.distance());
    System.out.println(describe(p));
    System.out.println(describe(new User("Ava", 29)));
}
```

## Trade-offs

- ✅ Zero boilerplate, immutable, thread-safe, correct `equals/hashCode`.
- ✅ Deconstructs in pattern matching (no getters noise).
- ❌ Final + shallow immutability — if a component is a mutable list, defensively copy.

## How it compares

|  | `record` | `class` + Lombok `@Value` | `class` manual |
|--|----------|---------------------------|----------------|
| Boilerplate | none | annotation | getters/equals/hashCode |
| Immutability | shallow, enforced | shallow | manual |
| Pattern matching | yes (`Point(int x,int y)`) | no | no |
| Extensibility | final | final by default | open |

## Interview Q&A

**Q: `record` vs `class` vs `record` with custom constructor?**  
`record` header is state + canonical constructor; compact constructor (`public Point { ... }`) runs before field assignment and can normalize/validate. Custom constructor must delegate to canonical via `this(...)`.

**Q: Can a record be a JPA `@Entity`?**  
No — JPA needs no-arg constructor + non-final + mutable proxies. Use class for entities; record for projections/DTOs.

**Q: Records + compact headers (JEP 450)?**  
Records are small objects; compact headers (128→64 bits) make millions of records cheaper — relevant for `SequencedCollection` of records.

## Pitfalls

- Mutable component (`record Box(List<String> items)`) — caller mutates list. Fix: `public Box { items = List.copyOf(items); }`.
- Adding behavior that belongs elsewhere — records should stay data carriers; heavy logic → class.

## Related

- [[02 Sealed Classes]] • [[03 Pattern Matching]] • [[../01_Core-Java/Types/Immutable Class|Immutable Class]] • [[../03_Collections/List/ArrayList|ArrayList]] (SequencedCollection of records)

---
*Category: Modern-Java • java25*
