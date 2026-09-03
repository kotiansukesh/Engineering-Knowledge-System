---
title: "Sliding Window"
pattern: 3
category: Array
tags: [pattern/array, sliding-window]
leetcode: [643, 3, 76]
created: 2026-09-02
source: "https://blog.algomaster.io/p/20-dsa-patterns"
---

# Sliding window

> Part of [[README|20 DSA Patterns]], Pattern #3

## Definition

A window `[l, r]` slides across the array. Expand `r` one step, then shrink `l` until the window satisfies the condition again. Each element enters and leaves once, so O(n).

Two flavors: fixed size `k` (max sum of k elements) and variable size (longest substring without repeating chars, minimum window substring).

Example fixed-k: `nums=[2,1,5,1,3,2]`, `k=3` → first window sum `8` (2+1+5), slide to `7` (1+5+1), then `9` (5+1+3), best is `9`.

## When to use

- Need a contiguous subarray or substring with a max, min, longest, or shortest condition
- Keywords: "contiguous", "subarray", "substring", "maximum window", "longest without repeating"

## Complexity

| type | time | space |
|---|---|---|
| fixed k | O(n) | O(1) |
| variable + map | O(n) | O(k) for frequency map |

## Java example

```java
// Fixed k, max sum of k consecutive
int maxSumK(int[] nums, int k) {
    int sum = 0;
    for (var i = 0; i < k; i++) sum += nums[i];
    int best = sum;
    for (var i = k; i < nums.length; i++) {
        sum += nums[i] - nums[i - k];
        best = Math.max(best, sum);
    }
    return best;
}

// Variable, longest substring without repeating chars, LC 3
int lengthOfLongestSubstring(String s) {
    var cnt = new java.util.HashMap<Character,Integer>();
    int l = 0, ans = 0;
    for (var r = 0; r < s.length(); r++) {
        cnt.put(s.charAt(r), cnt.getOrDefault(s.charAt(r), 0) + 1);
        while (cnt.get(s.charAt(r)) > 1) {
            cnt.put(s.charAt(l), cnt.get(s.charAt(l)) - 1);
            l++;
        }
        ans = Math.max(ans, r - l + 1);
    }
    return ans;
}
```

For fixed-k, do not recompute the sum from scratch each time. For variable windows, use `while` to shrink, not `if`, and update the answer after the window is valid again.

## Pitfalls

- Fixed-k: initialize with first k before sliding.
- Variable: update answer after shrinking, not before.
- Use `HashSet` when you only care about existence, `HashMap` when you count.

## Practice

- [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)
- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

## Related DSA notes

- [[Java/07_DSA/Array]]
