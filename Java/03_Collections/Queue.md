---
title: "Queue"
category: Collections
tags: [java, collections, queue]
created: 2026-01-18
updated: 2026-09-02
---

# Queue — java.util.Queue

Part of [[README|Java MOC]]

Queue holds elements for processing. The usual order is FIFO, priority, or deque.

## Hierarchy

```
Collection -> Queue -> Deque
              |-- PriorityQueue (heap, natural or comparator)
              |-- ArrayDeque (circular array, also implements Deque)
              

BlockingQueue, TransferQueue are for concurrency.
```

Core methods have two forms. One throws, one returns a special value.

- add vs offer: insert, second returns false if full
- remove vs poll: remove head, second returns null if empty
- element vs peek: read head, second returns null if empty

Deque adds addFirst, addLast, pollFirst, pollLast, peekFirst, peekLast, and stack operations push and pop.

## Implementations

- ArrayDeque: circular array, no nulls, fastest for queue and stack, no capacity limit except memory
- LinkedList: doubly linked list, allows nulls, implements both List and Deque, but slower and heavier
- PriorityQueue: binary heap, not FIFO, sorted by priority, O(log n) offer and poll, iteration not sorted
- ArrayBlockingQueue, LinkedBlockingQueue, etc: blocking queues for producer consumer

## Example

```java
// Queue/Deque — FIFO vs priority vs stack (ArrayDeque preferred)
Queue<String> q = new ArrayDeque<>();
q.offer("a"); q.offer("b"); q.offer("c");
System.out.println(q.peek());
System.out.println(q.poll());
System.out.println(q);

Deque<String> stack = new ArrayDeque<>();
stack.push("a"); stack.push("b");
System.out.println(stack.pop());

Queue<Integer> pq = new PriorityQueue<>();
pq.addAll(List.of(5,1,3));
System.out.println(pq.poll());
System.out.println(pq.poll());

Queue<String> pq2 = new PriorityQueue<>(Comparator.comparingInt(String::length));
pq2.addAll(List.of("aaa","b","cc"));
System.out.println(pq2.poll());
```

## When to use which

- plain FIFO queue: ArrayDeque
- stack: ArrayDeque as Deque, not Stack
- priority: PriorityQueue
- blocking producer consumer: ArrayBlockingQueue or LinkedBlockingQueue

## Interview questions

Queue vs Deque?
Queue is FIFO from one end, Deque allows insertion and removal from both ends and can act as queue or stack.

How does PriorityQueue order elements?
Binary heap by natural order or comparator, head is smallest. Poll is O(log n).

Why prefer ArrayDeque over LinkedList for a queue?
ArrayDeque is backed by an array, less memory, better locality, O(1) ops, no node allocations.

<!-- SR -->
How does ArrayDeque implement a queue?:: Circular array, offer at tail and poll at head, both O(1). #flashcard
What is the difference between poll and remove?:: Poll returns null if empty, remove throws. #flashcard
How does PriorityQueue order elements?:: Heap ordered by natural order or comparator, head is the smallest. #flashcard
When to use ArrayDeque vs LinkedList?:: Prefer ArrayDeque for queue or stack, it is faster and more compact. #flashcard
