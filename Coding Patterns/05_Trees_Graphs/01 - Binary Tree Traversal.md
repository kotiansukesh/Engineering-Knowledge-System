---
title: "Binary Tree Traversal"
type: pattern
pattern: 11
domain: "Tree"
category: "Coding Patterns/05_Trees_Graphs"
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
leetcode: [94, 102, 103, 104]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - tree
---

# Binary Tree Traversal

> Pattern #11 · Tree

## Recognition

- Systematic visitation of every tree node
- Output depends on preorder, inorder, postorder, or level order
- Tree structure gives recursive subproblems

### Strong signals
- Systematic visitation of every tree node
- Output depends on preorder, inorder, postorder, or level order

### Do not infer it from
- A keyword alone
- A familiar example without checking constraints

## Invariant

> Every node is visited according to the selected traversal ordering exactly once.

## Mental model

This pattern reduces the search space by maintaining a compact state that represents all information needed for the next decision.

## Core implementation

```java
record TreeNode(int val, TreeNode left, TreeNode right) {}

void preorder(TreeNode r, java.util.List<Integer> out) {
    if (r == null) return;
    out.add(r.val());
    preorder(r.left(), out);
    preorder(r.right(), out);
}

void inorder(TreeNode r, java.util.List<Integer> out) {
    if (r == null) return;
    inorder(r.left(), out);
    out.add(r.val());
    inorder(r.right(), out);
}

void postorder(TreeNode r, java.util.List<Integer> out) {
    if (r == null) return;
    postorder(r.left(), out);
    postorder(r.right(), out);
    out.add(r.val());
}

// Iterative inorder with stack
java.util.List<Integer> inorderIter(TreeNode root) {
    var res = new java.util.ArrayList<Integer>();
    var st = new java.util.ArrayDeque<TreeNode>();
    var cur = root;
    while (cur != null || !st.isEmpty()) {
        while (cur != null) { st.push(cur); cur = cur.left(); }
        cur = st.pop();
        res.add(cur.val());
        cur = cur.right();
    }
    return res;
}

// Morris Inorder — O(1) space (modifies tree temporarily)
java.util.List<Integer> morrisInorder(TreeNode root) {
    var res = new java.util.ArrayList<Integer>();
    TreeNode cur = root;
    while (cur != null) {
        if (cur.left() == null) {
            res.add(cur.val());
            cur = cur.right();
        } else {
            TreeNode pre = cur.left();
            while (pre.right() != null && pre.right() != cur) pre = pre.right();
            if (pre.right() == null) {
                // Thread to cur
                // Note: record is immutable, use mutable class for Morris
                cur = cur.left();
            } else {
                // Thread exists, restore
                pre.right = null;
                res.add(cur.val());
                cur = cur.right();
            }
        }
    }
    return res;
}
```

## Variants

Start with the core implementation. Introduce a variant only when the problem changes the invariant or required state.

## When to use
- visit every node in fixed order; serialize tree; operate on BST (inorder = sorted); delete tree (postorder).

## When NOT to use
- level-order (use BFS); path existence / shortest path (use BFS/DFS); Morris only for inorder.

## Complexity & trade-offs

| Approach | Time | Space | Orders |
|----------|------|-------|--------|
| Recursive | O(n) | O(h) call stack (O(n) worst) | pre/in/post |
| Iterative stack | O(n) | O(h) explicit | pre/in/post (post awkward) |
| Morris | O(n) | O(1) | inorder only (mutates tree temporarily) |

| Aspect | DFS Recursion | Iterative Stack | Morris Traversal | BFS Level Order |
|--------|---------------|-----------------|------------------|-----------------|
| Space | O(h) call stack | O(h) explicit | O(1) | O(w) queue (max width) |
| Orders | pre/in/post | pre/in/post (post tricky) | inorder only | breadth |
| Mutates tree | No | No | Temporarily, restored | No |
| Pick when | clarity, balanced tree | deep tree, stack overflow risk | O(1) space required | level-by-level processing |

## Pitfalls

- Null check **first** in every recursive call.
- Iterative inorder: inner `while` pushes all left nodes *before* popping — missing this is the #1 bug.
- Postorder iterative is trickiest — easiest is two stacks or reversed modified preorder (root, right, left) then reverse.
- Morris traversal requires mutable nodes (Java `record` is immutable — use `class TreeNode` with `left`/`right` fields).

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 94 | Easy |
| 102 | Medium |
| 103 | Medium |
| 104 | Easy |

## Interview Q&A

(Senior Depth)

**Q: Why does iterative inorder need the inner `while (cur != null)` loop?**
**A:** It simulates the recursive call stack. Recursion goes left as deep as possible before returning. The inner `while` pushes the entire left spine onto the stack, then we pop, visit, and go right. Without the inner loop, you'd only push one left child per iteration, breaking the depth-first order.

**Q: Morris traversal — how does it achieve O(1) space?**
**A:** It uses the tree's own null right pointers as "threads" to remember where to return after visiting the left subtree. When we go left, we find the rightmost node of the left subtree (predecessor) and thread its right pointer to the current node. After visiting the left subtree, we follow the thread back, remove it, and go right. No stack needed — the tree *is* the stack.

**Q: Postorder iterative — why is it harder than preorder/inorder?**
**A:** In preorder/inorder, the node is processed *before* or *between* children, so the stack naturally holds the parent while we process children. In postorder, the node is processed *after* both children, but the stack only gives us the parent *after* children are done. The two-stack trick: push root to stack1, pop to stack2, push left then right to stack1 — stack2 ends up with postorder (reverse of root-right-left).

**Q: BST validation — why is inorder traversal the right approach?**
**A:** BST property: left < root < right. Inorder visits left, then root, then right → produces strictly increasing sequence for valid BST. Check `prev < curr` during inorder traversal. O(n) time, O(h) space. Alternative: pass min/max bounds recursively (also O(n), O(h)).

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Binary Tree Traversal? :: **A:** preorder/inorder/postorder/level-order, tree serialization, path sum, BST validation #flashcard

#flashcard
**Q:** Time/space complexity of Binary Tree Traversal? :: **A:** Time: O(n) visit each node once, Space: O(h) recursion / O(w) queue #flashcard

#flashcard
**Q:** When do you NOT use Binary Tree Traversal? :: **A:** only need height/count (single pass no traversal order needed) #flashcard

#flashcard
**Q:** Core Java 25 snippet for Binary Tree Traversal? :: **A:** `void dfs(TreeNode n){ if(n==null) return; process(n.val); dfs(n.left); dfs(n.right); } // iterative: stack.push(root);` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- [[05_Trees_Graphs/02 - DFS|DFS]] (generalizes to graphs)
- [[05_Trees_Graphs/03 - BFS|BFS]] (level order)
- [[Java/07_DSA/Trees]]
