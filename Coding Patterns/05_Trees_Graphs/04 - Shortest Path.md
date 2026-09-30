---
title: "Shortest Path"
type: pattern
pattern: 14
domain: "Graph"
category: "Coding Patterns/05_Trees_Graphs"
advanced: false
mastery: learn
recognition_score: 0
difficulty: "Hard"
leetcode: [743, 787, 1514]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - graph
---

# Shortest Path

> Pattern #14 · Graph

## Recognition

- Weighted graph shortest path
- Different edge costs
- Need minimum total cost rather than minimum number of hops

### Strong signals
- Weighted graph shortest path
- Different edge costs

### Do not infer it from
- A keyword alone
- A familiar example without checking constraints

## Invariant

> For Dijkstra, when a node is removed with the smallest tentative distance, that distance is final when all edge weights are non-negative.

## Mental model

Maintain the smallest state that completely describes the part of the search space still relevant to the answer.

## Core implementation

```java
record Edge(int to, int w) {}
record State(int dist, int node) {}

// Dijkstra — LC 743 Network Delay Time
int[] dijkstra(int n, java.util.List<java.util.List<Edge>> g, int src) {
    var dist = new int[n];
    java.util.Arrays.fill(dist, Integer.MAX_VALUE);
    dist[src] = 0;
    var pq = new java.util.PriorityQueue<State>((a, b) -> a.dist() - b.dist());
    pq.offer(new State(0, src));
    while (!pq.isEmpty()) {
        var cur = pq.poll();
        if (cur.dist() > dist[cur.node()]) continue; // stale-entry skip
        for (var e : g.get(cur.node())) {
            int nd = cur.dist() + e.w();
            if (nd < dist[e.to()]) {
                dist[e.to()] = nd;
                pq.offer(new State(nd, e.to()));
            }
        }
    }
    return dist;
}

// Cheapest Flights Within K Stops — LC 787 (Bellman-Ford style)
int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
    var dist = new int[n];
    java.util.Arrays.fill(dist, Integer.MAX_VALUE);
    dist[src] = 0;
    // k stops = k+1 edges = k+1 relaxation rounds
    for (int i = 0; i <= k; i++) {
        var tmp = dist.clone();
        for (int[] f : flights) {
            int u = f[0], v = f[1], w = f[2];
            if (dist[u] == Integer.MAX_VALUE) continue;
            tmp[v] = Math.min(tmp[v], dist[u] + w);
        }
        dist = tmp;
    }
    return dist[dst] == Integer.MAX_VALUE ? -1 : dist[dst];
}

// Find City With Smallest Number of Neighbors at Threshold — LC 1334
// Run Dijkstra from each city, or Floyd-Warshall O(V^3) for dense small V
int findTheCity(int n, int[][] edges, int distanceThreshold) {
    int[][] dist = new int[n][n];
    for (int i = 0; i < n; i++) {
        java.util.Arrays.fill(dist[i], Integer.MAX_VALUE);
        dist[i][i] = 0;
    }
    for (int[] e : edges) {
        dist[e[0]][e[1]] = e[2];
        dist[e[1]][e[0]] = e[2];
    }
    // Floyd-Warshall
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (dist[i][k] != Integer.MAX_VALUE && dist[k][j] != Integer.MAX_VALUE)
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
    int best = n, ans = -1;
    for (int i = 0; i < n; i++) {
        int cnt = 0;
        for (int j = 0; j < n; j++) if (i != j && dist[i][j] <= distanceThreshold) cnt++;
        if (cnt <= best) { best = cnt; ans = i; }
    }
    return ans;
}
```

## Variants

Start with the core implementation. Introduce a variant only when the required state or proof changes.

## When to use

- minimum cost, network delay, cheapest flight with k stops, any "weighted shortest" phrasing; "minimum distance", "shortest path" with weights.
- **NOT:** unweighted graph (use BFS); negative weights with Dijkstra (use Bellman-Ford); all-pairs on dense small graph (use Floyd-Warshall).

## When NOT to use

unweighted graph (use BFS); negative weights with Dijkstra (use Bellman-Ford); all-pairs on dense small graph (use Floyd-Warshall).

## Complexity & trade-offs

| Algorithm | Time | When |
|-----------|------|------|
| Dijkstra + heap | O((V+E) log V) | weights ≥ 0 |
| Bellman-Ford | O(V·E) | negative weights, detect cycle, k-hop limit |
| BFS | O(V+E) | unweighted only |
| Floyd-Warshall | O(V³) | all-pairs, dense small V (V ≤ 400) |

| Aspect | Dijkstra | Bellman-Ford | Floyd-Warshall | BFS |
|--------|----------|--------------|----------------|-----|
| Weights | non-negative | any, detects negative cycles | any | unit only |
| Solves | single source | single source | all pairs | single source, unweighted |
| Time | O((V+E) log V) | O(V·E) | O(V³) | O(V+E) |
| Pick when | standard weighted shortest | negative weights or k-hop limit | dense graph, every pair | no weights at all |

## Pitfalls

- **Dijkstra breaks with negative weights.** Switch to Bellman-Ford.
- **0-index vs 1-index** graph building is a common off-by-one.
- **Stale-entry skip** in Dijkstra is mandatory — without it, time degrades to O(E log E) with many duplicate heap entries.
- For "k stops", the edge count matters, not just cost — Bellman-Ford style relaxation per stop (k+1 rounds) is used, not Dijkstra.
- Use `long` for distances if weights are large (sum can overflow `int`).

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 743 | Medium |
| 787 | Medium |
| 1514 | Medium |

## Interview Q&A

(Senior Depth)

**Q: Why is the stale-entry skip in Dijkstra not just an optimization but a correctness requirement for time complexity?**
**A:** Without the skip, every time we find a shorter path to a node, we push a new entry to the heap. The old entry remains and will be popped later. A node can be pushed O(E) times (once per incoming edge), leading to O(E log E) heap operations instead of O((V+E) log V). The skip ensures each node is *processed* (relaxes edges) at most once.

**Q: Cheapest Flights Within K Stops (LC 787) — why Bellman-Ford and not Dijkstra?**
**A:** Dijkstra minimizes total cost but doesn't constrain the number of edges (stops). A path with lower cost might use more than k+1 edges. Bellman-Ford's round-based relaxation naturally enforces the hop limit: round i computes shortest paths with at most i edges. After k+1 rounds, we have shortest paths with ≤ k+1 edges (k stops).

**Q: When would you use Floyd-Warshall over running Dijkstra from each node?**
**A:** Floyd-Warshall O(V³) vs Dijkstra V times = O(V·E log V). For dense graphs (E ≈ V²), Floyd-Warshall is O(V³) vs O(V³ log V) — Floyd wins. For sparse graphs (E ≈ V), V×Dijkstra is O(V² log V) vs O(V³) — Dijkstra wins. Also Floyd-Warshall is simpler code and handles negative weights (no negative cycles).

**Q: Dijkstra with Fibonacci heap gives O(E + V log V) — why don't we use it?**
**A:** Fibonacci heap has large constant factors and complex implementation. Binary heap O((V+E) log V) is faster in practice for typical interview constraints (V ≤ 10^4). In interviews, binary heap is expected and accepted.

**Q: How does A* differ from Dijkstra?**
**A:** A* = Dijkstra + heuristic `h(n)` estimating distance to target. Priority = `g(n) + h(n)` (cost so far + estimated remaining). If `h` is admissible (never overestimates), A* finds optimal path faster by directing search toward target. Dijkstra is A* with `h(n) = 0`.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Shortest Path? :: **A:** weighted graph, Dijkstra, Bellman-Ford, Floyd-Warshall, A*, negative weights #flashcard

#flashcard
**Q:** Time/space complexity of Shortest Path? :: **A:** Dijkstra: O((V+E)log V), Bellman-Ford: O(VE), Floyd: O(V³) #flashcard

#flashcard
**Q:** When do you NOT use Shortest Path? :: **A:** unweighted (use BFS O(V+E)), all-pairs small V (Floyd), negative cycles (Bellman-Ford detect) #flashcard

#flashcard
**Q:** Core Java 25 snippet for Shortest Path? :: **A:** `PriorityQueue<int[]> pq=new PriorityQueue<>(Comparator.comparingInt(a->a[1])); pq.offer(new int[]{src,0}); while(!pq.isEmpty())...` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- [[05_Trees_Graphs/03 - BFS|BFS]] (unweighted shortest)
- [[05_Trees_Graphs/06 - Union Find|Union Find]] (connectivity, not distances)
- [[Java/07_DSA/Graph]] · [[Java/07_DSA/Heap]]
