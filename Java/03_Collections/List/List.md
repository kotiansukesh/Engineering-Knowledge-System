---
title: "List"
category: Collections
tags: [java, collections, list]
created: 2026-01-18
updated: 2026-09-02
---

# List — java.util.List

Part of [[README|Java MOC]]

List is an ordered collection with index access. It allows duplicates and nulls. Order is insertion order.

Since Java 21, List is a SequencedCollection, so it has getFirst, getLast, addFirst, addLast, removeFirst, removeLast, and reversed.

## Contract

- ordered by index, from 0 to size minus 1
- allows duplicates, add returns true even if duplicate
- allows nulls except where implementation forbids
- index ops like get, set, add at index, remove at index

## Implementations

- ArrayList: resizable array, 1.5x growth, fast get and set O(1), add O(1) amortized, insert or remove in middle O(n)
- LinkedList: doubly linked list, fast insert or remove at ends, slow get O(n), allows nulls, implements Deque too
- Vector: legacy synchronized resizable array, 2x growth, synchronized per method, prefer ArrayList
- Stack: legacy LIFO over Vector, prefer ArrayDeque
- CopyOnWriteArrayList: thread safe for read heavy cases, copy on write

## When to use which

- random access and mostly append: ArrayList
- frequent insert or remove at ends or need deque: ArrayDeque or LinkedList
- thread safe list: CopyOnWriteArrayList for reads, or Collections.synchronizedList

## Example

```java
// List — ordered, indexed, duplicates allowed
List<String> list = new ArrayList<>(List.of("b","a","c"));
System.out.println(list.get(1));
list.add("a");
System.out.println(list);
list.set(1, "z");
System.out.println(list.getFirst());
System.out.println(list.getLast());
System.out.println(list.reversed());

var nums = List.of(1,2,2,3);
Set<Integer> dedup = new LinkedHashSet<>(nums);
```

Memory note: List.of is immutable and compact. ArrayList copies on growth.

## Interview questions

List vs Set?
List is ordered, indexed, allows duplicates. Set has no index, no duplicates, membership is O(1) for HashSet.

ArrayList vs LinkedList?
ArrayList is array backed, O(1) get, O(n) insert in middle. LinkedList is node based, O(n) get, O(1) insert at ends when you have the node.

<!-- SR -->
What defines a List?:: Ordered, indexed, allows duplicates and nulls. #flashcard
When to use ArrayList vs LinkedList?:: ArrayList for random access, LinkedList when you need frequent insert or remove at ends and deque ops. #flashcard
What did Java 21 add to List?:: SequencedCollection with getFirst, getLast and reversed. #flashcard
