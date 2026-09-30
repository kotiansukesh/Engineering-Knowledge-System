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

## Disambiguation questions

### Arrays / strings

- **Contiguous range?** Sliding Window or Prefix Sum.
- **Sorted / sortable pair reasoning?** Two Pointers.
- **Counts, anagrams, equivalence?** Frequency Counting.
- **Repeated range aggregation?** Prefix Sum.
- **Monotonic search space?** Binary Search.

### Trees / graphs / grids

- **Fewest unweighted steps?** BFS.
- **Exhaustive traversal or path state?** DFS.
- **Weighted shortest path?** Shortest Path algorithms.
- **Dynamic connectivity?** Union Find.
- **Prefix dictionary?** Trie.
- **Grid connectivity?** Matrix + DFS/BFS.

### Optimization / search

- **Enumerate valid choices?** Backtracking.
- **Repeated state?** DP.
- **Local choice has a proof?** Greedy.
- **K best?** Heap / Top K.
- **Feasibility is monotonic?** Binary Search on Answer.

## Complexity filter

Use constraints to reject approaches before coding.

- n around 10^5 usually rules out O(n²).
- n around 10^3 can make O(n²) reasonable.
- Exponential solutions need small inputs and/or strong pruning.

## Pattern combinations

| Combination | Typical use |
|---|---|
| Sliding Window + HashMap | constrained substring |
| Prefix Sum + HashMap | target-sum subarrays |
| Binary Search + Greedy | feasible answer optimization |
| BFS + HashSet | shortest unweighted path |
| DFS + Memoization | repeated state |
| Heap + HashMap | frequency + Top K |
| Matrix + BFS | shortest grid path |
| Backtracking + pruning | constrained enumeration |

## Pre-code checklist

- [ ] State the brute force.
- [ ] State the constraint that breaks it.
- [ ] Name the state you maintain.
- [ ] State the invariant.
- [ ] Explain why discarded candidates cannot matter.
- [ ] List edge cases.
- [ ] State time and space complexity.

> **Recognition rule:** ask “What information can I maintain so I never recompute the same work?”
