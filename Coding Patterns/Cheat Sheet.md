---
category: CheatSheet
tags: [dsa, coding-patterns, cheatsheet]
title: Coding Patterns - Cheat Sheet (Overall)
---

# Coding Patterns - Cheat Sheet (all dsa Patterns)

## Pattern → When → Template (Interview Decision Table)

| # | Pattern | Signal Keywords | Data Structure | Time | One-Liner Template |
|---|---------|-----------------|----------------|------|-------------------|
| 1 | Prefix Sum | range sum, subarray sum k, immutable array | prefix array | O(1) query | `pref[j+1]-pref[i]` |
| 2 | Two Pointers | sorted, pair, palindrome, remove duplicates | Array/String | O(n) | `l=0,r=n-1; while(l<r){... l++ / r--}` |
| 3 | Sliding Window | subarray/substring, k, longest/shortest, distinct | Array/String + Map | O(n) | `for r: expand; while(invalid) shrink l++; update` |
| 4 | Fast & Slow (Floyd) | cycle, middle, linked list | LinkedList | O(n) | `slow=slow.next; fast=fast.next.next` |
| 5 | In-place Reversal | reverse linked list, k-group | LinkedList | O(n) | `prev=null; cur=head; nxt=cur.next` |
| 6 | Frequency Counting | anagram, duplicate, group by freq, top-k | HashMap / int[26] | O(n) | `freq.put(x, getOrDefault+1)` |
| 7 | Monotonic Stack | next greater/smaller, histogram, span | Stack (indices) | O(n) | `while(!st.empty() && nums[st.top()]<nums[i]) pop` |
| 8 | Bitwise XOR | single number, missing, appears once | int | O(n) | `x^=v; x^ x =0; x^0=x` |
| 9 | Top K / Heap | k largest/smallest/frequent | Heap / QuickSelect | O(n log k) | `minHeap size k; offer+poll` |
| 10 | Merge Intervals | intervals, overlap, meeting | Sort + List | O(n log n) | Sort by start, merge if `curr.start <= prev.end` |
| 11 | Modified Binary Search | rotated, infinite, bitonic, 2D matrix | Array | O(log n) | Check which half is sorted |
| 12 | Binary Tree Traversal | tree traversal, BST sorted | Recursion/Stack | O(n) | Pre/in/post order visit position |
| 13 | DFS (Tree/Graph) | path, all solutions, connected | Stack/Recursion | O(V+E) | `dfs(node){ for(child) dfs(child) }` |
| 14 | BFS (Level Order) | shortest, level, tree traversal | Queue | O(V+E) | `queue.add(root); while(!q.isEmpty()) levelSize=q.size()` |
| 15 | Shortest Path (Dijkstra) | weighted shortest, network delay | PQ + Graph | O((V+E) log V) | `pq.poll(); if(stale) continue; relax edges` |
| 16 | Matrix Traversal | flood fill, islands, maze | DFS/BFS + grid | O(m·n) | `DIRS` 4-dir, mark on entry |
| 17 | Backtracking | subsets, permutations, N-Queens | Recursion + choose/explore/unchoose | O(2ⁿ)/O(n!) | `pick → recurse → unpick` |
| 18 | Trie | prefix, autocomplete, dictionary | TrieNode[26] | O(L) | `insert/search/startsWith walk` |
| 19 | Greedy | interval scheduling, jump game, activity | Sort | O(n log n) | Sort by end, pick earliest finishing |
| 20 | DP | optimal + overlapping subproblems | dp table / rolling | O(n·choices) | `dp[i]=max/choice(dp[i-1], dp[i-2]+...)` |
| 21 | Union Find | connected components, cycle, islands | DSU | α(n) | `find + union by rank + path compression` |

## Vs Tables

| Comparison | A | B | Pick |
|------------|---|---|------|
| Sliding Window vs Two Pointers | Contiguous subarray (variable/fixed window) | Pair from ends / sorted search | Window for substring; pointers for pair/palindrome |
| BFS vs DFS | Shortest path, level order | All paths, backtracking, topological | BFS for shortest; DFS for exhaustive |
| Heap vs Sort for Top-K | Heap O(n log k) | Sort O(n log n) | Heap when k << n |
| DP vs Greedy | Optimal substructure + overlapping, need global optimum | Local optimum → global (interval, Huffman) | Try greedy; if counterexample → DP |
| Backtracking vs DP | Enumerate all solutions | Count/optimize (memoize) | DP = backtracking + memo |
| Binary Search vs Two Pointers | Sorted search / boundary | Sorted pair / partition | BS for existence; pointers for pair |
| Union Find vs DFS Components | Online, edges arrive over time | Offline, whole graph known | Union Find for dynamic; DFS for static |

## Java 25 One-liners per Pattern

```java
// 1. Prefix Sum - range sum immutable
int rangeSum(int[] pref, int i, int j) { return pref[j+1] - pref[i]; }

// 2. Two Pointers - two sum sorted / palindrome
boolean isPal(String s){ int l=0,r=s.length()-1; while(l<r) if(s.charAt(l++)!=s.charAt(r--)) return false; return true; }

// 3. Sliding Window - longest without repeating
int longestUnique(String s){ var set=new HashSet<Character>(); int l=0,max=0;
 for(int r=0;r<s.length();r++){ while(set.contains(s.charAt(r))) set.remove(s.charAt(l++)); set.add(s.charAt(r)); max=Math.max(max,r-l+1);} return max; }

// 4. Fast & Slow - cycle detect
boolean hasCycle(ListNode h){ var s=h,f=h; while(f!=null&&f.next!=null){s=s.next; f=f.next.next; if(s==f) return true;} return false; }

// 5. In-place Reversal - reverse list
Node reverse(Node head){ Node prev=null, cur=head; while(cur!=null){ var nxt=cur.next; cur.next=prev; prev=cur; cur=nxt; } return prev; }

// 6. Frequency Counting - anagram
boolean isAnagram(String s, String t){ if(s.length()!=t.length()) return false; int[] f=new int[26]; for(char c:s.toCharArray()) f[c-'a']++; for(char c:t.toCharArray()) if(--f[c-'a']<0) return false; return true; }

// 7. Monotonic Stack - next greater
int[] nextGreater(int[] a){ int n=a.length; int[] res=new int[n]; Arrays.fill(res,-1); var st=new ArrayDeque<Integer>();
 for(int i=0;i<n;i++){ while(!st.isEmpty()&&a[st.peek()]<a[i]) res[st.pop()]=a[i]; st.push(i);} return res; }

// 8. Bitwise XOR - single number
int single(int[] a){ int x=0; for(int n:a) x^=n; return x; }

// 9. Top K frequent - heap vs bucket O(n)
var freq=new HashMap<Integer,Integer>(); for(int x:nums) freq.merge(x,1,Integer::sum);
var pq=new PriorityQueue<Map.Entry<Integer,Integer>>(Comparator.comparingInt(Map.Entry::getValue));
for(var e: freq.entrySet()){ pq.offer(e); if(pq.size()>k) pq.poll(); }

// 10. Merge Intervals
Arrays.sort(intervals, Comparator.comparingInt(a->a[0]));
var merged=new ArrayList<int[]>(); for(int[] cur: intervals){ if(merged.isEmpty()||cur[0]>merged.getLast()[1]) merged.add(cur); else merged.getLast()[1]=Math.max(merged.getLast()[1],cur[1]); }

// 11/12. Binary Search - lower bound
int lowerBound(int[] a,int t){ int lo=0,hi=a.length; while(lo<hi){int m=lo+(hi-lo)/2; if(a[m]<t) lo=m+1; else hi=m;} return lo; }

// 13/14. BFS & DFS
void bfs(TreeNode root){ var q=new ArrayDeque<TreeNode>(); q.add(root); while(!q.isEmpty()){ var n=q.poll(); if(n.left!=null)q.add(n.left); if(n.right!=null)q.add(n.right);} }
void dfs(TreeNode n){ if(n==null) return; dfs(n.left); dfs(n.right); }

// 15. Dijkstra
int[] dijkstra(List<List<Edge>> g, int src){ var dist=new int[g.size()]; Arrays.fill(dist, Integer.MAX_VALUE); dist[src]=0;
 var pq=new PriorityQueue<State>(Comparator.comparingInt(s->s.dist)); pq.add(new State(0,src));
 while(!pq.isEmpty()){ var s=pq.poll(); if(s.dist>dist[s.node]) continue; for(var e:g.get(s.node)){ int nd=s.dist+e.w; if(nd<dist[e.to]){ dist[e.to]=nd; pq.add(new State(nd,e.to)); }}} return dist; }

// 16. Matrix DFS
int[][] DIRS={{1,0},{-1,0},{0,1},{0,-1}};
void dfsGrid(char[][] g,int r,int c){ if(r<0||r>=g.length||c<0||c>=g[0].length||g[r][c]!='1') return; g[r][c]='0'; for(var d:DIRS) dfsGrid(g,r+d[0],c+d[1]); }

// 17. Backtracking - subsets
void subsets(int[] nums,int i,List<Integer> cur,List<List<Integer>> res){ res.add(new ArrayList<>(cur)); for(int j=i;j<nums.length;j++){cur.add(nums[j]); subsets(nums,j+1,cur,res); cur.removeLast();} }

// 18. Trie
class TrieNode{ TrieNode[] ch=new TrieNode[26]; boolean end; }
class Trie{ TrieNode r=new TrieNode(); void insert(String w){ var c=r; for(char x:w){ int i=x-'a'; if(c.ch[i]==null) c.ch[i]=new TrieNode(); c=c.ch[i]; } c.end=true; } }

// 19. Greedy - interval scheduling
Arrays.sort(intervals, Comparator.comparingInt(a->a[1])); int end=Integer.MIN_VALUE, cnt=0; for(int[] in: intervals){ if(in[0]>=end) end=in[1]; else cnt++; }

// 20. DP - knapsack 1D optimized, LCS
int knapsack(int[] wt,int[] val,int W){ int[] dp=new int[W+1]; for(int i=0;i<wt.length;i++) for(int w=W;w>=wt[i];w--) dp[w]=Math.max(dp[w],dp[w-wt[i]]+val[i]); return dp[W]; }
int lcs(String a,String b){ int[][] dp=new int[a.length()+1][b.length()+1]; for(int i=1;i<=a.length();i++) for(int j=1;j<=b.length();j++) dp[i][j]= a.charAt(i-1)==b.charAt(j-1)?1+dp[i-1][j-1]:Math.max(dp[i-1][j],dp[i][j-1]); return dp[a.length()][b.length()]; }

// 21. Union-Find
class DSU{ int[] p,r; DSU(int n){p=IntStream.range(0,n).toArray(); r=new int[n];} int find(int x){return p[x]==x?x:(p[x]=find(p[x]));} void union(int a,int b){a=find(a);b=find(b); if(a==b)return; if(r[a]<r[b])p[a]=b;else if(r[a]>r[b])p[b]=a;else{p[b]=a; r[a]++;}} }

// Sliding window max - deque O(n)
int[] maxWindow(int[] a,int k){ var dq=new ArrayDeque<Integer>(); var res=new int[a.length-k+1];
 for(int i=0;i<a.length;i++){while(!dq.isEmpty()&&a[dq.peekLast()]<=a[i])dq.pollLast(); dq.addLast(i); if(dq.peekFirst()<=i-k)dq.pollFirst(); if(i>=k-1)res[i-k+1]=a[dq.peekFirst()];} return res; }
```

> **How to pick in interview:** Read constraints → spot keyword → map to pattern above → state time/space → code template. If `sorted` + `pair` → Two Pointers; `substring` → Sliding Window; `k` + `largest` → Heap; `shortest` → BFS; `all combinations` → Backtracking; `optimal + overlapping subproblems` → DP.

## Related
- [[Coding Patterns/DSA-Roadmap-AlgoMaster|DSA Roadmap (AlgoMaster)]], how to schedule these patterns against a deadline
- [[Coding Patterns/01_Array/02 - Two Pointers|Two Pointers]] · [[Coding Patterns/01_Array/03 - Sliding Window|Sliding Window]]
- [[Coding Patterns/03_Stack_Heap/02 - Top K Elements|Top K Elements]] · [[Coding Patterns/07_Backtracking_DP/02 - Dynamic Programming|Dynamic Programming]]
- [[Java/07_DSA/Array]] · [[Java/07_DSA/HashMap]] · [[Java/07_DSA/Heap]]

*Category: CheatSheet*