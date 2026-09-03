---
title: "Greedy"
pattern: 19
category: Greedy
tags: [pattern/greedy, optimization]
leetcode: ["55", "45", "121"]
created: 2026-09-02
source: "https://blog.algomaster.io/p/20-dsa-patterns"
---

# Greedy

> Part of [[README|20 DSA Patterns]] - Pattern #19

## Definition

Pick the locally best move at each step and never look back. Works only when a local optimum leads to a global optimum, provable by exchange argument. Example: jump game `nums=[2,3,1,1,4]` → at `0` reach is `2`, at `1` reach extends to `4`, greedy expands reachable window each pass and reaches the end.

Fails where future consequences matter, then use DP instead.

## When to use

- Interval scheduling, activity selection, jump game, Huffman coding
- Keywords: "minimum", "maximum", "optimal", "earliest", "farthest reachable"

## Complexity

| time | space |
|---|---|
| O(n log n) if sorting needed, otherwise O(n) | O(1) |

## Java example

```java
// Jump game, LC 55 - can reach end?
boolean canJump(int[] nums) {
    int reach = 0;
    for (var i = 0; i < nums.length; i++) {
        if (i > reach) return false;
        reach = Math.max(reach, i + nums[i]);
    }
    return true;
}

// Jump game II, LC 45 - min jumps
int jump(int[] nums) {
    int jumps = 0, curEnd = 0, far = 0;
    for (var i = 0; i < nums.length - 1; i++) {
        far = Math.max(far, i + nums[i]);
        if (i == curEnd) { jumps++; curEnd = far; }
    }
    return jumps;
}

// Best time to buy and sell stock, LC 121
int maxProfit(int[] prices) {
    int best = 0, minPrice = prices[0];
    for (var p : prices) { best = Math.max(best, p - minPrice); minPrice = Math.min(minPrice, p); }
    return best;
}
```

Greedy proofs are part of the answer in interviews. If you cannot argue why picking the earliest end or farthest reach is safe, the reviewer assumes you guessed.

## Pitfalls

- Greedy fails silently, test on a case where looking ahead would help (coin change with `[1,3,4]` for amount `6`).
- Do not backtrack in greedy; once you pick, you commit.
- Sort by the right criterion: for intervals it is end, not start.

## Practice

- [55. Jump Game](https://leetcode.com/problems/jump-game/)
- [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/)
- [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Related DSA notes

- [[Java/07_DSA/Array]]
