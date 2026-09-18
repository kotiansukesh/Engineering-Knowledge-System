---
title: "20 DSA Patterns: Master Guide"
type: MOC
tags: [MOC, leetcode, coding-patterns, interview-prep, dsa]
created: 2026-09-02
updated: 2026-09-02
source: "https://blog.algomaster.io/p/20-dsa-patterns"
status: complete
patterns: 20
---
# 20 dsa Patterns: Master Guide

> Source: [AlgoMaster: DSA was hard until I learned these 20 patterns](https://blog.algomaster.io/p/20-dsa-patterns), Ashish Pratap Singh. Templates included.
> **Thesis:** DSA is less about quantity, more about recognizing *patterns*. Same patterns repeatedly appeared in interviews at Amazon & Google.

> Previous version: 15 patterns. **Update 2026-09-02:** Added 5 new patterns → **Frequency Counting (6), Bit Manipulation (8), Shortest Path (15), Trie (18), Greedy (19)** and shifted numbering. See migration note at bottom.
```dataview
TABLE pattern as "#", category as "Category", leetcode as "LeetCode"
FROM "Coding Patterns"
WHERE pattern
SORT pattern ASC
```
---

## Vault Structure

```
Coding Patterns/
├── README.md (you are here, 20-pattern MOC)
├── 01_Array/ → 1 Prefix Sum, 2 Two Pointers, 3 Sliding Window, 6 Frequency Counting
├── 02_LinkedList/ → 4 Fast & Slow, 5 LinkedList Reversal
├── 03_Stack_Heap/ → 7 Monotonic Stack, 9 Top K
├── 08_Bit_Manipulation/ → 8 Bit Manipulation (new)
├── 04_Intervals_Search/ → 10 Overlapping Intervals, 11 Modified Binary Search
├── 05_Trees_Graphs/ → 12 Tree Traversal, 13 DFS, 14 BFS, 15 Shortest Path (new), 18 Trie (new)
├── 06_Matrix/ → 16 Matrix Traversal
├── 07_Backtracking_DP/ → 17 Backtracking, 19 Greedy (new), 20 Dynamic Programming
├── _attachments/ → images
└── _templates/ → pattern template
```
> Legacy folder `𝗖𝗼𝗱𝗶𝗻𝗴 𝗣𝗮𝘁𝘁𝗲𝗿𝗻𝘀` (stylized unicode) is deprecated, use `Coding Patterns`.

---

## Overview map - 20 Patterns

| # | Pattern | Folder | When to Use | Core DS | Time |
|---|---------|--------|-------------|---------|------|
| 1 | [[01_Array/01 - Prefix Sum\|Prefix Sum]] | `01_Array` | multiple range sum queries | prefix[] | O(1) query |
| 2 | [[01_Array/02 - Two Pointers\|Two Pointers]] | `01_Array` | sorted pair, partition, palindrome | 2 indices | O(n) |
| 3 | [[01_Array/03 - Sliding Window\|Sliding Window]] | `01_Array` | contiguous subarray/substring | window [l,r] | O(n) |
| 4 | [[02_LinkedList/01 - Fast and Slow Pointers\|Fast & Slow Pointers]] | `02_LinkedList` | cycle, middle, duplicate | tortoise & hare | O(n) |
| 5 | [[02_LinkedList/02 - LinkedList In-place Reversal\|LinkedList Reversal]] | `02_LinkedList` | reverse section O(1) space | pointer flip | O(n) |
| 6 | [[01_Array/04 - Frequency Counting\|Frequency Counting]] (new) | `01_Array` | duplicates, anagrams, k-times | HashMap / array | O(n) |
| 7 | [[03_Stack_Heap/01 - Monotonic Stack\|Monotonic Stack]] | `03_Stack_Heap` | next greater/smaller, histogram | stack | O(n) |
| 8 | [[08_Bit_Manipulation/01 - Bit Manipulation\|Bit Manipulation]] (new) | `08_Bit_Manipulation` | unique via XOR, power of 2, bits | bitwise | O(n) |
| 9 | [[03_Stack_Heap/02 - Top K Elements\|Top K Elements]] | `03_Stack_Heap` | k largest/smallest/frequent | heap | O(n log k) |
| 10 | [[04_Intervals_Search/01 - Overlapping Intervals\|Overlapping Intervals]] | `04_Intervals_Search` | merge intervals, scheduling | sort+merge | O(n log n) |
| 11 | [[04_Intervals_Search/02 - Modified Binary Search\|Modified Binary Search]] | `04_Intervals_Search` | rotated array, boundaries | BS variant | O(log n) |
| 12 | [[05_Trees_Graphs/01 - Binary Tree Traversal\|Binary Tree Traversal]] | `05_Trees_Graphs` | preorder/inorder/postorder | recursion/stack | O(n) |
| 13 | [[05_Trees_Graphs/02 - DFS\|DFS]] | `05_Trees_Graphs` | all paths, components, topo sort | recursion+visited | O(V+E) |
| 14 | [[05_Trees_Graphs/03 - BFS\|BFS]] | `05_Trees_Graphs` | shortest path unweighted, level order | queue | O(V+E) |
| 15 | [[05_Trees_Graphs/04 - Shortest Path\|Shortest Path]] (new) | `05_Trees_Graphs` | weighted shortest path | Dijkstra / Bellman-Ford | O((V+E) log V) |
| 16 | [[06_Matrix/01 - Matrix Traversal\|Matrix Traversal]] | `06_Matrix` | grid islands, flood fill, maze | DFS/BFS + dirs | O(m·n) |
| 17 | [[07_Backtracking_DP/01 - Backtracking\|Backtracking]] | `07_Backtracking_DP` | permutations/combinations/subsets | choose→explore→unchoose | O(2ⁿ) |
| 18 | [[05_Trees_Graphs/05 - Trie\|Trie (Prefix Search)]] (new) | `05_Trees_Graphs` | autocomplete, prefix search | Trie (prefix tree) | O(L) per word |
| 19 | [[07_Backtracking_DP/03 - Greedy\|Greedy]] (new) | `07_Backtracking_DP` | interval scheduling, jump game | sort + local optimal | O(n log n) |
| 20 | [[07_Backtracking_DP/02 - Dynamic Programming\|Dynamic Programming]] | `07_Backtracking_DP` | overlapping subproblems, optimal substructure | memo/tabulation | O(n·states) |

> (new) = 5 patterns added in 20-pattern update

> Beyond 20: [[05_Trees_Graphs/06 - Union Find|#21 Union Find]] (the course-named pattern the 20 list omits) · [[DSA-Roadmap-AlgoMaster|DSA Roadmap]] (75/150/300 tracks, study loop, animations)

---

## Pattern Summaries

### 01 - Array

#### 1. Prefix sum -`[[01_Array/01 - Prefix Sum|→ note]]`
**Idea:** `pref[i+1]=pref[i]+nums[i]`, `sum(l,r)=pref[r+1]-pref[l]`
**Template:** build + O(1) query | **LC:** #303, #525, #560

#### 2. two Pointers -`[[01_Array/02 - Two Pointers|→ note]]`
**Idea:** opposite ends (`left=0,right=n-1`) or same direction (`slow/fast`)
**LC:** #167, #15, #11

#### 3. Sliding Window -`[[01_Array/03 - Sliding Window|→ note]]`
**Idea:** fixed-k (initial window + slide) vs variable (`while` shrink)
**LC:** #643, #3, #76

#### 6. Frequency Counting -`[[01_Array/04 - Frequency Counting|→ note]]`(New)
**Idea:** `Map` or `int[26]` to count occurrences; trade space for O(n)
**Template:** `freq.put(x, getOrDefault+1)` + second pass | **LC:** #242, #49, #347

### 02 - Linked List

#### 4. Fast and Slow -`[[02_LinkedList/01 - Fast and Slow Pointers|→ note]]`
**Idea:** `slow=1, fast=2` → meet if cycle; middle when `fast` hits end | **LC:** #141, #202, #287

#### 5. Linked List Reversal -`[[02_LinkedList/02 - LinkedList In-place Reversal|→ note]]`
**Idea:** `prev,curr,nxt` flip; dummy + move-to-front for sublist m-n | **LC:** #206, #92, #24

### 03 - Stack and Heap

#### 7. Monotonic Stack -`[[03_Stack_Heap/01 - Monotonic Stack|→ note]]`
**Idea:** keep increasing/decreasing; pop while violating → reveals next greater | **LC:** #496, #739, #84

#### 8. bit Manipulation -`[[08_Bit_Manipulation/01 - Bit Manipulation|→ note]]`(New)
**Idea:** `a^a=0`, `n&(n-1)==0` is power of 2; `xor` finds single | **LC:** #136, #191, #231

#### 9. top k -`[[03_Stack_Heap/02 - Top K Elements|→ note]]`
**Idea:** min-heap size k for k largest (`peek()` is k-th) | **LC:** #215, #347, #373

### 04 - Intervals and Search

#### 10. Overlapping Intervals -`[[04_Intervals_Search/01 - Overlapping Intervals|→ note]]`
**Idea:** sort by start, overlap if `b >= c` → `end=max(end, currEnd)` | **LC:** #56, #57, #435

#### 11. Modified Binary Search -`[[04_Intervals_Search/02 - Modified Binary Search|→ note]]`
**Idea:** one half always sorted in rotated array | **LC:** #33, #153, #240

### 05 - Trees and Graphs

#### 12. Binary Tree Traversal -`[[05_Trees_Graphs/01 - Binary Tree Traversal|→ note]]`
Pre / In / Post | **LC:** #257, #230, #124

#### 13. dfs -`[[05_Trees_Graphs/02 - DFS|→ note]]`
Recursion + `visited[]`, deep before backtrack | **LC:** #133, #113, #210

#### 14. bfs -`[[05_Trees_Graphs/03 - BFS|→ note]]`
Queue level-by-level, shortest path unweighted | **LC:** #102, #994, #127

#### 15. Shortest Path -`[[05_Trees_Graphs/04 - Shortest Path|→ note]]`(New)
**Idea:** Dijkstra (non-negative, heap) vs Bellman-Ford (negative, V-1 relaxations) | **LC:** #743, #787

### 06 - Matrix

#### 16. Matrix Traversal -`[[06_Matrix/01 - Matrix Traversal|→ note]]`
4 dirs `{{1,0},{-1,0},{0,1},{0,-1}}` DFS/BFS | **LC:** #733, #200, #130

### 07 - Backtracking, Greedy and dp

#### 17. Backtracking -`[[07_Backtracking_DP/01 - Backtracking|→ note]]`
`choose → explore → un-choose` | **LC:** #46, #78, #51

#### 18. Trie -`[[05_Trees_Graphs/05 - Trie|→ note]]`(New)
**Idea:** `children[26]` + `isEnd`; paths = prefixes; `insert/search/startsWith` O(L) | **LC:** #208, #211, #212

#### 19. Greedy -`[[07_Backtracking_DP/03 - Greedy|→ note]]`(New)
**Idea:** sort by greedy criterion, locally optimal → globally optimal if provable | **LC:** #55, #45, #435

#### 20. Dynamic Programming -`[[07_Backtracking_DP/02 - Dynamic Programming|→ note]]`
Memo vs tabulation; sub-patterns: Fib, 0/1 Knapsack, LCS, LIS… | **Deep dive:** https://blog.algomaster.io/p/20-patterns-to-master-dynamic-programming | **LC:** #70, #300, #1143

---

## Migration from 15 to 20

| Old # (15) | Pattern | New # (20) | Change |
|------------|---------|------------|--------|
| 6 | Monotonic Stack | 7 | shifted +1 |
| 7 | Top K | 9 | shifted +2 (inserted Freq 6 + Bit 8) |
| 8 | Overlapping Intervals | 10 | shifted +2 |
| 9 | Modified Binary Search | 11 | shifted +2 |
| 10 | Binary Tree Traversal | 12 | shifted +2 |
| 11 | DFS | 13 | shifted +2 |
| 12 | BFS | 14 | shifted +2 |
| - | - | 15 | (new) Shortest Path |
| 13 | Matrix Traversal | 16 | shifted +3 |
| 14 | Backtracking | 17 | shifted +3 |
| - | - | 18 | (new) Trie |
| - | - | 19 | (new) Greedy |
| 15 | DP | 20 | shifted +5 |
| - | - | 6 | (new) Frequency Counting |
| - | - | 8 | (new) Bit Manipulation |

Files kept stable names (`01 - Prefix Sum.md` etc.); pattern number is in frontmatter `pattern:`, sorted by that field in Dataview.

---

## How to Practice (AlgoMaster Plan)

1. **One pattern per week**, 3 easy → 2 medium → 1 hard
2. **Template first**, memorize skeleton, then adapt
3. **Trigger words**, identify pattern in 30 seconds
4. **Spaced repetition**, re-solve without looking after 3 days

---

## Quick Revision Checklist - 20

- [ ] Prefix sum `pref[r+1]-pref[l]` ?
- [ ] Two pointers (opposite + same direction)?
- [ ] Fixed vs variable sliding window?
- [ ] Tortoise & hare (cycle + middle + start)?
- [ ] Reverse linked list in-place?
- [ ] Frequency counting with HashMap vs array[26]?
- [ ] Monotonic stack for next greater?
- [ ] Bit tricks: `xor`, `n&(n-1)`, `1<<i`?
- [ ] Min-heap for top-K?
- [ ] Merge intervals (`b>=c`)?
- [ ] Rotated BS half-sorted check?
- [ ] Pre/In/Post traversals?
- [ ] DFS recursion + visited?
- [ ] BFS queue level-order?
- [ ] Dijkstra pq template?
- [ ] Matrix 4-dir DFS/BFS?
- [ ] Backtrack `choose→explore→un-choose`?
- [ ] Trie `children[26]` + `isEnd`?
- [ ] Greedy sorting criterion?
- [ ] DP state + transition (1D/2D)?
```dataview
TABLE WITHOUT ID
 file.link as "Pattern",
 choice(completed, "✅", "⬜") as "Done",
 choice(reviewed, "✅", "⬜") as "Reviewed"
FROM "Coding Patterns"
WHERE pattern
SORT pattern ASC
```
*Add `completed: true` and `reviewed: true` to frontmatter when done.*

---

> **Java 25 (Sep 2025) refresh:** All 20 pattern templates annotated `// Java 25:`, `var`, `record`, `instanceof` pattern matching, `SequencedCollection`/`SequencedMap` (`getFirst`/`getLast`/`reversed`), and virtual-thread `StructuredTaskScope` notes for parallel BFS/DFS/Backtracking. `Compact Object Headers` (JEP 450) noted for HashMap/Trie node memory.

Created: 2026-09-02 | Updated: 2026-09-02 for 20 DSA Patterns · Java 25 snippets Sep 2025 | Source: AlgoMaster
