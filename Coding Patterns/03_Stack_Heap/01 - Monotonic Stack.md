---
title: "Monotonic Stack"
type: pattern
pattern: 7
domain: "Stack"
category: "Coding Patterns/03_Stack_Heap"
advanced: false
mastery: learn
recognition_score: 0
difficulty: "Medium"
leetcode: [739, 901, 84, 496]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - stack
---

# Monotonic Stack

> Pattern #7 · Stack

## Recognition

- Next or previous greater/smaller element
- Need nearest unresolved candidate
- Each element can be pushed and popped once

### Strong signals
- Next or previous greater/smaller element
- Need nearest unresolved candidate

### Do not infer it from
- A keyword alone
- A familiar example without checking constraints

## Invariant

> The stack remains monotonic, so every element below the top is still a valid unresolved candidate.

## Mental model

This pattern reduces the search space by maintaining a compact state that represents all information needed for the next decision.

## Core implementation

```java
// Next Greater Element — LC 496
int[] nextGreater(int[] nums) {
    int n = nums.length;
    var res = new int[n];
    java.util.Arrays.fill(res, -1);
    var st = new java.util.ArrayDeque<Integer>(); // stores indices
    for (int i = 0; i < n; i++) {
        while (!st.isEmpty() && nums[st.peek()] < nums[i]) {
            res[st.pop()] = nums[i];
        }
        st.push(i);
    }
    return res;
}

// Daily Temperatures — LC 739 (answer is distance, not value)
int[] dailyTemperatures(int[] temps) {
    int n = temps.length;
    var ans = new int[n];
    var st = new java.util.ArrayDeque<Integer>();
    for (int i = 0; i < n; i++) {
        while (!st.isEmpty() && temps[st.peek()] < temps[i]) {
            int j = st.pop();
            ans[j] = i - j; // days until warmer
        }
        st.push(i);
    }
    return ans;
}

// Largest Rectangle in Histogram — LC 84 (sentinel flush)
int largestRectangleArea(int[] heights) {
    int n = heights.length;
    var st = new java.util.ArrayDeque<Integer>();
    int maxArea = 0;
    for (int i = 0; i <= n; i++) {
        int h = (i == n) ? 0 : heights[i]; // sentinel 0 flushes stack
        while (!st.isEmpty() && heights[st.peek()] > h) {
            int height = heights[st.pop()];
            int width = st.isEmpty() ? i : i - st.peek() - 1;
            maxArea = Math.max(maxArea, height * width);
        }
        st.push(i);
    }
    return maxArea;
}
```

## Variants

Start with the core implementation. Introduce a variant only when the problem changes the invariant or required state.

## When to use

- next greater/smaller element; daily temperatures/span; histogram (largest rectangle); trapping rain water; stock span; sliding window maximum (monotonic deque variant).
- **NOT:** arbitrary range queries (use segment tree / sparse table); need all historical values (stack discards dominated elements).

## When NOT to use

arbitrary range queries (use segment tree / sparse table); need all historical values (stack discards dominated elements).

## Complexity & trade-offs

| Metric | Value |
|--------|-------|
| Time | O(n) — each element pushed/popped at most once |
| Space | O(n) worst case (monotonic input) |

| Aspect | Monotonic Stack | Brute Force Next Greater | Sorting |
|--------|-----------------|--------------------------|---------|
| Next greater element | O(n) | O(n²) | N/A (doesn't solve) |
| Space | O(n) | O(1) | O(n) |
| Solves range queries | No | No | No |
| Pick when | nearest greater/smaller, histogram, span | n tiny | order is the whole question |

## Pitfalls

- **Store indices, not values** — you need positions to write answers by index and compute distances.
- For histogram, add sentinel `0` at end to flush stack — otherwise remaining bars never get processed.
- Decide increasing vs decreasing *before* coding: decreasing stack (top is largest) → next greater; increasing stack (top is smallest) → next smaller.
- `ArrayDeque` is the Java 25 choice over legacy `Stack`. `peek()` and `pop()` work as expected.

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 739 | Medium |
| 901 | Medium |
| 84 | Hard |
| 496 | Easy |

## Interview Q&A

(Senior Depth)

**Q: Why is the inner `while` loop O(n) total, not O(n²)?**
**A:** Each index is pushed onto the stack exactly once and popped at most once. The total number of `pop` operations across the entire algorithm ≤ n. The `while` condition is checked O(n) times for successful pops + O(n) times for failed checks (when loop exits). Total operations = O(2n) = O(n).

**Q: Daily Temperatures — why does storing indices let us compute the answer?**
**A:** When `temps[i] > temps[stack.top()]`, we found the next warmer day for the popped index `j`. The answer is `i - j` (days between them). If we stored values, we'd know *that* a warmer day exists but not *when*. Indices preserve position information.

**Q: Largest Rectangle in Histogram — explain the width calculation when stack becomes empty after pop.**
**A:** When stack is empty after popping index `j`, the popped bar `heights[j]` is the smallest seen so far (extending to index 0). Width = `i` (current index, which is the first bar to the right that's lower). If stack not empty, new top `k` is the first bar to the left that's lower than `heights[j]`, so width = `i - k - 1`. The sentinel `0` at `i=n` ensures all bars get popped.

**Q: Trapping Rain Water (LC 42) — how does monotonic stack apply?**
**A:** Decreasing stack of indices. When `heights[i] > heights[stack.top()]`, we pop the bottom `bottom = stack.pop()`. If stack now empty, no left wall → continue. Else left wall = `stack.top()`. Trapped water over `bottom` = `(min(heights[left], heights[i]) - heights[bottom]) * (i - left - 1)`. Each bar is the "bottom" of a trapped pocket exactly once.

**Q: Monotonic Stack vs Monotonic Deque (Sliding Window Maximum).**
**A:** Stack = LIFO, discards dominated elements permanently (for next greater). Deque = double-ended, maintains window of candidates for sliding window max. For sliding window max, you need to remove elements that leave the window (from front) AND elements dominated by new arrival (from back). Deque supports both; stack only supports back removal.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Monotonic Stack? :: **A:** next greater/smaller element, largest rectangle in histogram, trapping rain water, stock span #flashcard

#flashcard
**Q:** Time/space complexity of Monotonic Stack? :: **A:** Time: O(n) each element pushed/popped once, Space: O(n) #flashcard

#flashcard
**Q:** When do you NOT use Monotonic Stack? :: **A:** need all pairs (O(n²)), offline queries (use segment tree) #flashcard

#flashcard
**Q:** Core Java 25 snippet for Monotonic Stack? :: **A:** `Deque<Integer> st=new ArrayDeque<>(); for(int i=0;i<n;i++){ while(!st.isEmpty() && a[st.peek()]<a[i]) ans[st.pop()]=i; st.push(i); }` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- [[01_Array/03 - Sliding Window|Sliding Window]] (monotonic deque for sliding window max)
- [[03_Stack_Heap/02 - Top K Elements|Top K Elements]] (heap for top-k, different use case)
- [[Java/07_DSA/Stack]]
