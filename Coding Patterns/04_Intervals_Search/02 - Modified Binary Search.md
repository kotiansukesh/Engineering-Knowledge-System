---
title: "Modified Binary Search"
pattern: 11
category: Search
tags: [pattern/binary-search]
leetcode: [33, 153, 74]
created: 2026-09-02
source: "https://blog.algomaster.io/p/20-dsa-patterns"
---

# Modified binary search

> Part of [[README|20 DSA Patterns]], Pattern #11

## Definition

Classic binary search plus extra logic. For rotated sorted arrays one half is always sorted, so check which half is sorted and decide where the target can live. Example: `[4,5,6,7,0,1,2]`, target `0` → mid is `7`, left half `[4..7]` sorted, target not in left, so search right → finds `0` at index 4.

Same idea applies to 2D matrix, peak finding, first and last position.

## When to use

- Sorted or rotated sorted array, search in 2D matrix, find peak, find first or last occurrence
- Keywords: "sorted", "rotated", "search", "peak", "matrix"

## Complexity

| time | space |
|---|---|
| O(log n) | O(1) |

## Java example

```java
// Search in rotated sorted array, LC 33
int search(int[] nums, int target) {
    int lo = 0, hi = nums.length - 1;
    while (lo <= hi) {
        var mid = lo + (hi - lo) / 2; // no overflow
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

// First and last position, run binary search twice, once for left bound, once for right
```

Mid formula `lo + (hi-lo)/2` avoids overflow. Java 25 `var` keeps it short.

## Pitfalls

- Use `<=` correctly when checking which half is sorted. Off-by-one on boundaries is common.
- Duplicates (LC 81) break the "one half sorted" guarantee, need extra handling.
- For 2D matrix, treat it as flattened 1D with `mid/n` and `mid%n`, or two-stage search.

## Practice

- [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

## Related DSA notes

- [[Java/07_DSA/Array]]
