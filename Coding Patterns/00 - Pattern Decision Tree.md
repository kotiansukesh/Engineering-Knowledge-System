---
title: Pattern Decision Tree
type: guide
category: Coding Patterns
tags:
  - pattern-recognition
  - decision-tree
---

# Pattern Decision Tree

> Start from problem shape. Use constraints to eliminate candidates. State the invariant before coding.

## Reasoning sequence

### 1. What is the required output?

- A count/sum/range result
- A pair/triple
- A path or minimum distance
- A traversal/order
- An optimal value
- All valid configurations
- Connectivity
- Prefix/string lookup

### 2. What is the input structure?

Array/string, linked list, interval set, tree, graph, grid, or implicit state space.

### 3. What breaks brute force?

Estimate the naive complexity against the actual constraint before choosing an algorithm.

### 4. What work repeats?

Ask what the brute-force solution recomputes. The answer often points to the state/data structure.

### 5. What can be maintained?

| Maintainable state | Candidate direction |
|---|---|
| Prefix aggregate | Prefix Sum |
| Active contiguous range | Sliding Window |
| Ordered endpoints | Two Pointers |
| Frequency state | Frequency Counting / Sliding Window |
| Monotonic frontier | Monotonic Stack |
| K best candidates | Heap / Top K |
| Search interval | Binary Search |
| Graph frontier | BFS / DFS |
| Recursive choice state | Backtracking |
| Repeated subproblem state | DP / Memoization |
| Component representative | Union Find |
| Prefix path | Trie |

### 6. State the invariant

Use 00 - Invariant Library before writing code.

### 7. Disambiguate

Use 00 - Pattern Confusion Matrix when two candidates remain plausible.

## Object → candidate patterns

| Shape | Start with |
|---|---|
| Array / string | Prefix Sum, Two Pointers, Sliding Window, Frequency Counting, Binary Search |
| Linked list | Fast/Slow, In-place Reversal |
| Intervals | Overlapping Intervals |
| Tree | Traversal, DFS, BFS |
| Graph | BFS, DFS, Shortest Path, Union Find |
| Matrix / grid | Matrix Traversal + BFS/DFS/DP |
| Generate configurations | Backtracking |
| Repeated subproblems | Dynamic Programming |
| Provably safe local choice | Greedy |
| Top/bottom K | Heap / Top K |
| Prefix lookup | Trie |
| XOR / masks / bit state | Bit Manipulation |

## Complexity filter

Use 00 - Complexity Decision Matrix before coding.

## Pattern combinations

Use 00 - Pattern Combinations for problems where one technique does not remove all repeated work.

## Pre-code checklist

- [ ] State the brute force.
- [ ] State the constraint that breaks it.
- [ ] Name the maintainable state.
- [ ] State the invariant.
- [ ] Explain why discarded candidates cannot matter.
- [ ] List edge cases.
- [ ] State time and space complexity.

> **Recognition rule:** do not choose a pattern because of one keyword. Constraints + required output + maintainable state + invariant are stronger evidence.
