---
title: "Behavioral Patterns"
type: folder-MOC
tags: [MOC, design-patterns, behavioral]
---
# Behavioral Patterns

> 11 patterns , algorithms and assignment of responsibilities. | Part of [[06_Design-Patterns/README|Design Patterns MOC]] → [[Java/README|Java MOC]]
```dataview
TABLE WITHOUT ID file.link as "Pattern", tags as "Tags"
FROM "Java/06_Design-Patterns/Behavioral"
WHERE file.name != "README"
SORT file.name ASC
```

## Patterns (11)

- [[06_Design-Patterns/Behavioral/Chain of Responsibility|Chain of Responsibility]] , Pass request along the chain
- [[06_Design-Patterns/Behavioral/Command|Command]] , Request as object , queue, undo
- [[06_Design-Patterns/Behavioral/Interpreter|Interpreter]] , Expression-tree evaluator for small grammars
- [[06_Design-Patterns/Behavioral/Iterator|Iterator]] , Traverse without exposing representation
- [[06_Design-Patterns/Behavioral/Mediator|Mediator]] , Central hub, decoupled peers
- [[06_Design-Patterns/Behavioral/Memento|Memento]] , Snapshot , save/restore state
- [[06_Design-Patterns/Behavioral/Observer|Observer]] , Pub-Sub subscription
- [[06_Design-Patterns/Behavioral/State|State]] , Behavior follows internal state
- [[06_Design-Patterns/Behavioral/Strategy|Strategy]] , Policy , interchangeable algorithms
- [[06_Design-Patterns/Behavioral/Template Method|Template Method]] , Skeleton in superclass, steps overridden
- [[06_Design-Patterns/Behavioral/Visitor|Visitor]] , Algorithms separated from objects

## Note Format

Each note follows **Intent → Problem → Solution → Diagram (mermaid classDiagram) → When to Use → When NOT to Use → Java example → Trade-offs → Versus → Interview Q&A (3) → Pitfalls → Related**.
```dataview
TABLE WITHOUT ID file.link as "Pattern", choice(completed, "✅", "⬜") as "Done"
FROM "Java/06_Design-Patterns/Behavioral"
WHERE group
SORT file.name ASC
```
[[06_Design-Patterns/README|← Back to Design Patterns MOC]]
