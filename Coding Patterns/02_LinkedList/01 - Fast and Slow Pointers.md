---
title: "Fast and Slow Pointers"
type: pattern
pattern: 5
domain: "Linked List"
category: "Coding Patterns/02_LinkedList"
advanced: false
mastery: learn
recognition_score: 0
difficulty: "Easy"
leetcode: [141, 876, 287]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - pattern/linked-list
---

# Fast and Slow Pointers

> Pattern #5 · Linked List

## Recognition

- Cycle detection
- Middle / relative-position queries
- A deterministic next-state function can be followed with two speeds

### Strong signals
- Cycle detection
- Middle / relative-position queries

### Do not infer it from
- A keyword alone
- A familiar LeetCode example without checking the constraints

## Invariant

> Fast advances at twice the speed of slow; if the state space contains a cycle, the relative distance between them eventually becomes zero modulo the cycle length.

## Mental model

Use different pointer speeds to expose cycle structure or relative position without storing visited nodes. The same idea applies to arrays or deterministic sequences when values can be treated as next-state pointers.

## Core implementation

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

## Variants

Use the implementation above as the base case. Extend it only after the invariant remains explicit.

## When to use

- linked list cycle detection; middle of list; happy number; find duplicate (array values as pointers); any sequence where next(x) is O(1).
- **NOT:** need to visit every node (just traverse); need all nodes in cycle (need extra pass); array where values aren't valid indices.

## When NOT to use

need to visit every node (just traverse); need all nodes in cycle (need extra pass); array where values aren't valid indices.

## Complexity & trade-offs

| Approach | Time | Space |
|----------|------|-------|
| Floyd (fast/slow) | O(n) | O(1) |
| HashSet visited | O(n) | O(n) |
| Brent's algorithm | O(n) | O(1) — fewer traversals on average |

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

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 141 | Linked List Cycle | Easy |
| 876 | Middle of the Linked List | Easy |
| 287 | Find the Duplicate Number | Medium |

## Interview Q&A

(Senior Depth)

**Q: Prove why resetting one pointer to head and advancing both at speed 1 finds the cycle entry.**
**A:** Let `L1` = distance head→entry, `L2` = distance entry→meeting, `C` = cycle length. Slow travels `L1 + L2`. Fast travels `L1 + L2 + kC` (k loops). Fast = 2×Slow → `L1 + L2 + kC = 2(L1 + L2)` → `L1 = kC - L2`. So distance from head to entry equals distance from meeting to entry (mod C). Moving both at speed 1, they meet at entry.

**Q: Happy Number — why does this work on a number sequence?**
**A:** The transformation `n → sum of squares of digits` defines a deterministic next-state function on a finite domain (max sum for 32-bit int is 9²×10=810). Any finite-state deterministic sequence must eventually cycle. If it reaches 1, it stays at 1 (cycle of length 1). If not, it enters a cycle not containing 1. Fast/slow detects which case.

**Q: Find Duplicate (LC 287) — why can we treat the array as a linked list?**
**A:** Array has n+1 elements with values in [1,n]. Treat `i → nums[i]` as a pointer. Since there are n+1 nodes and only n possible values, by pigeonhole principle there's a cycle. The duplicate value is the *entry point* of the cycle (two indices point to it). Floyd's algorithm finds the entry in O(1) space without modifying the array.

**Q: What if the linked list is very long and you're worried about stack overflow?**
**A:** Floyd's algorithm is iterative — no recursion, no stack overflow risk. The O(1) space guarantee holds regardless of list length. This is exactly why it's preferred over recursive or HashSet approaches in production.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Fast and Slow Pointers? :: **A:** linked list cycle, find middle, happy number, find duplicate (LC 287), palindrome linked list #flashcard

#flashcard
**Q:** Time/space complexity of Fast and Slow Pointers? :: **A:** Time: O(n) cycle detect / O(n) find entry, Space: O(1) #flashcard

#flashcard
**Q:** When do you NOT use Fast and Slow Pointers? :: **A:** need to visit all nodes (just traverse), need cycle length only (extra pass needed) #flashcard

#flashcard
**Q:** Core Java 25 snippet for Fast and Slow Pointers? :: **A:** `ListNode slow=head, fast=head; while(fast!=null && fast.next!=null){ slow=slow.next; fast=fast.next.next; if(slow==fast) break; }` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory 📅 2026-10-01
- [ ] Write the template from memory 📅 2026-10-03
- [ ] Solve one unseen problem without hints 📅 2026-10-07
- [ ] Explain the invariant aloud 📅 2026-10-14

## Related

- [[02_LinkedList/02 - LinkedList In-place Reversal|LinkedList In-place Reversal]]
- [[05_Trees_Graphs/02 - DFS|DFS]] (graph cycle detection uses visited set, not fast/slow)
- [[Java/07_DSA/Singly Linked List]] · [[Java/07_DSA/Linked List]]
