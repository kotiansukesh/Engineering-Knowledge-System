---
title: "Single inheritance"
category: OOP
tags: [java, oop, inheritance]
created: 2026-01-18
updated: 2026-09-02
---

# Single inheritance

Part of [[Inheritance]]

Single inheritance is one subclass inheriting from one superclass. It is the simplest form.

## How it looks

```
Animal { eat(), sleep() }
  ^ extends
Dog { bark() }
```

## Example

```java
class Animal { void eat(){ System.out.println("eat"); } }
class Dog extends Animal { void bark(){ System.out.println("bark"); } }

Dog d = new Dog();
d.eat();
d.bark();
Animal a = d; // Dog is an Animal
```

Use it when the is-a relation is clear and you need to add or refine behaviour. Keep the hierarchy shallow.

## Interview questions

What is single inheritance?
One child class extends one parent class.

<!-- SR -->
What is single inheritance?:: One subclass extends one superclass. #flashcard
