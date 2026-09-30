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
  implementation_score as "Implementation",
  attempts as "Attempts",
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
  recognition_score as "Recognition",
  implementation_score as "Implementation"
FROM "Coding Patterns"
WHERE type = "pattern" AND advanced = true
SORT pattern ASC
~~~

## Pattern families

### Arrays & strings
Prefix Sum · Two Pointers · Sliding Window · Frequency Counting

### Linked lists
Fast & Slow · In-place Reversal

### Stack & heap
Monotonic Stack · Top K

### Intervals & search
Intervals · Binary Search

### Trees & graphs
Traversal · DFS · BFS · Shortest Path · Trie · Union Find

### Grid & optimization
Matrix · Backtracking · DP · Greedy · Bits

### Advanced
Cyclic Sort · Kadane · Segment Tree

## Recognition support

00 - Pattern Decision Tree · 00 - Pattern Confusion Matrix · 00 - Pattern Recognition Lab · 00 - Mixed Pattern Sets

## Mastery support

00 - Invariant Library · 00 - Pattern Combinations · 00 - Adaptive Review Engine · 00 - Weakness Heatmap · 00 - Interview Mode · 00 - Senior Trade-offs · 00 - Java Quality Layer

## Progression support

00 - Difficulty Progression · _templates/Problem-Analysis-Template
