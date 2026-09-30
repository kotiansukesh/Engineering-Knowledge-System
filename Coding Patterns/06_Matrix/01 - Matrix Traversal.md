---
title: "Matrix Traversal"
type: pattern
pattern: 17
domain: "Matrix / Grid"
category: "Coding Patterns/06_Matrix"
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
difficulty: "Medium"
leetcode: [54, 733, 200]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - matrix-grid
---

# Matrix Traversal

> Pattern #17 · Matrix / Grid

## Recognition

- Islands, regions, flood fill, grid connectivity
- Movement across neighboring cells
- Grid shortest path or state traversal

### Strong signals
- Islands, regions, flood fill, grid connectivity
- Movement across neighboring cells

### Do not infer it from
- A keyword alone
- A familiar example without checking constraints

## Invariant

> Each cell is processed according to the traversal rule and marked so the algorithm never processes the same reachable state twice.

## Mental model

Maintain the smallest state that completely describes the part of the search space still relevant to the answer.

## Core implementation

```java
int[][] DIRS = {{1,0},{-1,0},{0,1},{0,-1}};

// Flood Fill DFS — LC 733
int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
    int old = image[sr][sc];
    if (old == newColor) return image; // critical: avoid infinite loop
    dfs(image, sr, sc, old, newColor);
    return image;
}

void dfs(int[][] img, int r, int c, int old, int nc) {
    if (r < 0 || r >= img.length || c < 0 || c >= img[0].length || img[r][c] != old) return;
    img[r][c] = nc;
    for (var d : DIRS) dfs(img, r + d[0], c + d[1], old, nc);
}

// BFS version — same DIRS, queue of int[2], mark when enqueuing
int[][] floodFillBFS(int[][] image, int sr, int sc, int newColor) {
    int old = image[sr][sc];
    if (old == newColor) return image;
    var q = new java.util.ArrayDeque<int[]>();
    q.offer(new int[]{sr, sc});
    image[sr][sc] = newColor;
    while (!q.isEmpty()) {
        var cur = q.poll();
        for (var d : DIRS) {
            int r = cur[0] + d[0], c = cur[1] + d[1];
            if (r >= 0 && r < image.length && c >= 0 && c < image[0].length && image[r][c] == old) {
                image[r][c] = newColor;
                q.offer(new int[]{r, c});
            }
        }
    }
    return image;
}

// Number of Islands — LC 200 (DFS sinks land)
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
    g[r][c] = '0'; // sink = mark visited
    for (var d : DIRS) dfsGrid(g, r + d[0], c + d[1]);
}

// Surrounded Regions — LC 130 (mark border-connected O's safe)
void solve(char[][] board) {
    if (board.length == 0) return;
    int m = board.length, n = board[0].length;
    // mark border O's
    for (int i = 0; i < m; i++) {
        if (board[i][0] == 'O') dfsMark(board, i, 0);
        if (board[i][n-1] == 'O') dfsMark(board, i, n-1);
    }
    for (int j = 0; j < n; j++) {
        if (board[0][j] == 'O') dfsMark(board, 0, j);
        if (board[m-1][j] == 'O') dfsMark(board, m-1, j);
    }
    // flip: O -> X, S -> O
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            if (board[i][j] == 'O') board[i][j] = 'X';
            else if (board[i][j] == 'S') board[i][j] = 'O';
        }
}
void dfsMark(char[][] b, int r, int c) {
    if (r < 0 || r >= b.length || c < 0 || c >= b[0].length || b[r][c] != 'O') return;
    b[r][c] = 'S'; // safe
    for (var d : DIRS) dfsMark(b, r + d[0], c + d[1]);
}
```

## Variants

Start with the core implementation. Introduce a variant only when the required state or proof changes.

## When to use
- flood fill, islands, surrounded regions, maze, distance to nearest cell, rotting oranges (multi-source BFS).

## When NOT to use
- weighted grids with varying costs (use Dijkstra / 0-1 BFS); need shortest path with weights.

## Complexity & trade-offs

| Approach | Time | Space |
|----------|------|-------|
| DFS on grid | O(m·n) | O(m·n) worst case recursion stack |
| BFS on grid | O(m·n) | O(m·n) queue |
| Union Find on grid | O(m·n α(mn)) | O(m·n) arrays |

| Aspect | DFS on Grid | BFS on Grid | Union Find on Grid |
|--------|-------------|-------------|-------------------|
| Shortest path in cells | No | Yes, unweighted | No |
| Flood fill / component | Yes | Yes | Yes, union of 4-neighbors |
| Space | O(m·n) recursion worst case | O(m·n) queue | O(m·n) arrays |
| Risk | Stack overflow on large grids | Wider memory | Heavier constant factor |
| Pick when | fill, connectivity, shape | "nearest", "min steps" | offline island counting |

## Pitfalls

- **Check `old == newColor` first** or flood fill loops infinitely.
- **Bounds check before value check** to avoid index error.
- **Mark visited at enqueue time for BFS**, not dequeue — otherwise same cell enqueued multiple times.
- For large grids, DFS recursion risks stack overflow — use BFS or iterative stack.
- Java 25: `record Cell(int r, int c) {}` keeps queue typed instead of `int[]`.

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 54 | Medium |
| 733 | Easy |
| 200 | Medium |

## Interview Q&A

(Senior Depth)

**Q: Flood Fill — why check `old == newColor` before DFS?**
**A:** If `old == newColor`, the condition `img[r][c] != old` in DFS would never be true after the first cell is colored, but wait — the first cell gets colored, then its neighbors are checked. Since they still have `old` color, they get colored, and so on. Actually, the check prevents infinite recursion because the DFS base case `img[r][c] != old` would fail *after* coloring, but the function would still return. Wait — the real issue: if `old == newColor`, the first call colors the cell, then recurses to neighbors. Neighbors have `old` color, so they get colored, etc. The base case `img[r][c] != old` stops at boundaries. So it *does* terminate but does unnecessary work. The early return is an optimization. Actually, for some implementations that don't mark before recursing, it can infinite loop. Safe pattern: check early and return.

**Q: Number of Islands — why is modifying the grid (`'1' → '0'`) acceptable for visited marking?**
**A:** The problem doesn't require preserving the input grid. It saves O(mn) space for a `visited[][]` array. In production, if the grid must be preserved, use a separate visited structure or copy the grid. The space savings (O(1) extra vs O(mn)) is significant for large grids.

**Q: Surrounded Regions (LC 130) — why start from border O's instead of scanning all O's?**
**A:** An O is "surrounded" iff it's *not* connected to the border. Starting from border O's and marking all reachable O's as "safe" (S) in one pass is O(mn). The alternative — for each interior O, DFS to check if it reaches border — is O(mn) per interior O, potentially O((mn)²). The border-first approach is the key insight.

**Q: 0-1 BFS — when do you use it on a grid?**
**A:** When edge weights are 0 or 1 (e.g., moving on free cell = 0, moving through obstacle = 1). Use deque: push 0-weight edges to front, 1-weight to back. Processes in increasing distance order. Faster than Dijkstra (O(V+E) vs O(E log V)). For general weights, use Dijkstra.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Matrix Traversal? :: **A:** spiral order, diagonal traversal, BFS/DFS on grid, flood fill, shortest path in grid, rotation #flashcard

#flashcard
**Q:** Time/space complexity of Matrix Traversal? :: **A:** Time: O(mn) visit each cell, Space: O(mn) visited or O(1) in-place marking #flashcard

#flashcard
**Q:** When do you NOT use Matrix Traversal? :: **A:** only need perimeter (O(m+n)), sparse grid (use coordinate compression) #flashcard

#flashcard
**Q:** Core Java 25 snippet for Matrix Traversal? :: **A:** `int[][] dirs={{0,1},{1,0},{0,-1},{-1,0}}; for(int[] d:dirs){ int nr=r+d[0], nc=c+d[1]; if(inBounds(nr,nc)) process(nr,nc); }` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- [[05_Trees_Graphs/02 - DFS|DFS]] (recursive grid traversal)
- [[05_Trees_Graphs/03 - BFS|BFS]] (level-order, shortest unweighted)
- [[05_Trees_Graphs/06 - Union Find|Union Find]] (offline connectivity)
- [[Java/07_DSA/Graph]]
