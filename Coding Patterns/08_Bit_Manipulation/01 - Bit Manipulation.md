---
title: "Bit Manipulation"
type: pattern
pattern: 21
domain: "Bit Manipulation"
category: "Coding Patterns/08_Bit_Manipulation"
advanced: false
mastery: learn
recognition_score: 0
difficulty: "Easy"
leetcode: [191, 136, 260]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - bit-manipulation
---

# Bit Manipulation

> Pattern #21 · Bit Manipulation

## Recognition

- XOR cancellation
- Masks or subsets represented as bits
- Need compact integer state or bit counts

### Strong signals
- XOR cancellation
- Masks or subsets represented as bits

### Do not infer it from
- A keyword alone
- A familiar example without checking constraints

## Invariant

> Each bit operation transforms the encoded state while preserving the property represented by the selected bits.

## Mental model

Maintain the smallest state that completely describes the part of the search space still relevant to the answer.

## Core implementation

```java
// Single Number — LC 136 (XOR all)
int singleNumber(int[] nums) {
    int x = 0;
    for (int v : nums) x ^= v;
    return x;
}

// Power of Two — LC 231
boolean isPowerOfTwo(int n) {
    return n > 0 && (n & (n - 1)) == 0;
}

// Count 1 Bits — LC 191 (Hamming weight)
int hammingWeight(int n) {
    int c = 0;
    while (n != 0) { n &= (n - 1); c++; } // drops lowest 1 each loop
    return c;
}

// Subsets via bit mask
java.util.List<java.util.List<Integer>> subsets(int[] nums) {
    int n = nums.length;
    var res = new java.util.ArrayList<java.util.List<Integer>>();
    for (int mask = 0; mask < (1 << n); mask++) {
        var cur = new java.util.ArrayList<Integer>();
        for (int i = 0; i < n; i++) if ((mask & (1 << i)) != 0) cur.add(nums[i]);
        res.add(cur);
    }
    return res;
}

// Missing Number — LC 268 (XOR indices ^ values)
int missingNumber(int[] nums) {
    int x = 0;
    for (int i = 0; i < nums.length; i++) x ^= i ^ nums[i];
    return x ^ nums.length; // index n missing
}

// Single Number II — LC 137 (two singles need bit counting per position)
int singleNumberII(int[] nums) {
    int ones = 0, twos = 0;
    for (int x : nums) {
        ones = (ones ^ x) & ~twos;
        twos = (twos ^ x) & ~ones;
    }
    return ones;
}
```

## Variants

Start with the core implementation. Introduce a variant only when the required state or proof changes.

## When to use
- find unique/single number; count bits; test power of two; enumerate subsets by bit mask; toggle flags; missing number.

## When NOT to use
- frequency of each value (use HashMap); two single numbers (need partition by differing bit); large bit operations beyond 64-bit (use BigInteger).

## Complexity & trade-offs

| Operation | Time | Space |
|-----------|------|-------|
| Scans / bit ops | O(n) / O(1) per op | O(1) |

| Aspect | XOR Accumulation | HashMap Count | Sorting |
|--------|------------------|---------------|---------|
| Find single value | O(n), O(1) | O(n), O(n) | O(n log n) |
| Two singles | insufficient, partition by differing bit first | yes | yes, adjacent compare |
| Frequency of each | no | yes | yes |
| Pick when | exactly one unpaired, bit flags, subset masks | counts or multiple uniques | only order matters |

## Pitfalls

- In Java, `>>` keeps sign, `>>>` does not. Use `>>>` for unsigned right shift.
- `1 << n` overflows at `n=31` for `int`. Use `1L << n` if needed.
- XOR finds one single; two singles need partition by differing bit (find any set bit in XOR, partition by that bit).
- `n & (n-1)` drops lowest set bit; `n | (n-1)` sets trailing zeros; `n + 1 & ~n` isolates lowest zero.

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 191 | Easy |
| 136 | Easy |
| 260 | Medium |

## Interview Q&A

(Senior Depth)

**Q: Single Number II (LC 137) — explain the two-bit state machine (ones, twos).**
**A:** Each bit position independently tracks count mod 3. `ones` = bits seen 1 time mod 3; `twos` = bits seen 2 times mod 3. On new bit `x`: `ones = (ones ^ x) & ~twos` (toggle if not in twos); `twos = (twos ^ x) & ~ones` (toggle if not in new ones). After 3 occurrences, both clear. Final `ones` holds the single number's bits.

**Q: Two singles (LC 260) — how to partition by differing bit?**
**A:** XOR all → `xor = a ^ b` (a,b are the two singles). Find any set bit in `xor` (e.g., `diff = xor & -xor` isolates lowest set bit). This bit differs between a and b. Partition array into two groups by this bit: group 1 has a, group 2 has b. XOR each group → a and b. O(n) time, O(1) space.

**Q: Why does `n & (n-1) == 0` test power of two?**
**A:** Powers of two have exactly one bit set: `1000...0`. Subtracting 1 gives `0111...1`. AND is zero. For non-powers-of-two, at least two bits set → subtracting 1 doesn't clear the highest bit → AND non-zero. Edge case: n=0 gives true, so check `n > 0` first.

**Q: Java `>>` vs `>>>` — when does it matter?**
**A:** `>>` is arithmetic shift (sign-extends). `>>>` is logical shift (fills with zeros). For positive numbers, same. For negative: `-8 >> 1 = -4` (sign bit copied), `-8 >>> 1 = 2147483644` (zeros filled). Use `>>>` when treating int as unsigned bit pattern (e.g., hash codes, bit masks).

**Q: Subset enumeration via bitmask — when is it better than backtracking?**
**A:** Bitmask: simple iterative, no recursion, generates in natural binary order. Backtracking: allows pruning (skip branches early), generates in lexicographic order if sorted. For n ≤ 20 with no pruning, bitmask is simpler. For n > 20 or with pruning, backtracking wins.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Bit Manipulation? :: **A:** power of two, single number (XOR), count bits, subset enumeration, bitmask DP, Hamming distance #flashcard

#flashcard
**Q:** Time/space complexity of Bit Manipulation? :: **A:** Time: O(1) per operation, Space: O(1) #flashcard

#flashcard
**Q:** When do you NOT use Bit Manipulation? :: **A:** need arithmetic (use + - * /), readability matters (use clear logic) #flashcard

#flashcard
**Q:** Core Java 25 snippet for Bit Manipulation? :: **A:** `boolean isPowerOfTwo(int n){ return n>0 && (n&(n-1))==0; } int countBits(int n){ int c=0; while(n>0){ n&=n-1; c++; } return c; }` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- [[01_Array/04 - Frequency Counting|Frequency Counting]] (XOR vs HashMap for single number)
- [[07_Backtracking_DP/01 - Backtracking|Backtracking]] (subset generation alternative)
- [[Java/07_DSA/Array]]
