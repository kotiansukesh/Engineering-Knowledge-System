---
title: "LinkedList In-place Reversal"
type: pattern
pattern: 6
domain: "Linked List"
category: "Coding Patterns/02_LinkedList"
advanced: false
mastery: learn
recognition_score: 0
difficulty: "Easy"
leetcode: [206, 92, 25]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - pattern/linked-list
---

# LinkedList In-place Reversal

> Pattern #6 · Linked List

## Recognition

- Reverse a list or sublist
- Reverse nodes in fixed-size groups
- Need O(1) extra space while changing links

### Strong signals
- Reverse a list or sublist
- Reverse nodes in fixed-size groups

### Do not infer it from
- A keyword alone
- A familiar LeetCode example without checking the constraints

## Invariant

> Before overwriting the current node's next pointer, the unprocessed suffix remains reachable through a saved reference.

## Mental model

Reverse links locally while keeping a reference to the unprocessed suffix. Three references—previous, current, next—are the minimal mental model for safe pointer rewiring.

## Core implementation

```java
// Mutable node for interviews (Java record is immutable)
class Node { int val; Node next; Node(int v){ val=v; } }

// Reverse entire list — LC 206
Node reverseList(Node head) {
    Node prev = null; var cur = head;
    while (cur != null) {
        var nxt = cur.next;
        cur.next = prev;
        prev = cur;
        cur = nxt;
    }
    return prev;
}

// Reverse between m and n — LC 92 (1-indexed)
Node reverseBetween(Node head, int m, int n) {
    Node dummy = new Node(0); dummy.next = head;
    Node prev = dummy;
    for (int i = 1; i < m; i++) prev = prev.next; // node before m
    Node cur = prev.next; // m-th node
    for (int i = 0; i < n - m; i++) {
        Node nxt = cur.next;
        cur.next = nxt.next;
        nxt.next = prev.next;
        prev.next = nxt; // head-insert nxt at front of sublist
    }
    return dummy.next;
}

// Reverse in k-groups — LC 25
Node reverseKGroup(Node head, int k) {
    Node dummy = new Node(0); dummy.next = head;
    Node groupPrev = dummy;
    while (true) {
        Node kth = groupPrev;
        for (int i = 0; i < k; i++) { kth = kth.next; if (kth == null) return dummy.next; }
        Node groupNext = kth.next;
        // reverse group
        Node prev = groupNext, cur = groupPrev.next;
        while (cur != groupNext) {
            var nxt = cur.next; cur.next = prev; prev = cur; cur = nxt;
        }
        Node tmp = groupPrev.next; groupPrev.next = kth; groupPrev = tmp;
    }
}
```

## Variants

Use the implementation above as the base case. Extend it only after the invariant remains explicit.

## When to use

- reverse whole list; reverse sublist [m,n]; reverse in k-groups; palindrome check (reverse second half); reorder list.
- **NOT:** when O(n) space is acceptable and recursive clarity wins (small n); immutable list (must rebuild).

## When NOT to use

when O(n) space is acceptable and recursive clarity wins (small n); immutable list (must rebuild).

## Complexity & trade-offs

| Approach | Time | Space | Stack Overflow Risk |
|----------|------|-------|---------------------|
| Iterative in-place | O(n) | O(1) | None |
| Recursive | O(n) | O(n) call stack | Deep lists |
| Copy to array, reverse, rebuild | O(n) | O(n) | None |

| Aspect | In-place Reversal | Recursive Reversal | Array Copy + Rebuild |
|--------|-------------------|--------------------|----------------------|
| Time | O(n) | O(n) | O(n) |
| Space | O(1) | O(n) call stack | O(n) |
| Stack overflow | None | Deep lists | None |
| Pick when | O(1) space required | Shortest code, small n | Never in interview |

## Pitfalls

- Save `next` **before** overwriting `cur.next` — classic bug.
- For sublist, use dummy head to handle `m=1` without special cases.
- Palindrome: reverse second half, compare, then **restore** the list (interviewers check this).
- Java 25 `record` is immutable — in interviews, explicitly declare a mutable `class Node` for pointer manipulation.

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 206 | Reverse Linked List | Easy |
| 92 | Reverse Linked List II | Medium |
| 25 | Reverse Nodes in k-Group | Hard |

## Interview Q&A

(Senior Depth)

**Q: Reverse Between (LC 92) — why does the head-insertion loop run `n-m` times, not `n-m+1`?**
**A:** The sublist has `n-m+1` nodes. The first node (at position m) becomes the *last* node of the reversed sublist — it's already in place as the tail. Each iteration moves the *next* node to the front. After `n-m` moves, all remaining `n-m` nodes are at the front, and the original m-th node is at the end. Total nodes in reversed section: `1 + (n-m) = n-m+1`. Correct.

**Q: Reverse K-Group — how do you handle the last group if it has fewer than k nodes?**
**A:** Before reversing, advance a pointer `k` steps from `groupPrev`. If it hits `null`, the remaining nodes < k — return immediately without reversing. The check `for (int i = 0; i < k; i++) { kth = kth.next; if (kth == null) return dummy.next; }` handles this.

**Q: Can you reverse a list using only two pointers?**
**A:** No — you need three: `prev`, `cur`, `nxt`. The `nxt` saves the rest of the list before you sever `cur.next`. With only two pointers, you lose the reference to the unprocessed portion. Some languages allow `cur.next, prev, cur = prev, cur, cur.next` (tuple assignment) which *looks* like two variables but semantically still has three values.

**Q: Palindrome check with O(1) space — walk me through the full algorithm.**
**A:** (1) Find middle with fast/slow. (2) Reverse second half starting from `slow` (or `slow.next` for odd). (3) Compare first half and reversed second half node by node. (4) **Restore** by reversing the second half again and reattaching. (5) Return comparison result. Restoration is required for production code; some interviewers skip it but seniors include it.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for LinkedList In-place Reversal? :: **A:** reverse linked list, reverse K-group, reverse sublist, palindrome check (reverse half) #flashcard

#flashcard
**Q:** Time/space complexity of LinkedList In-place Reversal? :: **A:** Time: O(n) single pass, Space: O(1) #flashcard

#flashcard
**Q:** When do you NOT use LinkedList In-place Reversal? :: **A:** need to preserve original (copy first), recursive reversal OK if stack depth safe #flashcard

#flashcard
**Q:** Core Java 25 snippet for LinkedList In-place Reversal? :: **A:** `ListNode prev=null, curr=head; while(curr!=null){ ListNode nxt=curr.next; curr.next=prev; prev=curr; curr=nxt; } return prev;` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- [[02_LinkedList/01 - Fast and Slow Pointers|Fast & Slow Pointers]] (find middle for palindrome)
- [[07_Backtracking_DP/01 - Backtracking|Backtracking]] (recursive reversal is backtracking)
- [[Java/07_DSA/Singly Linked List]] · [[Java/07_DSA/Linked List]]
