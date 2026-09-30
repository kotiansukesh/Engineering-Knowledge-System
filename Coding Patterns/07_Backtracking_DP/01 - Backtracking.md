---
title: "Backtracking"
type: pattern
pattern: 18
domain: "Search"
category: "Coding Patterns/07_Backtracking_DP"
advanced: false
mastery: learn
recognition_score: 0
difficulty: "Medium"
leetcode: [46, 77, 78, 39]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - search
---

# Backtracking

> Pattern #18 · Search

## Recognition

- Generate all valid combinations or permutations
- Build a candidate incrementally
- Undo a choice and explore another branch

### Strong signals
- Generate all valid combinations or permutations
- Build a candidate incrementally

### Do not infer it from
- A keyword alone
- A familiar example without checking constraints

## Invariant

> The path represents exactly the choices made on the current branch; every recursive call restores the path before returning.

## Mental model

Maintain the smallest state that completely describes the part of the search space still relevant to the answer.

## Core implementation

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

## Variants

Start with the core implementation. Introduce a variant only when the required state or proof changes.

## When to use
- generate all solutions — permutations, combinations, subsets, N-Queens, Sudoku, word search, brute force with pruning.

## When NOT to use
- "how many ways" / "minimum cost" (use DP — memoization deduplicates); single solution (use greedy / constructive).

## Complexity & trade-offs

| Problem | Time | Space |
|---------|------|-------|
| Permutations | O(n!) | O(n) recursion + output |
| Subsets | O(2^n) | O(n) recursion + output |
| N-Queens | O(n!) worst, much less with pruning | O(n) |

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

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 46 | Medium |
| 77 | Medium |
| 78 | Medium |
| 39 | Medium |

## Interview Q&A

(Senior Depth)

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

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Backtracking? :: **A:** permutations, combinations, subsets, N-Queens, Sudoku, word search, all valid configurations #flashcard

#flashcard
**Q:** Time/space complexity of Backtracking? :: **A:** Time: O(branching^depth) exponential, Space: O(depth) recursion stack #flashcard

#flashcard
**Q:** When do you NOT use Backtracking? :: **A:** only need count (use DP/math), optimal value only (use greedy/DP), large N #flashcard

#flashcard
**Q:** Core Java 25 snippet for Backtracking? :: **A:** `void backtrack(int idx){ if(idx==n){ addToAns(); return; } for(cand: candidates){ if(valid(cand)){ choose(cand); backtrack(idx+1); unchoose(cand); } } }` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- [[07_Backtracking_DP/02 - Dynamic Programming|Dynamic Programming]] (backtracking + memo = DP)
- [[07_Backtracking_DP/03 - Greedy|Greedy]] (local choice vs exhaustive)
- [[05_Trees_Graphs/02 - DFS|DFS]] (backtracking is DFS with state restoration)
- [[Java/07_DSA/Array]]
