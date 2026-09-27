---
title: Top K Elements
pattern: 9
category: Coding Patterns/03_Stack_Heap
tags:
- pattern/heap
- pattern/stack/top-k
leetcode:
- 215
- 347
- 973
created: '2026-09-02'
completed: false
reviewed: ''
sr-due: ''
difficulty: Medium
source: https://blog.algomaster.io/p/20-dsa-patterns
problems-solved: []
problems-solved-dates: {}
excalidraw: ''
type: note
---


# Top K Elements

> Part of [[README|20 DSA Patterns]] • `Coding Patterns/03_Stack_Heap` • Pattern #9

## Intent
Find k largest/smallest/most frequent elements in O(n log k) time and O(k) space using a heap of size k — the streaming-friendly alternative to full sort when k << n.

## Why it Matters
- **Min-heap for k largest:** root = k-th largest (smallest among the chosen k). When heap size > k, evict root — keeps the k largest survivors.
- **Max-heap for k smallest:** symmetric.
- **Top k frequent:** hashmap for frequencies + min-heap on frequency.
- **Bucket sort alternative:** O(n) time when max frequency ≤ n — array of lists indexed by frequency.
- Senior signal: knowing *why* min-heap for k largest (evicting smallest of chosen k keeps the largest k) and when bucket sort beats heap (k large or full frequency ordering needed).

## Diagram
```mermaid
flowchart LR
  A["stream 3,2,1,5,6,4"] --> H["min-heap size k=2"]
  H --> P{"size > k?"}
  P -->|yes| Evict["poll smallest of the kept k"]
  Evict --> A
  P -->|no| A
  H --> R["top = kth largest = 5"]
```


## Problems

### 215. Kth Largest Element in an Array (Medium)
> [LeetCode 215](https://leetcode.com/problems/kth-largest-element-in-an-array/) • Tags: Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect

**Problem Statement:**

Given an integer array nums and an integer k, return the k^th^ largest element in the array.

Note that it is the k^th^ largest element in the sorted order, not the k^th^ distinct element.

Can you solve it without sorting?

**Examples:**

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

---

### 347. Top K Frequent Elements (Medium)
> [LeetCode 347](https://leetcode.com/problems/top-k-frequent-elements/) • Tags: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect

**Problem Statement:**

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

**Examples:**

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

---

### 973. K Closest Points to Origin (Medium)
> [LeetCode 973](https://leetcode.com/problems/k-closest-points-to-origin/) • Tags: Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect, K-D Tree

**Problem Statement:**

Given an array of points where points[i] = [x_i_, y_i_] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x_1_ - x_2_)^2^ + (y_1_ - y_2_)^2^).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

**Examples:**

Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

---


## Code / Example
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

## When to Use / When NOT
- **Use:** k largest/smallest/most frequent/closest; stream of data where k << n; online algorithms (heap processes elements one at a time).
- **NOT:** k ≈ n (just sort O(n log n)); need all elements sorted; static array with single query (quickselect O(n) average).

## Trade-offs
| Approach | Time | Space | When |
|----------|------|-------|------|
| Min-heap size k | O(n log k) | O(k) | k << n, streaming |
| Quickselect | O(n) avg, O(n²) worst | O(1) | single k-th query, mutable array |
| Bucket sort | O(n) | O(n) | top-k frequent, bounded frequencies |
| Full sort | O(n log n) | O(1) extra | k ≈ n, or need full ordering |

## Vs Table
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

## Interview Q&A (Senior Depth)

**Q: Why min-heap for k largest? Explain the eviction logic.**
**A:** We want to keep the k largest elements. A min-heap puts the *smallest* of the kept elements at the root. When a new element arrives, if it's larger than the root, it belongs in the top k — we push it and pop the root (the smallest of the previous k). If it's smaller than the root, it's not in the top k — discard. The heap always contains the k largest seen so far, with the k-th largest at the root.

**Q: Quickselect vs Heap for kth largest — when do you choose which?**
**A:** Quickselect: O(n) average, O(1) space, but O(n²) worst case (bad pivot), and modifies the array. Heap: O(n log k) guaranteed, O(k) space, non-destructive, streaming-friendly. In interviews: "Quickselect for single k-th query on mutable array when average case is acceptable; heap for streaming, multiple queries, or when worst-case matters."

**Q: Top K Frequent — heap vs bucket sort. Decision rule?**
**A:** Bucket sort O(n) time, O(n) space — wins when k is large (close to n) or you need the full frequency ordering. Heap O(n log k) — wins when k << n and you only need top k. If k = n/2, bucket sort is faster. If k = 3, heap uses less space and is simpler.

**Q: K Closest Points — why max-heap instead of min-heap?**
**A:** We want k *smallest* distances. Max-heap root = largest distance among kept k. When new point has smaller distance than root, it belongs in top k — push and pop root. Min-heap would need to keep all n points and pop k times (O(n + k log n)). Max-heap of size k is O(n log k).

## Related
- [[03_Stack_Heap/01 - Monotonic Stack|Monotonic Stack]] (different stack/heap pattern)
- [[07_Backtracking_DP/02 - Dynamic Programming|Dynamic Programming]] (knapsack variants use different DP)
- [[Java/07_DSA/Heap]] · [[Java/07_DSA/HashMap]]

---
*Category: Coding Patterns/03_Stack_Heap*
- [[Architect/10_System-Design-Interviews/NET-01-Load-Balancer.md|NET-01-Load-Balancer]] — Least connections = min heap
- [[Architect/10_System-Design-Interviews/INT-02-Twitter-Timeline.md|INT-02-Twitter-Timeline]] — Merge k sorted lists = heap
