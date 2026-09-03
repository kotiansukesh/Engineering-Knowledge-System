---
title: "Multilevel inheritance"
category: OOP
tags: [java, oop, inheritance]
created: 2026-01-18
updated: 2026-09-02
---

# Multilevel inheritance

Part of [[Inheritance]]

Multilevel inheritance chains inheritance. For example Animal -> Dog -> Puppy. Puppy inherits from Dog, which inherits from Animal.

## How it looks

```
Animal { eat() }
  ^ 
Dog { bark() }
  ^
Puppy { weep() }
```

## Example

```java
class Animal { void eat(){ System.out.println("eat"); } }
class Dog extends Animal { void bark(){ System.out.println("bark"); } }
class Puppy extends Dog { void weep(){ System.out.println("weep"); } }

Puppy p = new Puppy();
p.eat(); p.bark(); p.weep();
```

Each level can add state or override methods. Keep chains short, deep hierarchies become fragile when a middle class changes.

## Interview questions

What is multilevel inheritance?
A class inherits from a class that itself inherits from another class, forming a chain.

<!-- SR -->
What is multilevel inheritance?:: A chain where a class inherits from a class that inherits from another, like Puppy extends Dog extends Animal. #flashcard
