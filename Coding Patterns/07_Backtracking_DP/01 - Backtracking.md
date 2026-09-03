---
title: "Backtracking"
pattern: 17
category: Backtracking
tags: [pattern/backtracking]
leetcode: [46, 78, 51]
created: 2026-09-02
source: "https://blog.algomaster.io/p/20-dsa-patterns"
---

# Backtracking

> Part of [[README|20 DSA Patterns]] - Pattern #17

## Definition

Choose, explore, unchoose. Build a path step by step; if it violates constraints, revert and try the next option. Recursion holds the path, backtracking restores state. Example: permutations of `[1,2,3]` → pick `1`, then `2`, then `3` gives `[1,2,3]`, backtrack to try `3` at second position gives `[1,3,2]`, and so on to six results.

## When to use

- Generate all solutions: permutations, combinations, subsets, N-Queens, Sudoku, word search, brute force with pruning

## Complexity

| time | space |
|---|---|
| O(n!) for permutations, O(2^n) for subsets | O(n) recursion depth plus output |

## Java example

```java
// Permutations - LC 46
java.util.List<java.util.List<Integer>> permute(int[] nums) {
    var res = new java.util.ArrayList<java.util.List<Integer>>();
    backtrack(nums, new java.util.ArrayList<>(), new boolean[nums.length], res);
    return res;
}

void backtrack(int[] nums, java.util.List<Integer> path, boolean[] used,
               java.util.List<java.util.List<Integer>> res) {
    if (path.size() == nums.length) { res.add(new java.util.ArrayList<>(path)); return; }
    for (var i = 0; i < nums.length; i++) if (!used[i]) {
        used[i] = true; path.add(nums[i]);
        backtrack(nums, path, used, res);
        path.remove(path.size() - 1); used[i] = false; // unchoose
    }
}
```

The last two lines are the backtrack. Leave them out and the path keeps growing wrong.

## Pitfalls

- Copy `path` when adding to result or you store a reference that keeps mutating.
- Prune early: check validity before recursing deeper.
- For subsets with duplicates, sort first and skip `i > start && nums[i]==nums[i-1]` when not using previous.

## Practice

- [46. Permutations](https://leetcode.com/problems/permutations/)
- [78. Subsets](https://leetcode.com/problems/subsets/)
- [51. N-Queens](https://leetcode.com/problems/n-queens/)

## Related DSA notes

- [[Java/07_DSA/Trees]]
