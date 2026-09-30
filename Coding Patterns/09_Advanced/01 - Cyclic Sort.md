---
title: "Cyclic Sort"
type: pattern
pattern: 22
domain: "Advanced Array"
category: "Coding Patterns/09_Advanced"
advanced: true
mastery: learn
recognition_score: 0
difficulty: "Easy"
leetcode: [268, 442, 448, 645]
created: "2026-09-29"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - advanced-array
---

# Cyclic Sort

> Advanced pattern · Advanced Array

## Recognition

- Values occupy a known contiguous range
- Correct value has a predictable index
- Need O(n) time and O(1) extra space

### Strong signals
- Values occupy a known contiguous range
- Correct value has a predictable index

### Do not infer it from
- A keyword alone
- A familiar example without checking constraints

## Invariant

> After processing position i, the value placed there is correct whenever its value maps to a valid index.

## Mental model

Maintain the smallest state that completely describes the part of the search space still relevant to the answer.

## Core implementation

```java
// Cyclic Sort template — elements in [1..n]
void cyclicSort(int[] nums) {
    int i = 0;
    while (i < nums.length) {
        int correct = nums[i] - 1; // 1-indexed values → 0-indexed position
        if (nums[i] != nums[correct]) {
            int tmp = nums[i];
            nums[i] = nums[correct];
            nums[correct] = tmp;
        } else {
            i++;
        }
    }
}

// Missing Number — LC 268 (0..n range)
int missingNumber(int[] nums) {
    int i = 0;
    while (i < nums.length) {
        int correct = nums[i]; // 0-indexed values → correct position
        if (nums[i] < nums.length && nums[i] != nums[correct]) {
            int tmp = nums[i];
            nums[i] = nums[correct];
            nums[correct] = tmp;
        } else {
            i++;
        }
    }
    for (i = 0; i < nums.length; i++)
        if (nums[i] != i) return i;
    return nums.length; // n is missing
}

// Find All Duplicates — LC 442
java.util.List<Integer> findDuplicates(int[] nums) {
    int i = 0;
    while (i < nums.length) {
        int correct = nums[i] - 1;
        if (nums[i] != nums[correct]) {
            int tmp = nums[i];
            nums[i] = nums[correct];
            nums[correct] = tmp;
        } else {
            i++;
        }
    }
    var res = new java.util.ArrayList<Integer>();
    for (i = 0; i < nums.length; i++)
        if (nums[i] != i + 1) res.add(nums[i]);
    return res;
}

// Find All Disappeared — LC 448
java.util.List<Integer> findDisappearedNumbers(int[] nums) {
    int i = 0;
    while (i < nums.length) {
        int correct = nums[i] - 1;
        if (nums[i] != nums[correct]) {
            int tmp = nums[i];
            nums[i] = nums[correct];
            nums[correct] = tmp;
        } else {
            i++;
        }
    }
    var res = new java.util.ArrayList<Integer>();
    for (i = 0; i < nums.length; i++)
        if (nums[i] != i + 1) res.add(i + 1);
    return res;
}

// Set Mismatch — LC 645 (duplicate + missing)
int[] findErrorNums(int[] nums) {
    int i = 0;
    while (i < nums.length) {
        int correct = nums[i] - 1;
        if (nums[i] != nums[correct]) {
            int tmp = nums[i];
            nums[i] = nums[correct];
            nums[correct] = tmp;
        } else {
            i++;
        }
    }
    for (i = 0; i < nums.length; i++)
        if (nums[i] != i + 1) return new int[]{nums[i], i + 1};
    return new int[0];
}
```

## Variants

Start with the core implementation. Introduce a variant only when the required state or proof changes.

## When to use

- array with elements in `[1..n]` or `[0..n-1]`; find missing, duplicate, first missing positive; any permutation of known range.
- **NOT:** values outside the range; need stable sort; array is read-only (cyclic sort mutates).

## When NOT to use

values outside the range; need stable sort; array is read-only (cyclic sort mutates).

## Complexity & trade-offs

| Approach | Time | Space | Mutates Input |
|----------|------|-------|---------------|
| Cyclic Sort | O(n) | O(1) | Yes |
| HashSet | O(n) | O(n) | No |
| Sort + Scan | O(n log n) | O(1) or O(n) | Depends |

| Aspect | Cyclic Sort | HashSet | Sort |
|--------|-------------|---------|------|
| Time | O(n) | O(n) | O(n log n) |
| Space | O(1) | O(n) | O(1) extra |
| Mutates | Yes | No | Yes |
| Pick when | range [1..n] known, O(1) space required | general duplicates, read-only | simpler code acceptable |

## Pitfalls

- **Infinite loop if `nums[i] == nums[correct]` but `i != correct`** — this happens when duplicates exist. The `else i++` handles it: we only swap when the target position has a *different* value.
- **Range check:** For `[0..n]` (LC 268), `correct = nums[i]`; for `[1..n]`, `correct = nums[i] - 1`. Get this wrong → `ArrayIndexOutOfBoundsException`.
- **Don't increment `i` after swap** — the new value at `i` needs to be checked again.
- **First Missing Positive (LC 41)** extends this: first segregate positives, then cyclic sort the positive segment.

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 268 | Easy |
| 442 | Medium |
| 448 | Easy |
| 645 | Easy |

## Interview Q&A

(Senior Depth)

**Q: Why is the inner `while` still O(n) total, not O(n²)?**
A: Each swap puts at least one element in its final correct position. An element never leaves its correct position once placed. With n elements, at most n swaps total. The `while` loop condition is checked O(n) times for successful swaps + O(n) times for failed checks (when `i++`). Total = O(2n) = O(n).

**Q: Cyclic Sort vs Counting Sort — what's the difference?**
A: Cyclic sort works *in-place* on arrays where values = indices (permutation of [1..n]). Counting sort allocates a frequency array of size `maxVal`, works for any range but uses O(k) space. Cyclic sort is a specialized in-place variant for the exact permutation case.

**Q: First Missing Positive (LC 41) — how does it extend cyclic sort?**
A: LC 41 has no range guarantee. Two-pass: (1) segregate: move all `≤0` and `>n` to front (or ignore), keep only `[1..n]` in the active segment. (2) Cyclic sort the active segment. (3) Scan for first `nums[i] != i+1`. The segregation step is the key addition.

**Q: Can cyclic sort handle negative numbers?**
A: Only if you transform the range. For `[-k..k]`, add `k` to make it `[0..2k]`, cyclic sort, subtract `k` after. But this is rarely asked — usually the problem guarantees `[1..n]` or `[0..n-1]`.

**Q: Set Mismatch (LC 645) — why does the duplicate value end up at the missing index?**
A: After cyclic sort, every index `i` should have value `i+1`. The missing value `m` means index `m-1` is empty. The duplicate `d` gets placed at index `d-1` (its correct spot), but since `d` appears twice, the *second* `d` has nowhere to go — it stays at the index where `m` should be. So `nums[m-1] = d` and `m` is missing.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Cyclic Sort? :: **A:** find missing/duplicate in 1..n, first missing positive, find corruption, sort array with elements in range #flashcard

#flashcard
**Q:** Time/space complexity of Cyclic Sort? :: **A:** Time: O(n) each element swapped at most once, Space: O(1) in-place #flashcard

#flashcard
**Q:** When do you NOT use Cyclic Sort? :: **A:** elements not in 1..n range, need stable sort, array has large values #flashcard

#flashcard
**Q:** Core Java 25 snippet for Cyclic Sort? :: **A:** `for(int i=0;i<n;){ if(nums[i]!=i+1 && nums[i]<=n && nums[i]!=nums[nums[i]-1]) swap(nums,i,nums[i]-1); else i++; }` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory 📅 2026-10-01
- [ ] Write the template from memory 📅 2026-10-03
- [ ] Solve one unseen problem without hints 📅 2026-10-07
- [ ] Explain the invariant aloud 📅 2026-10-14

## Related

- [[01_Array/01 - Prefix Sum|Prefix Sum]] (XOR alternative for missing number)
- [[01_Array/04 - Frequency Counting|Frequency Counting]] (HashMap alternative)
- [[08_Bit_Manipulation/01 - Bit Manipulation|Bit Manipulation]] (XOR for single missing)
