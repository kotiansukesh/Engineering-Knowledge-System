---
title: "Doubly Linked List"
category: DSA
tags: [dsa, linked-list]
created: 2026-01-18
updated: 2026-09-02
---

# Doubly Linked List

> Part of [[README|Java MOC]] • `DSA`

## Definition
A **doubly linked list** extends the singly linked list: each node stores `key`, `next`, and `prev` pointers. This enables **bidirectional traversal** and O(1) `PopBack` / `AddBefore` when the target node is known, at the cost of one extra pointer per node and more link maintenance.

- Node: `{ key, next, prev }`

![[Pasted image 20230728114551.png]]

## Operations — complexity

| Operation | No tail | With tail | Notes |
|---|---|---|---|
| `PushFront(key)` | **O(1)** | O(1) |  |
| `TopFront` | **O(1)** | O(1) |  |
| `PopFront` | **O(1)** | O(1) |  |
| `PushBack(key)` | **O(n)** | **O(1)** |  |
| `PopBack` | **O(1)**  | O(1) | Doubly → O(1) via `tail.prev` |
| `TopBack` | **O(n)** | **O(1)** |  |
| `Find(key)` | **O(n)** | O(n) |  |
| `Erase(key)` | **O(n)** | O(n) | Search dominates |
| `Empty()` | **O(1)** | O(1) |  |
| `AddBefore(node, key)` | **O(1)** | O(1) | Knows predecessor |
| `AddAfter(node, key)` | **O(1)** | O(1) |  |

## Algorithms (pseudocode)

#### PushBack(key)
```algorithm
node ← new Node; node.key ← key; node.next ← nil
if tail = nil:
  head ← tail ← node; node.prev ← nil
else:
  tail.next ← node; node.prev ← tail; tail ← node
```

#### PopBack()
```algorithm
if head = nil: ERROR empty
if head = tail: head ← tail ← nil
else: tail ← tail.prev; tail.next ← nil
```

#### AddAfter(node, key) — corrected
```algorithm
node2 ← new Node; node2.key ← key
node2.next ← node.next; node2.prev ← node
node.next ← node2
if node2.next ≠ nil: node2.next.prev ← node2
if tail = node: tail ← node2
```

#### AddBefore(node, key) — corrected
```algorithm
node2 ← new Node; node2.key ← key
node2.next ← node; node2.prev ← node.prev
node.prev ← node2
if node2.prev ≠ nil: node2.prev.next ← node2
if head = node: head ← node2
```

## Java 25 notes

- **Record Node:** `record Node<T>(T val, Node<T> next, Node<T> prev)` as immutable holder, or keep mutable class for bidirectional updates. Java 25 trend: record for data + separate structure for links.
- **Compact Object Headers (JEP 450):** doubly nodes have 2 pointers → header saving is proportionally huge (~16 B → 8 B per node).
- **SequencedCollection:** `java.util.LinkedList` is the stdlib doubly list, now `SequencedCollection` with `reversed()` view.
- **Pattern matching:** `if (node instanceof Node<T>(var v, var n, var p))` for destructuring.

## Java example — Java 25

```java

// Purpose: Doubly Linked List: prev+next links; O(1) both-ends insert; bidirectional traversal
// Representation: for, retained, DoublyLinkedList — records/nodes; contiguous vs linked trade-off
// Operations: push, pop
// Invariant: complexity assumes stated representation; handles empty/null boundaries
```

## Pitfalls
- **Four link updates** per insertion, missing one (`prev` or `next` on neighbour) corrupts the list.
- **Self-links on edge**, `AddBefore(head, ...)` must update `head`; `AddAfter(tail, ...)` must update `tail`.
- **Memory overhead**, two pointers per node; for tiny payloads consider `ArrayList`.
- **Iterator invalidation**, structural modification during traversal requires `ListIterator`.

## Interview Q&A
**Q: Singly vs Doubly, when to prefer doubly?** When `PopBack`, `AddBefore`, reverse traversal, or LRU cache (move-to-front) are frequent.

**Q: Can you implement LRU with it?** Yes, doubly list + `HashMap<key, Node>` gives O(1) `get`/`put` with eviction.

**Q: How to reverse a doubly list?** Swap `next`/`prev` for each node, then swap `head`/`tail`, O(n).


<!-- SR -->
Singly vs Doubly, when to prefer doubly?:: When `PopBack`, `AddBefore`, reverse traversal, or LRU cache (move-to-front) are frequent. #flashcard
Can you implement LRU with it?:: Yes, doubly list + `HashMap<key, Node>` gives O(1) `get`/`put` with eviction. #flashcard
How to reverse a doubly list?:: Swap `next`/`prev` for each node, then swap `head`/`tail`, O(n). #flashcard

## Related
- [[Linked List]] • [[Singly Linked List]] • [[Array]]
- [[README|Java MOC]]

## Solve with patterns
- [[Coding Patterns/02_LinkedList/01 - Fast and Slow Pointers]]

## Practice
- [146. Lru Cache](https://leetcode.com/problems/lru-cache/)
- [430. Problem 430](https://leetcode.com/problems/problem-430/)
- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)


---
*Category: DSA • Part of [[README|Java MOC]]*