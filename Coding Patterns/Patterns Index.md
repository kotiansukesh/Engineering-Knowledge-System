---
title: Patterns Index
type: index
category: Coding Patterns
tags:
  - index
  - dsa
  - pattern-recognition
---

# Patterns Index

> The catalog is generated from frontmatter. Status is not maintained manually.

## Core patterns

~~~dataview
TABLE WITHOUT ID
  pattern as "#",
  file.link as "Pattern",
  domain as "Domain",
  difficulty as "Difficulty",
  mastery as "Mastery",
  recognition_score as "Recognition",
  length(leetcode) as "Problems"
FROM "Coding Patterns"
WHERE type = "pattern" AND advanced != true
SORT pattern ASC
~~~

## Advanced patterns

~~~dataview
TABLE WITHOUT ID
  pattern as "#",
  file.link as "Pattern",
  domain as "Domain",
  difficulty as "Difficulty",
  mastery as "Mastery",
  recognition_score as "Recognition"
FROM "Coding Patterns"
WHERE type = "pattern" AND advanced = true
SORT pattern ASC
~~~

## Recognition rule

When two patterns look plausible, state:

1. Required output.
2. Input structure.
3. Constraint that breaks brute force.
4. State you can maintain.
5. Invariant that makes discarded work safe.

If you cannot state the invariant, you have not selected the pattern yet.

## Pattern families

### Arrays & strings
[[01_Array/01 - Prefix Sum|Prefix Sum]] · [[01_Array/02 - Two Pointers|Two Pointers]] · [[01_Array/03 - Sliding Window|Sliding Window]] · [[01_Array/04 - Frequency Counting|Frequency Counting]]

### Linked lists
[[02_LinkedList/01 - Fast and Slow Pointers|Fast & Slow]] · [[02_LinkedList/02 - LinkedList In-place Reversal|In-place Reversal]]

### Stack & heap
[[03_Stack_Heap/01 - Monotonic Stack|Monotonic Stack]] · [[03_Stack_Heap/02 - Top K Elements|Top K]]

### Intervals & search
[[04_Intervals_Search/01 - Overlapping Intervals|Intervals]] · [[04_Intervals_Search/02 - Modified Binary Search|Binary Search]]

### Trees & graphs
[[05_Trees_Graphs/01 - Binary Tree Traversal|Traversal]] · [[05_Trees_Graphs/02 - DFS|DFS]] · [[05_Trees_Graphs/03 - BFS|BFS]] · [[05_Trees_Graphs/04 - Shortest Path|Shortest Path]] · [[05_Trees_Graphs/05 - Trie|Trie]] · [[05_Trees_Graphs/06 - Union Find|Union Find]]

### Grid & optimization
[[06_Matrix/01 - Matrix Traversal|Matrix]] · [[07_Backtracking_DP/01 - Backtracking|Backtracking]] · [[07_Backtracking_DP/02 - Dynamic Programming|DP]] · [[07_Backtracking_DP/03 - Greedy|Greedy]] · [[08_Bit_Manipulation/01 - Bit Manipulation|Bits]]

### Advanced
[[09_Advanced/01 - Cyclic Sort|Cyclic Sort]] · [[09_Advanced/02 - Kadane's Algorithm|Kadane]] · [[09_Advanced/03 - Segment Tree|Segment Tree]]

## Recognition support

[[00 - Pattern Decision Tree|Decision Tree]] · [[00 - Pattern Confusion Matrix|Confusion Matrix]] · [[00 - Blind Practice|Blind Practice]]
