---
title: "Two Pointers"
type: pattern
pattern: 2
domain: "Array / String"
category: "Coding Patterns/01_Array"
advanced: false
mastery: learn
recognition_score: 0
difficulty: "Easy"
leetcode: [167, 11, 42, 75]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - pattern/array-string
---

# Two Pointers

> Pattern #2 · Array / String

## Recognition

- Sorted data with pair/triplet reasoning
- Two ends of a range constrain the answer
- In-place partitioning, deduplication, or palindrome checks

### Strong signals
- Sorted data with pair/triplet reasoning
- Two ends of a range constrain the answer

### Do not infer it from
- A keyword alone
- A familiar LeetCode example without checking the constraints

## Invariant

> Every pointer move permanently discards candidates that cannot produce a better or valid answer under the ordering property.

## Mental model

Maintain two indices whose movement is justified by ordering or a structural invariant. The pattern is valuable because one pointer movement eliminates an entire set of candidates.

## Core implementation

```java
// Sorted Two Sum — LC 167
int[] twoSumSorted(int[] nums, int target) {
    int l = 0, r = nums.length - 1;
    while (l < r) {
        int sum = nums[l] + nums[r];
        if (sum == target) return new int[]{l + 1, r + 1}; // 1-indexed
        if (sum < target) l++;
        else r--;
    }
    return new int[]{-1, -1};
}

// Container With Most Water — LC 11
int maxArea(int[] h) {
    int l = 0, r = h.length - 1, best = 0;
    while (l < r) {
        int area = Math.min(h[l], h[r]) * (r - l);
        best = Math.max(best, area);
        if (h[l] < h[r]) l++; else r--;
    }
    return best;
}

// 3Sum — LC 15 (sort + two pointers per fixed element)
java.util.List<java.util.List<Integer>> threeSum(int[] nums) {
    java.util.Arrays.sort(nums);
    var res = new java.util.ArrayList<java.util.List<Integer>>();
    for (int i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue; // skip dup fixed
        int l = i + 1, r = nums.length - 1;
        while (l < r) {
            int sum = nums[i] + nums[l] + nums[r];
            if (sum == 0) {
                res.add(java.util.List.of(nums[i], nums[l], nums[r]));
                while (l < r && nums[l] == nums[l + 1]) l++;
                while (l < r && nums[r] == nums[r - 1]) r--;
                l++; r--;
            } else if (sum < 0) l++;
            else r--;
        }
    }
    return res;
}
```

## Variants

Use the implementation above as the base case. Extend it only after the invariant remains explicit.

## When to use
- sorted array + pair/triple target; palindrome check; remove duplicates in-place; merge two sorted arrays; partition (Dutch national flag).

## When NOT to use
- unsorted array without sorting (use HashMap for two sum); need original indices after sort (must pair value with index before sorting); non-contiguous subsequence (not a two-pointer problem).

## Complexity & trade-offs

| Case | Time | Space |
|------|------|-------|
| Sorted pair search | O(n) | O(1) |
| 3Sum (sort + 2ptr) | O(n²) | O(1) extra |
| Container with most water | O(n) | O(1) |

| Aspect | Two Pointers | HashMap (Two Sum) | Sliding Window |
|--------|--------------|-------------------|----------------|
| Input requirement | sorted | unsorted OK | any sequence |
| Solves | pair, palindrome, sorted search | unsorted two sum (original indices) | contiguous subarray with condition |
| Space | O(1) | O(n) | O(1) fixed-k, O(k) variable |
| Pick when | sorted, pair or palindrome | unsorted two sum, need indices | contiguous subarray, max/min window |

## Pitfalls

- Input must be sorted for two-sum. If not, sort first and track original indices separately (pair value with index).
- For 3Sum, skip duplicates *after sorting* or you return the same triple many times.
- Move only **one** pointer per iteration — moving both can skip the answer.
- For palindrome, `l < r` not `l <= r` (middle char doesn't need comparison).

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 167 | Two Sum II - Input Array Is Sorted | Medium |
| 11 | Container With Most Water | Medium |
| 42 | Trapping Rain Water | Hard |
| 75 | Sort Colors | Medium |

## Interview Q&A

(Senior Depth)

**Q: Why does moving the shorter wall in Container With Most Water never miss the optimal answer?**
**A:** Area = `min(h[l], h[r]) * (r - l)`. The shorter wall caps the height. Moving the *taller* wall keeps the same cap but reduces width → area strictly decreases or stays same. Moving the *shorter* wall might find a taller wall that raises the cap. The invariant: at each step, all pairs involving the discarded shorter wall and any wall between `l` and `r` are provably suboptimal. Rejected alternative: check all pairs O(n²) — correct but fails time constraint.

**Q: Two Sum II (sorted) vs Two Sum I (unsorted). Why different approaches?**
**A:** Sorted → two pointers O(n) time, O(1) space. Unsorted → HashMap O(n) time, O(n) space. If you sort unsorted, you lose original indices (requirement in LC 1). Trade-off: HashMap uses extra space but preserves indices; two pointers uses O(1) space but needs sorted input.

**Q: 3Sum with duplicates — walk me through the skip logic.**
**A:** Three levels: (1) skip duplicate fixed element `i` with `i > 0 && nums[i] == nums[i-1]`. (2) After finding a valid triplet, skip duplicate `l` with `while(l<r && nums[l]==nums[l+1]) l++`. (3) Skip duplicate `r` similarly. Without all three, you emit duplicate triplets. The sort brings duplicates adjacent, making skip O(1) per duplicate.

**Q: Can two pointers work on a rotated sorted array for pair sum?**
**A:** No — rotated array isn't globally sorted. You'd need to find the pivot (min element) first, then treat as two sorted subarrays, or just use HashMap O(n). Two pointers requires monotonic ordering to know which direction to move.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Two Pointers? :: **A:** sorted array, pair/triplet sum, remove duplicates, palindrome check, container with most water #flashcard

#flashcard
**Q:** Time/space complexity of Two Pointers? :: **A:** Time: O(n) after sort O(n log n), Space: O(1) #flashcard

#flashcard
**Q:** When do you NOT use Two Pointers? :: **A:** unsorted array (sort first or use hashmap), need all pairs (O(n²) output) #flashcard

#flashcard
**Q:** Core Java 25 snippet for Two Pointers? :: **A:** `int l=0,r=n-1; while(l<r){ int s=a[l]+a[r]; if(s==t) return new int[]{l,r}; else if(s<t) l++; else r--; }` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- [[01_Array/03 - Sliding Window|Sliding Window]] (variable window also uses two pointers but both advance forward)
- [[02_LinkedList/01 - Fast and Slow Pointers|Fast & Slow Pointers]] (same direction, different speeds)
- [[Java/07_DSA/Array]]
