---
title: Sliding Window
pattern: 3
category: Coding Patterns/01_Array
tags:
- pattern/array
- pattern/array/sliding-window
leetcode:
- 3
- 438
- 76
- 209
created: '2026-09-02'
completed: false
reviewed: ''
sr-due: ''
difficulty: Medium
source: https://blog.algomaster.io/p/20-dsa-patterns
excalidraw: ''
---


# Sliding Window

> Part of [[README|20 DSA Patterns]] • `Coding Patterns/01_Array` • Pattern #3

## Intent
Maintain a mutable window `[l, r]` over a sequence where both ends advance forward — O(n) for contiguous subarray/substring problems with max/min/longest/shortest constraints by expanding `r` and shrinking `l` only when the window violates the condition.

## Why it Matters
- Two flavors: **fixed-k** (window size constant, e.g., max sum of k elements) and **variable** (window grows/shrinks based on condition, e.g., longest substring without repeats, minimum window substring).
- The "contiguous" + "subarray/substring" + "max/min/longest/shortest" keyword cluster is the trigger.
- Senior signal: knowing the invariant — after the inner `while` shrinks, the window is *valid* and *minimal* for the current `r`. Update answer *after* shrinking, not before.

## Diagram
```mermaid
flowchart LR
  Init["l=0, r=0"] --> Loop["for r in 0..n"]
  Loop --> Add["add nums[r] to window"]
  Add --> Bad{"window invalid?"}
  Bad -->|yes| Shrink["shrink l while invalid"]
  Shrink --> Ans
  Bad -->|no| Ans["update best with r-l+1"]
  Ans --> Loop
```


## Problems

### 3. Longest Substring Without Repeating Characters (Medium)
> [LeetCode 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) • Tags: Hash Table, String, Sliding Window

**Problem Statement:**

Given a string s, find the length of the longest substring without duplicate characters. 
Example 1: 
```
Input: s = "abcabcbb" 
Output: 3 Explanation: The answer is "abc", with the length of 3. 
Note that "bca" and "cab" are also correct answers. 
```

Example 2: 
```
Input: s = "bbbbb" 
Output: 1 Explanation: The answer is "b", with the length of 1. 
```

Example 3: 
```
Input: s = "pwwkew" 
Output: 3 Explanation: The answer is "wke", with the length of 3. 
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring. 
Constraints: 0 5 s consists of English letters, digits, symbols and spaces.
```

---

### 438. Find All Anagrams in a String (Medium)
> [LeetCode 438](https://leetcode.com/problems/find-all-anagrams-in-a-string/) • Tags: Hash Table, String, Sliding Window

**Problem Statement:**

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order. Example 1: Input: s = "cbaebabacd", p = "abc" Output: [0,6] Explanation: The substring with start index = 0 is "cba", which is an anagram of "abc". The substring with start index = 6 is "bac", which is an anagram of "abc". Example 2: Input: s = "abab", p = "ab" Output: [0,1,2] Explanation: The substring with start index = 0 is "ab", which is an anagram of "ab". The substring with start index = 1 is "ba", which is an anagram of "ab". The substring with start index = 2 is "ab", which is an anagram of "ab". Constraints: 1 4 s and p consist of lowercase English letters.

**Examples:**

Example 1:
```
"cbaebabacd"
```

Example 2:
```
"abc"
```

Example 3:
```
"abab"
```

Example 4:
```
"ab"
```
---

### 76. Minimum Window Substring (Hard)
> [LeetCode 76](https://leetcode.com/problems/minimum-window-substring/) • Tags: Hash Table, String, Sliding Window

**Problem Statement:**

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "". The testcases will be generated such that the answer is unique. Example 1: Input: s = "ADOBECODEBANC", t = "ABC" Output: "BANC" Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t. Example 2: Input: s = "a", t = "a" Output: "a" Explanation: The entire string s is the minimum window. Example 3: Input: s = "a", t = "aa" Output: "" Explanation: Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string. Constraints: m == s.length n == t.length 1 5 s and t consist of uppercase and lowercase English letters. Follow up: Could you find an algorithm that runs in O(m + n) time?

**Examples:**

Example 1:
```
"ADOBECODEBANC"
```

Example 2:
```
"ABC"
```

Example 3:
```
"a"
```

Example 4:
```
"a"
```

Example 5:
```
"a"
```

Example 6:
```
"aa"
```
---

### 209. Minimum Size Subarray Sum (Medium)
> [LeetCode 209](https://leetcode.com/problems/minimum-size-subarray-sum/) • Tags: Array, Binary Search, Sliding Window, Prefix Sum

**Problem Statement:**

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead. Example 1: Input: target = 7, nums = [2,3,1,2,4,3] Output: 2 Explanation: The subarray [4,3] has the minimal length under the problem constraint. Example 2: Input: target = 4, nums = [1,4,4] Output: 1 Example 3: Input: target = 11, nums = [1,1,1,1,1,1,1,1] Output: 0 Constraints: 1 9 1 5 1 4 Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

**Examples:**

Example 1:
```
7
```

Example 2:
```
[2,3,1,2,4,3]
```

Example 3:
```
4
```

Example 4:
```
[1,4,4]
```

Example 5:
```
11
```

Example 6:
```
[1,1,1,1,1,1,1,1]
```
---


## Code / Example
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

## When to Use / When NOT
- **Use:** contiguous subarray/substring with max/min/longest/shortest condition; fixed-k sums/averages; "window" / "substring" / "subarray" keywords.
- **NOT:** non-contiguous subsequence (use DP/backtracking); need original order but not contiguous; sorted pair search (use two pointers).

## Trade-offs
| Type | Time | Space |
|------|------|-------|
| Fixed-k | O(n) | O(1) |
| Variable + HashMap | O(n) | O(k) for frequency map (k = distinct chars in window) |
| Variable + HashSet | O(n) | O(min(n, alphabet)) |

## Vs Table
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

## Interview Q&A (Senior Depth)

**Q: Longest substring without repeating — why update answer *after* the `while` shrink loop?**
**A:** The `while` loop guarantees the window `[l, r]` has all unique characters. Before the `while`, the window is invalid (has a duplicate). Updating before shrink would record an invalid window. The invariant: at the top of the `for` loop, `[l, r-1]` is valid; we add `r`, possibly invalid; `while` restores validity; *then* `[l, r]` is the maximal valid window ending at `r`.

**Q: Minimum window substring (LC 76) — why `formed == required` and not just "all chars present"?**
**A:** `t` can have duplicates (e.g., `t="AAB"` needs 2 A's, 1 B). `required` = distinct chars in `t` (2). `formed` increments only when a char's count *exactly matches* its required count. This handles duplicates correctly — we don't overcount when we have 3 A's but only need 2.

**Q: When does fixed-k sliding window beat prefix sum for max sum of k?**
**A:** Both O(n). Sliding window O(1) space, prefix sum O(n) space. Sliding window is simpler for fixed-k — no extra array. Prefix sum wins when you have *many different k queries* on the same array (preprocess once, answer any k in O(1)). For single k, sliding window is preferred.

**Q: Can sliding window handle negative numbers for "longest subarray with sum <= k"?**
**A:** No — with negatives, shrinking `l` can *increase* the sum (removing a negative), breaking the monotonicity that makes the `while` shrink correct. For negatives + sum constraint, use prefix sum + ordered map (TreeMap) or monotonic deque (LC 862).


## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the trigger keyword for Sliding Window? :: **A:** subarray/substring with condition, max/min length, fixed/variable window, at most K distinct #flashcard

#flashcard
**Q:** Time/space complexity of Sliding Window? :: **A:** Time: O(n) each element visited ≤2 times, Space: O(k) for hashmap/set #flashcard

#flashcard
**Q:** When do you NOT use Sliding Window? :: **A:** non-contiguous subsequence (use DP/backtrack), need all subarrays (O(n²) output) #flashcard

#flashcard
**Q:** Core Java 25 snippet for Sliding Window? :: **A:** `int l=0; for(int r=0;r<n;r++){ add(a[r]); while(invalid()) remove(a[l++]); updateAns(); }` #flashcard


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
- [[01_Array/01 - Prefix Sum|Prefix Sum]] (fixed-k sums, alternative for static arrays)
- [[01_Array/04 - Frequency Counting|Frequency Counting]] (hashmap on window for variable windows)
- [[01_Array/02 - Two Pointers|Two Pointers]] (two pointers move inward; window moves forward)
- [[Java/07_DSA/Array]] · [[Java/07_DSA/HashMap]]
---
*Category: Coding Patterns/01_Array*
- [[Architect/10_System-Design-Interviews/BB-04-Rate-Limiter.md|BB-04-Rate-Limiter]] — Sliding window rate limiting
- [[Architect/10_System-Design-Interviews/CACHE-02-Cache-Strategies.md|CACHE-02-Cache-Strategies]] — Sliding window cache eviction
