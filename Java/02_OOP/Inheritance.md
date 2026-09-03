---
title: "Inheritance"
category: OOP
tags: [java, oop, inheritance]
created: 2026-01-18
updated: 2026-09-02
---

# Inheritance

Part of [[README|Java MOC]]

Inheritance lets a subclass acquire fields and methods from a superclass and then add or override behaviour. It creates an is-a relation. Code written against Bicycle also works with MountainBike.

Terms: super class is the parent that is inherited from, sub class is the child that inherits and can add members, reusability is the side effect of sharing code.

## When to use it

Use inheritance when there is a true is-a relation and Liskov substitution holds, every MountainBike is a Bicycle. It fits template method patterns where the base defines the skeleton and subclasses fill hooks, or when a framework expects an extension point.

Prefer composition when reuse is just code sharing without is-a, when the hierarchy would go deep or unstable, or when behaviour must vary at runtime. Has-a with delegation is looser and swappable.

Inheritance is not primarily for code reuse. Design for subtyping, reuse follows.

## How it looks

```
Bicycle { gear, speed, applyBrake(), speedUp() }
   ^ extends
MountainBike { seatHeight, setHeight(), toString() override }

Test uses MountainBike as a Bicycle
```

Inheritance vs composition:

- inheritance is is-a, tight coupling, compile time, has the diamond issue
- composition is has-a, loose coupling, swappable at runtime, no diamond

## Example

```java
class Bicycle {
    int gear, speed;
    Bicycle(int g,int s){ gear=g; speed=s; }
    void applyBrake(int d){ speed-=d; }
    void speedUp(int i){ speed+=i; }
}
class MountainBike extends Bicycle {
    int seatHeight;
    MountainBike(int g,int s,int h){ super(g,s); seatHeight=h; }
    public String toString(){ return "gear " + gear + " speed " + speed + " height " + seatHeight; }
}

Bicycle b = new MountainBike(3, 20, 5);
b.speedUp(10);
System.out.println(b); // MountainBike toString runs
```

Composition alternative:

```java
class Engine { void start(){ System.out.println("start"); } }
class Car {
    private final Engine engine; // has-a
    Car(Engine e){ this.engine=e; }
    void start(){ engine.start(); }
}
```

Java notes: a class extends one class, implements many interfaces. Use super to call the parent constructor or method, use @Override to catch mistakes, constructors are not inherited.

## Types

- single: one parent, one child
- multilevel: chain like Animal -> Dog -> Puppy
- hierarchical: one parent, many children
- multiple: many parents, not allowed for classes in Java, allowed for interfaces with default methods, use with care
- hybrid: combination, usually via interfaces and class inheritance together

See separate notes for each type.

## Interview questions

What is inheritance?
A mechanism where one class acquires fields and methods of another.

Why does Java not allow multiple class inheritance?
To avoid the diamond problem and ambiguity. Interfaces can have multiple inheritance of type, and default methods handle conflicts explicitly.

What is the difference between inheritance and composition?
Inheritance is is-a with tight coupling, composition is has-a with delegation and looser coupling.

<!-- SR -->
What is inheritance?:: A subclass acquires fields and methods from a superclass and can add or override. #flashcard
When should you use inheritance?:: When there is a true is-a relation that satisfies Liskov substitution. #flashcard
Why does Java avoid multiple class inheritance?:: To avoid the diamond problem, interfaces provide multiple inheritance of type. #flashcard
What is the difference between inheritance and composition?:: Inheritance is is-a with tight coupling, composition is has-a with delegation and looser coupling. #flashcard
