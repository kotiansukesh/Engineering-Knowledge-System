---
title: "Set"
category: Collections
tags: [java, collections, set]
created: 2026-01-18
updated: 2026-09-02
---

# Set — java.util.Set

No duplicates, no index. Membership with contains is the main operation. Backed by a Map internally.

Since Java 21, SequencedSet adds getFirst, getLast and reversed for LinkedHashSet.

## Contract

- no duplicates, add returns false if already present
- no index, no get by position
- one null allowed in HashSet and LinkedHashSet, not in TreeSet
- equals means same size and every element contained in the other

## When to use it vs List or Map

- need uniqueness, dedup, membership test: Set
- need order, index and duplicates: List
- need key to value: Map

## Methods

- add, contains, remove, size, isEmpty
- addAll, retainAll for intersection, removeAll for difference
- iterator

## Implementations

- HashSet backed by HashMap, no order, fastest, default choice. See [[HashSet]]
- LinkedHashSet backed by LinkedHashMap, insertion order, slightly heavier
- TreeSet backed by TreeMap, sorted, range ops, O(log n). See [[TreeSet]] and [[Sorted Set]]
- EnumSet bit vector for enums, very fast

## Example

```java
// Set — unique elements; HashSet/LinkedHashSet/TreeSet trades
var set = new HashSet<>(List.of("B","A","C","A"));
System.out.println(set);
System.out.println(set.add("A"));
System.out.println(set.contains("B"));

List<Integer> nums = List.of(1,2,2,3,3,3);
Set<Integer> unique = new HashSet<>(nums);

Set<String> ordered = new LinkedHashSet<>(List.of("B","A","C","A"));
System.out.println(ordered);

Set<Integer> sorted = new TreeSet<>(List.of(5,1,3,1));
System.out.println(sorted);

Set<Integer> a = new HashSet<>(Set.of(1,2,3));
Set<Integer> b = Set.of(2,3,4);
a.retainAll(b);
```

## Pitfalls

- mutating an element so hashCode or equals changes while in a HashSet loses the element, contains and remove fail
- TreeSet needs Comparable or a Comparator at construction, otherwise ClassCastException
- HashSet iteration order is not stable across runs

<!-- SR -->
How does HashSet avoid duplicates?:: Backed by HashMap, element is the key, add delegates to map put. #flashcard
What breaks if you mutate an element in a HashSet?:: Hash code changes and the bucket mismatches, so lookups fail. #flashcard
When to use Set vs List?:: Set for uniqueness and fast membership, List for order and index. #flashcard
How to dedup while keeping order?:: Use a LinkedHashSet, for example new ArrayList<>(new LinkedHashSet<>(list)). #flashcard
