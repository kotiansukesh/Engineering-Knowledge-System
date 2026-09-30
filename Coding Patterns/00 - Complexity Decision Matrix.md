---
title: Complexity Decision Matrix
type: guide
category: Coding Patterns
tags:
  - complexity
  - algorithms
  - interview-prep
---

# Complexity Decision Matrix

> Use constraints as an early filter. These are heuristics, not mathematical laws.

| Approx. n | Often acceptable starting point | Usually suspicious |
|---:|---|---|
| ≤ 10 | O(n!), O(2^n), heavy backtracking | — |
| ≤ 20 | O(2^n), meet-in-the-middle | O(3^n) without justification |
| ≤ 100 | O(n³), O(n²) | factorial/exponential |
| ≤ 1,000 | O(n²), O(n² log n) | O(n³) unless optimized |
| ≤ 100,000 | O(n), O(n log n) | O(n²) |
| ≥ 1,000,000 | O(n), O(log n), streaming | O(n log n) may need scrutiny |

## Constraint → technique prompts

| Property | Candidate direction |
|---|---|
| Sorted input | Binary Search / Two Pointers |
| Monotonic feasibility | Binary Search on Answer |
| Contiguous range + constraint | Sliding Window |
| Range aggregate / target relation | Prefix Sum |
| Pair/triple + ordering | Two Pointers |
| K best elements | Heap |
| Nearest greater/smaller | Monotonic Stack |
| Unweighted minimum steps | BFS |
| Weighted non-negative shortest path | Shortest Path |
| Repeated subproblems | DP / Memoization |
| Enumerate configurations | Backtracking |
| Connectivity under merges | Union Find |

Before coding, state: “Given n ≈ ___, my target is approximately ___ time and ___ space because ___.”
