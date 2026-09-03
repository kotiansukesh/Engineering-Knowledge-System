---
title: "LinkedList In-place Reversal"
pattern: 5
category: LinkedList
tags: [pattern/linkedlist, reversal]
leetcode: [206, 92, 24]
created: 2026-09-02
source: "https://blog.algomaster.io/p/20-dsa-patterns"
---

# Linked list in place reversal

> Part of [[README|20 DSA Patterns]], Pattern #5

## Definition

Flip `next` pointers with three variables: `prev`, `curr`, `next`. One pass, O(1) space. Example: `1→2→3→null` → iterate: `prev=null,curr=1` → `next=2, curr.next=prev, prev=1,curr=2` → repeat → result `3→2→1→null`.

For sublist `[m,n]` anchor `prev` before `m`, then move each next node to front of the sublist. For k-groups, reverse each group and link.

## When to use

- Reverse whole list, reverse between m and n, reverse in k-groups, palindrome check, reorder list
- Question says "in O(1) extra space"

## Complexity

| time | space |
|---|---|
| O(n) | O(1) |

## Java example

```java
record ListNode(int val, ListNode next) {}

// Reverse entire list, LC 206
ListNode reverseList(ListNode head) {
    ListNode prev = null; var curr = head;
    while (curr != null) {
        var nxt = curr.next();
        // need mutable version for interview: curr.next = prev
        // with record, rebuild: curr = new ListNode(curr.val(), prev)
        // below uses classic mutable node for clarity
        curr.next = prev;
        prev = curr;
        curr = nxt;
    }
    return prev;
}

// Mutable node version commonly used in interviews:
class Node { int val; Node next; Node(int v){val=v;} }

Node reverse(Node head) {
    Node prev = null; var cur = head;
    while (cur != null) {
        var nxt = cur.next;
        cur.next = prev;
        prev = cur;
        cur = nxt;
    }
    return prev;
}

// LC 92 reverse between m and n: find node before m, then head-insertion for n-m steps
```

Java 25 `record` is immutable, so real interview code keeps a mutable `Node` class. Mention `record` as value holder if asked about Java 25.

## Pitfalls

- Save `next` before overwriting `curr.next`.
- For sublist, keep a dummy head to handle `m==1`.
- Palindrome check: reverse second half, compare, then restore.

## Practice

- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
- [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

## Related DSA notes

- [[Java/07_DSA/Singly Linked List]]
- [[Java/07_DSA/Linked List]]
