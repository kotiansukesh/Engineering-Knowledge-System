---
title: Fast and Slow Pointers
pattern: 4
category: Coding Patterns/02_LinkedList
tags:
  - pattern/linkedlist
  - pattern/linkedlist/fast-slow
leetcode:
  - 141
  - 202
  - 287
created: 2026-09-02
completed: false
reviewed: ""
sr-due: ""
difficulty: Easy
source: https://blog.algomaster.io/p/20-dsa-patterns
---

# Fast and Slow Pointers

> Part of [[README|20 DSA Patterns]] • `Coding Patterns/02_LinkedList` • Pattern #4

## Intent
Two pointers traversing a sequence at different speeds (slow +1, fast +2) to detect cycles, find middles, or locate cycle entry — O(1) space alternative to HashSet for linked list and sequence problems.

## Why it Matters
- **Cycle detection (Floyd's algorithm):** If a cycle exists, fast and slow *must* meet. Proof: relative speed is 1 step per iteration; in a cycle of length C, they meet within C steps.
- **Cycle entry:** After meeting, reset one pointer to head, advance both at speed 1 — they meet at cycle entry. Distance from head to entry = distance from meeting point to entry (mod C).
- **Middle of list:** When fast reaches end, slow is at middle (even length → first middle).
- Senior signal: knowing the *proof* of cycle entry — not just the code. The second phase works because `distance(head→entry) = distance(meeting→entry)` when both move at speed 1.

## Diagram
```mermaid
flowchart LR
  S["slow +1"] --> M["meet"]
  F["fast +2"] --> M
  M --> N{"fast hits null?"}
  N -->|yes| NC["no cycle"]
  N -->|no| R["reset one to head"]
  R --> E["both +1 until equal<br/>= cycle entry"]
```


## Problems

### 141. Linked List Cycle (Easy)
> [LeetCode 141](https://leetcode.com/problems/linked-list-cycle/) • Tags: Hash Table, Linked List, Two Pointers, Floyd's Cycle Finding Algorithm

**Problem Statement:**

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

**Examples:**

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

---

### 202. Happy Number (Easy)
> [LeetCode 202](https://leetcode.com/problems/happy-number/) • Tags: Hash Table, Math, Two Pointers, Floyd's Cycle Finding Algorithm

**Problem Statement:**

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

	Starting with any positive integer, replace the number by the sum of the squares of its digits.
	Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
	Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

**Examples:**

Example 1:

Input: n = 19
Output: true
Explanation:
1^2^ + 9^2^ = 82
8^2^ + 2^2^ = 68
6^2^ + 8^2^ = 100
1^2^ + 0^2^ + 0^2^ = 1

Example 2:

Input: n = 2
Output: false

---

### 287. Find the Duplicate Number (Medium)
> [LeetCode 287](https://leetcode.com/problems/find-the-duplicate-number/) • Tags: Array, Two Pointers, Binary Search, Bit Manipulation, Pigeonhole Principle, Floyd's Cycle Finding Algorithm

**Problem Statement:**

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

**Examples:**

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

Example 3:

Input: nums = [3,3,3,3,3]
Output: 3

---


## Code / Example
```java
record Node(int val, Node next) {}

// Cycle detection — LC 141
boolean hasCycle(Node head) {
    var slow = head; var fast = head;
    while (fast != null && fast.next() != null) {
        slow = slow.next();
        fast = fast.next().next();
        if (slow == fast) return true;
    }
    return false;
}

// Find middle — when fast ends, slow is middle
Node middle(Node head) {
    var slow = head; var fast = head;
    while (fast != null && fast.next() != null) {
        slow = slow.next();
        fast = fast.next().next();
    }
    return slow;
}

// Cycle entry — LC 142
Node detectCycle(Node head) {
    var slow = head; var fast = head;
    while (fast != null && fast.next() != null) {
        slow = slow.next();
        fast = fast.next().next();
        if (slow == fast) {
            var p = head;
            while (p != slow) { p = p.next(); slow = slow.next(); }
            return p;
        }
    }
    return null;
}

// Happy Number — LC 202 (sequence cycle)
boolean isHappy(int n) {
    int slow = n, fast = next(n);
    while (fast != 1 && slow != fast) {
        slow = next(slow);
        fast = next(next(fast));
    }
    return fast == 1;
}
int next(int n) {
    int sum = 0;
    while (n > 0) { int d = n % 10; sum += d * d; n /= 10; }
    return sum;
}

// Find Duplicate — LC 287 (array as linked list via values as pointers)
int findDuplicate(int[] nums) {
    int slow = nums[0], fast = nums[0];
    do { slow = nums[slow]; fast = nums[nums[fast]]; } while (slow != fast);
    slow = nums[0];
    while (slow != fast) { slow = nums[slow]; fast = nums[fast]; }
    return slow;
}
```

## When to Use / When NOT
- **Use:** linked list cycle detection; middle of list; happy number; find duplicate (array values as pointers); any sequence where next(x) is O(1).
- **NOT:** need to visit every node (just traverse); need all nodes in cycle (need extra pass); array where values aren't valid indices.

## Trade-offs
| Approach | Time | Space |
|----------|------|-------|
| Floyd (fast/slow) | O(n) | O(1) |
| HashSet visited | O(n) | O(n) |
| Brent's algorithm | O(n) | O(1) — fewer traversals on average |

## Vs Table
| Aspect | Floyd Fast/Slow | HashSet Visited | Brent's Algorithm |
|--------|-----------------|-----------------|-------------------|
| Space | O(1) | O(n) | O(1) |
| Cycle detect | O(n) | O(n) | O(n), fewer traversals avg |
| Find cycle length | extra pass from meeting | trivial | direct |
| Pick when | O(1) space required | debugging, or must report every visited | competitive tuning only |

## Pitfalls
- Check `fast != null && fast.next() != null` **every loop**. Checking only `fast != null` misses `fast.next` and causes NPE.
- Meeting point is **not** the cycle start. You *must* do the second phase (reset one to head, both +1).
- For array-as-linked-list (LC 287), values must be valid indices `[1, n-1]` for 1..n array with n+1 elements.

## Interview Q&A (Senior Depth)

**Q: Prove why resetting one pointer to head and advancing both at speed 1 finds the cycle entry.**
**A:** Let `L1` = distance head→entry, `L2` = distance entry→meeting, `C` = cycle length. Slow travels `L1 + L2`. Fast travels `L1 + L2 + kC` (k loops). Fast = 2×Slow → `L1 + L2 + kC = 2(L1 + L2)` → `L1 = kC - L2`. So distance from head to entry equals distance from meeting to entry (mod C). Moving both at speed 1, they meet at entry.

**Q: Happy Number — why does this work on a number sequence?**
**A:** The transformation `n → sum of squares of digits` defines a deterministic next-state function on a finite domain (max sum for 32-bit int is 9²×10=810). Any finite-state deterministic sequence must eventually cycle. If it reaches 1, it stays at 1 (cycle of length 1). If not, it enters a cycle not containing 1. Fast/slow detects which case.

**Q: Find Duplicate (LC 287) — why can we treat the array as a linked list?**
**A:** Array has n+1 elements with values in [1,n]. Treat `i → nums[i]` as a pointer. Since there are n+1 nodes and only n possible values, by pigeonhole principle there's a cycle. The duplicate value is the *entry point* of the cycle (two indices point to it). Floyd's algorithm finds the entry in O(1) space without modifying the array.

**Q: What if the linked list is very long and you're worried about stack overflow?**
**A:** Floyd's algorithm is iterative — no recursion, no stack overflow risk. The O(1) space guarantee holds regardless of list length. This is exactly why it's preferred over recursive or HashSet approaches in production.

## Related
- [[02_LinkedList/02 - LinkedList In-place Reversal|LinkedList In-place Reversal]]
- [[05_Trees_Graphs/02 - DFS|DFS]] (graph cycle detection uses visited set, not fast/slow)
- [[Java/07_DSA/Singly Linked List]] · [[Java/07_DSA/Linked List]]

---
*Category: Coding Patterns/02_LinkedList*
