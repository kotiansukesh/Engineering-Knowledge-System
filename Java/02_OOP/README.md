---
title: "Object-Oriented Programming"
type: folder-MOC
tags: [MOC, 02_oop]
---
# Object-Oriented Programming

> Pillars + SOLID + relationships , the OOP + LLD interview core. Course map: [AlgoMaster LLD](https://algomaster.io/learn/lld/course-introduction). | Part of [[README|Java MOC]]

## Pillars

| Note | Covers |
|---|---|
| [[02_OOP/00 - OOP Overview\|Overview]] | Map of the folder: class vs object, composition-first |
| [[02_OOP/Classes-and-Objects\|Classes and Objects]] | Nouns→classes, verbs→methods, record vs class |
| [[02_OOP/Interfaces\|Interfaces]] | Contracts, seams, program-to-interface |
| [[02_OOP/Encapsulation\|Encapsulation]] | State hiding, invariants, defensive copies |
| [[02_OOP/Abstraction\|Abstraction]] | What vs how: abstract class vs interface vs sealed |
| [[02_OOP/Inheritance\|Inheritance]] | Reuse + the fragility tax; is-a vs has-a |
| [[02_OOP/Polymorphism\|Polymorphism]] | One call, many behaviors: overloading vs overriding |

Inheritance flavors: [[02_OOP/Inheritance/Single Inheritance\|Single]] • [[02_OOP/Inheritance/Multilevel Inheritance\|Multilevel]] • [[02_OOP/Inheritance/Hierarchical Inheritance\|Hierarchical]] • [[02_OOP/Inheritance/Multiple Inheritance\|Multiple]] • [[02_OOP/Inheritance/Hybrid Inheritance\|Hybrid]]

## SOLID (5 + Field Guide)

| Principle | One-liner |
|---|---|
| [[02_OOP/SOLID-Single-Responsibility\|SRP]] | One reason to change |
| [[02_OOP/SOLID-Open-Closed\|OCP]] | Open for extension, closed for modification |
| [[02_OOP/SOLID-Liskov-Substitution\|LSP]] | Subtypes must honor the contract (Square≠Rectangle) |
| [[02_OOP/SOLID-Interface-Segregation\|ISP]] | Small focused interfaces over fat ones |
| [[02_OOP/SOLID-Dependency-Inversion\|DIP]] | Depend on abstractions; inject implementations |
| [[02_OOP/SOLID-Summary\|SOLID Summary]] | Field guide: all five at a glance + conflict map |

## Relationships & Pragmatics

- [[02_OOP/Class-Relationships\|Class Relationships]] , association vs aggregation vs composition vs dependency (with UML diagram)
- [[02_OOP/Law-of-Demeter\|Law of Demeter]] , talk only to friends; tell, don't ask
- [[02_OOP/Pragmatic-Principles-DRY-YAGNI-KISS\|DRY / YAGNI / KISS]] , when not to apply the above
- [[02_OOP/Cheat Sheet\|Cheat Sheet]] , one-page revision (pillars + SOLID + vs-tables)

## Bridge to lld

SOLID applied under time pressure: [[10_LLD-Machine-Coding/README\|10_LLD-Machine-Coding MOC]] · [[10_LLD-Machine-Coding/00_Method-How-to-Answer-LLD\|LLD method]] · [[10_LLD-Machine-Coding/00_UML-Class-and-Sequence-Diagrams\|UML diagrams]]
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "Java/02_OOP"
WHERE file.name != "README"
SORT file.name ASC
```

## Progress

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done"
FROM "Java/02_OOP"
WHERE category
SORT file.name ASC
```
[[README|← Back to Java MOC]]

---
*Category: Java/02_OOP*
