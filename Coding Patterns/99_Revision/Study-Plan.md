---
title: "Study Plan - Coding Patterns"
category: "Coding Patterns/99_Revision"
tags: [study-plan, roadmap, interview-prep, dsa]
created: "2026-09-27"
completed: false
difficulty: "Medium"
reviewed: ""
sr-due: ""
source: "Coding Patterns Vault 20-Week Roadmap"
weeks: "1-20"
type: "study-plan"
---

# Study Plan - Coding Patterns Vault

> **20-Week Roadmap** for LeetCode patterns mastery.
> Goal: Recognize pattern → Code in 15 min → Explain trade-offs.
> 21 patterns, 78 LeetCode problems mapped.

---

## Pattern Coverage Map

| # | Pattern | Folder | Problems | Key LeetCode |
|---|---------|--------|----------|--------------|
| 1 | Prefix Sum | 01_Array | 4 | 560, 930, 525 |
| 2 | Two Pointers | 01_Array | 6 | 167, 11, 42, 75 |
| 3 | **Sliding Window** | 01_Array | 8 | 3, 438, 76, 209 |
| 4 | Frequency Counting | 01_Array | 3 | 242, 49, 347 |
| 5 | Fast/Slow Pointers | 02_LinkedList | 4 | 141, 876, 287 |
| 6 | In-place Reversal | 02_LinkedList | 3 | 206, 92, 25 |
| 7 | Binary Tree Traversal | 05_Trees_Graphs | 6 | 94, 102, 103, 104 |
| 8 | **BFS** | 05_Trees_Graphs | 5 | 102, 199, 127, 1161 |
| 9 | **DFS** | 05_Trees_Graphs | 7 | 104, 110, 112, 129 |
| 10 | **Shortest Path** | 05_Trees_Graphs | 4 | 743, 787, 1514 |
| 11 | **Trie** | 05_Trees_Graphs | 3 | 208, 211, 212 |
| 12 | **Union Find** | 05_Trees_Graphs | 4 | 200, 684, 959 |
| 13 | Monotonic Stack | 03_Stack_Heap | 5 | 739, 901, 84, 496 |
| 14 | **Top K Elements** | 03_Stack_Heap | 6 | 215, 347, 378, 973 |
| 15 | Overlapping Intervals | 04_Intervals_Search | 5 | 56, 57, 986, 435 |
| 16 | Modified Binary Search | 04_Intervals_Search | 6 | 33, 34, 35, 153 |
| 17 | Backtracking | 07_Backtracking_DP | 6 | 46, 77, 78, 39 |
| 18 | **Dynamic Programming** | 07_Backtracking_DP | 10 | 70, 322, 300, 1143 |
| 19 | Greedy | 07_Backtracking_DP | 4 | 455, 135, 435 |
| 20 | Matrix Traversal | 06_Matrix | 4 | 54, 733, 200 |
| 21 | Bit Manipulation | 08_Bit_Manipulation | 4 | 191, 136, 260 |

---

## Phase 1: Array & String Patterns (Weeks 1-4)

### Week 1: Prefix Sum + Two Pointers
- [ ] [[Coding Patterns/01_Array/01 - Prefix Sum|Prefix Sum]] - 4 problems 📅 2026-09-28
- [ ] [[Coding Patterns/01_Array/02 - Two Pointers|Two Pointers]] - 6 problems 📅 2026-09-29
- [ ] **Code**: All 10 problems in Java 📅 2026-09-30
- [ ] **SR Review**: Template + 2 Pointers 📅 2026-10-01

### Week 2: Sliding Window (HIGH PRIORITY)
- [ ] [[Coding Patterns/01_Array/03 - Sliding Window|Sliding Window]] - 8 problems 📅 2026-10-02
- [ ] **Focus**: Variable vs fixed window, atMost(k) pattern
- [ ] **Cross-link**: [[Architect/10_System-Design-Interviews/BB-04-Rate-Limiter|Rate Limiter]] 📅 2026-10-03
- [ ] **SR Review**: All sliding window variants 📅 2026-10-04

### Week 3: Frequency Counting + Intervals
- [ ] [[Coding Patterns/01_Array/04 - Frequency Counting|Frequency Counting]] - 3 problems 📅 2026-10-05
- [ ] [[Coding Patterns/04_Intervals_Search/01 - Overlapping Intervals|Overlapping Intervals]] - 5 problems 📅 2026-10-06
- [ ] [[Coding Patterns/04_Intervals_Search/02 - Modified Binary Search|Modified Binary Search]] - 6 problems 📅 2026-10-07
- [ ] **SR Review**: Week 1-3 patterns 📅 2026-10-08

### Week 4: Linked List Patterns
- [ ] [[Coding Patterns/02_LinkedList/01 - Fast and Slow Pointers|Fast/Slow Pointers]] - 4 problems 📅 2026-10-09
- [ ] [[Coding Patterns/02_LinkedList/02 - LinkedList In-place Reversal|In-place Reversal]] - 3 problems 📅 2026-10-10
- [ ] **Code**: All 7 problems 📅 2026-10-11
- [ ] **SR Review**: Cycle detection, palindrome, reorder 📅 2026-10-12

---

## Phase 2: Tree & Graph Patterns (Weeks 5-9)

### Week 5: Tree Traversal (BFS/DFS)
- [ ] [[Coding Patterns/05_Trees_Graphs/01 - Binary Tree Traversal|Tree Traversal]] - 6 problems 📅 2026-10-13
- [ ] [[Coding Patterns/05_Trees_Graphs/03 - BFS|BFS]] - 5 problems 📅 2026-10-14
- [ ] **Cross-link**: [[Architect/10_System-Design-Interviews/INT-03-Web-Crawler|Web Crawler]] 📅 2026-10-15
- [ ] **SR Review**: Level-order, zigzag, right view 📅 2026-10-16

### Week 6: DFS Deep Dive
- [ ] [[Coding Patterns/05_Trees_Graphs/02 - DFS|DFS]] - 7 problems 📅 2026-10-17
- [ ] Focus: Path sum, diameter, max path, serialize 📅 2026-10-18
- [ ] **SR Review**: All DFS patterns 📅 2026-10-19

### Week 7: Graph Algorithms
- [ ] [[Coding Patterns/05_Trees_Graphs/04 - Shortest Path|Shortest Path]] - 4 problems 📅 2026-10-20
- [ ] [[Coding Patterns/05_Trees_Graphs/06 - Union Find|Union Find]] - 4 problems 📅 2026-10-21
- [ ] **Cross-link**: [[Architect/10_System-Design-Interviews/DB-05-Sharding|Sharding]] (consistent hashing) 📅 2026-10-22
- [ ] **SR Review**: Dijkstra, Union-Find optimizations 📅 2026-10-23

### Week 8: Trie + Advanced Trees
- [ ] [[Coding Patterns/05_Trees_Graphs/05 - Trie|Trie]] - 3 problems 📅 2026-10-24
- [ ] **Cross-link**: [[Architect/10_System-Design-Interviews/INT-08-Design-Autocomplete|Autocomplete]] 📅 2026-10-25
- [ ] [[Coding Patterns/05_Trees_Graphs/01 - Binary Tree Traversal|BST problems]] - Review 📅 2026-10-26
- [ ] **SR Review**: Trie insert/search/startsWith 📅 2026-10-27

### Week 9: Stack & Heap Patterns
- [ ] [[Coding Patterns/03_Stack_Heap/01 - Monotonic Stack|Monotonic Stack]] - 5 problems 📅 2026-10-28
- [ ] [[Coding Patterns/03_Stack_Heap/02 - Top K Elements|Top K (Heap)]] - 6 problems 📅 2026-10-29
- [ ] **Cross-link**: [[Architect/10_System-Design-Interviews/NET-01-Load-Balancer|Load Balancer]] (least connections = min-heap) 📅 2026-10-30
- [ ] [[Architect/10_System-Design-Interviews/INT-02-Twitter-Timeline|Twitter Timeline]] (merge k lists = heap) 📅 2026-10-31
- [ ] **SR Review**: NGE, daily temperatures, top K 📅 2026-11-01

---

## Phase 3: DP & Backtracking (Weeks 10-14)

### Week 10: DP Foundation
- [ ] [[Coding Patterns/07_Backtracking_DP/02 - Dynamic Programming|DP Patterns]] - 10 problems 📅 2026-11-02
- [ ] Focus: 0/1 Knapsack, LIS, Coin Change, House Robber
- [ ] **Template**: State definition → recurrence → base case 📅 2026-11-03

### Week 11: DP Advanced
- [ ] DP on strings (Edit Distance, LCS) 📅 2026-11-04
- [ ] DP on grids (Unique Paths, Min Path Sum) 📅 2026-11-05
- [ ] **SR Review**: All DP patterns 📅 2026-11-06

### Week 12: Backtracking
- [ ] [[Coding Patterns/07_Backtracking_DP/01 - Backtracking|Backtracking]] - 6 problems 📅 2026-11-07
- [ ] Focus: Subsets, Permutations, Combination Sum, N-Queens
- [ ] **SR Review**: Pruning strategies 📅 2026-11-08

### Week 13: Greedy + Matrix
- [ ] [[Coding Patterns/07_Backtracking_DP/03 - Greedy|Greedy]] - 4 problems 📅 2026-11-09
- [ ] [[Coding Patterns/06_Matrix/01 - Matrix Traversal|Matrix]] - 4 problems 📅 2026-11-10
- [ ] **SR Review**: Interval scheduling, jump game 📅 2026-11-11

### Week 14: Bit Manipulation
- [ ] [[Coding Patterns/08_Bit_Manipulation/01 - Bit Manipulation|Bit Manipulation]] - 4 problems 📅 2026-11-12
- [ ] Focus: XOR tricks, bit counting, masks
- [ ] **SR Review**: Single Number, Hamming Distance 📅 2026-11-13

---

## Phase 4: Mastery & Interview (Weeks 15-20)

### Week 15: Pattern Recognition Drills
- [ ] **Blind 75**: Solve 10 mixed (no pattern hints) 📅 2026-11-14
- [ ] Time each: Target < 20 min medium, < 35 min hard 📅 2026-11-15
- [ ] Tag each with pattern used 📅 2026-11-16

### Week 16: Mock Interviews (Coding)
- [ ] Mock 1: 45 min - 2 mediums 📅 2026-11-17
- [ ] Mock 2: 45 min - 1 hard 📅 2026-11-18
- [ ] Mock 3: 60 min - 2 mediums (system design context) 📅 2026-11-19
- [ ] **Review**: Record solutions, compare to templates 📅 2026-11-20

### Week 17: System Design + Coding Integration
- [ ] [[Architect/10_System-Design-Interviews/Practice-Problems/README|Practice Problems]] - 3 problems 📅 2026-11-21
- [ ] For each: Code core algorithm (rate limiter, cache, sharding) 📅 2026-11-22
- [ ] Explain how pattern maps to system design 📅 2026-11-23

### Week 18: Weak Area Blitz
- [ ] Top 5 stale patterns → re-solve 3 problems each 📅 2026-11-24
- [ ] Update all notes: `completed=true`, add missing flashcards 📅 2026-11-25
- [ ] **SR Review**: Full vault pass 📅 2026-11-26

### Week 19: Final Polish
- [ ] All 78 problems: code committed, explained 📅 2026-11-27
- [ ] Cheat sheet: 1-page per pattern (template + key insight) 📅 2026-11-28
- [ ] Anki export: `python3 export_anki.py` 📅 2026-11-29

### Week 20: Interview Week
- [ ] Light review only: flashcards, cheat sheets 📅 2026-11-30
- [ ] Sleep, hydrate, mental prep 📅 2026-12-01
- [ ] **Interview Day** 🎯 📅 2026-12-02

---

## Weekly Rituals

### Daily (Mon-Fri): 1.5 hrs
- [ ] **30 min**: 1 new problem (code + explain aloud)
- [ ] **30 min**: 2 review problems (spaced repetition)
- [ ] **30 min**: Pattern note update (flashcards, cross-links)

### Saturday: 2 hrs
- [ ] Mock coding session (timed)
- [ ] Update SR fields (`reviewed`, `sr-due`)

### Sunday: 1 hr
- [ ] Master Dashboard review
- [ ] Plan next week's pattern focus
- [ ] Anki sync

---

## Tracking Queries

```dataview
TABLE WITHOUT ID
  file.link as "Pattern",
  "leetcode" as "LC Problems",
  "problems-solved" as "Solved",
  round("problems-solved" / "leetcode" * 100, 0) as "%",
  completed as "Done",
  reviewed as "Reviewed"
FROM "Coding Patterns"
WHERE type = "note" AND file.name != "README"
SORT file.folder, file.name
```

---

## Milestone Gates

| Milestone | Criteria | Target |
|-----------|----------|--------|
| **Arrays Mastered** | Sliding Window, Two Pointers: all problems < 15 min | Week 4 |
| **Trees/Graphs** | BFS, DFS, Trie, Union Find: recognize instantly | Week 9 |
| **DP Confidence** | Identify state/recurrence in < 5 min | Week 14 |
| **Interview Ready** | All 78 problems solved, 3 mock passed | Week 20 |

---

## Cross-Vault Links

| Pattern | System Design Application |
|---------|---------------------------|
| Sliding Window | [[Architect/10_System-Design-Interviews/BB-04-Rate-Limiter\|Rate Limiter]] |
| Two Pointers | [[Architect/10_System-Design-Interviews/DB-05-Sharding\|Sharding]] range queries |
| BFS/DFS | [[Architect/10_System-Design-Interviews/INT-03-Web-Crawler\|Web Crawler]] |
| Heap (Top K) | [[Architect/10_System-Design-Interviews/NET-01-Load-Balancer\|Load Balancer]] least-conn |
| Trie | [[Architect/10_System-Design-Interviews/INT-08-Design-Autocomplete\|Autocomplete]] |
| Union Find | [[Architect/10_System-Design-Interviews/DB-05-Sharding\|Sharding]] (connected components) |
| DP | [[Architect/10_System-Design-Interviews/DB-01-Database-Internals\|Query Optimization]] |
| Monotonic Stack | [[Architect/10_System-Design-Interviews/CACHE-02-Cache-Strategies\|Cache Eviction]] |

---

*Next: [[Architect/_templates/Daily-Review-Queue|Daily Review Queue]]*