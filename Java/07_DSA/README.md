---
title: "Data Structures & Algorithms"
type: folder-MOC
tags: [MOC, 07_dsa]
---

# Data Structures & Algorithms

> Array, Linked Lists, Stack/Queue, HashMap, Trees — fundamentals. **Java 25** refresh: `record Node`, `SequencedCollection`, pattern matching, Compact Object Headers (JEP 450). | Part of [[README|Java MOC]]

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
