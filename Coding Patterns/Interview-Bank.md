---
title: "Interview Bank"
category: revision
tags: [coding-patterns, interview, revision]
created: 2026-09-23
completed: false
---

# Interview Bank — Coding Patterns

> Part of [[README|20 DSA Patterns]] • `revision` • Curated Q&A aggregated from all 21 patterns. Source of truth remains in each note.

## How to Use
- This is a **cram index** — answers live in source notes (linked). Don't duplicate.
- For spaced repetition, add `sr-due: YYYY-MM-DD` to source notes; [[Master Dashboard|Master Dashboard]] tracks due.
- Drill rule: **Answer aloud, then check the note.** Recognition (reading the answer and nodding) is not retrieval.

---

## 01 Array

### 1. Prefix Sum → [[01_Array/01 - Prefix Sum]]
- **Q:** Count subarrays with sum k — why does hashmap on prefix sums work?
- **Q:** When would you NOT use prefix sum for range queries?
- **Q:** 2D range sum query immutable — formula?

### 2. Two Pointers → [[01_Array/02 - Two Pointers]]
- **Q:** Container With Most Water — why does moving the shorter wall never miss the optimum?
- **Q:** 3Sum with duplicates — walk through the skip logic.
- **Q:** Can two pointers work on rotated sorted array for pair sum?

### 3. Sliding Window → [[01_Array/03 - Sliding Window]]
- **Q:** Longest substring without repeating — why update answer *after* the shrink loop?
- **Q:** Minimum window substring — why `formed == required` not just "all chars present"?
- **Q:** Can sliding window handle negatives for "longest subarray with sum ≤ k"?

### 6. Frequency Counting → [[01_Array/04 - Frequency Counting]]
- **Q:** Valid Anagram — why `int[26]` over HashMap? Actual performance difference?
- **Q:** Group Anagrams — frequency array key vs sorted string key?
- **Q:** Top K Frequent — heap vs bucket sort decision rule?

---

## 02 LinkedList

### 4. Fast & Slow Pointers → [[02_LinkedList/01 - Fast and Slow Pointers]]
- **Q:** Prove why resetting one pointer to head finds cycle entry.
- **Q:** Happy Number — why does fast/slow work on a number sequence?
- **Q:** Find Duplicate (LC 287) — why treat array as linked list?

### 5. In-place Reversal → [[02_LinkedList/02 - LinkedList In-place Reversal]]
- **Q:** Reverse Between (LC 92) — why does head-insertion loop run `n-m` times?
- **Q:** Reverse K-Group — how handle last group with < k nodes?
- **Q:** Palindrome check O(1) space — full algorithm including restore.

---

## 03 Stack & Heap

### 7. Monotonic Stack → [[03_Stack_Heap/01 - Monotonic Stack]]
- **Q:** Why is inner `while` loop O(n) total, not O(n²)?
- **Q:** Daily Temperatures — why store indices, not values?
- **Q:** Largest Rectangle in Histogram — width calc when stack empties after pop?
- **Q:** Trapping Rain Water — how does monotonic stack apply?

### 9. Top K Elements → [[03_Stack_Heap/02 - Top K Elements]]
- **Q:** Why min-heap for k largest? Explain eviction logic.
- **Q:** Quickselect vs Heap for kth largest — when choose which?
- **Q:** Top K Frequent — heap vs bucket sort decision rule?
- **Q:** K Closest Points — why max-heap instead of min-heap?

---

## 04 Intervals & Search

### 10. Overlapping Intervals → [[04_Intervals_Search/01 - Overlapping Intervals]]
- **Q:** Merge vs Non-overlapping — why different sort keys (start vs end)?
- **Q:** Insert Interval (LC 57) — why three-phase better than binary search?
- **Q:** `[1,3], [3,5]` — do they overlap? Depends on problem.
- **Q:** Meeting Rooms II — how does it relate to this pattern?

### 11. Modified Binary Search → [[04_Intervals_Search/02 - Modified Binary Search]]
- **Q:** Search in Rotated — why `nums[lo] <= nums[mid]` not `<`?
- **Q:** Find Min in Rotated — why `lo < hi` not `lo <= hi`?
- **Q:** Binary Search on Answer — how do you know predicate is monotonic?
- **Q:** Search in Rotated with Duplicates (LC 81) — what breaks?

---

## 05 Trees & Graphs

### 12. Binary Tree Traversal → [[05_Trees_Graphs/01 - Binary Tree Traversal]]
- **Q:** Iterative inorder — why inner `while (cur != null)` loop?
- **Q:** Morris traversal — how O(1) space?
- **Q:** Postorder iterative — why harder than pre/in?
- **Q:** BST validation — why inorder works?

### 13. DFS → [[05_Trees_Graphs/02 - DFS]]
- **Q:** Number of Islands — why modify grid vs visited array?
- **Q:** Clone Graph — why hashmap serves dual purpose (visited + cache)?
- **Q:** Topological Sort via DFS — how does it work?
- **Q:** Path Sum II — why copy path when adding to result?

### 14. BFS → [[05_Trees_Graphs/03 - BFS]]
- **Q:** Why capture `sz = q.size()` before inner loop?
- **Q:** Word Ladder — why bidirectional BFS? Complexity win?
- **Q:** Rotting Oranges — why multi-source BFS?
- **Q:** Can BFS find shortest path in weighted graph with positive integer weights?

### 15. Shortest Path → [[05_Trees_Graphs/04 - Shortest Path]]
- **Q:** Dijkstra stale-entry skip — optimization or correctness requirement?
- **Q:** Cheapest Flights K Stops — why Bellman-Ford not Dijkstra?
- **Q:** Floyd-Warshall vs V×Dijkstra — when use which?
- **Q:** A* vs Dijkstra — difference?

### 18. Trie → [[05_Trees_Graphs/05 - Trie]]
- **Q:** Word Search II — why Trie + DFS prunes so effectively?
- **Q:** Trie vs HashMap for exact lookup — when HashMap wins?
- **Q:** Unicode/case-insensitive Trie — how implement?
- **Q:** Add and Search Words (LC 211) — handle `.` wildcard?

### 21. Union Find → [[05_Trees_Graphs/06 - Union Find]]
- **Q:** Why path compression AND union by rank both necessary?
- **Q:** Redundant Connection — why first failed union gives answer?
- **Q:** Accounts Merge — why DSU on emails not account indices?
- **Q:** Number of Islands II (LC 305) — how DSU handles dynamic addition?
- **Q:** Why can't Union Find detect directed cycles?

---

## 06 Matrix

### 16. Matrix Traversal → [[06_Matrix/01 - Matrix Traversal]]
- **Q:** Flood Fill — why check `old == newColor` first?
- **Q:** Number of Islands — why is grid modification acceptable?
- **Q:** Surrounded Regions — why start from border O's?
- **Q:** 0-1 BFS — when use on grid?

---

## 07 Backtracking & DP

### 17. Backtracking → [[07_Backtracking_DP/01 - Backtracking]]
- **Q:** Subsets vs Permutations — why `start` index vs `used[]`?
- **Q:** N-Queens bitmask — explain three bitmasks (cols, diag1, diag2).
- **Q:** Word Search — why mark board `#` instead of visited array?
- **Q:** Backtracking vs DP — how decide which applies?

### 19. Greedy → [[07_Backtracking_DP/03 - Greedy]]
- **Q:** Jump Game II — why `curEnd`/`far` gives minimum jumps?
- **Q:** Non-overlapping Intervals — why sort by end not start?
- **Q:** Coin change [1,3,4] for 6 — why greedy fails?
- **Q:** Gas Station (LC 134) — how is it greedy?
- **Q:** "Prove your greedy choice" — what's the exchange argument structure?

### 20. Dynamic Programming → [[07_Backtracking_DP/02 - Dynamic Programming]]
- **Q:** 0/1 vs Unbounded Knapsack — why loop direction matters?
- **Q:** Coin Change — why outer loop over coins (combinations)?
- **Q:** LCS — why 2D harder to compress to 1D?
- **Q:** House Robber — how get O(1) space?
- **Q:** DP vs Greedy — how know which?

---

## 08 Bit Manipulation

### 8. Bit Manipulation → [[08_Bit_Manipulation/01 - Bit Manipulation]]
- **Q:** Single Number II — explain two-bit state machine (ones, twos).
- **Q:** Two singles (LC 260) — how partition by differing bit?
- **Q:** `n & (n-1) == 0` tests power of two — why?
- **Q:** Java `>>` vs `>>>` — when does it matter?
- **Q:** Subset enumeration bitmask vs backtracking — when better?

---

## Drill Schedule (Weekly)

| Day | Activity |
|-----|----------|
| Mon | 3 Array patterns (cold recall) |
| Tue | 2 LinkedList + 2 Stack/Heap |
| Wed | 2 Intervals + 2 Trees/Graphs |
| Thu | 2 Matrix/Backtrack + 1 DP |
| Fri | 1 Greedy + 1 Bit + 1 Union Find |
| Sat | Timed: 5 random Q&A + 1 LeetCode Medium |
| Sun | Review misses, set `reviewed` + `sr-due` |

---

## Related
- [[README|20 DSA Patterns]] · [[Cheat Sheet]] · [[DSA-Roadmap-AlgoMaster]]
- [[Master Dashboard|Master Dashboard]] (tracks `sr-due` across all vaults)

---
*Category: revision*