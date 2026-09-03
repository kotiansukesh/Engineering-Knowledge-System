---
title: "TreeSet"
category: Collections
tags: [java, collections, set]
created: 2026-01-18
updated: 2026-09-02
---

# TreeSet — java.util.TreeSet

Sorted unique set backed by TreeMap. No duplicates, no null, sorted iteration, O(log n). Implements NavigableSet and SortedSet.

## Internals

- wraps TreeMap with element as key and dummy PRESENT as value
- red black balanced tree, guarantees O(log n) height
- ordering by natural Comparable or a Comparator given at construction
- compare defines equality for the set, if compare returns 0 the element is treated as duplicate even if equals differs

## Time complexity

- add, remove, contains: O(log n)
- first, last: O(log n)
- lower, floor, ceiling, higher: O(log n)
- subSet, headSet, tailSet: O(log n) plus O(k)
- iteration: O(n) sorted
- pollFirst, pollLast: O(log n)

## Example

```java
// TreeSet — Red-Black tree via TreeMap, O(log n), sorted, no null
var ts = new TreeSet<>(List.of(5,1,3,2,5));
System.out.println(ts);
System.out.println(ts.first());
System.out.println(ts.last());

TreeSet<String> ci = new TreeSet<>(String.CASE_INSENSITIVE_ORDER);
ci.add("Banana"); ci.add("apple"); ci.add("APPLE");
System.out.println(ci);

System.out.println(ts.lower(3));
System.out.println(ts.higher(3));
System.out.println(ts.floor(3));
System.out.println(ts.ceiling(4));
System.out.println(ts.subSet(2,true,5,false));

System.out.println(ts.pollFirst());
System.out.println(ts.descendingSet());

// Custom domain type — Comparator defines TreeSet ordering
record Student(String name, int score) {}
TreeSet<Student> byScore = new TreeSet<>(Comparator.comparingInt(Student::score));
byScore.add(new Student("Ada",90)); byScore.add(new Student("Bob",85));
System.out.println(byScore.first());
```

If compare says 0 but equals says false, the set still treats it as duplicate.

## TreeSet vs HashSet vs LinkedHashSet

- backing: HashMap vs LinkedHashMap vs TreeMap
- order: none vs insertion vs sorted
- cost: O(1) vs O(1) vs O(log n)
- null: allowed vs allowed vs not allowed
- needs Comparable: only TreeSet
- range ops: only TreeSet

Pick TreeSet when you need sorted uniqueness or range and nearest queries, otherwise HashSet is faster.

<!-- SR -->
How is TreeSet implemented?:: Wrapper over TreeMap, red black tree, comparator defines order and duplicates. #flashcard
How does TreeSet compare to HashSet?:: HashSet is hash table O(1) no order one null, TreeSet is tree O(log n) sorted no null. #flashcard
Can TreeSet hold null or mixed types?:: No, null fails on compare and mixed incomparable types throw ClassCastException. #flashcard
Why can TreeSet treat unequal objects as duplicates?:: It uses compare to zero for equality, not equals. #flashcard
When to prefer TreeSet?:: When you need sorted iteration, ranges or nearest match like leaderboards and interval scheduling. #flashcard
