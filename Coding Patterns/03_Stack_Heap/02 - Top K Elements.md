---
title: "Top K Elements"
type: pattern
pattern: 8
domain: "Heap"
category: "Coding Patterns/03_Stack_Heap"
advanced: false
mastery: learn
recognition_score: 0
difficulty: "Medium"
leetcode: [215, 347, 378, 973]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - heap
---

# Top K Elements

> Pattern #8 · Heap

## Recognition

- Top K or kth largest/smallest
- Maintain only the best K candidates
- Streaming or partial-order problems

### Strong signals
- Top K or kth largest/smallest
- Maintain only the best K candidates

### Do not infer it from
- A keyword alone
- A familiar example without checking constraints

## Invariant

> The heap contains the K candidates that can still affect the final answer.

## Mental model

This pattern reduces the search space by maintaining a compact state that represents all information needed for the next decision.

## Core implementation

```java
// Kth Largest Element — LC 215
int findKthLargest(int[] nums, int k) {
    var minHeap = new java.util.PriorityQueue<Integer>();
    for (int x : nums) {
        minHeap.offer(x);
        if (minHeap.size() > k) minHeap.poll();
    }
    return minHeap.peek();
}

// Top K Frequent — LC 347
int[] topKFrequent(int[] nums, int k) {
    var freq = new java.util.HashMap<Integer, Integer>();
    for (int x : nums) freq.put(x, freq.getOrDefault(x, 0) + 1);
    var heap = new java.util.PriorityQueue<Integer>((a, b) -> freq.get(a) - freq.get(b));
    for (int key : freq.keySet()) {
        heap.offer(key);
        if (heap.size() > k) heap.poll();
    }
    int[] res = new int[k];
    for (int i = 0; i < k; i++) res[i] = heap.poll();
    return res;
}

// K Closest Points to Origin — LC 973
int[][] kClosest(int[][] points, int k) {
    var maxHeap = new java.util.PriorityQueue<int[]>((a, b) -> 
        Integer.compare(b[0]*b[0] + b[1]*b[1], a[0]*a[0] + a[1]*a[1]));
    for (int[] p : points) {
        maxHeap.offer(p);
        if (maxHeap.size() > k) maxHeap.poll();
    }
    int[][] res = new int[k][2];
    for (int i = 0; i < k; i++) res[i] = maxHeap.poll();
    return res;
}

// Bucket sort O(n) for top-k frequent (when k large or full ordering needed)
int[] topKFrequentBucket(int[] nums, int k) {
    var freq = new java.util.HashMap<Integer, Integer>();
    for (int x : nums) freq.put(x, freq.getOrDefault(x, 0) + 1);
    var buckets = new java.util.ArrayList<java.util.List<Integer>>(nums.length + 1);
    for (int i = 0; i <= nums.length; i++) buckets.add(new java.util.ArrayList<>());
    for (var e : freq.entrySet()) buckets.get(e.getValue()).add(e.getKey());
    int[] res = new int[k];
    int idx = 0;
    for (int f = nums.length; f >= 0 && idx < k; f--)
        for (int x : buckets.get(f)) if (idx < k) res[idx++] = x;
    return res;
}
```

## Variants

Start with the core implementation. Introduce a variant only when the problem changes the invariant or required state.

## When to use
- k largest/smallest/most frequent/closest; stream of data where k << n; online algorithms (heap processes elements one at a time).

## When NOT to use
- k ≈ n (just sort O(n log n)); need all elements sorted; static array with single query (quickselect O(n) average).

## Complexity & trade-offs

| Approach | Time | Space | When |
|----------|------|-------|------|
| Min-heap size k | O(n log k) | O(k) | k << n, streaming |
| Quickselect | O(n) avg, O(n²) worst | O(1) | single k-th query, mutable array |
| Bucket sort | O(n) | O(n) | top-k frequent, bounded frequencies |
| Full sort | O(n log n) | O(1) extra | k ≈ n, or need full ordering |

| Aspect | Heap size k | Full Sort | Quickselect | Bucket Sort |
|--------|-------------|-----------|-------------|-------------|
| Time | O(n log k) | O(n log n) | O(n) avg | O(n) |
| Space | O(k) | O(1) extra | O(1) extra | O(n) |
| Streaming | Yes | No | No | No |
| Pick when | k << n, or data streams | k ≈ n | O(n) wanted, array indexable | top-k frequent, domain bounded |

## Pitfalls

- **Min-heap for k largest is counterintuitive** — get it straight before coding. Root = smallest of the kept k = k-th largest.
- For kth largest you can also use quickselect O(n) average if asked to optimize — but heap is more robust (no worst-case O(n²)).
- Heap of `int` vs heap of entries (record with value + frequency) — pick the right one for comparator.
- Bucket sort only works when max frequency is bounded (e.g., ≤ n for array length n). For unbounded frequencies, use heap.

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 215 | Medium |
| 347 | Medium |
| 378 | Medium |
| 973 | Medium |

## Interview Q&A

(Senior Depth)

**Q: Why min-heap for k largest? Explain the eviction logic.**
**A:** We want to keep the k largest elements. A min-heap puts the *smallest* of the kept elements at the root. When a new element arrives, if it's larger than the root, it belongs in the top k — we push it and pop the root (the smallest of the previous k). If it's smaller than the root, it's not in the top k — discard. The heap always contains the k largest seen so far, with the k-th largest at the root.

**Q: Quickselect vs Heap for kth largest — when do you choose which?**
**A:** Quickselect: O(n) average, O(1) space, but O(n²) worst case (bad pivot), and modifies the array. Heap: O(n log k) guaranteed, O(k) space, non-destructive, streaming-friendly. In interviews: "Quickselect for single k-th query on mutable array when average case is acceptable; heap for streaming, multiple queries, or when worst-case matters."

**Q: Top K Frequent — heap vs bucket sort. Decision rule?**
**A:** Bucket sort O(n) time, O(n) space — wins when k is large (close to n) or you need the full frequency ordering. Heap O(n log k) — wins when k << n and you only need top k. If k = n/2, bucket sort is faster. If k = 3, heap uses less space and is simpler.

**Q: K Closest Points — why max-heap instead of min-heap?**
**A:** We want k *smallest* distances. Max-heap root = largest distance among kept k. When new point has smaller distance than root, it belongs in top k — push and pop root. Min-heap would need to keep all n points and pop k times (O(n + k log n)). Max-heap of size k is O(n log k).

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Top K Elements? :: **A:** K largest/smallest, K closest, merge K sorted lists, top K frequent elements #flashcard

#flashcard
**Q:** Time/space complexity of Top K Elements? :: **A:** Time: O(n log k) heap / O(n) quickselect avg, Space: O(k) heap / O(1) quickselect #flashcard

#flashcard
**Q:** When do you NOT use Top K Elements? :: **A:** K ≈ n (just sort), need all sorted (use sort O(n log n)) #flashcard

#flashcard
**Q:** Core Java 25 snippet for Top K Elements? :: **A:** `PriorityQueue<Integer> minHeap=new PriorityQueue<>(); for(int x:nums){ minHeap.offer(x); if(minHeap.size()>k) minHeap.poll(); }` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- [[03_Stack_Heap/01 - Monotonic Stack|Monotonic Stack]] (different stack/heap pattern)
- [[07_Backtracking_DP/02 - Dynamic Programming|Dynamic Programming]] (knapsack variants use different DP)
- [[Java/07_DSA/Heap]] · [[Java/07_DSA/HashMap]]
