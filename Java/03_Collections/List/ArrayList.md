---
title: "ArrayList"
category: Collections
tags: [java, collections, list]
created: 2026-01-18
updated: 2026-09-02
---

# ArrayList — java.util.ArrayList

Part of [[List]]

ArrayList is the default List. It is a resizable array, ordered, allows duplicates and nulls.

## Internals

- backs with Object[] of default capacity 10 when first element added
- grows by about 1.5x when full: newCapacity = old + old/2
- stores elements contiguously, so cache friendly
- not synchronized
- since Java 21 implements SequencedCollection

## Time complexity

- get and set by index: O(1)
- add at end: O(1) amortized, O(n) when resizing
- add or remove in middle: O(n) to shift
- contains and indexOf: O(n)
- iteration: O(n)

## Example

```java
// ArrayList — resizable array, O(1) random access, 1.5x growth
var list = new ArrayList<String>();
list.add("a"); list.add("b"); list.add("c");
System.out.println(list.get(1));
list.add(1, "z");
System.out.println(list);
list.remove("z");
System.out.println(list.getFirst());
System.out.println(list.reversed());

var big = new ArrayList<Integer>(10_000);

var imm = List.of("a","b","c");
```

Pitfalls: concurrent modification during iteration throws. Use iterator.remove or CopyOnWriteArrayList for concurrent cases. List.of does not allow null.

## ArrayList vs siblings

- vs LinkedList: ArrayList faster for get and append, LinkedList faster for deque ops
- vs Vector: ArrayList is unsynchronized, 1.5x growth, preferred
- vs CopyOnWriteArrayList: ArrayList for single thread, copy on write for many readers

<!-- SR -->
How does ArrayList grow?:: Backed by an array that grows by about 1.5x when full. #flashcard
What is the cost of adding in the middle of an ArrayList?:: O(n) because elements shift. #flashcard
What is get by index cost in ArrayList?:: O(1). #flashcard
When should you size an ArrayList upfront?:: When you know the expected size, to avoid repeated resizing. #flashcard
