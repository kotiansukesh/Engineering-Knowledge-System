---
title: "Extra , Beyond GoF 23"
type: folder-MOC
tags: [MOC, design-patterns, extra]
---
# Extra , Beyond gof 23

> 2 enterprise patterns beyond the classic 23 , kept from Interview Prep. | Part of [[06_Design-Patterns/README|Design Patterns MOC]] → [[Java/README|Java MOC]]
```dataview
TABLE WITHOUT ID file.link as "Pattern", tags as "Tags"
FROM "Java/06_Design-Patterns/Extra"
WHERE file.name != "README"
SORT file.name ASC
```

## Patterns (2)

- [[06_Design-Patterns/Extra/DAO Pattern|DAO Pattern]] , Isolate business code from persistence
- [[06_Design-Patterns/Extra/Dependency Injection Pattern|Dependency Injection Pattern]] , Give, don't create , constructor-wired collaborators

## Note Format

Each note follows **Intent → Problem → Solution → Diagram (mermaid classDiagram) → When to Use → When NOT to Use → Java example → Trade-offs → Versus → Interview Q&A (3) → Pitfalls → Related**.
```dataview
TABLE WITHOUT ID file.link as "Pattern", choice(completed, "✅", "⬜") as "Done"
FROM "Java/06_Design-Patterns/Extra"
WHERE group
SORT file.name ASC
```
[[06_Design-Patterns/README|← Back to Design Patterns MOC]]
