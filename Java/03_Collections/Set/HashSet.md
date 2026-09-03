---
title: "HashSet"
category: Collections
tags: [java, collections, set]
created: 2026-01-18
updated: 2026-09-02
---

# HashSet — java.util.HashSet

Default Set. Hash table, no order, no duplicates, one null allowed. Fastest membership test. Backed by HashMap.

## Internals

- wraps HashMap with element as key and a dummy PRESENT as value
- capacity is number of buckets, default 16, load factor 0.75, rehash when size exceeds capacity times load factor
- hash to bucket index, collisions go to a list then to a tree at 8 entries
- no ordering, iteration order can change across runs

## Time complexity

- add, contains, remove: O(1) average, O(log n) worst after treeify
- iteration: O(capacity plus size)
- addAll: O(n)

## Example

```java
// HashSet — hash table, unique, one null, O(1) avg
var set = new HashSet<String>();
set.add("A"); set.add("B"); set.add("A"); set.add(null);
System.out.println(set);
System.out.println(set.contains("A"));

Set<Integer> deduped = new HashSet<>(List.of(1,2,2,3));

// Record — correct equals/hashCode for HashSet membership
record User(int id, String name) {}
Set<User> users = new HashSet<>();
users.add(new User(1,"Ada"));
users.add(new User(1,"Ada"));
System.out.println(users.size());

Set<Integer> big = new HashSet<>(10_000, 0.75f);
```

Fail fast iterator: structural change after creating an iterator causes ConcurrentModificationException on next use.

## HashSet vs LinkedHashSet vs TreeSet

- HashSet: HashMap, no order, O(1), one null, lowest memory, fastest for membership
- LinkedHashSet: LinkedHashMap, insertion order, O(1), one null, higher memory
- TreeSet: TreeMap, sorted, O(log n), no null, highest memory, supports ranges

Pick HashSet unless you need order or sorting.

<!-- SR -->
How is HashSet implemented?:: Wrapper over HashMap, element is key, dummy PRESENT is value. #flashcard
When does HashSet rehash?:: When size exceeds capacity times load factor, default 0.75, then table doubles. #flashcard
Why override hashCode with equals for HashSet elements?:: Hash picks the bucket, equals confirms the match, mismatched hashes cause duplicates and missed lookups. #flashcard
Can HashSet hold null? Can TreeSet?:: HashSet yes one null, TreeSet no. #flashcard
Is HashSet iteration order insertion order?:: No, it is undefined and can change, use LinkedHashSet for insertion order. #flashcard
