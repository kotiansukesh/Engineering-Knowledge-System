---
title: "Segment Tree"
type: pattern
pattern: 24
domain: "Advanced Data Structure"
category: "Coding Patterns/09_Advanced"
advanced: true
mastery: learn
recognition_score: 0
difficulty: "Hard"
leetcode: [307, 308, 218, 303]
created: "2026-09-29"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - advanced-data-structure
---

# Segment Tree

> Advanced pattern · Advanced Data Structure

## Recognition

- Range queries plus updates
- Need logarithmic query and update time
- Operation can be combined from child segments

### Strong signals
- Range queries plus updates
- Need logarithmic query and update time

### Do not infer it from
- A keyword alone
- A familiar example without checking constraints

## Invariant

> Every tree node stores the aggregate for exactly its represented range; parent state is the combination of its children.

## Mental model

Maintain the smallest state that completely describes the part of the search space still relevant to the answer.

## Core implementation

```java
// Segment Tree for Range Sum + Point Update — LC 307
class NumArray {
    int[] tree;
    int n;

    public NumArray(int[] nums) {
        n = nums.length;
        tree = new int[4 * n];
        build(nums, 1, 0, n - 1);
    }

    void build(int[] nums, int node, int l, int r) {
        if (l == r) {
            tree[node] = nums[l];
            return;
        }
        int mid = (l + r) / 2;
        build(nums, node * 2, l, mid);
        build(nums, node * 2 + 1, mid + 1, r);
        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    public void update(int index, int val) {
        update(1, 0, n - 1, index, val);
    }

    void update(int node, int l, int r, int idx, int val) {
        if (l == r) {
            tree[node] = val;
            return;
        }
        int mid = (l + r) / 2;
        if (idx <= mid) update(node * 2, l, mid, idx, val);
        else update(node * 2 + 1, mid + 1, r, idx, val);
        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    public int sumRange(int left, int right) {
        return query(1, 0, n - 1, left, right);
    }

    int query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return 0; // no overlap
        if (ql <= l && r <= qr) return tree[node]; // full overlap
        int mid = (l + r) / 2;
        return query(node * 2, l, mid, ql, qr) + query(node * 2 + 1, mid + 1, r, ql, qr);
    }
}

// Generic Segment Tree (min, max, sum, gcd...)
class SegTree {
    int[] tree;
    int n;
    java.util.function.IntBinaryOperator op;
    int identity;

    SegTree(int[] arr, java.util.function.IntBinaryOperator op, int identity) {
        this.op = op;
        this.identity = identity;
        n = arr.length;
        tree = new int[4 * n];
        build(arr, 1, 0, n - 1);
    }

    void build(int[] arr, int node, int l, int r) {
        if (l == r) { tree[node] = arr[l]; return; }
        int mid = (l + r) / 2;
        build(arr, node * 2, l, mid);
        build(arr, node * 2 + 1, mid + 1, r);
        tree[node] = op.applyAsInt(tree[node * 2], tree[node * 2 + 1]);
    }

    void update(int idx, int val) { update(1, 0, n - 1, idx, val); }
    void update(int node, int l, int r, int idx, int val) {
        if (l == r) { tree[node] = val; return; }
        int mid = (l + r) / 2;
        if (idx <= mid) update(node * 2, l, mid, idx, val);
        else update(node * 2 + 1, mid + 1, r, idx, val);
        tree[node] = op.applyAsInt(tree[node * 2], tree[node * 2 + 1]);
    }

    int query(int ql, int qr) { return query(1, 0, n - 1, ql, qr); }
    int query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return identity;
        if (ql <= l && r <= qr) return tree[node];
        int mid = (l + r) / 2;
        return op.applyAsInt(
            query(node * 2, l, mid, ql, qr),
            query(node * 2 + 1, mid + 1, r, ql, qr)
        );
    }
}

// Usage examples:
var sumTree = new SegTree(nums, (a, b) -> a + b, 0);
var minTree = new SegTree(nums, Math::min, Integer.MAX_VALUE);
var maxTree = new SegTree(nums, Math::max, Integer.MIN_VALUE);
var gcdTree = new SegTree(nums, (a, b) -> {
    while (b != 0) { int t = a % b; a = b; b = t; }
    return a;
}, 0);
```

## Variants

Start with the core implementation. Introduce a variant only when the required state or proof changes.

## When to use
- range query + point update interleaved; range min/max/gcd; non-invertible operations; 2D segment tree (matrix).

## When NOT to use
- static array (use Prefix Sum / Sparse Table); prefix sum only (use Fenwick/BIT — simpler); only count queries (use BIT).

## Complexity & trade-offs

| Structure | Query | Update | Operations | Space |
|-----------|-------|--------|------------|-------|
| Segment Tree | O(log n) | O(log n) | Any associative | O(4n) |
| Fenwick (BIT) | O(log n) | O(log n) | Invertible only (sum, xor) | O(n) |
| Prefix Sum | O(1) | O(n) | Sum only | O(n) |
| Sparse Table | O(1) | N/A (static) | Idempotent (min/max/gcd) | O(n log n) |

| Aspect | Segment Tree | Fenwick Tree | Sparse Table | Prefix Sum |
|--------|--------------|--------------|--------------|------------|
| Range query | Yes | Prefix only | Yes | Yes |
| Point update | Yes | Yes | No | No |
| Range update | With lazy | Complex | No | No |
| Operations | Any associative | Invertible only | Idempotent | Sum only |
| Code complexity | Medium | Low | Low | Trivial |
| Pick when | General range query+update | Prefix sum/xor | Static min/max/gcd | Static sum only |

## Pitfalls

- **Tree size `4*n`** — safe upper bound for any n. Exact bound is `2 * 2^ceil(log2(n)) - 1` but `4*n` is simpler and safe.
- **1-indexed nodes** — root = 1, left = `2*node`, right = `2*node+1`. Using 0-indexed nodes is error-prone.
- **Identity element** — for sum it's 0, for min it's `Integer.MAX_VALUE`, for max it's `Integer.MIN_VALUE`, for gcd it's 0. Wrong identity = wrong results.
- **Overlap logic:** three cases — no overlap (return identity), full overlap (return node), partial overlap (recurse both).
- **Lazy propagation** for range updates: store pending update in `lazy[node]`, push down before recursing. Required for "add v to range [l,r]" + range query.

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 307 | Medium |
| 308 | Hard |
| 218 | Hard |
| 303 | Easy |

## Interview Q&A

(Senior Depth)

**Q: Why `4*n` size for the tree array?**
A: A segment tree is a full binary tree. For n leaves, the next power of 2 is `2^ceil(log2(n))`. Total nodes = `2 * 2^ceil(log2(n)) - 1`. Worst case when n = 2^k + 1, `ceil(log2(n)) = k+1`, so `2 * 2^(k+1) - 1 = 4 * 2^k - 1 < 4 * n`. `4*n` is a safe, simple upper bound.

**Q: Segment Tree vs Fenwick Tree — when do you choose which?**
A: Fenwick: only prefix queries (sum, xor, product) with point updates. Simpler code, smaller constant, O(n) space. Segment Tree: arbitrary range queries (min, max, gcd, any associative op), or when you need range updates with lazy propagation. If the operation is invertible (has inverse) and you only need prefix queries, BIT wins. Otherwise segment tree.

**Q: How does lazy propagation work for range add + range sum?**
A: Each node stores `lazy` = pending addition for its entire segment. On query/update, if `lazy[node] != 0`, apply it: `tree[node] += lazy[node] * (r-l+1)`, push to children `lazy[child] += lazy[node]`, then clear `lazy[node] = 0`. This defers work until needed. Time remains O(log n) because each level is visited at most once per operation.

**Q: Sparse Table vs Segment Tree for range min/max?**
A: Sparse Table: O(1) query, O(n log n) build, **static only** (no updates). Segment Tree: O(log n) query, O(n) build, **supports updates**. If array is static and you need many queries, Sparse Table is faster. If updates are interleaved, Segment Tree is the only choice.

**Q: 2D Segment Tree vs 2D BIT?**
A: 2D BIT: `O(log^2 n)` for prefix sum + point update. Simpler. 2D Segment Tree: `O(log^2 n)` for range query + point update. Can handle range min/max. 2D Segment Tree with lazy is complex — often 1D segment tree of 1D segment trees (tree of trees). For LeetCode 308, 2D BIT is preferred for simplicity.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Segment Tree? :: **A:** range query + point update, range min/max/sum, range assignment, lazy propagation #flashcard

#flashcard
**Q:** Time/space complexity of Segment Tree? :: **A:** Time: O(log n) query/update, Space: O(4n) array or O(n) nodes #flashcard

#flashcard
**Q:** When do you NOT use Segment Tree? :: **A:** static array (use prefix sum/sparse table O(1) query), only point queries (use array) #flashcard

#flashcard
**Q:** Core Java 25 snippet for Segment Tree? :: **A:** `class SegTree{ int n; long[] t; SegTree(int[] a){ n=a.length; t=new long[4*n]; build(1,0,n-1,a); } void build(int v,int tl,int tr,int[] a){ if(tl==tr) t[v]=a[tl]; else{ int tm=(tl+tr)/2; build(v*2,tl,tm,a); build(v*2+1,tm+1,tr,a); t[v]=t[v*2]+t[v*2+1]; } } }` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- [[01_Array/01 - Prefix Sum|Prefix Sum]] (static range sum)
- [[09_Advanced/02 - Kadane's Algorithm|Kadane's Algorithm]] (max subarray = segment tree with custom node)
- [[Java/07_DSA/Tree]] (tree structure)
