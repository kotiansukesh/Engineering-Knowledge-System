---
title: "HashMap (DSA)"
category: DSA
tags: [dsa, hashmap, hashtable]
created: 2026-01-18
updated: 2026-09-02
---

# HashMap (DSA)

> Part of [[README|Java MOC]] • `DSA`

## Definition
A **HashMap / Hash Table** is a **[[Map]]** implementation that maps **keys → values** via a **hash function**: `index = hash(key) % capacity`. It provides expected **O(1)** `get`/`put`/`remove` by indexing into an array of **buckets**, each holding a chain (linked list / tree) for collisions. Transformation of a key to a fixed-length hash enables fast indexing.

- **Hashing**, `hash(key)` → integer → bucket index. Good hash spreads keys uniformly.

![[Pasted image 20230727120429.png]]

## Structure

```
hash(key) → bucket index
┌──────────────────────────────────┐
│ buckets: Array<Node<K,V>>        │
│ [0] → Node(k1,v1) → Node(k2,v2) │  (chain)
│ [1] → null                       │
│ [2] → Node(k3,v3) → (tree if long chain, Java 8+) │
│ ...                              │
└──────────────────────────────────┘
  collision → chaining (or open addressing in other designs)
```

**Java 8+ optimisation:** when a bucket's chain length ≥ 8 and capacity ≥ 64, it treeifies into a red-black tree → worst-case O(log n) instead of O(n).

## Operations — complexity

| Operation | Average | Worst (many collisions) | Notes |
|---|---|---|---|
| `put(key, val)` | **O(1)** | O(log n) tree / O(n) list | Rehash on load factor |
| `get(key)` | **O(1)** | O(log n) / O(n) |  |
| `remove(key)` | **O(1)** | O(log n) / O(n) |  |
| `containsKey` | **O(1)** | O(log n) / O(n) |  |
| Traverse / `entrySet` | **O(n)** | O(n) |  |
| Resize (rehash) | **O(n)** | O(n) | Amortised |

**Load factor** (default 0.75) = `size / capacity`; when exceeded, capacity doubles and all entries are rehashed.

## Java example

```java

// Purpose: HashMap: hash buckets + chaining; O(1) avg get/put; rehash on load factor
// Representation: HashMapDemo, equals, collapses — records/nodes; contiguous vs linked trade-off
// Operations: insert
// Invariant: complexity assumes stated representation; handles empty/null boundaries
```

## Java 25 notes
- **Record keys:** `record User(int id, String name)` auto-generates correct `equals/hashCode`, eliminates broken-contract bug.
- **Pattern instanceof:** `if (o instanceof User(int id, String name))` (record pattern, Java 21/25) for destructuring keys.
- **SequencedMap:** `LinkedHashMap` now `SequencedMap`, `firstEntry()`/`lastEntry()`/`reversed()` replace manual iteration for LRU ordered maps.
- **Compact Object Headers (JEP 450):** each bucket `Node` header 8 B → HashMap with 1M entries saves ~8 MB. Mention in interviews on memory tuning.

## Pitfalls
- **Broken `hashCode`/`equals` contract**, equal objects must have equal hash codes; mutating a key after insertion corrupts the map.
- **Mutable keys**, changing a field that affects `hashCode` after `put` makes `get` fail.
- **`null` keys**, `HashMap` allows one `null` key (bucket 0); `Hashtable`/`ConcurrentHashMap` do not.
- **Iteration order is not insertion order**, use `LinkedHashMap` for that; `TreeMap` for sorted order.
- **Not thread-safe**, concurrent `put` can cause infinite loops (pre-Java 8) or lost updates; use `ConcurrentHashMap` or external sync.
- **Poor hash function**, many collisions degrade to O(n); ensure uniform distribution.
- **Capacity vs load factor tuning**, small initial capacity + many puts causes repeated rehashing.

## Interview Q&A
**Q: `HashMap` vs `HashTable` vs `ConcurrentHashMap`?** `HashMap` non-sync, allows null; `Hashtable` legacy sync, no nulls; `ConcurrentHashMap` segmented/CAS, high concurrency, no nulls, fail-safe iteration.

**Q: What happens when two keys collide?** Chaining, stored in same bucket's linked list / tree; lookup walks the chain.

**Q: Why treeify buckets in Java 8?** To bound worst-case from O(n) to O(log n) under hash-collision attack (many keys with same hash).

**Q: Time complexity of resize?** O(n) to rehash all entries; amortised O(1) per `put`.

Reference: [How HashMap works in Java, Animation (Java 8)](https://www.youtube.com/watch?v=c3RVW3KGIIE)


<!-- SR -->
`HashMap` vs `HashTable` vs `ConcurrentHashMap`?:: `HashMap` non-sync, allows null; `Hashtable` legacy sync, no nulls; `ConcurrentHashMap` segmented/CAS, high concurrency, no nulls, fail-safe iteration. #flashcard
What happens when two keys collide?:: Chaining, stored in same bucket's linked list / tree; lookup walks the chain. #flashcard
Why treeify buckets in Java 8?:: To bound worst-case from O(n) to O(log n) under hash-collision attack (many keys with same hash). #flashcard
Time complexity of resize?:: O(n) to rehash all entries; amortised O(1) per `put`. Reference: [How HashMap works in Java, Animation (Java 8)](https://www.youtube.com/watch?v=c3RVW3KGIIE) #flashcard

## Related
- [[Array]] • [[Linked List]] • [[Trees]] (bucket tree)
- [[README|Java MOC]]

## Solve with patterns
- [[Coding Patterns/01_Array/01 - Prefix Sum]]
- [[Coding Patterns/01_Array/04 - Frequency Counting]]
- [[Coding Patterns/03_Stack_Heap/02 - Top K Elements]]
- [[Coding Patterns/08_Bit_Manipulation/01 - Bit Manipulation]]

## Practice
- [1. Two Sum](https://leetcode.com/problems/two-sum/)
- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)


---
*Category: DSA • Part of [[README|Java MOC]]*