---
title: "Structural Patterns"
type: folder-MOC
tags: [MOC, design-patterns, structural]
---
# Structural Patterns

> 7 patterns , assembling objects/classes into larger structures while keeping them flexible. | Part of [[06_Design-Patterns/README|Design Patterns MOC]] → [[Java/README|Java MOC]]
```dataview
TABLE WITHOUT ID file.link as "Pattern", tags as "Tags"
FROM "Java/06_Design-Patterns/Structural"
WHERE file.name != "README"
SORT file.name ASC
```

## Patterns (7)

- [[06_Design-Patterns/Structural/Adapter|Adapter]] , Wrapper , incompatible interfaces collaborate
- [[06_Design-Patterns/Structural/Bridge|Bridge]] , Split abstraction & implementation hierarchies
- [[06_Design-Patterns/Structural/Composite|Composite]] , Tree structures, uniform treatment
- [[06_Design-Patterns/Structural/Decorator|Decorator]] , Wrapper , add behavior by wrapping
- [[06_Design-Patterns/Structural/Facade|Facade]] , Simplified interface to a subsystem
- [[06_Design-Patterns/Structural/Flyweight|Flyweight]] , Cache , share state to save RAM
- [[06_Design-Patterns/Structural/Proxy|Proxy]] , Surrogate controlling access

## Note Format

Each note follows **Intent → Problem → Solution → Diagram (mermaid classDiagram) → When to Use → When NOT to Use → Java example → Trade-offs → Versus → Interview Q&A (3) → Pitfalls → Related**.
```dataview
TABLE WITHOUT ID file.link as "Pattern", choice(completed, "✅", "⬜") as "Done"
FROM "Java/06_Design-Patterns/Structural"
WHERE group
SORT file.name ASC
```
[[06_Design-Patterns/README|← Back to Design Patterns MOC]]
