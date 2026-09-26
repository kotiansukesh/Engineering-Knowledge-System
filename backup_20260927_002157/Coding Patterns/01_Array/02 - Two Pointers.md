---
title: Two Pointers
pattern: 2
category: Coding Patterns/01_Array
tags:
  - pattern/array
  - pattern/array/two-pointers
leetcode:
  - 167
  - 15
  - 11
created: '2026-09-02'
completed: false
reviewed: ''
sr-due: ''
difficulty: Easy
source: 'https://blog.algomaster.io/p/20-dsa-patterns'
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---

# Two Pointers

> Part of [[README|20 DSA Patterns]] • `Coding Patterns/01_Array` • Pattern #2

## Intent
Replace nested O(n²) scans on sorted arrays with a single O(n) pass using two indices moving toward each other or in lockstep — the pattern for pair search, partitioning, and palindrome checks.

## Why it Matters
- The "sorted" keyword is the primary trigger: sorted + pair/target → two pointers. Unsorted? Sort first (O(n log n)) and track original indices if needed.
- Two variants: opposite ends (`l=0, r=n-1`) for pair sum / container / palindrome; same direction (slow/fast) for cycle / middle / dedup.
- Senior signal: knowing when the pointer movement logic is *correct by invariant* — each step permanently discards elements that cannot participate in any valid solution.

## Diagram
```mermaid
flowchart LR
  subgraph Sorted["sorted [1,2,3,4,6], target 6"]
    L["l -> 1"] --- R["r -> 6"]
  end
  L --> Ch{"sum vs target"}
  Ch -->|"< target"| Lm["l++"]
  Ch -->|"> target"| Rm["r--"]
  Ch -->|"="| Done["return (l,r)"]
  Lm --> Ch
  Rm --> Ch
```


## Problems

### 167. Two Sum II - Input Array Is Sorted (Medium)
> [LeetCode 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) • Tags: Array, Two Pointers, Binary Search

**Problem Statement:**

You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order.

Find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index_1_] and numbers[index_2_] where 1 <= index_1_ < index_2_ <= numbers.length.

Return the indices of the two numbers index_1_ and index_2_ as an integer array [index_1_, index_2_] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

**Examples:**

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index_1_ = 1, index_2_ = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index_1_ = 1, index_2_ = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index_1_ = 1, index_2_ = 2. We return [1, 2].

---

### 15. 3Sum (Medium)
> [LeetCode 15](https://leetcode.com/problems/3sum/) • Tags: Array, Two Pointers, Sorting

**Problem Statement:**

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

**Examples:**

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

---

### 11. Container With Most Water (Medium)
> [LeetCode 11](https://leetcode.com/problems/container-with-most-water/) • Tags: Array, Two Pointers, Greedy

**Problem Statement:**

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the i^th^ line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

**Examples:**

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

---


## Code / Example
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

## When to Use / When NOT
- **Use:** sorted array + pair/triple target; palindrome check; remove duplicates in-place; merge two sorted arrays; partition (Dutch national flag).
- **NOT:** unsorted array without sorting (use HashMap for two sum); need original indices after sort (must pair value with index before sorting); non-contiguous subsequence (not a two-pointer problem).

## Trade-offs
| Case | Time | Space |
|------|------|-------|
| Sorted pair search | O(n) | O(1) |
| 3Sum (sort + 2ptr) | O(n²) | O(1) extra |
| Container with most water | O(n) | O(1) |

## Vs Table
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

## Interview Q&A (Senior Depth)

**Q: Why does moving the shorter wall in Container With Most Water never miss the optimal answer?**
**A:** Area = `min(h[l], h[r]) * (r - l)`. The shorter wall caps the height. Moving the *taller* wall keeps the same cap but reduces width → area strictly decreases or stays same. Moving the *shorter* wall might find a taller wall that raises the cap. The invariant: at each step, all pairs involving the discarded shorter wall and any wall between `l` and `r` are provably suboptimal. Rejected alternative: check all pairs O(n²) — correct but fails time constraint.

**Q: Two Sum II (sorted) vs Two Sum I (unsorted). Why different approaches?**
**A:** Sorted → two pointers O(n) time, O(1) space. Unsorted → HashMap O(n) time, O(n) space. If you sort unsorted, you lose original indices (requirement in LC 1). Trade-off: HashMap uses extra space but preserves indices; two pointers uses O(1) space but needs sorted input.

**Q: 3Sum with duplicates — walk me through the skip logic.**
**A:** Three levels: (1) skip duplicate fixed element `i` with `i > 0 && nums[i] == nums[i-1]`. (2) After finding a valid triplet, skip duplicate `l` with `while(l<r && nums[l]==nums[l+1]) l++`. (3) Skip duplicate `r` similarly. Without all three, you emit duplicate triplets. The sort brings duplicates adjacent, making skip O(1) per duplicate.

**Q: Can two pointers work on a rotated sorted array for pair sum?**
**A:** No — rotated array isn't globally sorted. You'd need to find the pivot (min element) first, then treat as two sorted subarrays, or just use HashMap O(n). Two pointers requires monotonic ordering to know which direction to move.

## Related
- [[01_Array/03 - Sliding Window|Sliding Window]] (variable window also uses two pointers but both advance forward)
- [[02_LinkedList/01 - Fast and Slow Pointers|Fast & Slow Pointers]] (same direction, different speeds)
- [[Java/07_DSA/Array]]

---
*Category: Coding Patterns/01_Array*
