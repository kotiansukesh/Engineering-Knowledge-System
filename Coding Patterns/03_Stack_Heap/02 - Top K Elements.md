---
title: "Top K Elements"
pattern: 9
category: Heap
tags: [pattern/heap, top-k]
leetcode: [215, 347, 973]
created: 2026-09-02
source: "https://blog.algomaster.io/p/20-dsa-patterns"
---

# Top k elements

> Part of [[README|20 DSA Patterns]], Pattern #9

## Definition

Keep a heap of size `k` instead of sorting the whole array. For k largest, use a min-heap of size k. The top is the kth largest and the smallest among the chosen k. For k smallest, use a max-heap. For k frequent, heap by frequency or use bucket sort.

Example: `nums=[3,2,1,5,6,4]`, `k=2` → push through min-heap size 2 → heap `[5,6]` → top `5`.

## When to use

- k largest, smallest, most frequent, closest, or top k pairs
- Stream of data where `k` is much smaller than `n`

## Complexity

| time | space |
|---|---|
| O(n log k) with heap | O(k) |
| O(n) with bucket sort for frequencies | O(n) |

## Java example

```java
// Kth largest, LC 215
int findKthLargest(int[] nums, int k) {
    var minHeap = new java.util.PriorityQueue<Integer>();
    for (var x : nums) {
        minHeap.offer(x);
        if (minHeap.size() > k) minHeap.poll();
    }
    return minHeap.peek();
}

// Top k frequent, LC 347
int[] topKFrequent(int[] nums, int k) {
    var freq = new java.util.HashMap<Integer,Integer>();
    for (var x : nums) freq.put(x, freq.getOrDefault(x, 0) + 1);
    var heap = new java.util.PriorityQueue<Integer>((a,b) -> freq.get(a) - freq.get(b));
    for (var key : freq.keySet()) {
        heap.offer(key);
        if (heap.size() > k) heap.poll();
    }
    var res = new int[k];
    for (var i = 0; i < k; i++) res[i] = heap.poll();
    return res;
}
```

Record for heap entries in Java 25: `record Entry(int num, int freq){}` with comparator on `freq`.

## Pitfalls

- Min-heap for k largest is counterintuitive. Get it straight before coding.
- For kth largest you can also use quickselect O(n) average if asked to optimize.
- Heap of ints vs heap of entries, pick the right one for comparator.

## Practice

- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

## Related DSA notes

- [[Java/07_DSA/Heap]]
