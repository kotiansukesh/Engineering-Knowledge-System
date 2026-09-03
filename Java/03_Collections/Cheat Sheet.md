---
category: CheatSheet
tags: [java, collections, cheatsheet]
title: Collections — Cheat Sheet
## Practice
- [1. Two Sum](https://leetcode.com/problems/two-sum/)
- [215. Kth Largest Element In An Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)


---

# Collections — Cheat Sheet

## Hierarchy (remember for MCQs)

`Collection → List / Set / Queue` + `Map` (separate) + `Deque`

| Interface | Ordered? | Duplicates? | Null? | Use When |
|---|---|---|---|---|
| **ArrayList** | Yes (index) | Yes | Yes | Random access, mostly reads |
| **LinkedList** | Yes | Yes | Yes | Deque ops; rarely as List |
| **HashSet** | No | No | 1 null | Fast membership, no order |
| **LinkedHashSet** | Insertion | No | 1 null | Preserve insertion order |
| **TreeSet** | Sorted (Red-Black) | No | No (comparator NPE) | Sorted + range queries |
| **EnumSet** | Enum order | No | No | Fastest Set for enums (bit vector) |
| **HashMap** | No | Keys unique | 1 null key | General map |
| **LinkedHashMap** | Insertion / Access-order | Keys unique | 1 null | LRU cache (`accessOrder=true`) |
| **TreeMap** | Sorted by key | Keys unique | No null key | Sorted map, `subMap`, `ceilingKey` |
| **EnumMap** | Enum order | — | No null key | Fastest Map for enum keys |
| **PriorityQueue** | Heap order | Yes | No | Min-heap, k-largest |
| **ArrayDeque** | Insertion | Yes | No | Stack & Queue — faster than Stack/LinkedList |

## Time Complexities

| Structure | get / contains | add / put | remove | Notes |
|---|---|---|---|---|
| **ArrayList** | O(1) / O(n) | O(1) amortized; O(n) insert mid | O(n) shift | Resize 1.5× |
| **LinkedList** | O(n) | O(1) ends | O(1) if iterator | Bad cache locality |
| **HashMap/HashSet** | O(1) avg, O(log n) treeified | O(1) avg | O(1) avg | Bucket → linked list → RB tree at threshold 8 |
| **LinkedHashMap** | O(1) | O(1) | O(1) | Doubly-linked bucket order |
| **TreeMap/TreeSet** | O(log n) | O(log n) | O(log n) | Red-Black tree |
| **PriorityQueue** | O(n) contains; O(1) peek | O(log n) | O(log n) poll | Heap array |
| **ArrayDeque** | O(1) peek | O(1) both ends | O(1) | Circular array, no null |

## Vs Tables

| Comparison | A | B | Pick |
|---|---|---|---|
| **ArrayList vs LinkedList** | AL: O(1) random, O(n) insert mid | LL: O(n) random, O(1) insert via iterator | Default to ArrayList; LL only as Deque |
| **HashMap vs TreeMap** | HM: O(1), unordered, 1 null | TM: O(log n), sorted, no null, `NavigableMap` | HM unless ordering needed |
| **HashSet vs TreeSet** | HS: O(1) | TS: O(log n) sorted | Same as Map analogue |
| **PriorityQueue vs TreeSet** | PQ: duplicates, heap, O(n) contains | TS: unique, sorted, O(log n) contains | PQ for top-k; TS for sorted unique |
| **Fail-Fast vs Fail-Safe** | `ArrayList` iterator → CME on mod | `CopyOnWriteArrayList`, `ConcurrentHashMap` iterators snapshot | Never modify while iterating fail-fast |
| **Comparable vs Comparator** | `compareTo` (natural order) | `Comparator` (external, multiple) | Implement Comparable for natural; Comparator for custom sorts |

```mermaid
flowchart LR
    bucket["bucket[i]"] --> n1["Node(hash,key,val,next)"] --> n2["Node"] --> n3["..."]
    n3 -. treeify threshold 8 .-> tree["RB-Tree Node"]
    style bucket fill:#1a1a2e,stroke:#e94560,color:#fff
    style tree fill:#16213e,stroke:#0f3460,color:#fff
```

> **HashMap internals:** `hash = key.hashCode() ^ (hash>>>16)`, index ` (n-1) & hash`, load factor 0.75. Java 8+: list → tree when bin ≥ 8 and table ≥ 64.

## Java 25 One-Liners

```java
// Collections — factories, LRU, heap idioms
var list = List.of(1,2,3); var map = Map.of("a",1,"b",2); var set = Set.of(1,2,3);

var first = list.getFirst(); var last = list.getLast(); var rev = list.reversed();

list.sort(Comparator.comparing(User::age).thenComparing(User::name).reversed());

var byDept = users.stream().collect(Collectors.groupingBy(User::dept));
var top3 = users.stream().sorted(comparing(User::salary).reversed()).limit(3).toList();

map.computeIfAbsent(key, k -> new ArrayList<>()).add(val);
map.merge(word, 1, Integer::sum);
var val = map.getOrDefault(key, -1);

Map<Integer,String> lru = new LinkedHashMap<>(16,0.75f,true){
    protected boolean removeEldestEntry(Map.Entry<Integer,String> e){ return size()>100; }
};

var minHeap = new PriorityQueue<Integer>();
var maxHeap = new PriorityQueue<Integer>(Comparator.reverseOrder());
var pq = new PriorityQueue<Integer>(); for(int x: nums){ pq.offer(x); if(pq.size()>k) pq.poll(); }

var cow = new CopyOnWriteArrayList<>(list);
```

*Category: CheatSheet*
