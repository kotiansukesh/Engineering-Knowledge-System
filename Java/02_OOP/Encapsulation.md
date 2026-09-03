---
title: "Encapsulation"
category: OOP
tags: [java, oop, encapsulation]
created: 2026-01-18
updated: 2026-09-02
---

# Encapsulation

Part of [[README|Java MOC]]

Encapsulation bundles data and behaviour and hides the data. Outside code reaches the state only through methods that can validate, log, or change representation.

Wrapping data in a single unit and shielding it from outside access is the core idea. Variables are private and public methods expose controlled access. This is often described as combining data hiding and abstraction.

## When to use it

Always encapsulate mutable state, especially when validation is needed, when invariants span several fields, or when representation might change later.

You can keep it light for pure data carriers with no invariants. A record is a good fit there, it is still encapsulated but concise. Private inner classes used only internally also need less ceremony.

Watch for public mutable fields, setters that just assign with no check, and getters that return a mutable internal collection without a defensive copy.

## How it looks

```
Encapsulate { -name, -roll, -age | +getName(), +setName(), +getAge() with validate }
  ^
  | caller uses only public methods
 TestEncapsulation
```

## Example

Preferred modern form with a record. Fields are private final, validation runs in the compact constructor.

```java
import java.util.Objects;
record Geek(String name, int roll, int age) {
    Geek {
        Objects.requireNonNull(name);
        if (age < 0) throw new IllegalArgumentException("age < 0");
        if (roll <= 0) throw new IllegalArgumentException("roll > 0");
    }
    String display(){ return name + " #" + roll + " " + age; }
}

var g = new Geek("Harsh", 51, 19);
System.out.println(g.display());
if (g instanceof Geek(String n, int r, int a))
    System.out.println(n + " " + r);
```

Legacy POJO form:

```java
class Encapsulate {
    private String name; private int roll; private int age;
    public String getName(){ return name; }
    public void setName(String v){ name = Objects.requireNonNull(v); }
    public int getAge(){ return age; }
    public void setAge(int v){ if(v<0) throw new IllegalArgumentException(); age=v; }
}
```

Production detail with a mutable field that needs a defensive copy:

```java
final class Account {
    private final String id;
    private final List<String> tags;
    private int balance;
    Account(String id, int b, List<String> tags){
        if(b<0) throw new IllegalArgumentException();
        this.id=id; this.balance=b; this.tags=new ArrayList<>(tags);
    }
    public List<String> getTags(){ return Collections.unmodifiableList(tags); }
    public void deposit(int a){ if(a<=0) throw new IllegalArgumentException(); balance+=a; }
}
```

Callers cannot add to the list directly, they get an unmodifiable view.

## Encapsulation and related ideas

- encapsulation hides how data is stored, via private plus methods
- abstraction hides how it is done, via interface or abstract class
- composition reuses behaviour by delegation with a has-a field

Use the first two together: one protects state, the other defines the minimal contract. Use composition to reuse encapsulated parts safely.

## Interview questions

How do you achieve encapsulation in Java?
Make fields private and expose public getters, setters or behaviour methods, with validation and defensive copies.

Is encapsulation the same as data hiding?
Data hiding is the technique of making fields private. Encapsulation is the principle of bundling data and methods and hiding state.

Do getters and setters break encapsulation?
Blind getters and setters for every field do. Prefer behaviour methods like deposit instead of setBalance.

How do you keep a class encapsulated when it holds a list?
Copy on construction and return an unmodifiable view or List.copyOf.

<!-- SR -->
How do you achieve encapsulation in Java?:: Private fields with public accessors or behaviour methods, plus validation and defensive copies. #flashcard
Is encapsulation the same as data hiding?:: Data hiding is the technique, encapsulation is the broader principle. #flashcard
When do getters and setters hurt encapsulation?:: When they expose every field with no behaviour and let callers break invariants. #flashcard
How to encapsulate a list field?:: Copy the list in the constructor and return an unmodifiable view. #flashcard
