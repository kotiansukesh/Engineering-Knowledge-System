---
title: "Coding Patterns MOC"
category: "Coding Patterns"
tags: [MOC, dsa, leetcode, patterns, interview-prep]
created: "2026-09-29"
completed: false
reviewed: ""
sr-due: ""
---

# Coding Patterns Vault

> **21 Core Patterns + 3 Advanced Patterns** → **78 LeetCode Problems** → **Pattern Recognition Mastery**
> 20-week roadmap: Recognize pattern → Code in 15 min → Explain trade-offs.
---


## 🧭 How to Use This Vault

**1. Start with [[00 - Pattern Decision Tree|Pattern Decision Tree]]**  
Use problem characteristics to narrow down candidate patterns.

**2. Learn from [[Patterns Index|Patterns Index]]**  
Pattern notes are the primary knowledge units; problem notes are applications.

**3. Practice with [[00 - Blind Practice|Blind Practice]]**  
Hide the pattern name and force recognition from the problem statement.

**4. Record failures in [[00 - Mistake Log|Mistake Log]]**  
Track incorrect reasoning, not just syntax mistakes.

**5. Measure mastery**  
**Solved ≠ Learned ≠ Recognized ≠ Mastered.**

The target is:
**Learn → Guided → Blind → Mixed → Mastered**

## 📊 Master Dashboard

```dataviewjs
const all = dv.pages('"Coding Patterns"').where(p => p.category && p.type === "note");
const total = all.length;
const done = all.where(p => p.completed === true).length;
const pct = total ? Math.round(done/total*100) : 0;
const bar = (p, w=30) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w-Math.round(p/100*w));
dv.paragraph(`**Patterns: ${total} | Completed: ${done} | Remaining: ${total-done}** — \`${pct}%\``);
dv.paragraph(`\`${bar(pct)}\` **${pct}%**`);
if (total === done && total > 0) dv.paragraph(`🎉 **All patterns completed!**`);
```
---

## 🎯 Pattern Index

| # | Pattern | Folder | Problems | Key LeetCode | Status |
|---|---------|--------|----------|--------------|--------|
| 1 | [[01_Array/01 - Prefix Sum\|Prefix Sum]] | 01_Array | 4 | 303, 525, 560 | `= this.file.link` |
| 2 | [[01_Array/02 - Two Pointers\|Two Pointers]] | 01_Array | 6 | 167, 11, 42, 75 | |
| 3 | [[01_Array/03 - Sliding Window\|Sliding Window]] | 01_Array | 8 | 3, 438, 76, 209 | |
| 4 | [[01_Array/04 - Frequency Counting\|Frequency Counting]] | 01_Array | 3 | 242, 49, 347 | |
| 5 | [[02_LinkedList/01 - Fast and Slow Pointers\|Fast/Slow Pointers]] | 02_LinkedList | 4 | 141, 202, 287 | |
| 6 | [[02_LinkedList/02 - LinkedList In-place Reversal\|In-place Reversal]] | 02_LinkedList | 3 | 206, 92, 25 | |
| 7 | [[03_Stack_Heap/01 - Monotonic Stack\|Monotonic Stack]] | 03_Stack_Heap | 5 | 739, 901, 84, 496 | |
| 8 | [[03_Stack_Heap/02 - Top K Elements\|Top K Elements]] | 03_Stack_Heap | 6 | 215, 347, 378, 973 | |
| 9 | [[04_Intervals_Search/01 - Overlapping Intervals\|Overlapping Intervals]] | 04_Intervals_Search | 5 | 56, 57, 986, 435 | |
| 10 | [[04_Intervals_Search/02 - Modified Binary Search\|Modified Binary Search]] | 04_Intervals_Search | 6 | 33, 34, 35, 153 | |
| 11 | [[05_Trees_Graphs/01 - Binary Tree Traversal\|Binary Tree Traversal]] | 05_Trees_Graphs | 6 | 94, 102, 103, 104 | |
| 12 | [[05_Trees_Graphs/02 - DFS\|DFS]] | 05_Trees_Graphs | 7 | 104, 110, 112, 129 | |
| 13 | [[05_Trees_Graphs/03 - BFS\|BFS]] | 05_Trees_Graphs | 5 | 102, 199, 127, 1161 | |
| 14 | [[05_Trees_Graphs/04 - Shortest Path\|Shortest Path]] | 05_Trees_Graphs | 4 | 743, 787, 1514 | |
| 15 | [[05_Trees_Graphs/05 - Trie\|Trie]] | 05_Trees_Graphs | 3 | 208, 211, 212 | |
| 16 | [[05_Trees_Graphs/06 - Union Find\|Union Find]] | 05_Trees_Graphs | 4 | 200, 684, 959 | |
| 17 | [[06_Matrix/01 - Matrix Traversal\|Matrix Traversal]] | 06_Matrix | 4 | 54, 733, 200 | |
| 18 | [[07_Backtracking_DP/01 - Backtracking\|Backtracking]] | 07_Backtracking_DP | 6 | 46, 77, 78, 39 | |
| 19 | [[07_Backtracking_DP/02 - Dynamic Programming\|Dynamic Programming]] | 07_Backtracking_DP | 10 | 70, 322, 300, 1143 | |
| 20 | [[07_Backtracking_DP/03 - Greedy\|Greedy]] | 07_Backtracking_DP | 4 | 455, 135, 435 | |
| 21 | [[08_Bit_Manipulation/01 - Bit Manipulation\|Bit Manipulation]] | 08_Bit_Manipulation | 4 | 191, 136, 260 | |

> **Advanced Patterns (3):** [[09_Advanced/01 - Cyclic Sort\|Cyclic Sort]], [[09_Advanced/02 - Kadane's Algorithm\|Kadane's Algorithm]], [[09_Advanced/03 - Segment Tree\|Segment Tree]]
---

## 📅 20-Week Roadmap (from Study Plan)

### Phase 1: Array & String (Weeks 1-4)
- **Week 1:** Prefix Sum + Two Pointers
- **Week 2:** Sliding Window (HIGH PRIORITY)
- **Week 3:** Frequency Counting + Intervals
- **Week 4:** Linked List Patterns

### Phase 2: Tree & Graph (Weeks 5-9)
- **Week 5:** Tree Traversal (BFS/DFS)
- **Week 6:** DFS Deep Dive
- **Week 7:** Graph Algorithms (Shortest Path, Union Find)
- **Week 8:** Trie + Advanced Trees
- **Week 9:** Stack & Heap Patterns

### Phase 3: DP & Backtracking (Weeks 10-14)
- **Week 10:** DP Foundation
- **Week 11:** DP Advanced
- **Week 12:** Backtracking
- **Week 13:** Greedy + Matrix
- **Week 14:** Bit Manipulation

### Phase 4: Mastery & Interview (Weeks 15-20)
- **Week 15:** Pattern Recognition Drills
- **Week 16:** Mock Interviews
- **Week 17:** System Design + Coding Integration
- **Week 18:** Weak Area Blitz
- **Week 19:** Final Polish
- **Week 20:** Interview Week
---

## 📋 Spaced Repetition Status

```dataview
TABLE WITHOUT ID
  file.link as "Pattern",
  reviewed as "Last Reviewed",
  "sr-due" as "Due",
  choice(!reviewed, "🔴 Never", choice(date(now)-reviewed > dur(7 days), "🟡 Stale", "🟢 Fresh")) as "Status"
FROM "Coding Patterns"
WHERE type = "note" AND (reviewed OR "sr-due")
SORT "sr-due" ASC
```
---

## 🏋️ Practice Tasks (All Notes)

```tasks
not done
path includes Coding Patterns
sort by due
group by filename
limit 30
```
---

## 🔗 Cross-Vault Links

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

## 📁 Folder Structure

```
Coding Patterns/
├── README.md                    ← This file (Vault MOC)
├── Patterns Index.md            ← Canonical pattern catalog
├── 00 - Pattern Decision Tree.md ← Recognition guide
├── 00 - Blind Practice.md       ← Unhinted practice
├── 00 - Mistake Log.md          ← Reasoning failure log
├── 01_Array/
│   ├── README.md               ← Folder MOC
│   ├── 01 - Prefix Sum.md
│   ├── 02 - Two Pointers.md
│   ├── 03 - Sliding Window.md
│   └── 04 - Frequency Counting.md
├── 02_LinkedList/
│   ├── README.md
│   ├── 01 - Fast and Slow Pointers.md
│   └── 02 - LinkedList In-place Reversal.md
├── 03_Stack_Heap/
│   ├── README.md
│   ├── 01 - Monotonic Stack.md
│   └── 02 - Top K Elements.md
├── 04_Intervals_Search/
│   ├── README.md
│   ├── 01 - Overlapping Intervals.md
│   └── 02 - Modified Binary Search.md
├── 05_Trees_Graphs/
│   ├── README.md
│   ├── 01 - Binary Tree Traversal.md
│   ├── 02 - DFS.md
│   ├── 03 - BFS.md
│   ├── 04 - Shortest Path.md
│   ├── 05 - Trie.md
│   └── 06 - Union Find.md
├── 06_Matrix/
│   ├── README.md
│   └── 01 - Matrix Traversal.md
├── 07_Backtracking_DP/
│   ├── README.md
│   ├── 01 - Backtracking.md
│   ├── 02 - Dynamic Programming.md
│   └── 03 - Greedy.md
├── 08_Bit_Manipulation/
│   ├── README.md
│   └── 01 - Bit Manipulation.md
├── 09_Advanced/                  ← Optional patterns
│   ├── README.md
│   ├── 01 - Cyclic Sort.md
│   ├── 02 - Kadane's Algorithm.md
│   └── 03 - Segment Tree.md
├── 99_Revision/
│   ├── README.md
│   └── Study-Plan.md
├── _templates/
│   └── Pattern-Note-Template.md
```
---

*Start here: [[Patterns Index|Patterns Index]] • [[00 - Pattern Decision Tree|Decision Tree]] • [[00 - Blind Practice|Blind Practice]] • [[00 - Mistake Log|Mistake Log]] • [[Coding Patterns/99_Revision/Study-Plan|20-Week Study Plan]] • [[Coding Patterns/01_Array/README\|01 Array]] • [[Coding Patterns/02_LinkedList/README\|02 LinkedList]] • [[Coding Patterns/03_Stack_Heap/README\|03 Stack/Heap]] • [[Coding Patterns/04_Intervals_Search/README\|04 Intervals/Search]] • [[Coding Patterns/05_Trees_Graphs/README\|05 Trees/Graphs]] • [[Coding Patterns/06_Matrix/README\|06 Matrix]] • [[Coding Patterns/07_Backtracking_DP/README\|07 Backtracking/DP]] • [[Coding Patterns/08_Bit_Manipulation/README\|08 Bit Manipulation]] • [[Coding Patterns/09_Advanced/README\|09 Advanced (Optional)]]*