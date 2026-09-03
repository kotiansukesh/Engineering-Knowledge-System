---
title: "Nested Inner Class"
category: Core-Java
tags: [java, class, nested, java25]
created: 2026-01-18
updated: 2026-09-02
---
# Nested Inner Class

> A non-static member inner class. It is associated with an instance of the enclosing class and has implicit access to all members (even `private`) of the outer instance.

## Why it matters

Model a helper that is intrinsically tied to an outer instance, e.g., an iterator that traverses its owning collection's private state.

## When to use it

| Use | Avoid |
|-----|-------|
| Helper needs outer instance's state (collection + iterator) | Helper doesn't need outer state, use static nested class |
| Logical ownership by outer type | Independent lifecycle, use top-level class |
| Need access modifiers on nested type | Overly deep nesting |

## A quick example

> **Java 25:** Inner classes unchanged, `Outer.this` capture and `final`/effectively-final locals identical; use `var` for locals and exhaustive `switch` when dispatching on sealed types.

Runnable Java 25, outer private access + instantiation syntax:

```java
public class NestedInnerClassDemo {
    private int outerValue = 42;
    private void outerPrivate() { System.out.println("outerPrivate called"); }

    // Member inner class — holds implicit outer reference, can access private state
    public class Inner {
        private int innerValue = 7;
        void display() {
            System.out.println("outerValue=" + outerValue);
            outerPrivate();
            System.out.println("innerValue=" + innerValue);
        }
    }
}
```

## Trade-offs
- Direct access to outer private members; strong encapsulation.
- Natural ownership semantics.
- Implicit outer reference → serialization and memory overhead; outer cannot be GC'd while inner lives.
## How it compares

| Aspect | Member Inner (this note) | Static Nested | Local Inner |
|--------|--------------------------|---------------|-------------|
| Outer instance required | Yes | No | Yes (enclosing method) |
| Access to outer private | Yes | Only via instance / static members | Yes |
| Static members allowed | Limited (constants pre-Java 16) | Yes | No |
## Interview notes

**Q1. How do you instantiate a member inner class outside the outer class?**
`Outer o = new Outer(); Outer.Inner i = o.new Inner();`

**Q2. Does an inner class hold a reference to outer?**
Yes, synthetic field `this$0`. Can cause memory leaks if inner outlives intended scope.
## Related

- [[Types/Nested Classes Overview|Nested Classes Overview]]
- [[Types/Nested/Static Nested Class|Static Nested Class]]
- [[Types/Nested/Method Local Inner Class|Method Local Inner Class]]

## Pitfalls

- Creating inner instances in bulk while holding onto them, outer instances leak.
- Serializing an inner instance implicitly serializes outer, prefer static nested for serializable helpers.
- Confusing `Inner.this` vs `Outer.this`, qualify when shadowing.

---
*Category: Core-Java • java25*
