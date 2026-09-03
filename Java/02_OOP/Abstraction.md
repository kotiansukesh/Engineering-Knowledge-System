---
title: "Abstraction"
category: OOP
tags: [java, oop, abstraction]
created: 2026-01-18
updated: 2026-09-02
---

# Abstraction

Part of [[README|Java MOC]]

Abstraction means showing what an object does and hiding how it does it. Callers depend on the contract, not the concrete class.

Think of driving: you use the accelerator and brake without knowing how combustion works. In Java you get this with abstract classes and interfaces.

Data abstraction is showing only essential details and ignoring the rest. Properties and behaviour that distinguish an object help classify it. In Java, both interface and abstract class provide abstraction, interfaces give full abstraction of the contract.

## When to use it

Use abstraction when several implementations share the same contract, like Payment with UPI, card and COD, or Shape with circle and rectangle. It lets you depend on the abstraction and swap implementations. It also helps at framework or plugin boundaries.

Avoid it when only one implementation will ever exist, indirection then just adds noise, or when callers still check instanceof on the concrete type, which leaks the implementation.

Abstract class vs interface:

- abstract class can hold state, has constructors, allows one extends
- interface holds no instance state, only constants, no constructor, allows multiple implements
- since Java 8, interfaces can have default and static methods, since Java 9 private methods, so they can evolve without breaking implementors
- use abstract class when subclasses share state and common code, use interface when you want a role or capability

## How it looks

Abstract class holds shared state and declares abstract methods. Subclasses fill them in.

```
Shape (abstract) { color, area() abstract, toString() abstract }
  |-- Circle { radius, area() }
  |-- Rectangle { length, width, area() }
```

## Example

Abstract class version:

```java
abstract class Shape {
    String color;
    Shape(String c) { this.color = c; }
    abstract double area();
}

class Circle extends Shape {
    double radius;
    Circle(String c, double r) { super(c); radius = r; }
    double area() { return Math.PI * radius * radius; }
}

class Rectangle extends Shape {
    double l, w;
    Rectangle(String c, double l, double w) { super(c); this.l = l; this.w = w; }
    double area() { return l * w; }
}

Shape s1 = new Circle("red", 2.2);
Shape s2 = new Rectangle("yellow", 2, 4);
System.out.println(s1.area());
```

Interface version:

```java
interface Payment { void pay(double amount); }
class UpiPayment implements Payment { public void pay(double a){ System.out.println("UPI " + a);} }
class CardPayment implements Payment { public void pay(double a){ System.out.println("card " + a);} }
void checkout(Payment p){ p.pay(499); }
```

Modern sealed version in Java 21 or later, exhaustive switch with no default needed:

```java
sealed interface Shape2 permits Circle2, Rectangle2 { double area(); String color(); }
record Circle2(String color, double radius) implements Shape2 { public double area(){ return Math.PI*radius*radius; } }
record Rectangle2(String color, double l, double w) implements Shape2 { public double area(){ return l*w; } }

String describe(Shape2 s){
    return switch(s){
        case Circle2(String c, double r) -> "circle " + c;
        case Rectangle2(String c, double l, double w) -> "rect " + c;
    };
}
```

Note: abstract classes can have constructors and fields, interface fields are public static final.

## Encapsulation vs abstraction

- encapsulation hides data, via private fields and methods
- abstraction hides implementation, via interface or abstract class
- one protects state, the other defines what to expose

## Interview questions

How do you get abstraction in Java?
With abstract class and interface.

Can an abstract class have a constructor? Can a constructor be abstract?
Yes it can have a constructor, called via super. A constructor cannot be abstract, static or final.

When to choose abstract class over interface?
Choose abstract class when you need shared state and common code in an is-a hierarchy. Choose interface for a capability that many unrelated types can implement.

What if a subclass does not override an abstract method?
It must be declared abstract or compilation fails.

<!-- SR -->
How do you achieve abstraction in Java?:: With abstract class and interface. #flashcard
Can an abstract class have a constructor?:: Yes, subclasses call it via super. Constructors cannot be abstract. #flashcard
When to use abstract class vs interface?:: Abstract class for shared state and common code, interface for a role or capability. #flashcard
What happens if a subclass skips an abstract method?:: The subclass must be declared abstract, otherwise it does not compile. #flashcard
