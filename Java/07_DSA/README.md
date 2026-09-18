---
title: "Data Structures & Algorithms"
type: folder-MOC
tags: [MOC, 07_dsa]
---
# Data Structures & Algorithms

> Array, Linked Lists, Stack/Queue, HashMap, Trees , fundamentals. **Java 25** refresh: `record Node`, `SequencedCollection`, pattern matching, Compact Object Headers (JEP 450). | Part of [[README|Java MOC]]

> 11 notes • updated 2026-09-04 • static index (dataview queries follow for live use).

## Notes (11)

| Note | Category | |
| ----------------------------------- | -------------------- | ---------- |
| [[Java/07_DSA/Array.md \| Array]] | DSA |
| [[Java/07_DSA/Cheat Sheet.md \| Cheat Sheet]] | CheatSheet |
| [[Java/07_DSA/Doubly Linked List.md \| Doubly Linked List]] | DSA |
| [[Java/07_DSA/Graph.md \| Graph]] | DSA |
| [[Java/07_DSA/HashMap.md \| HashMap]] | DSA |
| [[Java/07_DSA/Heap.md \| Heap]] | DSA |
| [[Java/07_DSA/Linked List.md \| Linked List]] | DSA |
| [[Java/07_DSA/Queue.md \| Queue]] | DSA |
| [[Java/07_DSA/Singly Linked List.md \| Singly Linked List]] | DSA |
| [[Java/07_DSA/Stack.md \| Stack]] | DSA |
| [[Java/07_DSA/Trees.md \| Trees]] | DSA |
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "Java/07_DSA"
WHERE file.name != "README"
SORT file.name ASC
```
> **Java 25 (Sep 2025):** Nodes use `record Node<T>(T val, Node<T> next)` (see [[Singly Linked List]]), collections use `SequencedCollection` (`getFirst`/`getLast`/`reversed`), traversal uses pattern matching (`instanceof Node(var v, var nxt)`), and `Compact Object Headers` (`-XX:+UseCompactObjectHeaders`) shrinks per-node headers to 8 B.
## Progress

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done"
FROM "Java/07_DSA"
WHERE category
SORT file.name ASC
```
[[README|← Back to Java MOC]]
