---
title: "Sliding Window"
type: pattern
pattern: 3
domain: "Array / String"
category: "Coding Patterns/01_Array"
advanced: false
mastery: learn
recognition_score: 0
difficulty: "Medium"
leetcode: [- 3]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - pattern/array-string
---

# Sliding Window

> Pattern #3 · Array / String

## Recognition

- Contiguous substring or subarray
- Longest, shortest, or fixed-size window
- Window validity can be updated incrementally

### Strong signals
- Contiguous substring or subarray
- Longest, shortest, or fixed-size window

### Do not infer it from
- A keyword alone
- A familiar LeetCode example without checking the constraints

## Invariant

> The active window always represents exactly the range currently being evaluated, and its tracked state is consistent with the elements inside it.

## Mental model

Maintain a contiguous range and update its state as the right edge advances. Move the left edge only when the window violates the required condition or when a fixed size must be maintained.

## Core implementation

```java
// Fixed-k: max sum of k consecutive — LC 643
int maxSumK(int[] nums, int k) {
    int sum = 0;
    for (int i = 0; i < k; i++) sum += nums[i];
    int best = sum;
    for (int i = k; i < nums.length; i++) {
        sum += nums[i] - nums[i - k];
        best = Math.max(best, sum);
    }
    return best;
}

// Variable: longest substring without repeating chars — LC 3
int lengthOfLongestSubstring(String s) {
    var cnt = new java.util.HashMap<Character, Integer>();
    int l = 0, ans = 0;
    for (int r = 0; r < s.length(); r++) {
        char c = s.charAt(r);
        cnt.put(c, cnt.getOrDefault(c, 0) + 1);
        while (cnt.get(c) > 1) { // shrink until valid
            char cl = s.charAt(l);
            cnt.put(cl, cnt.get(cl) - 1);
            l++;
        }
        ans = Math.max(ans, r - l + 1); // update AFTER shrink
    }
    return ans;
}

// Variable: minimum window substring — LC 76
String minWindow(String s, String t) {
    var need = new java.util.HashMap<Character, Integer>();
    for (char c : t.toCharArray()) need.put(c, need.getOrDefault(c, 0) + 1);
    int required = need.size();
    var have = new java.util.HashMap<Character, Integer>();
    int l = 0, formed = 0, bestLen = Integer.MAX_VALUE, bestL = 0;
    for (int r = 0; r < s.length(); r++) {
        char c = s.charAt(r);
        have.put(c, have.getOrDefault(c, 0) + 1);
        if (need.containsKey(c) && have.get(c).equals(need.get(c))) formed++;
        while (formed == required) {
            if (r - l + 1 < bestLen) { bestLen = r - l + 1; bestL = l; }
            char cl = s.charAt(l);
            if (need.containsKey(cl) && have.get(cl).equals(need.get(cl))) formed--;
            have.put(cl, have.get(cl) - 1);
            l++;
        }
    }
    return bestLen == Integer.MAX_VALUE ? "" : s.substring(bestL, bestL + bestLen);
}
```

## Variants

Use the implementation above as the base case. Extend it only after the invariant remains explicit.

## When to use

- contiguous subarray/substring with max/min/longest/shortest condition; fixed-k sums/averages; "window" / "substring" / "subarray" keywords.
- **NOT:** non-contiguous subsequence (use DP/backtracking); need original order but not contiguous; sorted pair search (use two pointers).

## When NOT to use

non-contiguous subsequence (use DP/backtracking); need original order but not contiguous; sorted pair search (use two pointers).

## Complexity & trade-offs

| Type | Time | Space |
|------|------|-------|
| Fixed-k | O(n) | O(1) |
| Variable + HashMap | O(n) | O(k) for frequency map (k = distinct chars in window) |
| Variable + HashSet | O(n) | O(min(n, alphabet)) |

| Aspect      | Sliding Window                           | Two Pointers                    | Prefix Sum                    |
| ----------- | ---------------------------------------- | ------------------------------- | ----------------------------- |
| Window      | contiguous, both ends advance forward    | two ends walking inward         | no window, precomputed        |
| Solves      | longest/shortest substring, fixed-k sums | pair, palindrome, sorted search | static range sums             |
| Needs order | any sequence                             | sorted for two-sum              | immutable array               |
| Space       | O(1) fixed-k, O(k) variable              | O(1)                            | O(n)                          |
| Pick when   | contiguous + condition                   | sorted + pair                   | repeated static range queries |

## Pitfalls

- Fixed-k: initialize with first `k` elements *before* sliding loop.
- Variable: update answer **after** shrinking (`while`), not before — the window is only guaranteed valid after the shrink loop.
- Use `HashSet` when only existence matters; `HashMap` when counts matter (e.g., min window substring).
- For min window substring, track `formed` (distinct chars meeting required count) vs `required` — don't recompute.

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 3 | Longest Substring Without Repeating Characters | Medium |
| 438 | Find All Anagrams in a String | Medium |
| 76 | Minimum Window Substring | Hard |
| 209 | Minimum Size Subarray Sum | Medium |

## Interview Q&A

(Senior Depth)

**Q: Longest substring without repeating — why update answer *after* the `while` shrink loop?**
**A:** The `while` loop guarantees the window `[l, r]` has all unique characters. Before the `while`, the window is invalid (has a duplicate). Updating before shrink would record an invalid window. The invariant: at the top of the `for` loop, `[l, r-1]` is valid; we add `r`, possibly invalid; `while` restores validity; *then* `[l, r]` is the maximal valid window ending at `r`.

**Q: Minimum window substring (LC 76) — why `formed == required` and not just "all chars present"?**
**A:** `t` can have duplicates (e.g., `t="AAB"` needs 2 A's, 1 B). `required` = distinct chars in `t` (2). `formed` increments only when a char's count *exactly matches* its required count. This handles duplicates correctly — we don't overcount when we have 3 A's but only need 2.

**Q: When does fixed-k sliding window beat prefix sum for max sum of k?**
**A:** Both O(n). Sliding window O(1) space, prefix sum O(n) space. Sliding window is simpler for fixed-k — no extra array. Prefix sum wins when you have *many different k queries* on the same array (preprocess once, answer any k in O(1)). For single k, sliding window is preferred.

**Q: Can sliding window handle negative numbers for "longest subarray with sum <= k"?**
**A:** No — with negatives, shrinking `l` can *increase* the sum (removing a negative), breaking the monotonicity that makes the `while` shrink correct. For negatives + sum constraint, use prefix sum + ordered map (TreeMap) or monotonic deque (LC 862).

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Sliding Window? :: **A:** subarray/substring with condition, max/min length, fixed/variable window, at most K distinct #flashcard

#flashcard
**Q:** Time/space complexity of Sliding Window? :: **A:** Time: O(n) each element visited ≤2 times, Space: O(k) for hashmap/set #flashcard

#flashcard
**Q:** When do you NOT use Sliding Window? :: **A:** non-contiguous subsequence (use DP/backtrack), need all subarrays (O(n²) output) #flashcard

#flashcard
**Q:** Core Java 25 snippet for Sliding Window? :: **A:** `int l=0; for(int r=0;r<n;r++){ add(a[r]); while(invalid()) remove(a[l++]); updateAns(); }` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory 📅 2026-10-01
- [ ] Write the template from memory 📅 2026-10-03
- [ ] Solve one unseen problem without hints 📅 2026-10-07
- [ ] Explain the invariant aloud 📅 2026-10-14

## Related

- [[01_Array/01 - Prefix Sum|Prefix Sum]] (fixed-k sums, alternative for static arrays)
- [[01_Array/04 - Frequency Counting|Frequency Counting]] (hashmap on window for variable windows)
- [[01_Array/02 - Two Pointers|Two Pointers]] (two pointers move inward; window moves forward)
- [[Java/07_DSA/Array]] · [[Java/07_DSA/HashMap]]
