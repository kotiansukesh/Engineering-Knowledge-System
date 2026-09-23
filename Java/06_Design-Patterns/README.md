---
title: "Design Patterns"
category: "Design-Patterns"
tags: [java, design-patterns, gof]
created: 2026-09-03
pattern: 0
difficulty: Medium
completed: false
reviewed:
sr-due:
---# Design Patterns

> **Source:** [Refactoring.Guru , Design Patterns](https://refactoring.guru/design-patterns) & [Catalog](https://refactoring.guru/design-patterns/catalog) , 23 classic GoF patterns grouped by intent. Each pattern is a blueprint you can customize.
> **Vault:** `Java/06_Design-Patterns/` , Creational (5) • Structural (7) • Behavioral (11) + Extra (2 J2EE) | Part of [[README|Java MOC]]
```dataview
TABLE WITHOUT ID file.link as "Pattern", group as "Group", tags as "Tags"
FROM "Java/06_Design-Patterns"
WHERE group
SORT group ASC, file.name ASC
```
---

## Catalog , 23 Patterns

### Creational , Object Creation, Flexibility & Reuse (5)

| Pattern | Also known as | Purpose | Note |
|---------|---------------|---------|------|
| [[Creational/Factory Method\|Factory Method]] | Virtual Constructor | Interface for creating objects, subclasses decide type | [[Creational/Factory Method\|→]] |
| [[Creational/Abstract Factory\|Abstract Factory]] | | Families of related objects without specifying concrete classes | [[Creational/Abstract Factory\|→]] |
| [[Creational/Builder\|Builder]] | | Step-by-step construction of complex objects | [[Creational/Builder\|→]] |
| [[Creational/Prototype\|Prototype]] | Clone | Copy objects without depending on classes | [[Creational/Prototype\|→]] |
| [[Creational/Singleton\|Singleton]] | | One instance + global access | [[Creational/Singleton\|→]] |
```dataview
TABLE file.link as "Pattern", source as "Source"
FROM "Java/06_Design-Patterns/Creational"
SORT file.name ASC
```

### Structural , Assembling Objects/classes into Larger Structures (7)

| Pattern | Also known as | Purpose | Note |
|---------|---------------|---------|------|
| [[Structural/Adapter\|Adapter]] | Wrapper | Incompatible interfaces collaborate | [[Structural/Adapter\|→]] |
| [[Structural/Bridge\|Bridge]] | | Split abstraction & implementation hierarchies | [[Structural/Bridge\|→]] |
| [[Structural/Composite\|Composite]] | | Tree structures, part-whole, uniform treatment | [[Structural/Composite\|→]] |
| [[Structural/Decorator\|Decorator]] | Wrapper | Add behaviors by wrapping | [[Structural/Decorator\|→]] |
| [[Structural/Facade\|Facade]] | | Simplified interface to complex subsystem | [[Structural/Facade\|→]] |
| [[Structural/Flyweight\|Flyweight]] | Cache | Share common state to save RAM | [[Structural/Flyweight\|→]] |
| [[Structural/Proxy\|Proxy]] | | Surrogate to control access | [[Structural/Proxy\|→]] |
```dataview
TABLE file.link as "Pattern", source as "Source"
FROM "Java/06_Design-Patterns/Structural"
SORT file.name ASC
```

### Behavioral , Algorithms & Responsibility Assignment (11)

| Pattern | Also known as | Purpose | Note |
|---------|---------------|---------|------|
| [[Behavioral/Chain of Responsibility\|Chain of Responsibility]] | | Pass request along chain until handled | [[Behavioral/Chain of Responsibility\|→]] |
| [[Behavioral/Command\|Command]] | | Request as object (queue, undo) | [[Behavioral/Command\|→]] |
| [[Behavioral/Interpreter\|Interpreter]] | | Interpret sentences in a simple language via expression tree | [[Behavioral/Interpreter\|→]] |
| [[Behavioral/Iterator\|Iterator]] | | Traverse without exposing representation | [[Behavioral/Iterator\|→]] |
| [[Behavioral/Mediator\|Mediator]] | | Reduce chaotic dependencies via central mediator | [[Behavioral/Mediator\|→]] |
| [[Behavioral/Memento\|Memento]] | Snapshot | Save/restore state without breaking encapsulation | [[Behavioral/Memento\|→]] |
| [[Behavioral/Observer\|Observer]] | Pub-Sub | Subscription mechanism | [[Behavioral/Observer\|→]] |
| [[Behavioral/State\|State]] | | Alter behavior when state changes | [[Behavioral/State\|→]] |
| [[Behavioral/Strategy\|Strategy]] | Policy | Family of algorithms, interchangeable | [[Behavioral/Strategy\|→]] |
| [[Behavioral/Template Method\|Template Method]] | | Skeleton in superclass, steps overridden | [[Behavioral/Template Method\|→]] |
| [[Behavioral/Visitor\|Visitor]] | | Separate algorithms from objects | [[Behavioral/Visitor\|→]] |
```dataview
TABLE file.link as "Pattern", source as "Source"
FROM "Java/06_Design-Patterns/Behavioral"
SORT file.name ASC
```

### Extra , Beyond gof 23 (2)

| Pattern | Note |
|---------|------|
| [[Extra/DAO Pattern\|DAO Pattern]] | J2EE persistence layer , isolates business from persistence (JDBC/Hibernate) |
| [[Extra/Dependency Injection Pattern\|Dependency Injection Pattern]] | J2EE/Spring , composition of services via constructor/setter, IoC container |

---

## How to use this Folder

- **Creational:** Start with [[Creational/Singleton|Singleton]] → [[Creational/Factory Method|Factory Method]] → [[Creational/Builder|Builder]] (most frequent in interviews)
- **Structural:** [[Structural/Adapter|Adapter]] and [[Structural/Decorator|Decorator]] are most asked; [[Structural/Proxy|Proxy]] for Spring AOP
- **Behavioral:** [[Behavioral/Strategy|Strategy]] ↔ [[Behavioral/State|State]] (compare!), [[Behavioral/Observer|Observer]] ↔ Pub-Sub in Spring Events
- Each note follows **Intent → Problem → Solution → Diagram (native mermaid classDiagram) → When to Use → When NOT to Use → Java example (runnable *Demo with `// =>` outputs) → Trade-offs → Versus → Interview Q&A (3) → Pitfalls → Related** , adapted from Refactoring.Guru with runnable Java snippets

## Classification (from Refactoring.Guru)

> **By intent:** Creational (5) / Structural (7) / Behavioral (11)
> **By complexity & applicability:** See [Classification](https://refactoring.guru/design-patterns/classification)

## Benefits & Criticism

- **Benefits:** Toolkit for common problems, common language for team, proven tradeoffs , [more](https://refactoring.guru/design-patterns/why-design-patterns)
- **Criticism:** Not silver bullet, can add complexity, sometimes harmful if misapplied , [more](https://refactoring.guru/design-patterns/criticism)

---

## Progress

```dataview
TABLE WITHOUT ID file.link as "Pattern", choice(completed, "✅", "⬜") as "Done"
FROM "Java/06_Design-Patterns"
WHERE group
SORT group ASC, file.name ASC
```
*Add `completed: true` to frontmatter when revised.*

---

[[README|← Back to Java MOC]] • [Refactoring.Guru Catalog](https://refactoring.guru/design-patterns/catalog) • *Updated 2026-09-04: all 25 notes restructured (native diagrams, 3 Q&A, pitfalls, vault-relative links)*
