---
title: "LinkedList"
category: Collections
tags: [java, collections, list]
created: 2026-01-18
updated: 2026-09-04
---
## Why it Matters

A **doubly-linked `List` + `Deque`** in one class: **O(1) at both ends**, O(n) by index. The only JDK list that is also a queue , but heavier per element than `ArrayDeque`, so prefer the latter for pure queues.

## Diagram

```mermaid
flowchart LR
 H["head"] --> N1["node(prev,item,next)"]
 N1 --> N2["node"]
 N2 --> T["tail"]
 T -. prev .-> N2
```

## Code

```java
// LinkedList — doubly-linked List+Deque, O(n) index, O(1) ends
var list = new LinkedList<String>();
list.add("b"); list.add("c");
list.addFirst("a");
System.out.println(list); // => [a, b, c]
System.out.println(list.get(1)); // => b
list.pollFirst();
list.pollLast();

Deque<String> dq = new LinkedList<>();
dq.offer("a"); dq.offer("b");
System.out.println(dq.poll()); // => a

Deque<String> fast = new ArrayDeque<>(List.of("a","b"));
```

## When to use / not

| Use | NOT |
|-----|-----|
| Need `List` + `Deque` ends in one object | Pure queue/stack → `ArrayDeque` is faster and smaller |
| Frequent add/remove at ends via iterator | Random access (`get(i)` is O(n)) |
| Bidirectional traversal | Memory-tight workloads (node overhead) |

## Trade-offs

- O(1) at both ends; `List` + `Deque` in one object.
- O(n) index access; high per-node memory; poor cache locality.
- Almost always beaten by `ArrayList` (list use) or `ArrayDeque` (deque use).

## Vs

- random access: ArrayList O(1), LinkedList O(n), ArrayDeque none
- add at ends: LinkedList O(1), ArrayDeque O(1), ArrayList amortized O(1) but shifts for insert
- memory: ArrayList lowest for dense data, LinkedList highest
- iteration: ArrayList most cache friendly

## Pitfalls

- `get(i)` walks from the nearer end , still O(n); never index-loop a `LinkedList`.
- As a `Queue`, `ArrayDeque` beats it on memory and speed , justify each `LinkedList`.
- Mid-list mutation needs `ListIterator`, not index math.

## Interview q&a

**Q: How is `LinkedList` implemented?** Doubly-linked nodes (`prev`, `item`, `next`) with head/tail pointers; O(1) at ends, O(n) by index (walks from nearer end).

**Q: When is it better than `ArrayList`?** Frequent insert/remove at ends with deque ops in one object , otherwise `ArrayList` (list) or `ArrayDeque` (queue) wins.

**Q: Why is `ArrayDeque` preferred for queues?** Circular array: less memory, better locality, no node allocation.

## Related

- [[Java/03_Collections/List/List|List]] • [[Java/03_Collections/Queue|Queue]] (`ArrayDeque` preferred)
- [[Java/07_DSA/Linked List|Linked List (DSA)]] (nodes, O(1) ends)

How is LinkedList implemented?:: Doubly linked nodes with prev and next pointers plus head and tail. #flashcard
What is get by index cost in LinkedList?:: O(n), it walks from the closer end. #flashcard
When is LinkedList better than ArrayList?:: When you need frequent insert or remove at the ends and deque operations. #flashcard
Why is ArrayDeque often preferred over LinkedList for a queue?:: ArrayDeque uses a circular array, less memory and better locality. #flashcard

# LinkedList , Java.util.LinkedList

> Part of [[Java/03_Collections/List/List|List]]

> LinkedList is a doubly linked list that implements both List and Deque. It allows duplicates and nulls.

## Internals

- each element is a node with prev, next and item
- maintains head and tail pointers
- not synchronized
- bidirectional iteration

## Time Complexity

- addFirst, addLast, pollFirst, pollLast: O(1)
- get by index: O(n), walks from nearer end
- add or remove in middle: O(n) to find, O(1) to link
- contains: O(n)
- memory: more per element than ArrayList due to nodes
