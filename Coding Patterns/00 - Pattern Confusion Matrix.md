---
title: Pattern Confusion Matrix
type: guide
category: Coding Patterns
tags:
  - pattern-recognition
  - interview-prep
---

# Pattern Confusion Matrix

> Most recognition failures happen between two plausible patterns. Use this page when you are unsure.

| If you are deciding between | Ask this question | Choose |
|---|---|---|
| [[01_Array/01 - Prefix Sum]] vs [[01_Array/03 - Sliding Window]] | Do I need arbitrary historical ranges, or one active contiguous window? | Prefix = reusable prefix state; Window = maintain one active range |
| [[01_Array/02 - Two Pointers]] vs [[01_Array/03 - Sliding Window]] | Is the range itself the object being optimized? | Pair/order/partition = Two Pointers; contiguous range = Window |
| [[01_Array/04 - Frequency Counting]] vs [[01_Array/03 - Sliding Window]] | Does the count describe the whole problem or the active range? | Global/canonical counts = Frequency; window constraint = Sliding Window + counts |
| [[05_Trees_Graphs/03 - BFS]] vs [[05_Trees_Graphs/02 - DFS]] | Do I need minimum unweighted distance or complete exploration? | Minimum levels = BFS; exhaustive/path reasoning = DFS |
| [[05_Trees_Graphs/03 - BFS]] vs [[05_Trees_Graphs/04 - Shortest Path]] | Do edges have different non-negative costs? | Equal cost = BFS; weighted = shortest-path algorithm |
| [[05_Trees_Graphs/02 - DFS]] vs [[07_Backtracking_DP/01 - Backtracking]] | Am I traversing an existing structure or constructing candidate states? | Existing structure = DFS; constructing choices = Backtracking |
| [[07_Backtracking_DP/02 - Dynamic Programming]] vs [[07_Backtracking_DP/01 - Backtracking]] | Do different branches reach the same state? | Repeated state = DP; unique configurations = Backtracking |
| [[07_Backtracking_DP/02 - Dynamic Programming]] vs [[07_Backtracking_DP/03 - Greedy]] | Can the local choice be proved safe without remembering alternatives? | Yes = Greedy; no / alternatives interact = DP |
| [[03_Stack_Heap/02 - Top K Elements]] vs sorting | Do I need only K results or the entire order? | K only = Heap; full ordering = Sort |
| [[03_Stack_Heap/01 - Monotonic Stack]] vs heap | Is the required answer the nearest greater/smaller unresolved element? | Yes = Monotonic Stack; global K/order = Heap |
| [[04_Intervals_Search/02 - Modified Binary Search]] vs Two Pointers | Is there a monotonic decision that eliminates half the search space? | Yes = Binary Search; local ordered scan = Two Pointers |
| [[05_Trees_Graphs/06 - Union Find]] vs BFS/DFS | Do I only care whether components are connected? | Repeated connectivity queries = Union Find; traversal/path data = BFS/DFS |

## Diagnostic sequence

When stuck:

1. State the brute force.
2. Identify the expensive repeated work.
3. Ask what state could summarize that work.
4. Ask whether the state is **local**, **prefix-based**, **graph frontier**, **recursive**, or **global priority**.
5. State the invariant.
6. Only then choose the implementation data structure.

## Anti-pattern

Do not choose a pattern because a problem contains a familiar word such as “substring,” “sorted,” or “minimum.”

Keywords are signals. **Constraints + required output + invariant are evidence.**
