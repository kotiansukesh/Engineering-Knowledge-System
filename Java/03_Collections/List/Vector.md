---
title: "Vector"
category: Collections
tags: [java, collections, list]
created: 2026-01-18
updated: 2026-09-02
---

# Vector — java.util.Vector

Legacy synchronized resizable array from Java 1.0. Ordered, indexed, allows duplicates and nulls. Prefer ArrayList for new code.

## Internals

- synchronized methods, so thread safe per operation but coarse grained
- default capacity 10, grows by 2x when full (or by increment if set)
- implements List, not SequencedCollection in Java 21

## Time complexity

- get, set, add at end: O(1) amortized
- insert or remove in middle: O(n)
- synchronized adds overhead

## Example

```java
// Vector — legacy synchronized array (prefer ArrayList/CopyOnWriteArrayList)
var v = new Vector<String>();
v.add("a"); v.add("b");
System.out.println(v.get(0));

List<String> list = new ArrayList<>(List.of("a","b"));
List<String> sync = Collections.synchronizedList(new ArrayList<>(list));
List<String> cow = new CopyOnWriteArrayList<>(list);
```

Stack extends Vector and inherits the same issues, use ArrayDeque for a stack.

## Vector vs ArrayList

- backing: both arrays, Vector synchronized, ArrayList not
- growth: Vector 2x, ArrayList 1.5x
- performance: ArrayList faster due to no lock
- recommendation: ArrayList by default, concurrent collections for shared access

<!-- SR -->
What is Vector?:: Legacy synchronized resizable array, prefers ArrayList now. #flashcard
How does Vector grow?:: Doubles capacity when full, or by the configured increment. #flashcard
What replaces Vector in modern code?:: ArrayList, or CopyOnWriteArrayList or synchronizedList for thread safety. #flashcard
