---
title: "Greedy"
type: pattern
pattern: 20
domain: "Optimization"
category: "Coding Patterns/07_Backtracking_DP"
advanced: false
mastery: learn
recognition_score: 0
implementation_score: 0
attempts: 0
successful_attempts: 0
recognition_attempts: 0
recognition_successes: 0
avg_time_minutes:
hint_count: 0
last_attempt:
last_success:
failure_category:
difficulty: "Medium"
leetcode: [455, 135, 435]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - optimization
---

# Greedy

> Pattern #20 · Optimization

## Recognition

- Local choice appears to reduce future cost
- Sorting creates an exchange or dominance argument
- Problem has a proof that the local choice can be committed

### Strong signals
- Local choice appears to reduce future cost
- Sorting creates an exchange or dominance argument

### Do not infer it from
- A keyword alone
- A familiar example without checking constraints

## Invariant

> After each greedy choice, there exists an optimal solution consistent with every choice already committed.

## Mental model

Maintain the smallest state that completely describes the part of the search space still relevant to the answer.

## Core implementation

```java
// Jump Game — LC 55 (can reach end?)
boolean canJump(int[] nums) {
    int reach = 0;
    for (int i = 0; i < nums.length; i++) {
        if (i > reach) return false;
        reach = Math.max(reach, i + nums[i]);
    }
    return true;
}

// Jump Game II — LC 45 (min jumps)
int jump(int[] nums) {
    int jumps = 0, curEnd = 0, far = 0;
    for (int i = 0; i < nums.length - 1; i++) {
        far = Math.max(far, i + nums[i]);
        if (i == curEnd) { jumps++; curEnd = far; }
    }
    return jumps;
}

// Best Time to Buy and Sell Stock — LC 121
int maxProfit(int[] prices) {
    int best = 0, minPrice = prices[0];
    for (int p : prices) {
        best = Math.max(best, p - minPrice);
        minPrice = Math.min(minPrice, p);
    }
    return best;
}

// Non-overlapping Intervals (min removals) — LC 435 (greedy by end)
int eraseOverlapIntervals(int[][] intervals) {
    java.util.Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
    int end = Integer.MIN_VALUE, removed = 0;
    for (int[] in : intervals) {
        if (in[0] >= end) end = in[1];
        else removed++;
    }
    return removed;
}
```

## Variants

Start with the core implementation. Introduce a variant only when the required state or proof changes.

## When to use
- interval scheduling, activity selection, jump game, Huffman coding, gas station, "minimum", "maximum", "optimal", "earliest", "farthest reachable".

## When NOT to use
- future consequences can invalidate local pick (use DP); need all solutions (use backtracking); "coin change" with arbitrary denominations (greedy fails on [1,3,4] for amount 6).

## Complexity & trade-offs

| Scenario | Time | Space |
|----------|------|-------|
| With sorting | O(n log n) | O(1) |
| No sort (single pass) | O(n) | O(1) |

| Aspect | Greedy | DP | Divide and Conquer |
|--------|--------|----|-------------------|
| Decisions | irrevocable | revisits via recurrence | independent subproblems |
| Correctness | needs proof (exchange argument) | optimal substructure | combining solved halves |
| Time | O(n log n) sort + O(n) | O(n · choices) | O(n log n) typical |
| Pick when | local optimum implies global optimum | future choices can invalidate local pick | problem splits cleanly, no overlap |

## Pitfalls

- **Greedy fails silently** — test on a case where looking ahead would help (coin change with [1,3,4] for amount 6: greedy 4+1+1=3, optimal 3+3=2).
- **Do not backtrack in greedy** — once you pick, you commit.
- **Sort by the right criterion:** for intervals it's end time, not start. For jump game it's farthest reach.
- **Exchange argument is part of the answer** — if you can't argue why the greedy choice is safe, you don't have a solution, you have a guess.

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 455 | Easy |
| 135 | Hard |
| 435 | Medium |

## Interview Q&A

(Senior Depth)

**Q: Jump Game II (LC 45) — why does the `curEnd` / `far` two-pointer approach give minimum jumps?**
**A:** `curEnd` marks the end of the current jump's reach. `far` tracks the farthest we can reach from any position within the current jump. When `i == curEnd`, we've exhausted all positions reachable in the current number of jumps — we *must* jump again, and the best we can do is `far`. This is the exchange argument: any solution that jumps earlier lands at or before `far`, so jumping at `curEnd` to `far` is optimal.

**Q: Non-overlapping Intervals (LC 435) — why sort by end time, not start?**
**A:** Picking the interval that finishes earliest leaves maximum room for the rest. Exchange argument: suppose optimal picks interval A ending later, greedy picks B ending earlier (B ⊂ A or disjoint). Swapping A for B never reduces the number of subsequent intervals that fit. Sorting by start time fails: picking the earliest starting interval might be long and block many short ones.

**Q: Coin change with [1,3,4] for amount 6 — why does greedy fail?**
**A:** Greedy picks 4 (largest ≤ 6), remainder 2 → 1+1 → total 3 coins. Optimal: 3+3 = 2 coins. The failure is that a larger coin (4) leaves a remainder that requires more small coins than using two medium coins (3+3). The local "largest coin" choice doesn't guarantee global minimum.

**Q: Gas Station (LC 134) — how is it greedy?**
**A:** If total gas ≥ total cost, solution exists. Track `tank` from start; if `tank < 0` at station i, restart at i+1 and reset `tank`. Proof: if you can't reach i+1 from start, no station between start and i can reach i+1 either (they all had more gas but couldn't). O(n) single pass.

**Q: How do you respond when asked "prove your greedy choice is correct"?**
**A:** State the exchange argument: "Assume optimal solution O differs from greedy G at first decision. G picks X, O picks Y. Show that swapping Y for X in O yields a solution at least as good. Therefore an optimal solution exists that matches G's first choice. By induction, G is optimal." For intervals: "O picks A ending later, G picks B ending earlier. Replace A with B — B frees up space, so any intervals after A still fit after B. The rest of O's choices remain valid."

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Greedy? :: **A:** interval scheduling, Huffman, minimum spanning tree, jump game, gas station, assign cookies #flashcard

#flashcard
**Q:** Time/space complexity of Greedy? :: **A:** Time: O(n log n) sort + O(n) scan, Space: O(1) or O(n) #flashcard

#flashcard
**Q:** When do you NOT use Greedy? :: **A:** local optimum ≠ global (need DP/backtrack), need all solutions #flashcard

#flashcard
**Q:** Core Java 25 snippet for Greedy? :: **A:** `Arrays.sort(intervals, (a,b)->a[1]-b[1]); int end=-1, ans=0; for(int[] iv:intervals) if(iv[0]>=end){ end=iv[1]; ans++; }` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- Dynamic Programming (greedy = DP with memo deleted + choice made permanent)
- Overlapping Intervals (activity selection is greedy)
- BFS (level-order is greedy by distance)
- [[Java/07_DSA/Array]]
