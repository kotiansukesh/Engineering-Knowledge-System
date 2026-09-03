---
title: "Multiple inheritance"
category: OOP
tags: [java, oop, inheritance]
created: 2026-01-18
updated: 2026-09-02
---

# Multiple inheritance

Part of [[Inheritance]]

Multiple inheritance means one class inherits from more than one superclass. Java does not allow multiple class inheritance with extends because of the diamond problem, where two parents provide the same method.

Java allows multiple inheritance of type through interfaces. A class can implement many interfaces, and interfaces can provide default methods. If defaults clash, the class must resolve the conflict.

## How it looks

```
Not allowed: class C extends A, B

Allowed: class C implements A, B
interface A { default void show(){ } }
interface B { default void show(){ } }
C must override show()
```

## Example

```java
interface Flyable { default void move(){ System.out.println("fly"); } }
interface Swimmable { default void move(){ System.out.println("swim"); } }

class Duck implements Flyable, Swimmable {
    public void move(){ Flyable.super.move(); } // resolve conflict
}

Duck d = new Duck();
d.move();
```

If you need to share code from multiple sources, prefer composition and delegate to helper objects.

## Interview questions

Why does Java not allow multiple class inheritance?
To avoid ambiguity and the diamond problem. Interfaces give multiple inheritance of type with explicit conflict resolution.

How do you handle conflicting default methods?
Override the method in the implementing class and choose which super to call, like InterfaceName.super.method().

<!-- SR -->
Why does Java not allow multiple class inheritance?:: To avoid the diamond problem and method ambiguity. #flashcard
How do you resolve conflicting default methods from two interfaces?:: Override the method and call InterfaceName.super.method(). #flashcard
