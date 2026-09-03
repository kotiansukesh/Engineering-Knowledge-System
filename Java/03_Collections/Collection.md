---
title: "Collection"
category: Collections
tags: [java, collections]
created: 2026-01-18
updated: 2026-09-02
---

# Collection — java.util.Collection

Part of [[README|Java MOC]]

Collection is the root interface for List, Set and Queue. Map is separate. It defines common operations like add, remove, contains, size, and iterator.

## Hierarchy

```
Collection
  |-- List (ordered, indexed, duplicates allowed)
  |-- Set (unique, no index)
  |-- Queue (holds elements for processing, FIFO etc.)
Map (key to value, not a Collection)
```

Since Java 21, SequencedCollection adds getFirst, getLast and reversed for ordered collections.

## What it provides

- add and addAll
- remove, removeAll, retainAll, clear
- contains and containsAll
- size, isEmpty
- iterator, spliterator, stream
- toArray

All collections are fail fast for iterators: structural change during iteration throws ConcurrentModificationException.

## When to use which

- need index, order, duplicates: List, see [[List]]
- need uniqueness and fast membership: Set, see [[Set]]
- need processing order like FIFO or priority: Queue, see [[Queue]]
- need key to value lookup: Map, see [[Map]]

## Example

```java
// Collection — root interface for List/Set/Queue (Map separate)
Collection<String> c = new ArrayList<>();
c.add("a"); c.add("b");
System.out.println(c.contains("a"));
System.out.println(c.size());
c.remove("a");
for (var s : c) System.out.println(s);

Collection<String> c2 = new LinkedHashSet<>(List.of("b","a","a"));
System.out.println(c2);
```

For large collections, size the initial capacity to avoid rehash or resizing. For thread safety, use concurrent collections or wrap with Collections.synchronizedX.

## Interview questions

Is Map a Collection?
No, Map is key to value and has its own hierarchy.

What is the difference between Collection and Collections?
Collection is an interface, Collections is a utility class with static methods like sort and synchronizedList.

<!-- SR -->
Is Map a Collection?:: No, Collection is List Set Queue, Map is separate key to value. #flashcard
What does Collection define?:: Common operations like add, remove, contains, size and iterator. #flashcard
What is Collections vs Collection?:: Collection is the interface, Collections is a utility class with static helpers. #flashcard
