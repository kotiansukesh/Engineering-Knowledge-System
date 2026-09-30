---
title: "Pattern Decision Tree"
category: "Coding Patterns"
tags: [MOC, dsa, pattern-recognition, interview-prep]
created: "2026-09-30"
---

# Pattern Decision Tree

> Use this **before coding**. The goal is not to guess the exact algorithm immediately; narrow the search space from problem shape → invariant → pattern.

## 1. Start with the problem shape

### Array / String

| Signal | First candidates |
|---|---|
| Contiguous subarray / substring | [[01_Array/03 - Sliding Window|Sliding Window]], [[01_Array/01 - Prefix Sum|Prefix Sum]] |
| Sorted input / pair or triplet | [[01_Array/02 - Two Pointers|Two Pointers]] |
| Repeated range-sum queries | [[01_Array/01 - Prefix Sum|Prefix Sum]] |
| Frequency / anagram / counting | [[01_Array/04 - Frequency Counting|Frequency Counting]] |
| Search in ordered space | [[04_Intervals_Search/02 - Modified Binary Search|Modified Binary Search]] |
| Values are 1..n or nearly positional | [[09_Advanced/01 - Cyclic Sort|Cyclic Sort]] |
| Maximum subarray sum | [[09_Advanced/02 - Kadane's Algorithm|Kadane's Algorithm]] |

### Linked List

| Signal | First candidate |
|---|---|
| Cycle / middle / relative speed | [[02_LinkedList/01 - Fast and Slow Pointers|Fast & Slow Pointers]] |
| Reverse links in-place | [[02_LinkedList/02 - LinkedList In-place Reversal|In-place Reversal]] |

### Stack / Heap

| Signal | First candidate |
|---|---|
| Next greater/smaller element | [[03_Stack_Heap/01 - Monotonic Stack|Monotonic Stack]] |
| Top K / kth largest / closest K | [[03_Stack_Heap/02 - Top K Elements|Top K Elements]] |
| Nested delimiters / expression parsing | Stack |
| Need minimum/maximum repeatedly | Heap or monotonic structure |

### Intervals / Search

| Signal | First candidate |
|---|---|
| Ranges overlap / merge | [[04_Intervals_Search/01 - Overlapping Intervals|Overlapping Intervals]] |
| Sorted/monotonic search space | [[04_Intervals_Search/02 - Modified Binary Search|Modified Binary Search]] |

### Trees / Graphs

| Signal | First candidate |
|---|---|
| Visit every node / structural property | [[05_Trees_Graphs/01 - Binary Tree Traversal|Tree Traversal]], [[05_Trees_Graphs/02 - DFS|DFS]] |
| Minimum levels / unweighted shortest path | [[05_Trees_Graphs/03 - BFS|BFS]] |
| Weighted shortest path | [[05_Trees_Graphs/04 - Shortest Path|Shortest Path]] |
| Prefix/string dictionary | [[05_Trees_Graphs/05 - Trie|Trie]] |
| Connectivity / components / redundant edge | [[05_Trees_Graphs/06 - Union Find|Union Find]] |

### Matrix

| Signal | First candidate |
|---|---|
| Grid movement / islands / connected regions | [[06_Matrix/01 - Matrix Traversal|Matrix Traversal]] |
| Grid shortest path | Matrix + BFS |
| Grid state optimization | Matrix + DP |

### Backtracking / DP / Greedy

| Signal | First candidate |
|---|---|
| Generate all valid combinations/permutations | [[07_Backtracking_DP/01 - Backtracking|Backtracking]] |
| Same subproblem appears repeatedly | [[07_Backtracking_DP/02 - Dynamic Programming|Dynamic Programming]] |
| Local choice may lead to global optimum | [[07_Backtracking_DP/03 - Greedy|Greedy]] |
| XOR / masks / bit counts | [[08_Bit_Manipulation/01 - Bit Manipulation|Bit Manipulation]] |

## 2. The critical questions

Before selecting a pattern, ask:

1. **What is the input structure?** Array, string, linked list, tree, graph, grid?
2. **Is the data ordered or monotonic?**
3. **Is the requested region contiguous?**
4. **Do I need all solutions, one solution, an optimum, or a count?**
5. **Is the input mutable?**
6. **Can I maintain an invariant while scanning?**
7. **Does the same state/subproblem repeat?**
8. **Is the answer determined by local choices or global state?**
9. **What constraint rules out the obvious brute force?**
10. **What must remain true after every iteration?**

## 3. Pattern vs data structure

Do not confuse these.

- **Pattern** = the reasoning strategy.
- **Data structure** = the mechanism used to implement it.

Examples:

- Sliding Window + HashMap
- BFS + Queue
- Top K + PriorityQueue
- Prefix Sum + HashMap
- DFS + recursion/explicit stack
- Shortest Path + PriorityQueue

## 4. Pattern composition

Harder problems frequently combine patterns.

| Primary | Secondary | Typical use |
|---|---|---|
| Sliding Window | HashMap | constrained substring |
| Prefix Sum | HashMap | subarray count |
| Binary Search | Greedy | search the answer |
| BFS | HashSet | shortest unweighted path |
| DFS | Memoization | graph/tree DP |
| Backtracking | Pruning | constrained enumeration |
| Heap | HashMap | frequency + Top K |
| Matrix Traversal | BFS | grid shortest path |

## 5. Recognition rule

> **Do not ask “Which LeetCode problem is this?”**
>
> Ask **“What invariant would let me avoid recomputing work?”**

That question is the core of pattern recognition.
