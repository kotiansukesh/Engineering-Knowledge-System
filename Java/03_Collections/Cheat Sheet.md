---
title: "Collections Cheat Sheet"
category: "Collections"
tags: [java, cheat-sheet, collections]
created: 2026-09-03
pattern: 0
difficulty: Easy
completed: false
reviewed: ""
sr-due: ""
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---## Diagram

```mermaid
flowchart TD
 C["Collection"] --> L["List: ArrayList, LinkedList, Vector"]
 C --> S["Set: HashSet, LinkedHashSet, TreeSet"]
 C --> Q["Queue: ArrayDeque, PriorityQueue"]
 M["Map (not a Collection)"] --> HM["HashMap, LinkedHashMap, TreeMap, ConcurrentHashMap"]
 SC["SequencedCollection (Java 21+)"] -.-> L
 SC -.-> S2["LinkedHashSet"]
 SM["SequencedMap (Java 21+)"] -.-> HM2["LinkedHashMap"]
```

## Code

```java
// Pick by ordering/null/concurrency; SequencedCollection for ends + reversed
var list = new java.util.ArrayList<>(java.util.List.of("b", "c"));
list.addFirst("a"); // Java 21+
System.out.println(list.getFirst() + " " + list.reversed());

var lru = new java.util.LinkedHashMap<>(16, 0.75f, true) {
 protected boolean removeEldestEntry(Map.Entry<Integer, String> e) { return size() > 100; }
};

var sorted = new java.util.TreeMap<>(Map.of("b", 2, "a", 1));
System.out.println(sorted.firstKey()); // => a

var pq = new java.util.PriorityQueue<Integer>(); // min-heap, top-k
for (int x : nums) { pq.offer(x); if (pq.size() > k) pq.poll(); }

var cow = new java.util.concurrent.CopyOnWriteArrayList<>(list); // read-heavy
```

## When to use / not

| Use | NOT |
|-----|-----|
| `ArrayList` by default: O(1) get, cache-friendly | `LinkedList` as a `List`, O(n) random access |
| `LinkedHashSet` to keep insertion order | `HashSet` when order matters |
| `TreeSet`/`TreeMap` for sorted + range queries | `TreeSet` when nulls are needed, rejected |
| `ConcurrentHashMap` for any shared map | `Collections.synchronizedMap`, global lock |
| `ArrayDeque` for stack and queue | the legacy `Stack` class |
| `computeIfAbsent`/`merge` for atomic load-or-compute | `containsKey` then `put`, a check-then-act race |

## Trade-offs

- One table answers implementation selection by ordering, duplicates, null, and cost.
- Java 21 `SequencedCollection` unifies first/last/reversed across `List`, `Deque`, `LinkedHashSet`.
- Big-O here is average case; `HashMap` degrades to O(log n) on treeified buckets, worst case matters in interviews.

## Vs

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

## Pitfalls

- `ArrayList` iterator is fail-fast; mutate via `Iterator.remove` or use copy-on-write.
- `HashMap` allows one null key; `ConcurrentHashMap` and `TreeMap` allow none.
- Mutable keys whose `hashCode` changes get lost in the bucket; keep keys immutable.
- `PriorityQueue` is not sorted overall, only the head is guaranteed.
- `Collections.synchronizedMap` iterators still need external `synchronized(map)`.

## Interview q&a

**Q: `ArrayList` vs `LinkedList`?** `ArrayList` for random access and cache locality; `LinkedList` only for `Deque` ends or mid-list `ListIterator` inserts.

**Q: How does `HashMap` handle collisions?** Chain in a bucket, treeify to red-black after 8 entries and table size 64, rehash at capacity × 0.75.

**Q: `HashSet` vs `TreeSet`?** Hash O(1) unordered; tree O(log n) sorted, no null.

**Q: `HashMap` vs `ConcurrentHashMap`?** CHM is thread-safe with striped/CAS locking, atomic `computeIfAbsent`, no nulls, weakly consistent iterators.

ArrayList vs LinkedList?:: ArrayList for random access and cache locality; LinkedList only for deque ends or mid-list ListIterator inserts. #flashcard
How does HashMap handle collisions?:: Chain then treeify after 8 entries, rehash at capacity times load factor 0.75. #flashcard
HashSet vs TreeSet?:: Hash O(1) unordered; tree O(log n) sorted and no null. #flashcard

## Related

- [[03_Collections/README|Collections MOC]] • [[Collection]] • [[List]] • [[Set]] • [[Queue]] • [[Map]]
- [[03_Collections/List/ArrayList|ArrayList]] • [[03_Collections/List/LinkedList|LinkedList]] • [[03_Collections/Set/HashSet|HashSet]] • [[03_Collections/Set/TreeSet|TreeSet]]
- [[08_Modern-Java/04 Sequenced Collections|Sequenced Collections (Java 21+)]]

# Collections , Cheat Sheet

## Hierarchy (Remember for MCQs)

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
| **EnumMap** | Enum order | , | No null key | Fastest Map for enum keys |
| **PriorityQueue** | Heap order | Yes | No | Min-heap, k-largest |
| **ArrayDeque** | Insertion | Yes | No | Stack & Queue , faster than Stack/LinkedList |

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

## Java 25 One-liners

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
