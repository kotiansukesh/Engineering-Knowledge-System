---
title: "Singly Linked List"
category: DSA
tags: [dsa, linked-list]
created: 2026-01-18
updated: 2026-09-02
---

# Singly Linked List

> Part of [[README|Java MOC]] • `DSA`

## Definition
A **singly linked list** is a chain of **nodes** where each node stores a `key` and a single pointer `next` to the successor. The list is accessed via `head` (first node) and optionally `tail` (last node). Traversal is **forward-only**.

- Node: `{ key, next }`
- Head: first node; Tail: last node (`tail.next == null`)

![[Pasted image 20230725103254.png]]

## Operations — complexity

| Operation | No tail | With tail | Notes |
|---|---|---|---|
| `PushFront(key)` | **O(1)** | O(1) | Prepend |
| `TopFront` | **O(1)** | O(1) |  |
| `PopFront` | **O(1)** | O(1) |  |
| `PushBack(key)` | **O(n)** | **O(1)** | Scan to end without tail |
| `PopBack` | **O(n)** | O(n) | Needs predecessor scan |
| `TopBack` | **O(n)** | **O(1)** |  |
| `Find(key)` | **O(n)** | O(n) | Linear scan |
| `Erase(key)` | **O(n)** | O(n) | Find + relink |
| `AddBefore(node, key)` | **O(n)** | O(n) | Must find predecessor |
| `AddAfter(node, key)` | **O(1)** | O(1) | Node known |

## Algorithms (pseudocode)

#### PushFront(key)
```algorithm
node ← new Node; node.key ← key; node.next ← head
head ← node
if tail = nil: tail ← head
```

#### PopFront()
```algorithm
if head = nil: ERROR empty
head ← head.next
if head = nil: tail ← nil
```

#### PushBack(key)
```algorithm
node ← new Node; node.key ← key; node.next ← nil
if tail = nil: head ← tail ← node
else: tail.next ← node; tail ← node
```

#### PopBack()
```algorithm
if head = nil: ERROR empty
if head = tail: head ← tail ← nil
else:
  p ← head
  while p.next.next ≠ nil: p ← p.next
  p.next ← nil; tail ← p
```

#### AddAfter(node, key)
```algorithm
node2 ← new Node; node2.key ← key
node2.next ← node.next; node.next ← node2
if tail = node: tail ← node2
```

## Java 25 notes

- **Record Node (Java 25 idiom):** `record Node<T>(T val, Node<T> next) {}` replaces the inner class, concise, immutable value holder. For mutable `next` in algorithms, use `record Node<T>(T val, Node<T> next)` with reassignment via new record `head = new Node<>(key, head)` (persistent style) or keep a mutable wrapper for imperative code.
- **Compact Object Headers (JEP 450, Java 25):** `-XX:+UseCompactObjectHeaders` compresses headers to 8 B, tightens per-node overhead (saves ~30% for singly lists with millions of nodes).
- **SequencedCollection:** expose `getFirst()`/`getLast()`/`reversed()` when wrapping JDK collections.
- **Pattern matching in traversal:** replaces manual `x != null && x.next != null` with `if (curr instanceof Node<T>(var v, var nxt))`.

## Java example — Java 25

```java

// Purpose: Singly Linked List: forward-only links; O(1) head insert; O(n) traversal
// Representation: SinglyLinkedList, Node, alternative — records/nodes; contiguous vs linked trade-off
// Operations: push, pop
// Invariant: complexity assumes stated representation; handles empty/null boundaries
```

## Pitfalls
- **PopBack is O(n)**, frequently mistaken for O(1); use doubly linked list if `popBack` is hot.
- **Dangling `tail`** after `PopFront` on last element, must set `tail = null`.
- **Null key handling**, `Objects.equals` not `==`.
- **Cycle creation**, `node.next = node` creates self-loop; careful in `AddAfter`.

## Interview Q&A
**Q: Reverse a singly linked list?** Iterative three-pointer (`prev/curr/next`) O(n) time O(1) space; or recursion O(n) stack.

**Q: Find middle in one pass?** Slow/fast pointers.

**Q: When is `PushBack` O(1) without tail?** Never, need tail or circular trick; otherwise O(n).


<!-- SR -->
Reverse a singly linked list?:: Iterative three-pointer (`prev/curr/next`) O(n) time O(1) space; or recursion O(n) stack. #flashcard
Find middle in one pass?:: Slow/fast pointers. #flashcard
When is `PushBack` O(1) without tail?:: Never, need tail or circular trick; otherwise O(n). #flashcard

## Related
- [[Linked List]] • [[Doubly Linked List]] • [[Stack]] • [[Queue]]
- [[README|Java MOC]]

## Solve with patterns
- [[Coding Patterns/02_LinkedList/01 - Fast and Slow Pointers]]
- [[Coding Patterns/02_LinkedList/02 - LinkedList In-place Reversal]]

## Practice
- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [876. Middle Of The Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)


---
*Category: DSA • Part of [[README|Java MOC]]*