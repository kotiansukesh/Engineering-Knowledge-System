---
title: "Sequenced Collections"
category: Modern-Java
tags: [java25, sequenced, collections, jep431]
created: 2026-09-03
completed: false
---

# Sequenced Collections — Java 21/25

> `SequencedCollection`, `SequencedSet`, `SequencedMap` (JEP 431, Java 21) unify order-aware APIs: `getFirst()`, `getLast()`, `addFirst()`, `addLast()`, `removeFirst()`, `removeLast()`, `reversed()`. In Java 25 all `List`, `Deque`, `LinkedHashSet`, `LinkedHashMap` implement them.

## Why it matters

Before 21: `list.get(0)` / `list.get(list.size()-1)`, `map.keySet().iterator().next()`, no `reversed()`. Now: one API across `List`, `Deque`, `LinkedHashSet`, `LinkedHashMap`.

## Runnable Java 25

```java
// Sequenced collections — getFirst/getLast/reversed on ordered views
import java.util.*;

void demo() {
    SequencedCollection<String> seq = new ArrayList<>(List.of("b","c"));
    seq.addFirst("a");
    seq.addLast("d");
    System.out.println(seq.getFirst());
    System.out.println(seq.getLast());
    System.out.println(seq.reversed());

    SequencedSet<String> set = new LinkedHashSet<>(List.of("x","y","z"));
    set.addFirst("w");
    System.out.println(set);
    System.out.println(set.reversed());

    SequencedMap<String,Integer> map = new LinkedHashMap<>();
    map.put("a",1); map.put("b",2);
    map.putFirst("z",0);
    System.out.println(map.firstEntry());
    System.out.println(map.lastEntry());
    System.out.println(map.reversed());

    for (var e : seq.reversed()) System.out.print(e + " ");
}

SequencedCollection<Integer> nums = new ArrayList<>(List.of(1,2,3));
```

## How it compares

| Before | Java 25 |
|--------|---------|
| `list.get(0)` / `list.get(list.size()-1)` | `seq.getFirst()` / `seq.getLast()` |
| Manual reverse loop `for(i=size-1;...)` | `seq.reversed()` view |
| `LinkedHashMap` first key via iterator | `map.firstEntry()` / `putFirst()` |

## Interview Q&A

**Q: Does `HashSet` implement `SequencedSet`?**  
No — `HashSet` is unordered, so not sequenced. `LinkedHashSet` does.

**Q: `reversed()` — copy or view?**  
View — mutations reflect. `var rev = seq.reversed(); rev.addFirst("x")` adds to tail of original.

**Q: Why not just `Deque`?**  
`Deque` already had `getFirst/getLast` but `List` didn't; `SequencedCollection` unifies `List`+`Deque`+`LinkedHashSet` behind one interface.

## Pitfalls

- `HashSet`/`HashMap` not sequenced — compile error if you expect `getFirst()`.
- `reversed()` on `ArrayList` is a view with O(n) random access; for hot loops cache or copy.

## Related

- [[../03_Collections/List/ArrayList|ArrayList]] • [[../03_Collections/Set/HashSet|HashSet]] • [[01 Records]] (records in Sequenced collections)

---
*Category: Modern-Java • java25*
