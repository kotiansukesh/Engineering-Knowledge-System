---
type: note
mastery: learn
recognition_score: 0
title: Backtracking
pattern: 18
category: Coding Patterns/07_Backtracking_DP
tags:
- pattern/backtracking
leetcode:
- 46
- 77
- 78
- 39
created: '2026-09-02'
completed: false
reviewed: ''
sr-due: ''
difficulty: Medium
source: https://blog.algomaster.io/p/20-dsa-patterns
excalidraw: ''
---


# Backtracking

> Part of [[README|Coding Patterns]] • `Coding Patterns/07_Backtracking_DP` • Pattern #18

## Intent
Generate all solutions by choosing, exploring, and unchoosing — the exhaustive enumeration pattern for permutations, combinations, subsets, N-Queens, and constraint satisfaction.

## Why it Matters
- **Choose → Explore → Unchoose** is the invariant. The unchoose line restores state so the next branch starts clean.
- **Pruning:** check validity *before* recursing deeper — reject early, don't build invalid paths.
- **Subsets with duplicates:** sort first, skip `i > start && nums[i] == nums[i-1]` when previous duplicate not used.
- **N-Queens:** place queen, validate row/col/diag, recurse. Bitmask optimization for O(1) validation.
- Senior signal: the copy-on-success pattern (`res.add(new ArrayList<>(path))`) — without it, all results reference the same mutating list.

## Diagram
```mermaid
flowchart LR
  Ch["choose nums[i]"] --> Rec["recurse deeper"]
  Rec --> B{"base case?<br/>path complete"}
  B -->|yes| Out["copy path to result"]
  B -->|no| Ch
  Rec --> Un["unchoose:<br/>remove last, used[i]=false"]
  Un --> N{"next option?"}
  N -->|yes| Ch
  N -->|no| Ret["return to caller"]
```


## Problems

### 46. Permutations (Medium)
> [LeetCode 46](https://leetcode.com/problems/permutations/) • Tags: Array, Backtracking

**Problem Statement:**

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order. Example 1: Input: nums = [1,2,3] Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] Example 2: Input: nums = [0,1] Output: [[0,1],[1,0]] Example 3: Input: nums = [1] Output: [[1]] Constraints: 1 -10 All the integers of nums are unique.

**Examples:**

Example 1:
```
[1,2,3]
```

Example 2:
```
[0,1]
```

Example 3:
```
[1]
```
---

### 77. Combinations (Medium)
> [LeetCode 77](https://leetcode.com/problems/combinations/) • Tags: Backtracking

**Problem Statement:**

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n]. You may return the answer in any order. Example 1: Input: n = 4, k = 2 Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]] Explanation: There are 4 choose 2 = 6 total combinations. Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination. Example 2: Input: n = 1, k = 1 Output: [[1]] Explanation: There is 1 choose 1 = 1 total combination. Constraints: 1 1

**Examples:**

Example 1:
```
4
```

Example 2:
```
2
```

Example 3:
```
1
```

Example 4:
```
1
```
---

### 78. Subsets (Medium)
> [LeetCode 78](https://leetcode.com/problems/subsets/) • Tags: Array, Backtracking, Bit Manipulation

**Problem Statement:**

Given an integer array nums of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order. Example 1: Input: nums = [1,2,3] Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]] Example 2: Input: nums = [0] Output: [[],[0]] Constraints: 1 -10 All the numbers of nums are unique.

**Examples:**

Example 1:
```
[1,2,3]
```

Example 2:
```
[0]
```
---

### 39. Combination Sum (Medium)
> [LeetCode 39](https://leetcode.com/problems/combination-sum/) • Tags: Array, Backtracking

**Problem Statement:**

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different. The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input. Example 1: Input: candidates = [2,3,6,7], target = 7 Output: [[2,2,3],[7]] Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times. 7 is a candidate, and 7 = 7. These are the only two combinations. Example 2: Input: candidates = [2,3,5], target = 8 Output: [[2,2,2,2],[2,3,3],[3,5]] Example 3: Input: candidates = [2], target = 1 Output: [] Constraints: 1 2 All elements of candidates are distinct. 1

**Examples:**

Example 1:
```
[2,3,6,7]
```

Example 2:
```
7
```

Example 3:
```
[2,3,5]
```

Example 4:
```
8
```

Example 5:
```
[2]
```

Example 6:
```
1
```
---


## Code / Example
```java
// Permutations — LC 46
java.util.List<java.util.List<Integer>> permute(int[] nums) {
    var res = new java.util.ArrayList<java.util.List<Integer>>();
    backtrack(nums, new java.util.ArrayList<>(), new boolean[nums.length], res);
    return res;
}

void backtrack(int[] nums, java.util.List<Integer> path, boolean[] used,
               java.util.List<java.util.List<Integer>> res) {
    if (path.size() == nums.length) {
        res.add(new java.util.ArrayList<>(path)); // COPY on success
        return;
    }
    for (int i = 0; i < nums.length; i++) if (!used[i]) {
        used[i] = true; path.add(nums[i]);
        backtrack(nums, path, used, res);
        path.remove(path.size() - 1); used[i] = false; // UNCHOOSE
    }
}

// Subsets — LC 78
java.util.List<java.util.List<Integer>> subsets(int[] nums) {
    var res = new java.util.ArrayList<java.util.List<Integer>>();
    backtrackSubsets(nums, 0, new java.util.ArrayList<>(), res);
    return res;
}
void backtrackSubsets(int[] nums, int start, java.util.List<Integer> path,
                      java.util.List<java.util.List<Integer>> res) {
    res.add(new java.util.ArrayList<>(path)); // add current subset
    for (int i = start; i < nums.length; i++) {
        if (i > start && nums[i] == nums[i-1]) continue; // skip dups
        path.add(nums[i]);
        backtrackSubsets(nums, i + 1, path, res);
        path.remove(path.size() - 1);
    }
}

// N-Queens — LC 51 (bitmask validation)
java.util.List<java.util.List<String>> solveNQueens(int n) {
    var res = new java.util.ArrayList<java.util.List<String>>();
    char[][] board = new char[n][n];
    for (var row : board) java.util.Arrays.fill(row, '.');
    solve(board, 0, res, 0, 0, 0, n);
    return res;
}
void solve(char[][] board, int row, java.util.List<java.util.List<String>> res,
           int cols, int diag1, int diag2, int n) {
    if (row == n) {
        res.add(java.util.Arrays.stream(board).map(String::new).toList());
        return;
    }
    for (int col = 0; col < n; col++) {
        int bit = 1 << col;
        int d1 = 1 << (row + col);
        int d2 = 1 << (row - col + n - 1);
        if ((cols & bit) != 0 || (diag1 & d1) != 0 || (diag2 & d2) != 0) continue;
        board[row][col] = 'Q';
        solve(board, row + 1, res, cols | bit, diag1 | d1, diag2 | d2, n);
        board[row][col] = '.';
    }
}
```

## When to Use / When NOT
- **Use:** generate all solutions — permutations, combinations, subsets, N-Queens, Sudoku, word search, brute force with pruning.
- **NOT:** "how many ways" / "minimum cost" (use DP — memoization deduplicates); single solution (use greedy / constructive).

## Trade-offs
| Problem | Time | Space |
|---------|------|-------|
| Permutations | O(n!) | O(n) recursion + output |
| Subsets | O(2^n) | O(n) recursion + output |
| N-Queens | O(n!) worst, much less with pruning | O(n) |

## Vs Table
| Aspect | Backtracking | DP | Greedy | Bitmask Enumeration |
|--------|--------------|----|--------|---------------------|
| Returns | all solutions | count or optimum | one committed answer | all subsets of small set |
| Overlapping subproblems | irrelevant (each path distinct) | required (memoize) | irrelevant | no |
| Time | O(n!) / O(2^n) | O(n · choices) | O(n log n) | O(2^n) |
| Pick when | "generate all", "list all combinations" | "how many ways", "minimum cost" | provable local-optimal | n ≤ ~20 |

## Pitfalls
- **Copy `path` when adding to result** or you store a reference that keeps mutating.
- **Prune early:** check validity before recursing deeper.
- **Subsets with duplicates:** sort first, skip `i > start && nums[i]==nums[i-1]` when not using previous.
- **Permutations with duplicates:** sort, skip `used[i-1] == false` for duplicate.

## Interview Q&A (Senior Depth)

**Q: Subsets vs Permutations — why does subsets use `start` index but permutations use `used[]` array?**
**A:** Subsets: order doesn't matter, `{1,2}` = `{2,1}`. `start` ensures we only pick elements at or after current position, avoiding permutations of the same subset. Permutations: order matters, `[1,2]` ≠ `[2,1]`. `used[]` tracks which elements are in the current permutation, allowing any unused element at each position.

**Q: N-Queens bitmask validation — explain the three bitmasks.**
**A:** `cols`: bit i = column i occupied. `diag1` (row+col constant): bit (row+col) = \ diagonal occupied. `diag2` (row-col+n-1 constant): bit (row-col+n-1) = / diagonal occupied. All O(1) checks via bitwise AND. No arrays needed.

**Q: Word Search (LC 79) — why mark board cell as '#' instead of visited array?**
**A:** O(1) space vs O(mn) visited array. The board is modified in-place and restored on backtrack (`board[r][c] = ch`). This is the same pattern as Number of Islands sinking land. For production where board must be preserved, use visited array.

**Q: Backtracking vs DP — how do you decide which applies?**
**A:** Backtracking: "return all solutions" — each path is distinct, nothing deduplicates. DP: "how many ways" or "minimum cost" — subproblems overlap, memoization deduplicates. If you can phrase it as `f(i) = g(f(i-1), f(i-2)...)` with overlapping calls, DP. If you need the actual solutions, backtracking.

**Q: How do you handle large output sizes in backtracking (e.g., permutations of n=10 = 3.6M)?**
**A:** Interview constraints typically n ≤ 8 for permutations (40K outputs). For larger n, the problem usually asks for count (DP) or k-th permutation (mathematical). If actual generation is required, streaming/yield (Java: Iterator) avoids holding all in memory.


## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the trigger keyword for Backtracking? :: **A:** permutations, combinations, subsets, N-Queens, Sudoku, word search, all valid configurations #flashcard

#flashcard
**Q:** Time/space complexity of Backtracking? :: **A:** Time: O(branching^depth) exponential, Space: O(depth) recursion stack #flashcard

#flashcard
**Q:** When do you NOT use Backtracking? :: **A:** only need count (use DP/math), optimal value only (use greedy/DP), large N #flashcard

#flashcard
**Q:** Core Java 25 snippet for Backtracking? :: **A:** `void backtrack(int idx){ if(idx==n){ addToAns(); return; } for(cand: candidates){ if(valid(cand)){ choose(cand); backtrack(idx+1); unchoose(cand); } } }` #flashcard


## Practice Tasks (Tasks Plugin)
- [ ] Restate the intent from memory 📅 {date:YYYY-MM-DD, +1}
- [ ] Code the snippet without looking 📅 {date:YYYY-MM-DD, +3}
- [ ] Answer all Interview Q&A aloud 📅 {date:YYYY-MM-DD, +7}
- [ ] Review flashcards (Spaced Repetition) 📅 {date:YYYY-MM-DD, +1}

```tasks
not done
path includes {file.folder}
sort by due
limit 10
```

## Related
- [[07_Backtracking_DP/02 - Dynamic Programming|Dynamic Programming]] (backtracking + memo = DP)
- [[07_Backtracking_DP/03 - Greedy|Greedy]] (local choice vs exhaustive)
- [[05_Trees_Graphs/02 - DFS|DFS]] (backtracking is DFS with state restoration)
- [[Java/07_DSA/Array]]
---
*Category: Coding Patterns/07_Backtracking_DP*
- [[Architect/10_System-Design-Interviews/OOD-01-Design-Parking-Lot.md|OOD-01-Design-Parking-Lot]] — State space search in OOD
