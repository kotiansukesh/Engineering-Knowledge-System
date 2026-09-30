---
title: "Modified Binary Search"
type: pattern
pattern: 10
domain: "Search"
category: "Coding Patterns/04_Intervals_Search"
advanced: false
mastery: learn
recognition_score: 0
difficulty: "Medium"
leetcode: [33, 34, 35, 153]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - search
---

# Modified Binary Search

> Pattern #10 · Search

## Recognition

- Sorted or rotated input
- Monotonic feasibility predicate
- Need logarithmic search over an ordered space

### Strong signals
- Sorted or rotated input
- Monotonic feasibility predicate

### Do not infer it from
- A keyword alone
- A familiar example without checking constraints

## Invariant

> The answer remains inside the retained search interval; each comparison safely eliminates a region.

## Mental model

This pattern reduces the search space by maintaining a compact state that represents all information needed for the next decision.

## Core implementation

```java
// Search in Rotated Sorted Array — LC 33
int search(int[] nums, int target) {
    int lo = 0, hi = nums.length - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2; // no overflow
        if (nums[mid] == target) return mid;
        if (nums[lo] <= nums[mid]) { // left half sorted
            if (nums[lo] <= target && target < nums[mid]) hi = mid - 1;
            else lo = mid + 1;
        } else { // right half sorted
            if (nums[mid] < target && target <= nums[hi]) lo = mid + 1;
            else hi = mid - 1;
        }
    }
    return -1;
}

// Find Minimum in Rotated Sorted Array — LC 153
int findMin(int[] nums) {
    int lo = 0, hi = nums.length - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] > nums[hi]) lo = mid + 1; // min in right
        else hi = mid; // min in left (including mid)
    }
    return nums[lo];
}

// Search a 2D Matrix — LC 74 (flattened 1D)
boolean searchMatrix(int[][] matrix, int target) {
    int m = matrix.length, n = matrix[0].length;
    int lo = 0, hi = m * n - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        int val = matrix[mid / n][mid % n];
        if (val == target) return true;
        if (val < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return false;
}

// Binary Search on Answer — Split Array Largest Sum (LC 410)
int splitArray(int[] nums, int k) {
    int lo = 0, hi = 0;
    for (int x : nums) { lo = Math.max(lo, x); hi += x; }
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (canSplit(nums, k, mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
boolean canSplit(int[] nums, int k, int maxSum) {
    int sum = 0, parts = 1;
    for (int x : nums) {
        if (sum + x > maxSum) { parts++; sum = x; }
        else sum += x;
    }
    return parts <= k;
}
```

## Variants

Start with the core implementation. Introduce a variant only when the problem changes the invariant or required state.

## When to use

- rotated sorted array search; find min in rotated; search 2D matrix; find peak; first/last position; "minimum capacity", "split largest sum", "koko eating bananas" (binary search on answer).
- **NOT:** unsorted array (sort first or use hashmap); need all occurrences (linear scan).

## When NOT to use

unsorted array (sort first or use hashmap); need all occurrences (linear scan).

## Complexity & trade-offs

| Variant | Time | Space |
|---------|------|-------|
| Classic / Rotated / 2D matrix | O(log n) | O(1) |
| Binary search on answer | O(log(range) * n) | O(1) |

| Aspect | Plain Binary Search | Modified (Rotated) | Binary Search on Answer |
|--------|---------------------|--------------------|-------------------------|
| Input | fully sorted | rotated or bitonic | monotonic predicate over range |
| Invariant | target range halves | one sorted half identified first | feasible(v) monotonically flips |
| Time | O(log n) | O(log n) | O(log range * check) |
| Pick when | plain sorted array | rotated, peak, 2D matrix | "minimum capacity", "split largest sum" |

## Pitfalls

- Use `<=` correctly when checking which half is sorted (`nums[lo] <= nums[mid]`). Off-by-one on boundaries is the #1 bug.
- Duplicates (LC 81) break "one half sorted" guarantee — need extra handling (`nums[lo] == nums[mid] == nums[hi]` → shrink both ends).
- For 2D matrix, `mid/n` and `mid%n` mapping assumes row-major order with sorted rows and first element of each row > last of previous.
- Binary search on answer: `lo < hi` vs `lo <= hi` depends on whether you want lower bound (first true) or upper bound (last true). `lo < hi` with `hi = mid` / `lo = mid + 1` finds first true.

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 33 | Medium |
| 34 | Medium |
| 35 | Easy |
| 153 | Medium |

## Interview Q&A

(Senior Depth)

**Q: Search in Rotated Sorted Array — why `nums[lo] <= nums[mid]` and not `<`?**
**A:** When `lo == mid` (two elements), `nums[lo] <= nums[mid]` is true, correctly identifying left half (single element) as sorted. With `<`, it would be false and you'd check the right half incorrectly. The `<=` handles the base case where the sorted half has length 1.

**Q: Find Min in Rotated (LC 153) — why `lo < hi` not `lo <= hi`?**
**A:** We're finding the minimum *value*, not an index match. The loop invariant: min is in `[lo, hi]`. When `lo == hi`, the range has size 1 → that element is the min. `lo < hi` terminates when range size = 1. Using `lo <= hi` would require an extra iteration and careful mid handling.

**Q: Binary Search on Answer — how do you know the predicate is monotonic?**
**A:** For "split array largest sum": if you can split with max sum = X, you can definitely split with max sum = X+1 (just use the same splits). The predicate `feasible(maxSum)` is monotonic: false...false, true...true. This is the *exchange argument* for monotonicity — prove that increasing the capacity never makes a feasible split infeasible.

**Q: Search in Rotated with Duplicates (LC 81) — what breaks?**
**A:** When `nums[lo] == nums[mid] == nums[hi]`, you can't tell which half is sorted. Example: `[2,2,2,0,2]` — `lo=0, mid=2, hi=4` all 2. The fix: `lo++` and `hi--` to shrink the ambiguous region. Worst case degrades to O(n) (all elements equal), which is unavoidable.

**Q: 2D Matrix Search — why does treating as 1D work?**
**A:** The matrix is sorted such that `matrix[i][j] < matrix[i][j+1]` and `matrix[i][n-1] < matrix[i+1][0]`. This is exactly row-major order of a sorted 1D array. The mapping `row = mid / n, col = mid % n` is the inverse of `index = row * n + col`. Binary search on the virtual 1D array is isomorphic.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Modified Binary Search? :: **A:** search in rotated array, find min in rotated, search 2D matrix, Koko eating bananas, capacity to ship #flashcard

#flashcard
**Q:** Time/space complexity of Modified Binary Search? :: **A:** Time: O(log n) or O(log n × f(mid)), Space: O(1) #flashcard

#flashcard
**Q:** When do you NOT use Modified Binary Search? :: **A:** unsorted (sort first O(n log n)), need all occurrences (O(n)) #flashcard

#flashcard
**Q:** Core Java 25 snippet for Modified Binary Search? :: **A:** `int l=0,r=n-1; while(l<=r){ int m=l+(r-l)/2; if(check(m)) r=m-1; else l=m+1; } return l; // lower bound pattern` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory 📅 2026-10-01
- [ ] Write the template from memory 📅 2026-10-03
- [ ] Solve one unseen problem without hints 📅 2026-10-07
- [ ] Explain the invariant aloud 📅 2026-10-14

## Related

- [[04_Intervals_Search/01 - Overlapping Intervals|Overlapping Intervals]]
- [[07_Backtracking_DP/02 - Dynamic Programming|Dynamic Programming]] (binary search on answer often pairs with DP feasibility check)
- [[Java/07_DSA/Array]]
