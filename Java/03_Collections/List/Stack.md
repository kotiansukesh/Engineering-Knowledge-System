---
title: "Stack"
category: Collections
tags: [java, collections, list]
created: 2026-01-18
updated: 2026-09-02
---

# Stack — java.util.Stack

Legacy LIFO stack that extends Vector. It is synchronized. Prefer ArrayDeque for new code.

## Internals

- extends Vector, inherits a synchronized array with 2x growth
- adds push, pop, peek, empty and search
- because it extends Vector, you can still call get and add at index, which breaks LIFO encapsulation

## Time complexity

- push, pop, peek, empty: O(1)
- search: O(n), linear from top, returns 1 based position or minus 1

## Example

```java
// Stack vs Deque — legacy Stack (Vector) vs ArrayDeque for LIFO
var stack = new Stack<Integer>();
stack.push(10); stack.push(20); stack.push(30);
System.out.println(stack.peek());
System.out.println(stack.pop());
System.out.println(stack.search(10));
stack.add(0, 99);

Deque<Integer> s = new ArrayDeque<>();
s.push(10); s.push(20); s.push(30);
System.out.println(s.peek());
System.out.println(s.pop());

Deque<String> dq = new ArrayDeque<>();
dq.addLast("queue"); dq.pollFirst();
dq.push("stack"); dq.pop();
```

Rule: do not use Stack in new code. Use Deque as ArrayDeque.

## Stack vs ArrayDeque as stack

- backing: Stack is Vector, ArrayDeque is circular array
- thread safe: Stack yes coarse, ArrayDeque no
- encapsulation: Stack leaks indexed ops, ArrayDeque does not
- performance: ArrayDeque is faster

<!-- SR -->
Why is Stack flawed?:: It extends Vector and exposes indexed methods that break LIFO, plus synchronized overhead. #flashcard
What replaces Stack today?:: Deque as ArrayDeque with push, pop and peek. #flashcard
What does Stack.search return?:: 1 based position from the top, minus 1 if not found. #flashcard
How can one class act as both queue and stack?:: ArrayDeque as Deque, addLast and pollFirst for queue, push and pop for stack. #flashcard
