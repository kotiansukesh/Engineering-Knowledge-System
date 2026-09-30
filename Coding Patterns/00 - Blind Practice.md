---
title: "Blind Practice"
category: "Coding Patterns"
tags: [practice, blind-practice, pattern-recognition]
created: "2026-09-30"
---

# Blind Practice

> Solve these **without opening the pattern notes first**. The purpose is recognition, not memorization.

## Attempt template

Copy this block for every practice problem:

```markdown
### Problem

**Pattern guess:**  
**Why:**  
**Invariant:**  
**Brute force:**  
**Optimized idea:**  
**Time:**  
**Space:**  
**Confidence (1-5):**  
**What fooled me:**  
```

## Recognition drills

Start with 1–2 problems per session. Do not look at the solution until you have committed to a pattern.

| Problem | Hidden pattern | Recognition cue |
|---|---|---|
| Two Sum II | Two Pointers | sorted + pair |
| Container With Most Water | Two Pointers | opposite ends + maximize |
| Longest Substring Without Repeating Characters | Sliding Window | longest contiguous + constraint |
| Minimum Window Substring | Sliding Window | smallest valid window |
| Subarray Sum Equals K | Prefix Sum + HashMap | count contiguous sums |
| Group Anagrams | Frequency / canonical representation | equivalent character counts |
| Linked List Cycle | Fast & Slow Pointers | relative movement |
| Reverse Linked List II | In-place Reversal | mutate links in-place |
| Daily Temperatures | Monotonic Stack | next greater element |
| Kth Largest Element | Top K / Heap | kth order statistic |
| Merge Intervals | Overlapping Intervals | ranges + overlap |
| Search in Rotated Sorted Array | Modified Binary Search | partially ordered search |
| Binary Tree Level Order Traversal | BFS | level-by-level |
| Maximum Depth of Binary Tree | DFS | recursive tree property |
| Network Delay Time | Shortest Path | weighted graph |
| Number of Islands | DFS/BFS | connected grid components |
| Implement Trie | Trie | prefix lookup |
| Number of Connected Components | Union Find | connectivity |
| Word Search | Backtracking | path + choices + undo |
| Coin Change | Dynamic Programming | repeated subproblems |
| Jump Game | Greedy | reachable frontier |
| Single Number | Bit Manipulation | XOR cancellation |

## Scoring

After each attempt:

- **5 — Instant recognition:** pattern and invariant identified before coding.
- **4 — Correct recognition:** needed some exploration.
- **3 — Correct after brute-force analysis.**
- **2 — Pattern recognized only after seeing a hint.**
- **1 — Pattern missed completely.**

Track the score in the problem note or your personal review log.

## Promotion rule

A pattern is not “mastered” because you can solve its canonical problems.

Promote it to **Mastered** only when you can:

- identify it on an unseen problem;
- explain the invariant in one or two sentences;
- implement the core template from memory;
- state the complexity;
- explain when the pattern does **not** apply;
- recognize at least one problem that combines it with another pattern.
