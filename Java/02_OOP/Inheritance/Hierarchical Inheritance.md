---
title: "Hierarchical inheritance"
category: OOP
tags: [java, oop, inheritance]
created: 2026-01-18
updated: 2026-09-02
---

# Hierarchical inheritance

Part of [[Inheritance]]

Hierarchical inheritance has one superclass with many subclasses. For example Animal is the parent of Dog, Cat and Cow.

## How it looks

```
        Animal { eat() }
        /   |   \
     Dog   Cat  Cow
```

## Example

```java
class Animal { void eat(){ System.out.println("eat"); } }
class Dog extends Animal { void bark(){ System.out.println("bark"); } }
class Cat extends Animal { void meow(){ System.out.println("meow"); } }

Animal a1 = new Dog(); a1.eat();
Animal a2 = new Cat(); a2.eat();
```

Common behaviour stays in the parent, specialised behaviour lives in each child. This is common and easy to reason about.

## Interview questions

What is hierarchical inheritance?
One parent class with multiple child classes.

<!-- SR -->
What is hierarchical inheritance?:: One superclass with many subclasses, like Dog and Cat extending Animal. #flashcard
