---
title: Shortest Path
pattern: 15
category: Coding Patterns/05_Trees_Graphs
tags:
- pattern/graph
- pattern/tree/shortest-path
- pattern/tree/dijkstra
leetcode:
- 743
- 787
- 1334
created: '2026-09-02'
completed: false
reviewed: ''
sr-due: ''
difficulty: Hard
source: https://blog.algomaster.io/p/20-dsa-patterns
problems-solved: []
problems-solved-dates: {}
excalidraw: ''
type: note
---

# Shortest Path

> Part of [[README|20 DSA Patterns]] • `Coding Patterns/05_Trees_Graphs` • Pattern #15

## Intent
Find minimum cost/distance in a weighted graph — Dijkstra for non-negative weights (greedy + min-heap), Bellman-Ford for negative weights (detects negative cycles), BFS for unit weights only.

## Why it Matters
- **Dijkstra:** greedy + min-heap. Stale-entry skip (`if (cur.dist > dist[node]) continue`) is not optional — without it, each node is reprocessed once per heap entry instead of once.
- **Bellman-Ford:** V-1 relaxation passes over all edges. Detects negative cycles (if pass V still relaxes). Used for "k stops" problems (constrained hops).
- **BFS:** only when every edge weight = 1 (or uniform).
- Senior signal: knowing the stale-entry skip in Dijkstra, and that Bellman-Ford's V-1 passes correspond to path length (at most V-1 edges in a simple path).

## Diagram
```mermaid
flowchart LR
  Src["dist[src]=0<br/>heap (0,src)"] --> Poll["poll min"]
  Poll --> St{"stale?<br/>dist > known"}
  St -->|yes| Poll
  St -->|no| Rel["relax each edge"]
  Rel --> B{"improved?"}
  B -->|yes| Push["push new dist"]
  Push --> Poll
  B -->|no| Poll
```


## Problems

### 743. Network Delay Time (Medium)
> [LeetCode 743](https://leetcode.com/problems/network-delay-time/) • Tags: Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path, Dijkstra's Algorithm

**Problem Statement:**

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (u_i_, v_i_, w_i_), where u_i_ is the source node, v_i_ is the target node, and w_i_ is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

**Examples:**

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

---

### 787. Cheapest Flights Within K Stops (Medium)
> [LeetCode 787](https://leetcode.com/problems/cheapest-flights-within-k-stops/) • Tags: Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path

**Problem Statement:**

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [from_i_, to_i_, price_i_] indicates that there is a flight from city from_i_ to city to_i_ with cost price_i_.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

**Examples:**

Example 1:

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

---

### 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance (Medium)
> [LeetCode 1334](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) • Tags: Dynamic Programming, Graph Theory, Shortest Path, Dijkstra's Algorithm, Bellman–Ford Algorithm, Floyd–Warshall Algorithm

**Problem Statement:**

There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [from_i_, to_i_, weight_i_] represents a bidirectional and weighted edge between cities from_i_ and to_i_, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

**Examples:**

Example 1:

Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

Example 2:

Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.

---


## Code / Example
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

## When to Use / When NOT
- **Use:** minimum cost, network delay, cheapest flight with k stops, any "weighted shortest" phrasing; "minimum distance", "shortest path" with weights.
- **NOT:** unweighted graph (use BFS); negative weights with Dijkstra (use Bellman-Ford); all-pairs on dense small graph (use Floyd-Warshall).

## Trade-offs
| Algorithm | Time | When |
|-----------|------|------|
| Dijkstra + heap | O((V+E) log V) | weights ≥ 0 |
| Bellman-Ford | O(V·E) | negative weights, detect cycle, k-hop limit |
| BFS | O(V+E) | unweighted only |
| Floyd-Warshall | O(V³) | all-pairs, dense small V (V ≤ 400) |

## Vs Table
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

## Interview Q&A (Senior Depth)

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

## Related
- [[05_Trees_Graphs/03 - BFS|BFS]] (unweighted shortest)
- [[05_Trees_Graphs/06 - Union Find|Union Find]] (connectivity, not distances)
- [[Java/07_DSA/Graph]] · [[Java/07_DSA/Heap]]

---
*Category: Coding Patterns/05_Trees_Graphs*
