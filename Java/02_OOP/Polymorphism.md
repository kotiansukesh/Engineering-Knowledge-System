---
title: "Polymorphism"
category: OOP
tags: [java, oop, polymorphism]
created: 2026-01-18
updated: 2026-09-02
---

# Polymorphism

Part of [[README|Java MOC]]

Polymorphism lets one interface have many implementations. The same call behaves differently depending on the actual object.

There are two forms in Java. Compile time polymorphism is method overloading, same name with different parameters, resolved by the compiler. Runtime polymorphism is method overriding, a subclass provides its own version, resolved at runtime via dynamic dispatch.

## When to use it

Use it when callers should depend on a supertype or interface and remain unaware of the concrete type. This supports the open closed principle: add new types without changing existing code.

Avoid deep override chains that make behaviour hard to trace, and avoid overloading with ambiguous signatures.

## How it looks

```
Payment (interface) { pay() }
  |-- UpiPayment { pay() -> UPI }
  |-- CardPayment { pay() -> card }

checkout(Payment p) -> p.pay() dispatches to the actual type
```

## Example

Overriding, runtime dispatch:

```java
interface Payment { void pay(double amount); }
class UpiPayment implements Payment { public void pay(double a){ System.out.println("UPI " + a);} }
class CardPayment implements Payment { public void pay(double a){ System.out.println("card " + a);} }

void checkout(Payment p){ p.pay(100); } // same call, different behaviour
checkout(new UpiPayment());
checkout(new CardPayment());
```

Overloading, compile time:

```java
class Calculator {
    int add(int a, int b){ return a+b; }
    double add(double a, double b){ return a+b; }
    int add(int a, int b, int c){ return a+b+c; }
}
```

Modern dispatch with sealed types and pattern switch:

```java
sealed interface Shape permits Circle, Rectangle {}
record Circle(double r) implements Shape {}
record Rectangle(double l, double w) implements Shape {}

double area(Shape s){
    return switch(s){
        case Circle(double r) -> Math.PI*r*r;
        case Rectangle(double l, double w) -> l*w;
    };
}
```

## Overloading vs overriding

- overloading: same class, same name, different params, compile time, return type can differ
- overriding: subclass, same signature, runtime, uses @Override, cannot reduce visibility, respects Liskov

## Interview questions

What are the two types of polymorphism in Java?
Compile time via overloading and runtime via overriding.

Can you override a static or private method?
No. Static methods are hidden, not overridden. Private methods are not visible to subclasses.

What decides which overridden method runs?
The runtime type of the object, not the reference type.

<!-- SR -->
What are the two kinds of polymorphism in Java?:: Overloading at compile time and overriding at runtime. #flashcard
How does overriding work?:: A subclass redefines a method with the same signature, the call dispatches to the runtime type. #flashcard
Can you override a static method?:: No, it is method hiding, the reference type decides. #flashcard
What is the difference between overloading and overriding?:: Overloading is same name different params in one class at compile time, overriding is same signature in a subclass at runtime. #flashcard
