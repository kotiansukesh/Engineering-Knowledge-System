---
title: "Frequency Counting"
type: pattern
pattern: 4
domain: "Array / String"
category: "Coding Patterns/01_Array"
advanced: false
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
leetcode: [242, 49, 347]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - pattern/array-string
---

# Frequency Counting

> Pattern #4 · Array / String

## Recognition

- Counts, duplicates, anagrams, grouping, equivalence
- Need O(1)-average membership or frequency lookup
- A canonical key can represent a group

### Strong signals
- Counts, duplicates, anagrams, grouping, equivalence
- Need O(1)-average membership or frequency lookup

### Do not infer it from
- A keyword alone
- A familiar LeetCode example without checking the constraints

## Invariant

> The frequency structure exactly represents the relevant prefix or current window of input.

## Mental model

Convert repeated comparison into constant-time average lookup by maintaining counts or a canonical representation. The important decision is what the key must encode.

## Core implementation

```java
// General case with HashMap
var freq = new java.util.HashMap<Integer, Integer>();
for (var x : nums) freq.put(x, freq.getOrDefault(x, 0) + 1);

// Valid Anagram — LC 242 (bounded alphabet: int[26])
boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) return false;
    int[] freq = new int[26];
    for (char c : s.toCharArray()) freq[c - 'a']++;
    for (char c : t.toCharArray()) if (--freq[c - 'a'] < 0) return false;
    return true;
}

// Group Anagrams — LC 49 (frequency array as key)
java.util.List<java.util.List<String>> groupAnagrams(String[] strs) {
    var map = new java.util.HashMap<String, java.util.List<String>>();
    for (var s : strs) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) freq[c - 'a']++;
        String key = java.util.Arrays.toString(freq); // e.g., "[3,0,1,...]"
        map.computeIfAbsent(key, k -> new java.util.ArrayList<>()).add(s);
    }
    return new java.util.ArrayList<>(map.values());
}

// Top K Frequent Elements — LC 347 (frequency + heap)
int[] topKFrequent(int[] nums, int k) {
    var freq = new java.util.HashMap<Integer, Integer>();
    for (var x : nums) freq.put(x, freq.getOrDefault(x, 0) + 1);
    var heap = new java.util.PriorityQueue<Integer>((a, b) -> freq.get(a) - freq.get(b));
    for (var key : freq.keySet()) {
        heap.offer(key);
        if (heap.size() > k) heap.poll();
    }
    int[] res = new int[k];
    for (int i = 0; i < k; i++) res[i] = heap.poll();
    return res;
}
```

## Variants

Use the implementation above as the base case. Extend it only after the invariant remains explicit.

## When to use
- anagram, duplicate detection, grouping by frequency, "how many appear k times", top-k frequent.

## When NOT to use
- only order matters (use sort); range sum queries (use prefix sum); streaming with bounded memory (use Count-Min Sketch / reservoir sampling).

## Complexity & trade-offs

| Case | Time | Space |
|------|------|-------|
| HashMap (general) | O(n) | O(n) distinct values |
| Fixed alphabet (26/128) | O(n) | O(1) — array is constant size |

| Aspect | Frequency Map | Sorting | Prefix Sum |
|--------|---------------|---------|------------|
| Anagram / duplicate | O(n) | O(n log n) | N/A |
| Space | O(domain) | O(1) extra | O(n) |
| Bounded alphabet | `int[26]`, effectively O(1) | no benefit | N/A |
| Pick when | counts matter, values are the question | only order matters | range sums |

## Pitfalls

- Use `getOrDefault(key, 0)` to avoid NPE on missing keys.
- For anagram, decrement and check `< 0` immediately — early exit, no second pass needed.
- Group anagrams: key can be sorted string (`Arrays.sort(chars)`) or frequency array (`Arrays.toString(freq)`). Frequency array is O(L) vs O(L log L) for sort.
- For top-k frequent, bucket sort O(n) is possible when max frequency ≤ n (array of lists indexed by frequency).

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 242 | Valid Anagram | Easy |
| 49 | Group Anagrams | Medium |
| 347 | Top K Frequent Elements | Medium |

## Interview Q&A

(Senior Depth)

**Q: Valid Anagram — why `int[26]` over HashMap? What's the actual performance difference?**
**A:** `int[26]` avoids hashing overhead, has better cache locality, no object allocation per entry. For short strings the difference is negligible; for millions of short strings (e.g., dictionary processing), array is measurably faster. HashMap is the general case — use it when alphabet is large or unknown (Unicode). Both O(n) time, but constant factors differ.

**Q: Group Anagrams — frequency array key vs sorted string key. Which do you pick and why?**
**A:** Frequency array `int[26]` → `Arrays.toString(freq)` is O(L) to build + O(26) to convert to string. Sorted string is O(L log L) to sort. For long strings, frequency array wins asymptotically. For short strings (L < 10), sort overhead is tiny and sorted string is more readable. In interviews, mention both and the tradeoff.

**Q: Top K Frequent — heap vs bucket sort. When does bucket sort win?**
**A:** Bucket sort: `List<Integer>[] buckets = new List[n+1]`, bucket[freq].add(num). Iterate buckets from n down to 1, collect until k. Time O(n), space O(n). Heap is O(n log k). Bucket sort wins when k is large (close to n) or when you need *all* frequencies sorted. Heap wins when k << n and you only need top k. Interview answer: "Heap for k << n, bucket sort when k is large or you need full ordering."

**Q: Frequency counting with negative numbers or large range — what changes?**
**A:** `int[]` array no longer works (negative index, huge range). Must use HashMap. Time stays O(n), space becomes O(distinct values). No asymptotic change, just constant factors.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Frequency Counting? :: **A:** anagrams, character counts, frequency of elements, top K frequent, find duplicate #flashcard

#flashcard
**Q:** Time/space complexity of Frequency Counting? :: **A:** Time: O(n) build + O(1) lookup, Space: O(Σ) alphabet or O(n) distinct #flashcard

#flashcard
**Q:** When do you NOT use Frequency Counting? :: **A:** need order information (use array/list), range frequency queries (use Mo's algorithm) #flashcard

#flashcard
**Q:** Core Java 25 snippet for Frequency Counting? :: **A:** `int[] cnt = new int[26]; for(char c:s.toCharArray()) cnt[c-'a']++; // or Map<Integer,Integer> for general` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- [[01_Array/01 - Prefix Sum|Prefix Sum]] (hashmap on prefix sums for subarray sum = k)
- [[01_Array/03 - Sliding Window|Sliding Window]] (frequency map inside variable window)
- [[03_Stack_Heap/02 - Top K Elements|Top K Elements]] (frequency + heap)
- [[Java/07_DSA/Array]] · [[Java/07_DSA/HashMap]]
