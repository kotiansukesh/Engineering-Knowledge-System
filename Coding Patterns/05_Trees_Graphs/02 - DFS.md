---
title: "DFS"
type: pattern
pattern: 12
domain: "Tree / Graph"
category: "Coding Patterns/05_Trees_Graphs"
advanced: false
mastery: learn
recognition_score: 0
difficulty: "Medium"
leetcode: [104, 110, 112, 129]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - tree-graph
---

# DFS

> Pattern #12 · Tree / Graph

## Recognition

- Explore complete paths or connected regions
- Recursive state naturally represents the current subproblem
- Need postorder aggregation or exhaustive reachability

### Strong signals
- Explore complete paths or connected regions
- Recursive state naturally represents the current subproblem

### Do not infer it from
- A keyword alone
- A familiar example without checking constraints

## Invariant

> The recursive state completely represents the current subproblem; visited state prevents invalid revisits when the graph permits cycles.

## Mental model

This pattern reduces the search space by maintaining a compact state that represents all information needed for the next decision.

## Core implementation

```java
record TreeNode(int val, TreeNode left, TreeNode right) {}

// Binary tree: all root-to-leaf paths
void dfs(TreeNode node, String path, java.util.List<String> res) {
    if (node == null) return;
    path += node.val();
    if (node.left() == null && node.right() == null) res.add(path);
    else {
        dfs(node.left(), path + "->", res);
        dfs(node.right(), path + "->", res);
    }
}

// Graph: Clone Graph — LC 133
class Node { int val; java.util.List<Node> neighbors; Node(int v){ val=v; neighbors=new java.util.ArrayList<>(); } }

java.util.Map<Node, Node> seen = new java.util.HashMap<>();
Node cloneGraph(Node node) {
    if (node == null) return null;
    if (seen.containsKey(node)) return seen.get(node);
    var copy = new Node(node.val);
    seen.put(node, copy);
    for (var nb : node.neighbors) copy.neighbors.add(cloneGraph(nb));
    return copy;
}

// Grid DFS: Number of Islands — LC 200
int numIslands(char[][] grid) {
    if (grid.length == 0) return 0;
    int m = grid.length, n = grid[0].length, count = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            if (grid[i][j] == '1') { dfsGrid(grid, i, j); count++; }
    return count;
}
void dfsGrid(char[][] g, int r, int c) {
    if (r < 0 || r >= g.length || c < 0 || c >= g[0].length || g[r][c] != '1') return;
    g[r][c] = '0'; // mark visited by sinking
    dfsGrid(g, r+1, c);
    dfsGrid(g, r-1, c);
    dfsGrid(g, r, c+1);
    dfsGrid(g, r, c-1);
}
```

## Variants

Start with the core implementation. Introduce a variant only when the problem changes the invariant or required state.

## When to use
- explore all paths; count connected components; topological sort; clone graph; path existence; "all solutions" problems.

## When NOT to use
- shortest path in unweighted graph (use BFS); level-order traversal (use BFS); very deep graphs (stack overflow — use iterative stack).

## Complexity & trade-offs

| Scenario | Time | Space |
|----------|------|-------|
| Tree | O(n) | O(h) recursion stack |
| Graph | O(V+E) | O(V) visited + recursion stack |

| Aspect | DFS | BFS | Union Find |
|--------|-----|-----|------------|
| Finds | any path, all paths, components, topo order | shortest in hops, level order | connectivity queries only |
| Space | O(h) tree, O(V) graph | O(w) frontier | O(V) arrays |
| Cycles | needs visited set | needs visited set | detects undirected cycles via union |
| Pick when | exhaustive exploration, backtracking | shortest unweighted path, levels | many connectivity queries on growing graph |

## Pitfalls

- **Graph DFS without visited loops forever on cycles.** Mark visited *before* recursing (pre-order).
- Path string: copy or use `StringBuilder` + backtrack length. Forgetting to revert is a classic bug.
- Grid DFS: mark visited by writing to grid (`'1' → '0'`) or use `visited[][]` array. Don't allocate new objects per cell.
- For very deep trees (skewed), recursion hits stack overflow. Use iterative stack: `push(root); while(!stack.isEmpty()) { pop; push children; }`.

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 104 | Easy |
| 110 | Easy |
| 112 | Easy |
| 129 | Medium |

## Interview Q&A

(Senior Depth)

**Q: Number of Islands (LC 200) — why modify the grid instead of a `visited` array?**
**A:** Modifying `grid[r][c] = '0'` marks visited in O(1) space (no extra `visited[][]`). It's destructive but acceptable for the problem. In production, you'd use a separate visited structure if the grid must be preserved. The space savings (O(1) extra vs O(mn)) is significant for large grids.

**Q: Clone Graph — why does the hashmap serve dual purpose (visited + cache)?**
**A:** When we see a node, we create its copy *immediately* and put it in the map. If we encounter the same node again (cycle or shared neighbor), the map returns the already-created copy. This handles both cycle prevention and identity preservation in one structure. Without the map, you'd need separate `visited` set + `original→copy` map.

**Q: Topological Sort via DFS — how does it work?**
**A:** DFS on DAG. When a node finishes (all neighbors processed), push to stack. Reverse stack = topological order. Proof: for edge u→v, v finishes before u (v is deeper), so v appears earlier in reversed order. Cycle detection: if you encounter a gray (in-progress) node, cycle exists.

**Q: Path Sum II (LC 113) — why copy path when adding to result?**
**A:** The `path` list is mutated during recursion (add before recurse, remove after). If you add the *reference* to results, all entries point to the same mutating list. `res.add(new ArrayList<>(path))` creates a snapshot. This is the "copy on success" pattern — same in all backtracking/DFS path collection.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for DFS? :: **A:** connected components, cycle detection, topological sort, path existence, backtracking prerequisite #flashcard

#flashcard
**Q:** Time/space complexity of DFS? :: **A:** Time: O(V+E) adjacency list, Space: O(V) visited + O(h) recursion #flashcard

#flashcard
**Q:** When do you NOT use DFS? :: **A:** shortest path unweighted (use BFS), very deep graphs (stack overflow — use iterative) #flashcard

#flashcard
**Q:** Core Java 25 snippet for DFS? :: **A:** `boolean[] vis=new boolean[n]; void dfs(int u){ vis[u]=true; for(int v:adj[u]) if(!vis[v]) dfs(v); }` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- [[05_Trees_Graphs/01 - Binary Tree Traversal|Binary Tree Traversal]] (tree DFS)
- [[05_Trees_Graphs/03 - BFS|BFS]] (shortest unweighted)
- [[05_Trees_Graphs/06 - Union Find|Union Find]] (connectivity queries)
- [[07_Backtracking_DP/01 - Backtracking|Backtracking]] (DFS with state restoration)
- [[Java/07_DSA/Trees]] · [[Java/07_DSA/Graph]]
