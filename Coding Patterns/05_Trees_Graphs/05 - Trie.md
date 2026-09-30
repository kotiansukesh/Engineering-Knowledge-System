---
title: "Trie"
type: pattern
pattern: 15
domain: "Tree / String"
category: "Coding Patterns/05_Trees_Graphs"
advanced: false
mastery: learn
recognition_score: 0
difficulty: "Medium"
leetcode: [208, 211, 212]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - tree-string
---

# Trie

> Pattern #15 · Tree / String

## Recognition

- Prefix lookup
- Dictionary of strings
- Autocomplete or prefix-based search

### Strong signals
- Prefix lookup
- Dictionary of strings

### Do not infer it from
- A keyword alone
- A familiar example without checking constraints

## Invariant

> Each trie path represents exactly one character prefix, so a node contains all strings sharing that prefix.

## Mental model

Maintain the smallest state that completely describes the part of the search space still relevant to the answer.

## Core implementation

```java
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd = false;
}

class Trie {
    private final TrieNode root = new TrieNode();

    void insert(String word) {
        var cur = root;
        for (char c : word.toCharArray()) {
            int i = c - 'a';
            if (cur.children[i] == null) cur.children[i] = new TrieNode();
            cur = cur.children[i];
        }
        cur.isEnd = true;
    }

    boolean search(String word) {
        var node = walk(word);
        return node != null && node.isEnd;
    }

    boolean startsWith(String prefix) {
        return walk(prefix) != null;
    }

    private TrieNode walk(String s) {
        var cur = root;
        for (char c : s.toCharArray()) {
            int i = c - 'a';
            if (cur.children[i] == null) return null;
            cur = cur.children[i];
        }
        return cur;
    }
}

// Word Search II — LC 212 (Trie + DFS pruning)
class Solution {
    TrieNode root = new TrieNode();
    int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
    public java.util.List<String> findWords(char[][] board, String[] words) {
        for (String w : words) insert(w);
        var res = new java.util.ArrayList<String>();
        for (int i = 0; i < board.length; i++)
            for (int j = 0; j < board[0].length; j++)
                dfs(board, i, j, root, res);
        return res;
    }
    void dfs(char[][] b, int r, int c, TrieNode node, java.util.List<String> res) {
        char ch = b[r][c];
        if (ch == '#' || node.children[ch - 'a'] == null) return;
        node = node.children[ch - 'a'];
        if (node.isEnd) { res.add(node.word); node.isEnd = false; } // avoid duplicates
        b[r][c] = '#';
        for (int[] d : dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < b.length && nc >= 0 && nc < b[0].length) dfs(b, nr, nc, node, res);
        }
        b[r][c] = ch;
    }
    // Add String word field to TrieNode for LC 212
}
```

## Variants

Start with the core implementation. Introduce a variant only when the required state or proof changes.

## When to use
- autocomplete, spell check, word games, `startsWith(prefix)` queries; dictionary with prefix search.

## When NOT to use
- exact lookup only (HashMap is faster, simpler); static dictionary with no prefix queries (sorted array + binary search).

## Complexity & trade-offs

| Operation | Time | Space |
|-----------|------|-------|
| insert, search, startsWith | O(L) per word length | O(total characters) |

| Aspect | Trie | HashMap of Words | Sorted Array + Binary Search |
|--------|------|------------------|------------------------------|
| Insert | O(L) | O(L) hashing | O(n) shifting |
| Search exact | O(L) | O(L), fast constant | O(log n + L) |
| Prefix search | O(L + k) | not supported | lower bound, then scan |
| Space | O(total chars), shared prefixes | O(total chars), no sharing | O(total chars) |
| Pick when | autocomplete, prefix queries | exact lookup only | static dictionary |

## Pitfalls

- Use `walk` helper to share code between `search` and `startsWith`.
- `search` **must** check `isEnd`; `startsWith` **must not**.
- For non-lowercase or Unicode, use `Map<Character, TrieNode>` instead of size-26 array.
- Word Search II: mark `isEnd = false` after adding to results to avoid duplicates (or use a result set).
- Java 25: can use `record` for immutable nodes if building once, but mutable is standard for dynamic insert.

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 208 | Medium |
| 211 | Medium |
| 212 | Hard |

## Interview Q&A

(Senior Depth)

**Q: Why does Trie + DFS prune Word Search II so effectively?**
**A:** Without Trie, DFS from each cell tries all 4^L paths. With Trie, at each step we check `node.children[ch]`. If null, the current prefix doesn't exist in *any* dictionary word — the entire subtree is dead. We prune before exploring 4 directions. For a 4x4 board with 10 words, this reduces explored paths from ~4^10 to ~10 * 4^avg_len.

**Q: Trie vs HashMap for exact string lookup — when does HashMap win?**
**A:** HashMap: O(L) hashing + O(1) average lookup, very fast constant factors. Trie: O(L) char-by-char with pointer chasing. For pure exact lookup (no prefix), HashMap wins on speed and simplicity. Trie wins when you need prefix operations or autocomplete.

**Q: How do you implement a Trie for Unicode or case-insensitive strings?**
**A:** Replace `children[26]` with `Map<Character, TrieNode>`. For case-insensitive, normalize to lowercase on insert/search (`Character.toLowerCase(c)`). Trade-off: map has higher overhead per node but handles arbitrary alphabets. For a-z only, array is faster and cache-friendly.

**Q: Compressed Trie (Radix Tree / Patricia Trie) — what's the difference?**
**A:** Standard Trie has one node per character. Compressed Trie merges linear chains (nodes with single child) into edges labeled with strings. Saves space for long words with unique prefixes (e.g., "application", "apply" → common "appl" then branch). More complex insert/search; used in routing tables (IP prefixes) and databases.

**Q: Add and Search Words (LC 211) — how to handle `.` wildcard?**
**A:** `search(word)` with `.` matching any char. Recursive: at `.`, try all 26 children; at letter, follow that child. Time: O(26^d * L) where d = number of dots. For many dots, this is expensive — but dictionary size is typically small enough.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Trie? :: **A:** prefix search, autocomplete, word dictionary, XOR max/min, IP routing #flashcard

#flashcard
**Q:** Time/space complexity of Trie? :: **A:** Time: O(L) per operation (L=word length), Space: O(N×Σ) N words, Σ alphabet #flashcard

#flashcard
**Q:** When do you NOT use Trie? :: **A:** small dataset (hashset O(1) simpler), no prefix queries needed #flashcard

#flashcard
**Q:** Core Java 25 snippet for Trie? :: **A:** `class TrieNode{ TrieNode[] ch=new TrieNode[26]; boolean end; } void insert(String w){ TrieNode n=root; for(char c:w){ if(n.ch[c-'a']==null) n.ch[c-'a']=new TrieNode(); n=n.ch[c-'a']; } n.end=true; }` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory
- [ ] Write the core template from memory
- [ ] Solve one unseen problem without hints
- [ ] Explain the invariant aloud
- [ ] Update mastery and next_review after review


## Related

- [[05_Trees_Graphs/01 - Binary Tree Traversal|Binary Tree Traversal]] (Trie is a tree)
- [[01_Array/03 - Sliding Window|Sliding Window]] (string problems)
- [[Java/07_DSA/Trees]]
