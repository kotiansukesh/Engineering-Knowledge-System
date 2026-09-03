---
title: "Immutable Class"
category: Core-Java
tags: [java, class, immutable, java25]
created: 2026-01-18
updated: 2026-09-02
---
# Immutable Class

> A class whose objects cannot be changed after construction. All fields are set once (via constructor) and exposed only via getters, no setters, no leaking mutable references.

Wrapper classes (`Integer`, `Boolean`) and `String` are canonical immutable types in the JDK.

## Why it matters

Create thread-safe, cache-friendly value objects that can be freely shared without defensive publication or synchronization.

## When to use it

| Use | Avoid |
|-----|-------|
| Value objects (Money, City, DateRange) | Need frequent mutations, mutable + builder is more efficient |
| Keys in `HashMap` / `HashSet` | Performance-critical tight loops creating many instances, consider mutable alternatives |
| Multi-threaded sharing without locks | Objects with inherently mutable lifecycle (e.g., `StringBuilder`) |

## A quick example

> **Java 25:** Prefer `record` for shallow immutability (`record City(String name, int id) {}`), compact, immutable, auto `equals/hashCode/toString`. For classes with mutable fields, keep defensive copies (`new Date(d.getTime())`). Headers smaller via Compact Object Headers.

Runnable Java 25, immutable class + defensive copying for mutable fields (`Date`):

```java
import java.util.Date;

final class City {
 private final String name;
 private final int id;
 City(String name, int id) { this.name = name; this.id = id; }
 String getName() { return name; }
 int getId() { return id; }
 @Override public String toString() { return name + "#" + id; }
}

final class Employee {
 private final String name;
    }
}
```

**Checklist for immutability:**
1. `final` class (prevent subclassing that adds mutability).
2. All fields `private final`.
3. Parameterized constructor sets all fields (no setters).
4. Defensive copy for mutable field types (Date, collections) on both construction and getters.
5. No methods that mutate state.

## Trade-offs
- Thread-safe by design; safe to share/caches.
- Predictable, easier reasoning; good map keys.
- New object per "mutation", GC pressure if overused in hot paths.
## How it compares

| Aspect | Immutable | Mutable |
|--------|-----------|---------|
| Thread safety | Inherently safe | Needs synchronization |
| Hash key safety | Safe (hash stable) | Risky if fields mutate |
| Update style | `newObj = obj.withX(..)` | `obj.setX(..)` |
## Interview notes

**Q1. Requirements to make a class immutable?**
`final` class, `private final` fields, no setters, initialize via constructor, defensive copies for mutable members, no leaking `this` during construction.

**Q2. Is `final` alone enough for immutability?**
No, `final` only fixes the reference; the referenced object (e.g., `Date`, `List`) can still mutate unless defensively copied.
## Related

- [[Types/Final Class|Final Class]]
- [[Types/Wrapper Class|Wrapper Class]]
- [[Types/Concrete Class|Concrete Class]]

## Pitfalls

- Returning the internal `Date`/`List` directly, caller can mutate internal state.
- Forgetting `final` on class, subclass can add mutable state and break immutability contract.
- Exposing mutable collections without wrapping with `List.copyOf` / `Collections.unmodifiableList` + copy.
- Storing the caller's reference directly instead of copying in the constructor.

---
*Category: Core-Java • java25*
