---
title: "LinkedList"
category: Collections
tags: [java, collections, list]
created: 2026-01-18
updated: 2026-09-02
---

# LinkedList — java.util.LinkedList

Part of [[List]]

LinkedList is a doubly linked list that implements both List and Deque. It allows duplicates and nulls.

## Internals

- each element is a node with prev, next and item
- maintains head and tail pointers
- not synchronized
- bidirectional iteration

## Time complexity

- addFirst, addLast, pollFirst, pollLast: O(1)
- get by index: O(n), walks from nearer end
- add or remove in middle: O(n) to find, O(1) to link
- contains: O(n)
- memory: more per element than ArrayList due to nodes

## Example

```java
// LinkedList — doubly-linked List+Deque, O(n) index, O(1) ends
var list = new LinkedList<String>();
list.add("b"); list.add("c");
list.addFirst("a");
System.out.println(list);
System.out.println(list.get(1));
list.pollFirst();
list.pollLast();

Deque<String> dq = new LinkedList<>();
dq.offer("a"); dq.offer("b");
System.out.println(dq.poll());

Deque<String> fast = new ArrayDeque<>(List.of("a","b"));
```

## When to use it

Use LinkedList when you need both List and Deque operations and frequent insert or remove at the ends. For pure queue or stack, ArrayDeque is more compact and faster.

Many codebases now avoid LinkedList except where bidirectional list semantics matter.

## LinkedList vs ArrayList vs ArrayDeque

- random access: ArrayList O(1), LinkedList O(n), ArrayDeque none
- add at ends: LinkedList O(1), ArrayDeque O(1), ArrayList amortized O(1) but shifts for insert
- memory: ArrayList lowest for dense data, LinkedList highest
- iteration: ArrayList most cache friendly

<!-- SR -->
How is LinkedList implemented?:: Doubly linked nodes with prev and next pointers plus head and tail. #flashcard
What is get by index cost in LinkedList?:: O(n), it walks from the closer end. #flashcard
When is LinkedList better than ArrayList?:: When you need frequent insert or remove at the ends and deque operations. #flashcard
Why is ArrayDeque often preferred over LinkedList for a queue?:: ArrayDeque uses a circular array, less memory and better locality. #flashcard
