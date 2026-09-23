---
title: "OOP Cheat Sheet"
category: "OOP"
tags: [java, cheat-sheet, oop]
created: 2026-09-03
pattern: 0
difficulty: Medium
completed: false
reviewed: ""
sr-due: ""
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---# OOP , Cheat Sheet

## 4 Pillars + SOLID (vs Tables)

| Pillar | What | Java Mechanism | Interview One-Liner |
|---|---|---|---|
| **Encapsulation** | Hide state, expose behavior | `private` fields + getters/setters, `record` | "Make fields private, validate in constructor/compact constructor" |
| **Abstraction** | Hide complexity | `abstract class` / `interface` / sealed | "Program to interface, not implementation" |
| **Inheritance** | IS-A reuse | `extends` (1 class), `implements` (N interfaces) | "Favour composition over inheritance , inheritance breaks encapsulation" |
| **Polymorphism** | One name, many forms | Overloading (compile) / Overriding (runtime, dynamic dispatch) | "Overriding needs same signature + covariant return + @Override" |

| SOLID | Principle | Violation Smell | Fix |
|---|---|---|---|
| **S** | Single Responsibility | God class (User + DB + Email) | Split into User, UserRepository, EmailService |
| **O** | Open/Closed | `if (type==A) ... else if(B)` | Strategy / Polymorphism |
| **L** | Liskov | `Square extends Rectangle` breaks `setWidth` | Don't force IS-A where behavior differs |
| **I** | Interface Segregation | Fat `Worker{work(),eat()}` → Robot must eat | Split `Workable`, `Eatable` |
| **D** | Dependency Inversion | `Service → MySQLRepo` | `Service → Repository` interface, inject impl |

## Vs Tables (Interview Favorites)

| Comparison | A | B | Rule |
|---|---|---|---|
| **Abstract vs Interface** | `abstract class` : state + ctor + `protected` | `interface` : pure contract, `default`/`static`/`private` methods (Java 8+) | Use interface for capability, abstract for IS-A with shared state |
| **Overloading vs Overriding** | Compile-time, same name diff params | Runtime, same signature, `@Override` | Overloading: return type irrelevant; Overriding: covariant return OK |
| **Composition vs Inheritance** | HAS-A (`Car has Engine`) | IS-A (`Dog is Animal`) | Prefer composition , more testable, no fragile base class |
| **Association vs Aggregation vs Composition** | Association: uses-a | Aggregation: has-a (weak, shared) | Composition: owns-a (strong, lifecycle-bound, `final` field) |
| **This vs Super** | `this` → current | `super` → parent | `super()` must be first line in constructor |

## Object Class Contract

| Method | Contract | Must Pair With |
|---|---|---|
| `equals()` | Reflexive, symmetric, transitive, consistent | Always override `hashCode` together |
| `hashCode()` | Equal objects → same hash; use `Objects.hash()` | If used in HashMap/HashSet |
| `toString()` | Debug representation | Override for records/classes |
| `clone()` | Avoid , use copy constructor / record | `Cloneable` is broken by design |

## Java 25 One-Liners

```java
// Records and sealed hierarchies, immutable data + exhaustive switches
record Money(BigDecimal amount, Currency cur) {
 public Money { if (amount.signum() < 0) throw new IllegalArgumentException(); }
}

sealed interface Expr permits Add, Lit {}
record Add(Expr l, Expr r) implements Expr {}
record Lit(int v) implements Expr {}
int eval(Expr e){ return switch(e){ case Add(var l,var r) -> eval(l)+eval(r); case Lit(var v) -> v; }; }

// Interface default methods and composition
interface Repo<T> { default void saveAll(List<T> xs){ xs.forEach(this::save); } void save(T t); }

class OrderService {
 private final PaymentGateway gateway; // composition, inject for testability
 OrderService(PaymentGateway g){ this.gateway=g; }
}

// Covariant override
class Animal { Animal reproduce(){ return new Animal(); } }
class Dog extends Animal { @Override Dog reproduce(){ return new Dog(); } }
```
```mermaidclassDiagram
 class Shape:::sealed { <<sealed>> }
 class Circle { double r() }
 class Rect { double w(); double h() }
 Shape <|-- Circle
 Shape <|-- Rect
 class OrderService { -PaymentGateway gateway }
 OrderService o-- PaymentGateway : composes
```
*Category: CheatSheet*
