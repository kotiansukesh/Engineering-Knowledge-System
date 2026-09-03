---
title: "Object oriented programming"
category: OOP
tags: [java, oop]
created: 2026-01-18
updated: 2026-09-02
---

# Object oriented programming

Part of [[README|Java MOC]]

OOP groups data and the methods that operate on it into objects. Each object owns its state and exposes only the operations you want callers to use.

## What it is

Object oriented programming models real entities by binding data and behaviour together. Only the object's own methods should access its data directly.

A class is a blueprint that defines fields, methods and constructors. An object is an instance with its own field values and identity. The four ideas that come up again and again are abstraction, encapsulation, inheritance and polymorphism.

```
class (blueprint) --instantiates--> object (state + identity + behaviour)
```

- class: template with fields and methods. See [[Classes]]
- object: instance, holds values, responds to messages
- abstraction: expose what it does, hide how. See [[Abstraction]]
- encapsulation: hide state, access through methods. See [[Encapsulation]]
- inheritance: reuse and extend via extends or implements. See [[Inheritance]]
- polymorphism: one interface, many implementations. See [[Polymorphism]]

Class vs object:

```
Car class { engine, speed, accelerate() } --new--> car object { engine=V6, speed=80, accelerate() -> 95 }
```

## When to use it

Use OOP when your domain has entities that carry both state and behaviour, like Order or Payment, when you need to extend behaviour through subtypes or composition, or when encapsulation helps a team work without stepping on each other.

Skip it when the logic is a pure transformation with no identity, for one off scripts where a hierarchy just adds overhead, or in tight loops where virtual dispatch and allocation cost matters.

## Method declaration

A Java method has six parts.

- access: public for everywhere, protected for package plus subclasses, private for the defining class only, default for package only
- return type or void
- name
- parameter list
- exception list
- body

```java
public int getSpeed() { return speed; }
protected void reset() { speed = 0; }
```

## Example

A short modern example with record and sealed types. Records replace verbose POJOs, sealed interfaces make the hierarchy exhaustive.

```java
record Car(String model, int speed) {
    Car {
        if (speed < 0) throw new IllegalArgumentException("speed < 0");
    }
    Car withSpeed(int s) { return new Car(model, s); }
}

sealed interface Vehicle permits Car, Bike {}
record Bike(String brand, int speed) implements Vehicle {}

class Demo {
    static String describe(Vehicle v) {
        return switch (v) {
            case Car(String m, int s) -> "Car " + m + " @ " + s;
            case Bike(String b, int s) -> "Bike " + b + " @ " + s;
        };
    }
    public static void main(String[] args) {
        Vehicle v = new Car("Swift", 60);
        System.out.println(describe(v));
        if (v instanceof Car(String m, int s))
            System.out.println(m + " " + s);
    }
}
```

Notes on Java 25: flexible constructor bodies let you validate before the super call, and pattern switch handles sealed hierarchies without a default branch.

Legacy sketch for comparison:

```java
abstract class Vehicle { int speed; Vehicle(int s){this.speed=s;} abstract void accelerate(int d); }
class Car extends Vehicle {
    String model; Car(String m,int s){super(s);this.model=m;}
    void accelerate(int d){speed+=d;}
}
```

## Inheritance or composition

- reuse by copy or call: procedural
- reuse by extends: inheritance, medium flexibility, tight coupling
- reuse by has-a field and delegation: composition, high flexibility, loose coupling

Prefer composition unless you have a true is a relation that satisfies Liskov substitution.

## Interview questions

How many pillars does OOP have and what are they?
Abstraction, encapsulation, inheritance, polymorphism.

What is the difference between class and object?
Class is the blueprint, object is the instance with identity and state.

Why keep fields private and use getters or setters?
To validate, to change representation without breaking callers, and to keep invariants in one place.

When would you avoid OOP?
For stateless pipelines, pure functions, or scripts where a class adds no benefit.

<!-- SR -->
What are the four pillars of OOP?:: Abstraction, encapsulation, inheritance and polymorphism. #flashcard
What is the difference between a class and an object?:: A class is the blueprint, an object is an instance with its own state and identity. #flashcard
Why use private fields with accessors?:: To validate and to evolve representation without breaking callers. #flashcard
When should you prefer composition over inheritance?:: When reuse is not a true is-a relation or when behaviour needs to change at runtime. #flashcard

## Related

[[Abstraction]] · [[Encapsulation]] · [[Inheritance]] · [[Polymorphism]] · [[Classes]]
