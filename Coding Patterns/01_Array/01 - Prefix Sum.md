---
title: "Prefix Sum"
type: pattern
pattern: 1
domain: "Array / String"
category: "Coding Patterns/01_Array"
advanced: false
mastery: learn
recognition_score: 0
difficulty: "Easy"
leetcode: [560, 930, 525]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - pattern/array-string
---

# Prefix Sum

> Pattern #1 · Array / String

## Recognition

- Repeated range-sum queries
- Contiguous subarray sums or counts
- Static data where previous cumulative work can be reused

### Strong signals
- Repeated range-sum queries
- Contiguous subarray sums or counts

### Do not infer it from
- A keyword alone
- A familiar LeetCode example without checking the constraints

## Invariant

> At position j, the prefix value represents the aggregate of every element before j; any range can therefore be derived from two prefix states.

## Mental model

Precompute cumulative state once, then answer each range or subarray question by comparing two prefix states. The key is turning repeated work into constant-time subtraction or lookup.

## Core implementation

```java
// Java 25: var, record, pattern matching
record PrefixSum(int[] pref) {
    static PrefixSum of(int[] nums) {
        int n = nums.length;
        int[] pref = new int[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        return new PrefixSum(pref);
    }
    int rangeSum(int i, int j) { // inclusive
        return pref[j + 1] - pref[i];
    }
}

// Count subarrays with sum k (LC 560) — hashmap on prefix sums
int subarraySum(int[] nums, int k) {
    var count = new java.util.HashMap<Integer, Integer>();
    count.put(0, 1);
    int sum = 0, ans = 0;
    for (var x : nums) {
        sum += x;
        ans += count.getOrDefault(sum - k, 0);
        count.put(sum, count.getOrDefault(sum, 0) + 1);
    }
    return ans;
}
```

## Variants

Use the implementation above as the base case. Extend it only after the invariant remains explicit.

## When to use

- many range-sum queries on static array; subarray sum = k / count subarrays; "contiguous" + "sum" keywords; immutable data, repeated queries.
- **NOT:** array updates interleaved with queries (use Segment Tree / Fenwick); need min/max/gcd on range (use Sparse Table); single query (just loop).

## When NOT to use

array updates interleaved with queries (use Segment Tree / Fenwick); need min/max/gcd on range (use Sparse Table); single query (just loop).

## Complexity & trade-offs

| Dimension | Prefix Sum | Segment Tree | Sparse Table |
|-----------|------------|--------------|--------------|
| Build     | O(n)       | O(n)         | O(n log n)   |
| Query     | O(1) sum only | O(log n) any associative op | O(1) idempotent ops (min/max/gcd) |
| Update    | rebuild O(n) | O(log n) | rebuild O(n log n) |
| Space     | O(n)       | O(n)         | O(n log n)   |
| Pick when | immutable array, sum queries only | updates + queries interleaved | static array, min/max queries |

| Aspect | Prefix Sum | Segment Tree | Sparse Table | Decision Rule |
|--------|------------|--------------|--------------|---------------|
| Query type | sum only | any associative | idempotent only | sum → prefix; min/max → sparse; updates → segment |
| Mutability | immutable | mutable | immutable | updates needed? → segment tree |
| Implementation | trivial | moderate | moderate | simplest that fits constraints |

## Pitfalls

- `pref` length is `n+1` with leading zero — off-by-one is the #1 bug.
- Large sums need `long[]` for `pref` (overflow on `int`).
- Subarray count hashmap **must** `count.put(0, 1)` before the loop (empty prefix).
- For 2D prefix sums, `pref[r+1][c+1] = pref[r][c+1] + pref[r+1][c] - pref[r][c] + grid[r][c]`.

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 560 | Subarray Sum Equals K | Medium |
| 930 | Binary Subarrays With Sum | Medium |
| 525 | Contiguous Array | Medium |

## Interview Q&A

(Senior Depth)

**Q: Walk me through counting subarrays with sum k. Why does the hashmap-on-prefix work?**
**A:** We want `sum(i..j) = k`. With prefix sums `pref[j+1] - pref[i] = k` → `pref[i] = pref[j+1] - k`. So as we scan `j`, we count how many earlier `pref[i]` equal `pref[j+1] - k`. The hashmap stores frequency of each prefix sum seen so far. `count[0]=1` handles subarrays starting at index 0. Time O(n), space O(n). Rejected alternative: two pointers — fails because array has negatives / not sorted.

**Q: When would you NOT use prefix sum for range queries?**
**A:** When the array mutates. Prefix sum rebuild is O(n) per update. If updates + queries are interleaved, use Fenwick Tree (BIT) or Segment Tree — both O(log n) update and query. Prefix sum wins only for static data.

**Q: 2D range sum query immutable (LC 304). How does the formula change?**
**A:** `pref[r+1][c+1] = pref[r][c+1] + pref[r+1][c] - pref[r][c] + grid[r][c]`. Query `(r1,c1)-(r2,c2)`: `pref[r2+1][c2+1] - pref[r1][c2+1] - pref[r2+1][c1] + pref[r1][c1]`. Same O(1) query after O(mn) build. Inclusion-exclusion principle.

**Q: Given streaming data, can you maintain prefix sums?**
**A:** No — prefix sum assumes static array. For streaming, you need a Fenwick Tree or Segment Tree that supports point updates. Or if it's append-only, you *can* append to `pref` in O(1) per element.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Prefix Sum? :: **A:** range sum queries, subarray sum equals k, immutable array repeated queries #flashcard

#flashcard
**Q:** Time/space complexity of Prefix Sum? :: **A:** Time: O(n) build + O(1) query, Space: O(n) #flashcard

#flashcard
**Q:** When do you NOT use Prefix Sum? :: **A:** array mutates (use Fenwick/Segment Tree), single query (just loop), need min/max on range (use Sparse Table) #flashcard

#flashcard
**Q:** Core Java 25 snippet for Prefix Sum? :: **A:** `int[] pref = new int[n+1]; for (int i=0;i<n;i++) pref[i+1]=pref[i]+a[i]; int sum(int l,int r){return pref[r+1]-pref[l];}` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- [[01_Array/03 - Sliding Window|Sliding Window]] (fixed-k sums use prefix internally)
- [[01_Array/04 - Frequency Counting|Frequency Counting]] (hashmap on prefix for subarray count)
- [[Java/07_DSA/Array]] · [[Java/07_DSA/HashMap]]
