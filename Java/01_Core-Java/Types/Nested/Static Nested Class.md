---
title: Static Nested Class
category: Java/01_Core-Java/Types/Nested
tags:
- java
- class
- nested
- java25
created: 2026-01-18
pattern: 4
difficulty: Easy
completed: false
reviewed: ''
sr-due: ''
excalidraw: ''
source: ''
type: note
---

# Static Nested Class
> Part of [[Java/01_Core-Java/README|Core Java]]

> A `static` class defined inside another class. Like a static field, it belongs to the outer *class*, not to any outer *instance*. It has no implicit reference to an outer object.

## Why it Matters

Group a helper with its owner without the overhead or lifecycle coupling of an inner class. The classic example is `Map.Entry`.

## Diagram

```mermaid
classDiagram
 Outer *-- Nested : "static: no this"
 class Outer {
 -static int n
 }
 class Nested {
 +render() void
 }
```

## Code

> **Java 25:** Static nested classes unchanged, `static class Inner` has no enclosing instance; use `var` and `IO.println` in compact demos; compact headers reduce overhead.

Runnable Java 25:
```java
public class StaticNestedClassDemo {
 private static String staticOuter = "static-outer";
 private String instanceOuter = "instance-outer";

 // Static nested class — no outer instance, only static members accessible
 static class Nested {
 void show() {
 System.out.println(staticOuter);
 }
 static void staticMethod() { System.out.println("static nested static method"); }
 }
}
```
> **Access:** A static nested class can access `private static` members of the outer class. It behaves like a top-level class that happens to be namespaced inside another for encapsulation.

## When to use / not

| Use | Avoid |
|-----|-------|
| Helper tied to outer type but not to an instance (Builder, Entry, Node) | Need access to outer instance fields, use member inner |
| Want to avoid hidden outer reference / memory overhead | Helper is truly independent, consider top-level class |

## Trade-offs

- No implicit outer reference → no memory leak, freely instantiable.
- Can have all member types including `static` members.
- Encapsulation + namespace without coupling.

## Vs

| Aspect | Static Nested | Member Inner | Top-Level |
|--------|--------------|--------------|-----------|
| Needs outer instance | No | Yes | N/A |
| Holds outer reference | No | Yes (hidden) | No |
| Access outer `private` | Static members only (directly) | All members | No |

## Pitfalls

- Using member inner by habit when static nested would suffice → hidden outer retention.
- Expecting to access outer instance members directly from static nested, need an instance.
- Forgetting `static` on a Builder, forces `outer.new Builder()` which is rarely desired.

---
*Category: Core-Java • java25*

## Interview q&a

**Q1. Static nested vs inner, key difference?**
Static nested has no `this$0` outer reference; instantiated via `new Outer.Nested()` without an outer instance.

**Q2. Can a static nested class access non-static outer fields?**
Only via an explicit `Outer` instance reference, not implicitly.
Static nested vs inner, key difference?:: Static nested has no `this$0` outer reference; instantiated via `new Outer.Nested()` without an outer instance. #flashcard
Can a static nested class access non-static outer fields?:: Only via an explicit `Outer` instance reference, not implicitly. #flashcard

## Related

- [[Java/01_Core-Java/Types/Nested Classes Overview|Nested Classes Overview]]
- [[Java/01_Core-Java/Types/Nested/Nested Inner Class|Nested Inner Class]]
- [[Classes]]
