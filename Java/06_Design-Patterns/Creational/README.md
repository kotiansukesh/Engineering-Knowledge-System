---
title: "Creational Patterns"
category: "Creational"
tags: [java, design-patterns, creational]
created: 2026-09-03
pattern: 0
difficulty: Medium
completed: false
reviewed:
sr-due:
---# Creational Patterns

> 5 patterns , object creation mechanisms that increase flexibility and reuse. | Part of [[06_Design-Patterns/README|Design Patterns MOC]] → [[Java/README|Java MOC]]
```dataview
TABLE WITHOUT ID file.link as "Pattern", tags as "Tags"
FROM "Java/06_Design-Patterns/Creational"
WHERE file.name != "README"
SORT file.name ASC
```

## Patterns (5)

- [[06_Design-Patterns/Creational/Abstract Factory|Abstract Factory]] , Families of related objects
- [[06_Design-Patterns/Creational/Builder|Builder]] , Stepwise construction of complex objects
- [[06_Design-Patterns/Creational/Factory Method|Factory Method]] , Virtual Constructor , subclasses decide the type
- [[06_Design-Patterns/Creational/Prototype|Prototype]] , Clone , copy without depending on classes
- [[06_Design-Patterns/Creational/Singleton|Singleton]] , One instance + global access

## Note Format

Each note follows **Intent → Problem → Solution → Diagram (mermaid classDiagram) → When to Use → When NOT to Use → Java example → Trade-offs → Versus → Interview Q&A (3) → Pitfalls → Related**.
```dataview
TABLE WITHOUT ID file.link as "Pattern", choice(completed, "✅", "⬜") as "Done"
FROM "Java/06_Design-Patterns/Creational"
WHERE group
SORT file.name ASC
```
[[06_Design-Patterns/README|← Back to Design Patterns MOC]]
