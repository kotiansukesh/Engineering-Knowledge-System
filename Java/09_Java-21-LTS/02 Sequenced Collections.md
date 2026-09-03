---
title: "Sequenced Collections — JEP 431 (Java 21)"
category: java21
tags: [java21, jep431, sequenced, collections, interview]
created: 2026-09-03
completed: false
---

# Sequenced Collections — JEP 431 (Java 21 LTS)

> Uniform order-aware API: `SequencedCollection` / `SequencedSet` / `SequencedMap` — `getFirst()`, `getLast()`, `addFirst()`, `addLast()`, `removeFirst/Last()`, `reversed()`.

## Intent

One API for `List`, `Deque`, `LinkedHashSet`, `LinkedHashMap` — replace `list.get(0)` / `list.get(list.size()-1)` / manual reverse loops.

## When to Use / NOT

| Use | Avoid |
|-----|-------|
| Ordered collections need first/last/reversed uniformly | Unordered `HashSet`/`HashMap` — not `Sequenced` |

## Runnable Java 21

```java
// Sequenced collections (Java 21) — ordered Map/Set/List API
import java.util.*;

void demo21() {
    SequencedCollection<String> c = new ArrayList<>(List.of("b","c"));
    c.addFirst("a"); c.addLast("d");
    System.out.println(c.getFirst());
    System.out.println(c.getLast());
    System.out.println(c.reversed());

    SequencedSet<String> s = new LinkedHashSet<>(List.of("x","y"));
    s.addFirst("w");

    SequencedMap<String,Integer> m = new LinkedHashMap<>();
    m.put("a",1); m.put("b",2);
    m.putFirst("z",0);
    System.out.println(m.firstEntry());
    System.out.println(m.reversed());
}
```

## Vs — Before 21 vs 21

| Before | Java 21 |
|--------|---------|
| `list.get(0)` / `list.get(size-1)` | `c.getFirst()` / `c.getLast()` |
| `for(i=size-1;...)` | `c.reversed()` view |
| `LinkedHashMap` first via iterator | `m.firstEntry()` / `putFirst()` |

## Interview Q&A

**Q: Which collections are `Sequenced`?**  
`ArrayList`, `LinkedList`, `Deque` impls, `LinkedHashSet`, `LinkedHashMap`/`SortedMap` impls. Not `HashSet`/`HashMap`.

**Q: `reversed()` copy?**  
View — mutations propagate both ways.

## Pitfalls

- Expecting `HashSet.getFirst()` — compile error.
- Assuming `reversed()` on `ArrayList` is free — view is O(n) random access; copy if hot loop.

## Related

- [[01 Virtual Threads]] • [[03 Record Patterns]] • [[../08_Modern-Java/04 Sequenced Collections|08 — 25 uses same API]] • [[../03_Collections/List/ArrayList|03_Collections]]

---
*Category: java21*
