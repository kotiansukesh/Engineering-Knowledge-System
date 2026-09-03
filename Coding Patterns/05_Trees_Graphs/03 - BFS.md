---
title: "BFS"
pattern: 14
category: Trees
tags: [pattern/bfs, graph]
leetcode: [102, 107, 127]
created: 2026-09-02
source: "https://blog.algomaster.io/p/20-dsa-patterns"
---

# Breadth first search

> Part of [[README|20 DSA Patterns]], Pattern #14

## Definition

Explore level by level using a queue. Each pass processes one depth. Track level size to know when a layer ends. Example: `[1,2,3]` level order → queue starts `[1]` → process 1, queue `[2,3]` → process 2 and 3, done → `[[1],[2,3]]`.

For graphs, a visited set avoids revisiting.

## When to use

- Shortest path in unweighted graph, level order, word ladder, rotting oranges, minimum steps

## Complexity

| time | space |
|---|---|
| O(V+E) | O(V) for queue and visited |

## Java example

```java
record TreeNode(int val, TreeNode left, TreeNode right) {}

java.util.List<java.util.List<Integer>> levelOrder(TreeNode root) {
    var res = new java.util.ArrayList<java.util.List<Integer>>();
    if (root == null) return res;
    var q = new java.util.ArrayDeque<TreeNode>();
    q.offer(root);
    while (!q.isEmpty()) {
        int sz = q.size();
        var level = new java.util.ArrayList<Integer>();
        for (var i = 0; i < sz; i++) {
            var cur = q.poll();
            level.add(cur.val());
            if (cur.left() != null) q.offer(cur.left());
            if (cur.right() != null) q.offer(cur.right());
        }
        res.add(level);
    }
    return res;
}

// Unweighted shortest path, same loop, count steps instead of collecting levels
```

Java 25 `ArrayDeque` is the queue. `var` keeps declarations short.

## Pitfalls

- Save `q.size()` at start of each level. Do not read it inside the inner loop or the level boundary shifts.
- Mark visited when you enqueue, not when you dequeue, or you enqueue the same node many times.

## Practice

- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
- [127. Word Ladder](https://leetcode.com/problems/word-ladder/)

## Related DSA notes

- [[Java/07_DSA/Trees]]
- [[Java/07_DSA/Graph]]
