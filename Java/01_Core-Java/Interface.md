---
title: "Interface"
category: Core-Java
tags: [java, interface, java25]
created: 2026-01-18
updated: 2026-09-02
---
# Interface

> An interface declares *what* an object can do, not *how*. It forms a contract between a class and the outside world, enforced by the compiler at build time. Implementing classes provide the actual behavior.

## Why it matters

Decouple *what* is required from *who* provides it. Interfaces enable polymorphism across unrelated class hierarchies and are the basis for multiple inheritance of type in Java.

## When to use it

| Use | Avoid |
|-----|-------|
| Unrelated classes share a capability (`Comparable`, `Cloneable`, `Vehicle`) | Need to share state / constructors, use abstract class |
| Need multiple inheritance of type | Single hierarchy with common state |
| Defining strategy / callback / lambda target | Overusing interfaces for every class (YAGNI), concrete + tests may be enough |

## A quick example

> **Java 25:** Interfaces unchanged, `default`/`static`/`private` methods and `sealed` permits (JEP 409) for closed type hierarchies (`sealed interface Vehicle permits Car, Bike`). Use `sealed` + pattern-matching `switch` for exhaustive handling.

Runnable Java 25, interface with default, static, and functional usage:

```java
interface Vehicle {
 void changeGear(int g);
 void speedUp(int inc);
 void applyBrakes(int dec);

 default void printState(int speed, int gear) {
 System.out.println("speed:" + speed + " gear:" + gear);
 }
 static String type() { return "Vehicle"; }
}

class Car implements Vehicle {
 int speed = 0, gear = 1;
    }
}
```

> **Functional Interfaces:** Single-abstract-method interfaces (`Runnable`, `Consumer`, `Predicate`, `Supplier`) are lambda targets. `@FunctionalInterface` enforces the single-method rule but allows `default`/`static` methods.
>
> **Marker Interfaces:** Empty interfaces (`Serializable`, `Cloneable`) provide runtime type info. Modern code prefers annotations, marker interfaces blur "interface = behavior."

## Trade-offs
- Loose coupling, easy mocking/testing.
- Multiple inheritance of type.
- Clean API boundaries.
## How it compares

| Aspect | Interface | Abstract Class | Concrete Class |
|--------|-----------|----------------|----------------|
| State | No (only `static final` constants) | Yes | Yes |
| Constructors | No | Yes | Yes |
| Multiple inheritance | Yes | No (single) | No |
## Interview notes

**Q1. Why does a functional interface have exactly one abstract method?**
Because a lambda provides implementation for *one* method, the compiler needs an unambiguous target. Default/static methods don't count.

**Q2. Interface vs Abstract class, when to pick which?**
Interface for contracts across unrelated types; abstract class when subclasses share state, constructors, or non-trivial common code.
## Related

- [[Classes]]
- [[Types/Abstract Class|Abstract Class]]
- [[Types/Anonymous Class|Anonymous Class]]
- [[Method Overload]]

## Pitfalls

- Forgetting `public` is implicit, all abstract methods are `public`; implementing class must declare them `public`.
- Adding methods to a published interface is a breaking change (use `default` methods to evolve safely).
- Using marker interfaces where an annotation (`@Serializable`) would be clearer.

---
*Category: Core-Java • java25*
