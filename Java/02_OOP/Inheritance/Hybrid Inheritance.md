---
title: "Hybrid inheritance"
category: OOP
tags: [java, oop, inheritance]
created: 2026-01-18
updated: 2026-09-02
---

# Hybrid inheritance

Part of [[Inheritance]]

Hybrid inheritance mixes two or more forms, like hierarchical plus multilevel, or class plus interface inheritance. Java supports it only through interfaces, not through multiple class extends.

## How it looks

```
Animal
  |\
  Dog  Cat  (hierarchical)
  |
Puppy (multilevel from Dog)

Also: class Child extends Parent implements Flyable, Swimmable
```

## Example

```java
interface Flyable { void fly(); }
interface Swimmable { void swim(); }

class Animal { void eat(){ System.out.println("eat"); } }
class Duck extends Animal implements Flyable, Swimmable {
    public void fly(){ System.out.println("fly"); }
    public void swim(){ System.out.println("swim"); }
}

Duck d = new Duck();
d.eat(); d.fly(); d.swim();
```

Use hybrid when a type needs both an is-a parent and several roles. Prefer composition if the mix gets hard to follow.

## Interview questions

What is hybrid inheritance?
A combination of two or more inheritance types.

Does Java support hybrid inheritance with classes?
Only via interfaces. A class can extend one class and implement many interfaces.

<!-- SR -->
What is hybrid inheritance?:: A mix of two or more inheritance forms, like hierarchical plus multilevel. #flashcard
How does Java support hybrid inheritance?:: Through interfaces and single class inheritance combined. #flashcard
