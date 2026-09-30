---
title: Pattern Combinations
type: guide
category: Coding Patterns
tags:
  - pattern-recognition
  - combinations
---

# Pattern Combinations

> Real interview problems frequently combine two simple patterns.

| Primary | Secondary | Typical problem shape | Key interaction |
|---|---|---|---|
| Prefix Sum | HashMap | target-sum subarrays | map previous prefix frequencies |
| Sliding Window | Frequency Map | constrained substring | window movement updates counts |
| Two Pointers | Sorting | pair/triple constraints | ordering makes pointer elimination safe |
| Binary Search | Greedy | optimize a feasible answer | greedy feasibility must be monotonic |
| BFS | HashSet | shortest unweighted state path | visited prevents repeated frontier work |
| DFS | Memoization | repeated recursive states | cache overlapping subproblems |
| Heap | HashMap | frequency + Top K | map counts, heap retains K candidates |
| Monotonic Stack | Array | nearest greater/smaller | stack stores unresolved ordered candidates |
| Backtracking | Pruning | constrained enumeration | reject impossible partial states early |
| DP | Prefix Sum | range/state transitions | precomputed aggregates reduce transitions |
| Union Find | Sorting | connectivity under ordered events | process edges/events in useful order |
| Trie | DFS | word/grid search | prefix pruning reduces search |
| Graph | Topological Sort | dependency ordering | indegree captures unresolved prerequisites |
| Matrix | BFS/DFS | grid connectivity/path | coordinates become graph states |

## Combination recognition

1. What is the primary structure?
2. What repeated work remains?
3. Which secondary data structure removes it?
4. What combined invariant makes the solution safe?

Record only the primary technique, the secondary technique, and why they combine.
