---
title: "Kadane's Algorithm"
type: pattern
pattern: 23
domain: "Advanced Array"
category: "Coding Patterns/09_Advanced"
advanced: true
mastery: learn
recognition_score: 0
implementation_score: 0
attempts: 0
successful_attempts: 0
recognition_attempts: 0
recognition_successes: 0
avg_time_minutes:
hint_count: 0
last_attempt:
last_success:
failure_category:
difficulty: "Easy"
leetcode: [53, 152, 918, 1186]
created: "2026-09-29"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - advanced-array
---

# Kadane's Algorithm

> Advanced pattern · Advanced Array

## Recognition

- Maximum or minimum contiguous subarray score
- Each position can either extend a current run or start a new one
- Need linear time

### Strong signals
- Maximum or minimum contiguous subarray score
- Each position can either extend a current run or start a new one

### Do not infer it from
- A keyword alone
- A familiar example without checking constraints

## Invariant

> At each index, the running state is the best subarray score ending exactly at that index.

## Mental model

Maintain the smallest state that completely describes the part of the search space still relevant to the answer.

## Core implementation

```java
// Maximum Subarray — LC 53 (classic Kadane)
int maxSubArray(int[] nums) {
    int cur = nums[0], best = nums[0];
    for (int i = 1; i < nums.length; i++) {
        cur = Math.max(nums[i], cur + nums[i]);
        best = Math.max(best, cur);
    }
    return best;
}

// Maximum Product Subarray — LC 152 (track min+max)
int maxProduct(int[] nums) {
    int maxSoFar = nums[0], minSoFar = nums[0], best = nums[0];
    for (int i = 1; i < nums.length; i++) {
        int x = nums[i];
        if (x < 0) { int tmp = maxSoFar; maxSoFar = minSoFar; minSoFar = tmp; }
        maxSoFar = Math.max(x, maxSoFar * x);
        minSoFar = Math.min(x, minSoFar * x);
        best = Math.max(best, maxSoFar);
    }
    return best;
}

// Maximum Sum Circular Subarray — LC 918
int maxSubarraySumCircular(int[] nums) {
    int maxKadane = kadane(nums); // non-circular max
    int total = 0;
    for (int x : nums) total += x;
    // invert and find min subarray (non-empty)
    for (int i = 0; i < nums.length; i++) nums[i] = -nums[i];
    int minKadane = kadane(nums);
    // restore
    for (int i = 0; i < nums.length; i++) nums[i] = -nums[i];
    // circular max = total - min subarray (if not all negative)
    if (maxKadane < 0) return maxKadane; // all negative
    return Math.max(maxKadane, total + minKadane);
}
int kadane(int[] nums) {
    int cur = nums[0], best = nums[0];
    for (int i = 1; i < nums.length; i++) {
        cur = Math.max(nums[i], cur + nums[i]);
        best = Math.max(best, cur);
    }
    return best;
}

// Maximum Subarray Sum with One Deletion — LC 1186
int maximumSum(int[] arr) {
    int n = arr.length;
    int noDel = arr[0], oneDel = Integer.MIN_VALUE / 2, best = arr[0];
    for (int i = 1; i < n; i++) {
        // oneDel: either extend previous oneDel, or delete current (take previous noDel)
        oneDel = Math.max(oneDel + arr[i], noDel);
        // noDel: standard Kadane
        noDel = Math.max(arr[i], noDel + arr[i]);
        best = Math.max(best, Math.max(noDel, oneDel));
    }
    return best;
}
```

## Variants

Start with the core implementation. Introduce a variant only when the required state or proof changes.

## When to use
- maximum subarray sum/product; maximum circular subarray; max subarray with deletion/k-length constraint; "best contiguous segment".

## When NOT to use
- non-contiguous subsequence (use DP on subsequence); 2D max submatrix (use 2D Kadane / prefix sum); need the actual subarray indices (track start/end).

## Complexity & trade-offs

| Variant | Time | Space | Key Insight |
|---------|------|-------|-------------|
| Max Sum (LC 53) | O(n) | O(1) | `cur = max(x, cur + x)` |
| Max Product (LC 152) | O(n) | O(1) | Track min+max, swap on negative |
| Max Circular (LC 918) | O(n) | O(1) | `max(non-circular, total - min)` |
| One Deletion (LC 1186) | O(n) | O(1) | Two states: `noDel`, `oneDel` |

| Aspect | Kadane (Sum) | Kadane (Product) | Divide & Conquer | Prefix Sum + Min |
|--------|--------------|------------------|------------------|------------------|
| Time | O(n) | O(n) | O(n log n) | O(n) |
| Space | O(1) | O(1) | O(log n) stack | O(n) |
| Handles negatives | Yes | Yes (track min) | Yes | Yes |
| Circular variant | Total - min | Complex | Possible | Possible |
| Pick when | Standard max sum | Max product | Teaching/recursion | When prefix array exists |

## Pitfalls

- **All negative array:** `cur = max(x, cur + x)` works correctly — it picks the least negative element. But circular variant needs special handling: if `maxKadane < 0`, return it (total - min would be 0, incorrectly suggesting empty subarray).
- **Product: swap min/max on negative** — multiplying by negative flips min↔max. Forgetting this is the #1 bug.
- **One Deletion: initialize `oneDel` to `-inf`** — can't delete before having at least one element. `Integer.MIN_VALUE / 2` avoids overflow when adding.
- **Empty subarray not allowed** — initialize with `nums[0]`, not 0.
- **Track indices for subarray bounds:** need `curStart` updated when `cur` resets to `x`, and `bestStart/bestEnd` when `best` updates.

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 53 | Easy |
| 152 | Medium |
| 918 | Medium |
| 1186 | Medium |

## Interview Q&A

(Senior Depth)

**Q: Why does `cur = max(x, cur + x)` correctly find the maximum subarray sum?**
A: Optimal substructure: the max subarray ending at index i either (1) is just `nums[i]` (starting fresh), or (2) extends the max subarray ending at i-1 by appending `nums[i]`. If the max subarray ending at i-1 has negative sum, appending `nums[i]` makes it worse than starting fresh. So we take the max of the two choices. By induction, `cur` at each step is the max sum of subarrays ending at that index.

**Q: Maximum Product Subarray — why track both min and max?**
A: A negative number times a negative minimum becomes a positive maximum. Example: `[-2, 3, -4]`. At -2: max=-2, min=-2. At 3: max=3, min=-6. At -4: negative flips them — new max = max(-4, -6 * -4) = 24. If we only tracked max, we'd miss that -6 * -4 = 24. The min tracks the "most negative" which can become max when multiplied by a negative.

**Q: Maximum Sum Circular Subarray — why `total - minSubarray`?**
A: A circular subarray is the complement of a non-circular subarray. If you remove a middle segment (min subarray), the remaining wraps around = circular subarray. Sum = total - minMiddle. But if all negative, minMiddle = total, leaving empty subarray — invalid. Hence check `maxKadane < 0`.

**Q: Maximum Subarray with One Deletion — explain the two-state DP.**
A: `noDel[i]` = max subarray ending at i with 0 deletions. `oneDel[i]` = max subarray ending at i with exactly 1 deletion.
- `noDel[i] = max(arr[i], noDel[i-1] + arr[i])` (standard Kadane)
- `oneDel[i] = max(oneDel[i-1] + arr[i], noDel[i-1])` — either extend a subarray that already deleted one, or delete `arr[i]` (take `noDel[i-1]` which has 0 deletions up to i-1).
Answer = max over all i of both states.

**Q: Can Kadane be extended to "at most k elements"?**
A: Yes — sliding window + deque (monotonic queue on prefix sums) or DP with `dp[i][k]`. For exactly k: prefix sum + `pref[i] - min(pref[i-k])`. For at most k: maintain deque of candidate minimums within window of size k.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Kadane's Algorithm? :: **A:** maximum subarray sum, max product subarray, best time to buy/sell stock, circular subarray #flashcard

#flashcard
**Q:** Time/space complexity of Kadane's Algorithm? :: **A:** Time: O(n) single pass, Space: O(1) #flashcard

#flashcard
**Q:** When do you NOT use Kadane's Algorithm? :: **A:** need the subarray indices (track start/end), all negative (return max element) #flashcard

#flashcard
**Q:** Core Java 25 snippet for Kadane's Algorithm? :: **A:** `int maxSoFar=nums[0], maxEndingHere=nums[0]; for(int i=1;i<n;i++){ maxEndingHere=Math.max(nums[i], maxEndingHere+nums[i]); maxSoFar=Math.max(maxSoFar, maxEndingHere); }` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- Dynamic Programming (Kadane is 1D DP)
- Prefix Sum (circular variant uses total sum)
- Monotonic Stack (sliding window max for k-constraint)
