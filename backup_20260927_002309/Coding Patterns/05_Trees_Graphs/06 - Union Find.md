---
title: Union Find
pattern: 21
category: Coding Patterns/05_Trees_Graphs
tags:
  - pattern/graph
  - pattern/tree/union-find
  - pattern/tree/disjoint-set
leetcode:
  - 684
  - 721
  - 547
created: '2026-09-04'
completed: false
reviewed: ''
sr-due: ''
difficulty: Medium
source: 'https://algomaster.io/learn/dsa/'
---

# Union Find

> Part of [[README|20 DSA Patterns]] • `Coding Patterns/05_Trees_Graphs` • Pattern #21 (beyond original 20)

## Intent
Dynamic connectivity for undirected graphs — are `a` and `b` in the same component? Two optimizations (path compression + union by rank/size) make operations ~O(α(n)) ≈ O(1). The course-named pattern the 20-pattern list omits.

## Why it Matters
- **Path compression:** `find(x)` flattens the tree by pointing each visited node directly at the root.
- **Union by rank/size:** attaches smaller tree under larger root, keeping depth logarithmic.
- **Both together** are required — either alone leaves a path that can degrade toward O(n) per find.
- **Components counter:** maintain `components` variable, decrement on successful union. O(1) component count.
- Senior signal: implementing the *pair* together, and knowing that without both, worst case is a linked-list tree with O(n) find.

## Diagram
```mermaid
flowchart LR
  U["union(a,b)"] --> FA["find(a)"]
  U --> FB["find(b)"]
  FA --> S{"same root?"}
  FB --> S
  S -->|yes| C["cycle, do nothing"]
  S -->|no| M["attach smaller rank<br/>under larger"]
  M --> Dec["components--"]
  Dec --> F["find now flattens<br/>via path compression"]
  F --> U
```


## Problems

### 684. Redundant Connection (Medium)
> [LeetCode 684](https://leetcode.com/problems/redundant-connection/) • Tags: Depth-First Search, Breadth-First Search, Union-Find, Graph Theory

**Problem Statement:**

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [a_i_, b_i_] indicates that there is an edge between nodes a_i_ and b_i_ in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

**Examples:**

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

---

### 721. Accounts Merge (Medium)
> [LeetCode 721](https://leetcode.com/problems/accounts-merge/) • Tags: Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union-Find, Sorting

**Problem Statement:**

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

**Examples:**

Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

---

### 547. Number of Provinces (Medium)
> [LeetCode 547](https://leetcode.com/problems/number-of-provinces/) • Tags: Depth-First Search, Breadth-First Search, Union-Find, Graph Theory

**Problem Statement:**

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the i^th^ city and the j^th^ city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

**Examples:**

Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

---


## Code / Example
```java
class DSU {
    int[] parent, rank;
    int components;
    
    DSU(int n) {
        parent = new int[n];
        rank = new int[n];
        components = n;
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    
    // Path compression: point straight at the root
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    
    // Union by rank; returns false = already connected (cycle!)
    boolean union(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return false;
        if (rank[ra] < rank[rb]) parent[ra] = rb;
        else if (rank[ra] > rank[rb]) parent[rb] = ra;
        else { parent[rb] = ra; rank[ra]++; }
        components--;
        return true;
    }
}

// LC 684 Redundant Connection: first edge whose union() returns false is the answer
int[] findRedundantConnection(int[][] edges) {
    var dsu = new DSU(edges.length + 1);
    for (int[] e : edges) if (!dsu.union(e[0], e[1])) return e;
    return new int[0];
}

// LC 547 Number of Provinces: DSU on adjacency matrix
int findCircleNum(int[][] isConnected) {
    int n = isConnected.length;
    var dsu = new DSU(n);
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (isConnected[i][j] == 1) dsu.union(i, j);
    return dsu.components;
}

// LC 721 Accounts Merge: DSU on email indices
java.util.List<java.util.List<String>> accountsMerge(java.util.List<java.util.List<String>> accounts) {
    var emailToId = new java.util.HashMap<String, Integer>();
    var emailToName = new java.util.HashMap<String, String>();
    int id = 0;
    for (var acc : accounts) {
        String name = acc.get(0);
        for (int i = 1; i < acc.size(); i++) {
            String email = acc.get(i);
            if (!emailToId.containsKey(email)) emailToId.put(email, id++);
            emailToName.put(email, name);
        }
        for (int i = 2; i < acc.size(); i++) {
            int id1 = emailToId.get(acc.get(1));
            int id2 = emailToId.get(acc.get(i));
            dsu.union(id1, id2);
        }
    }
    var idToEmails = new java.util.HashMap<Integer, java.util.List<String>>();
    for (var e : emailToId.entrySet()) {
        int root = dsu.find(e.getValue());
        idToEmails.computeIfAbsent(root, k -> new java.util.ArrayList<>()).add(e.getKey());
    }
    var res = new java.util.ArrayList<java.util.List<String>>();
    for (var e : idToEmails.entrySet()) {
        var emails = e.getValue();
        java.util.Collections.sort(emails);
        emails.add(0, emailToName.get(emails.get(0)));
        res.add(emails);
    }
    return res;
}
```

## When to Use / When NOT
- **Use:** cycle detection in undirected graphs; connected components; redundant edge; account merging; "provinces", "groups", "merge" keywords.
- **NOT:** directed graphs (use DFS coloring for cycle detection / topo sort); online queries on static graph (DFS/BFS once is simpler).

## Trade-offs
| Operation | Time | Note |
|-----------|------|------|
| find / union | O(α(n)) ≈ O(1) | inverse Ackermann with both optimizations |
| count components | O(1) | maintain counter, decrement on real union |

## Vs Table
| Aspect | Union Find | DFS/BFS for Components | DFS Coloring |
|--------|------------|------------------------|--------------|
| Graph type | undirected | undirected or directed | directed |
| Queries | online, interleaved with edge additions | offline, whole graph known | cycle detection in digraph |
| Time | O(α(n)) per query | O(V+E) per rebuild | O(V+E) |
| Pick when | edges arrive over time, connectivity asked repeatedly | one-shot component count | directed cycle / topo sort |

## Pitfalls
- **Forgetting path compression** turns it into a slow tree walk on long chains — always implement the pair together.
- **1-indexed LeetCode inputs** vs 0-indexed arrays — size `n+1` and ignore index 0.
- **Union Find is undirected-only**; directed cycle detection needs DFS coloring (white/gray/black) instead.
- For "size" instead of "rank", track `size[root]` and attach smaller size under larger — same O(α(n)) guarantee.

## Interview Q&A (Senior Depth)

**Q: Why are path compression AND union by rank both necessary? What happens with only one?**
**A:** Path compression alone: find flattens paths, but union can create deep trees if you always attach larger to smaller. Union by rank alone: tree depth is O(log n), but find doesn't flatten, so repeated finds on deep nodes cost O(log n). Together: find flattens on the way up, union keeps depth minimal → O(α(n)) amortized.

**Q: Redundant Connection (LC 684) — why does the first edge with union() returning false give the answer?**
**A:** The input is a tree (n nodes, n-1 edges) plus one extra edge. The extra edge creates exactly one cycle. Processing edges in order, the first edge whose endpoints are already connected completes the cycle — that's the redundant edge. Any later edge in the cycle would also return false, but we want the *last* in the input that causes the cycle, which is the first one that finds both ends already connected.

**Q: Accounts Merge (LC 721) — why DSU on emails instead of account indices?**
**A:** Accounts can share emails (same email appears in multiple accounts). The DSU connects *emails* that belong to the same person. Each account's emails are unioned together. After all unions, each DSU component = one person's emails. Using account indices would require O(n²) pairwise comparison to find overlaps.

**Q: How does Union Find handle the "Number of Islands II" (LC 305) dynamic addition problem?**
**A:** Start with all water (each cell is its own component, or not counted). For each addLand(r,c): mark as land, components++. Check 4 neighbors; if neighbor is land, union(cell, neighbor) — if union succeeds, components--. After each addition, components = current island count. O(k α(mn)) for k additions.

**Q: Why can't Union Find detect cycles in directed graphs?**
**A:** Union Find merges sets based on undirected connectivity. In a directed graph A→B→C→A, all three are in the same undirected component, but the *directed* cycle isn't detected by union operations. Directed cycle detection needs DFS with three colors (white/unvisited, gray/in-stack, black/done) — a back edge to a gray node = directed cycle.

## Related
- [[05_Trees_Graphs/02 - DFS|DFS]] (directed cycles)
- [[05_Trees_Graphs/04 - Shortest Path|Shortest Path]] (weighted)
- [[Java/07_DSA/Graph]]

---
*Category: Coding Patterns/05_Trees_Graphs*
