---
title: "Linked List"
category: DSA
tags: [dsa, linked-list]
created: 2026-01-18
updated: 2026-09-02
---

# Linked List

> Part of [[README|Java MOC]] • `DSA`

## Definition
A **linked list** is a linear data structure where elements (**nodes**) are not stored contiguously but are linked via **references/pointers**. Each node holds a key (value) and one or two pointers to neighbours. Size is dynamic; insertion/deletion at known positions is O(1) without shifting, at the cost of O(n) random access.

## Variants

| Variant | Node fields | Navigation | Extra memory |
|---|---|---|---|
| **[[Singly Linked List]]** | `key`, `next` | Forward only | 1 pointer |
| **[[Doubly Linked List]]** | `key`, `next`, `prev` | Forward & backward | 2 pointers |
| Circular (singly/doubly) | last node points to head | Wrap-around | — |
| With `tail` pointer | head + tail references | O(1) pushBack / topBack | 1 ref |

## Operations — complexity

| Operation | Singly (with tail) | Doubly (with tail) |
|---|---|---|
| `PushFront` / `PopFront` / `TopFront` | **O(1)** | **O(1)** |
| `PushBack` / `TopBack` | **O(1)** | **O(1)** |
| `PopBack` | **O(n)** (needs predecessor scan) | **O(1)** |
| `Find(key)` / `Erase(key)` | **O(n)** | **O(n)** |
| `AddAfter(node, key)` | **O(1)** | **O(1)** |
| `AddBefore(node, key)` | **O(n)** (find predecessor) | **O(1)** |
| `Empty()` | **O(1)** | **O(1)** |
| Random access `get(i)` | **O(n)** | **O(n)** |

Choose **singly** when memory matters and backward traversal is unnecessary; **doubly** when `PopBack`/`AddBefore`/LRU behaviour is frequent.

## Java example — Minimal Generic List Interface

```java

// Purpose: Linked List: node chain; O(1) head insert; O(n) search; pointer-based
// Representation: SimpleList, LinkedListDemo — records/nodes; contiguous vs linked trade-off
// Operations: push, pop
// Invariant: complexity assumes stated representation; handles empty/null boundaries
```

## Java 25 notes
- **Record Node:** `record Node<T>(T val, Node<T> next)` replaces `static class Node { T key; Node next; }`, immutable, auto `equals/hashCode`, compact. For mutable lists keep `next` via wrapper or use `record` for value + separate link array (or make `next` mutable via `AtomicReference` if needed).
- **SequencedCollection:** `LinkedList`/`ArrayDeque` implement `SequencedCollection`, `getFirst`/`getLast`/`addFirst`/`addLast`/`reversed()` are idiomatic Java 25.
- **Pattern matching:** `if (node instanceof Node<String>(var v, var nxt))` or `switch (node) { case Node(var v, var n) -> ...; case null -> ...; }` for null-safe traversal.
- **Compact Object Headers (JEP 450):** each linked node header shrinks to 8 B, big win for million-node lists (saves ~4-8 MB per 1M nodes).

## Pitfalls
- **Lost references**, forgetting to update `head`/`tail` or `prev`/`next` creates leaks or cycles.
- **PopBack on singly without tail scan**, O(n); often mistakenly assumed O(1).
- **`==` vs `equals`** when searching for keys of object type.
- **Concurrent modification**, iterating while mutating without `Iterator` throws `ConcurrentModificationException`.
- **Stack overflow** on recursive traversal of very long lists.

## Interview Q&A
**Q: Array vs Linked List?** Array: O(1) random access, cache-friendly, fixed capacity. List: O(1) insert at ends (with tail), dynamic size, O(n) access.

**Q: When to use `ArrayList` vs `LinkedList` in Java?** Effective Java / modern guidance: `ArrayList` almost always wins due to cache locality; `LinkedList` only when many mid-list inserts via `ListIterator`.

**Q: How to detect a cycle?** Floyd's tortoise-and-hare (two pointers at 1× and 2× speed).


<!-- SR -->
Array vs Linked List?:: Array: O(1) random access, cache-friendly, fixed capacity. List: O(1) insert at ends (with tail), dynamic size, O(n) access. #flashcard
When to use `ArrayList` vs `LinkedList` in Java?:: Effective Java / modern guidance: `ArrayList` almost always wins due to cache locality; `LinkedList` only when many mid-list inserts via `ListIterator`. #flashcard
How to detect a cycle?:: Floyd's tortoise-and-hare (two pointers at 1× and 2× speed). #flashcard

## Related
- [[Singly Linked List]] • [[Doubly Linked List]] • [[Array]] • [[Stack]] • [[Queue]]
- [[README|Java MOC]]

## Solve with patterns
- [[Coding Patterns/02_LinkedList/01 - Fast and Slow Pointers]]
- [[Coding Patterns/02_LinkedList/02 - LinkedList In-place Reversal]]

## Practice
- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)


---
*Category: DSA • Part of [[README|Java MOC]]*