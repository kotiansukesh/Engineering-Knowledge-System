---
title: "Sorted set"
category: Collections
tags: [java, collections, set]
created: 2026-01-18
updated: 2026-09-02
---

# Sorted set — java.util.SortedSet and NavigableSet

Set with sorted iteration by natural order or a Comparator. No duplicates, no null, with range view operations.

## Hierarchy

```
Set
  -> SortedSet (first, last, comparator, subSet, headSet, tailSet)
    -> NavigableSet (lower, floor, ceiling, higher, pollFirst, pollLast, descendingSet)
      -> TreeSet (the JDK implementation)
```

## Contract

- sorted, not indexed
- no duplicates, no null
- extra ops: first, last, subSet from inclusive to exclusive, headSet, tailSet

## Time complexity with TreeSet

- add, contains, remove: O(log n)
- first, last: O(log n)
- subSet, headSet, tailSet: O(log n) to find plus O(k) to traverse
- lower, floor, ceiling, higher: O(log n)

## Example

```java
// SortedSet — sorted unique view (TreeSet/NavigableSet)
var sorted = new TreeSet<>(List.of(5,1,3,2,5));
System.out.println(sorted);
System.out.println(sorted.first());
System.out.println(sorted.last());
System.out.println(sorted.subSet(2,5));
System.out.println(sorted.headSet(3));
System.out.println(sorted.tailSet(3));

SortedSet<String> byLen = new TreeSet<>(Comparator.comparingInt(String::length));
byLen.addAll(List.of("a","bbb","cc"));
System.out.println(byLen);

NavigableSet<Integer> nav = new TreeSet<>(List.of(10,20,30));
System.out.println(nav.lower(20));
System.out.println(nav.floor(20));
System.out.println(nav.ceiling(25));
System.out.println(nav.higher(20));

SortedSet<Integer> view = nav.subSet(10,30);
view.add(15);
System.out.println(nav);
```

## SortedSet vs HashSet vs LinkedHashSet

- HashSet: no order, O(1), one null
- LinkedHashSet: insertion order, O(1), one null
- SortedSet via TreeSet: sorted, O(log n), no null, supports ranges and nearest match

<!-- SR -->
What is the difference between SortedSet and NavigableSet?:: SortedSet gives first last and subset views, NavigableSet adds lower floor ceiling higher and descendingSet. #flashcard
Can SortedSet hold null?:: No, null cannot be compared. #flashcard
How to get descending order?:: Use TreeSet with reverseOrder or call descendingSet. #flashcard
Are subSet views copies?:: No, they are backed views, changes show in both. #flashcard
