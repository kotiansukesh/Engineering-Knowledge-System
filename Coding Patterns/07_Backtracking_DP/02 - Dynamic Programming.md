---
title: "Dynamic Programming"
type: pattern
pattern: 19
domain: "Optimization"
category: "Coding Patterns/07_Backtracking_DP"
advanced: false
mastery: learn
recognition_score: 0
difficulty: "Hard"
leetcode: [70, 322, 300, 1143]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - optimization
---

# Dynamic Programming

> Pattern #19 · Optimization

## Recognition

- Same subproblem appears repeatedly
- Need optimum/count over choices
- A state can summarize all information needed for future decisions

### Strong signals
- Same subproblem appears repeatedly
- Need optimum/count over choices

### Do not infer it from
- A keyword alone
- A familiar example without checking constraints

## Invariant

> Each DP state stores the correct answer for exactly one subproblem, and every transition uses already-correct smaller states.

## Mental model

Maintain the smallest state that completely describes the part of the search space still relevant to the answer.

## Core implementation

```java
// Climbing Stairs — LC 70 (tabulation)
int climbStairs(int n) {
    if (n <= 2) return n;
    int[] dp = new int[n + 1];
    dp[1] = 1; dp[2] = 2;
    for (int i = 3; i <= n; i++) dp[i] = dp[i-1] + dp[i-2];
    return dp[n];
}

// Coin Change — LC 322 (unbounded knapsack, min coins)
int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    java.util.Arrays.fill(dp, amount + 1); // INF
    dp[0] = 0;
    for (int c : coins)
        for (int i = c; i <= amount; i++)
            dp[i] = Math.min(dp[i], dp[i-c] + 1);
    return dp[amount] > amount ? -1 : dp[amount];
}

// 0/1 Knapsack — space optimized to 1D
int knapsack(int[] wt, int[] val, int W) {
    int[] dp = new int[W + 1];
    for (int i = 0; i < wt.length; i++)
        for (int w = W; w >= wt[i]; w--) // backward for 0/1
            dp[w] = Math.max(dp[w], dp[w - wt[i]] + val[i]);
    return dp[W];
}

// Longest Common Subsequence — LC 1143 (2D, harder to compress)
int lcs(String a, String b) {
    int[][] dp = new int[a.length() + 1][b.length() + 1];
    for (int i = 1; i <= a.length(); i++)
        for (int j = 1; j <= b.length(); j++)
            dp[i][j] = a.charAt(i-1) == b.charAt(j-1)
                ? 1 + dp[i-1][j-1]
                : Math.max(dp[i-1][j], dp[i][j-1]);
    return dp[a.length()][b.length()];
}

// House Robber — LC 198 (rolling O(1) space)
int rob(int[] nums) {
    int prev = 0, curr = 0;
    for (int x : nums) {
        int tmp = Math.max(curr, prev + x);
        prev = curr;
        curr = tmp;
    }
    return curr;
}
```

## Variants

Start with the core implementation. Introduce a variant only when the required state or proof changes.

## When to use

- "maximum", "minimum", "ways to", "can you", "longest", "shortest" where choices at each step build the answer. Both overlapping subproblems and optimal substructure present.
- **NOT:** generate all solutions (use backtracking); greedy choice provably optimal (use greedy); no overlapping subproblems.

## When NOT to use

generate all solutions (use backtracking); greedy choice provably optimal (use greedy); no overlapping subproblems.

## Complexity & trade-offs

| Approach | Time | Space |
|----------|------|-------|
| Memoization (top-down) | O(n · choices) | O(n) cache + recursion stack |
| Tabulation (bottom-up) | O(n · choices) | O(n), often O(1) with rolling array |

| Aspect | Memoization (Top-down) | Tabulation (Bottom-up) | Greedy |
|--------|------------------------|------------------------|--------|
| Subproblems hit | only ones reached | all states filled | none |
| Time | O(n · choices) | O(n · choices) | O(n log n) |
| Space | O(n) cache + call stack | O(n), often O(1) rolling | O(1) |
| Stack overflow | risk on deep n | no | no |
| Pick when | recursion is clearest, sparse states | dense states, want speed/space tuning | local optimum provably global |

## Pitfalls

- **Define `dp` meaning before coding:** `dp[i]` is what exactly. Wrong definition sinks the solution.
- **Base case off-by-one** is the most common bug.
- **Coin change outer loop over `coins`** gives combinations; swapped loops give permutations — know which you need.
- **0/1 knapsack weight loop must go backward** (W down to wt[i]) to use previous iteration's values. Forward uses current iteration's values → unbounded knapsack.

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 70 | Easy |
| 322 | Medium |
| 300 | Medium |
| 1143 | Medium |

## Interview Q&A

(Senior Depth)

**Q: 0/1 Knapsack vs Unbounded Knapsack — why does loop direction matter?**
**A:** 0/1: each item used at most once. Backward loop (W..wt[i]) ensures `dp[w - wt[i]]` comes from previous iteration (item not yet considered). Forward loop would use current iteration's updated `dp[w - wt[i]]`, allowing the same item multiple times → unbounded. The loop direction *is* the constraint enforcement.

**Q: Coin Change (LC 322) — why outer loop over coins, inner over amount?**
**A:** This order counts combinations (order of coins doesn't matter). Swapped loops (amount outer, coins inner) counts permutations (order matters). For "minimum coins", both work for the minimum value, but combination order is standard and avoids overcounting states.

**Q: LCS (LC 1143) — why is 2D harder to compress to 1D?**
**A:** `dp[i][j]` depends on `dp[i-1][j-1]`, `dp[i-1][j]`, `dp[i][j-1]`. Compressing rows: `dp[j]` depends on `prevDiag` (old `dp[j-1]`), `prevRow[j]` (old `dp[j]`), and `dp[j-1]` (current row). Requires 3 variables or careful ordering. Doable but error-prone; 2D is acceptable in interviews for LCS (n,m ≤ 1000).

**Q: House Robber (LC 198) — how did you get O(1) space?**
**A:** Recurrence: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`. Only depends on previous two states. Keep `prev = dp[i-2]`, `curr = dp[i-1]`. Update: `next = max(curr, prev + nums[i])`; shift `prev = curr; curr = next`. This is the "rolling variables" pattern — works whenever recurrence only looks back constant steps.

**Q: How do you know if a problem is DP vs Greedy?**
**A:** Try greedy first. If you find a counterexample where local optimal fails (e.g., coin change with [1,3,4] for amount 6: greedy picks 4+1+1=3 coins, optimal is 3+3=2), then it's DP. DP = backtracking + memoization. If subproblems don't overlap, it's backtracking (enumerate all). If they overlap and you need count/optimum, it's DP.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Dynamic Programming? :: **A:** optimal substructure, overlapping subproblems, min/max/count ways, knapsack, LIS, edit distance, house robber #flashcard

#flashcard
**Q:** Time/space complexity of Dynamic Programming? :: **A:** Time: O(states × transitions), Space: O(states) or O(1) rolling #flashcard

#flashcard
**Q:** When do you NOT use Dynamic Programming? :: **A:** no overlapping subproblems (just recursion), greedy works (prove it), state space too large #flashcard

#flashcard
**Q:** Core Java 25 snippet for Dynamic Programming? :: **A:** `int[] dp=new int[n+1]; dp[0]=base; for(int i=1;i<=n;i++) for(opt: options) dp[i]=Math.max(dp[i], dp[i-opt]+val);` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- [[07_Backtracking_DP/01 - Backtracking|Backtracking]] (DP = backtracking + memo)
- [[07_Backtracking_DP/03 - Greedy|Greedy]] (local vs global optimum)
- [[01_Array/01 - Prefix Sum|Prefix Sum]] (DP often uses prefix sums)
- [[Java/07_DSA/Array]]
