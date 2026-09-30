---
title: "Overlapping Intervals"
type: pattern
pattern: 9
domain: "Intervals"
category: "Coding Patterns/04_Intervals_Search"
advanced: false
mastery: learn
recognition_score: 0
difficulty: "Medium"
leetcode: [- 56]
created: "2026-09-02"
reviewed:
next_review: "2026-10-07"
tags:
  - pattern
  - intervals
---

# Overlapping Intervals

> Pattern #9 · Intervals

## Recognition

- Ranges, bookings, meetings, time windows
- Overlap, merge, schedule, or minimum resources
- Sorting creates an order where local comparisons are sufficient

### Strong signals
- Ranges, bookings, meetings, time windows
- Overlap, merge, schedule, or minimum resources

### Do not infer it from
- A keyword alone
- A familiar example without checking constraints

## Invariant

> After sorting by start, all intervals that can still affect the current result are represented by the active interval or resource state.

## Mental model

This pattern reduces the search space by maintaining a compact state that represents all information needed for the next decision.

## Core implementation

```java
// Merge Intervals — LC 56
int[][] merge(int[][] intervals) {
    java.util.Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
    var merged = new java.util.ArrayList<int[]>();
    for (int[] in : intervals) {
        if (merged.isEmpty() || in[0] > merged.get(merged.size() - 1)[1]) {
            merged.add(in);
        } else {
            merged.get(merged.size() - 1)[1] = Math.max(merged.get(merged.size() - 1)[1], in[1]);
        }
    }
    return merged.toArray(new int[merged.size()][]);
}

// Insert Interval — LC 57 (same merge after adding newInterval)
int[][] insert(int[][] intervals, int[] newInterval) {
    var res = new java.util.ArrayList<int[]>();
    int i = 0, n = intervals.length;
    // add all before newInterval
    while (i < n && intervals[i][1] < newInterval[0]) res.add(intervals[i++]);
    // merge overlapping with newInterval
    while (i < n && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
        newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
        i++;
    }
    res.add(newInterval);
    // add remaining
    while (i < n) res.add(intervals[i++]);
    return res.toArray(new int[res.size()][]);
}

// Non-overlapping Intervals (min removals) — LC 435
// Sort by END, greedy keep earliest finishing
int eraseOverlapIntervals(int[][] intervals) {
    java.util.Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
    int end = Integer.MIN_VALUE, removed = 0;
    for (int[] in : intervals) {
        if (in[0] >= end) end = in[1];
        else removed++;
    }
    return removed;
}
```

## Variants

Start with the core implementation. Introduce a variant only when the problem changes the invariant or required state.

## When to use

- merge intervals; insert interval; min removals for non-overlapping; meeting scheduling; "overlap" / "interval" keywords.
- **NOT:** point stabbing queries (which intervals contain a point — use interval tree); dynamic insert/delete with queries (use balanced BST or segment tree).

## When NOT to use

point stabbing queries (which intervals contain a point — use interval tree); dynamic insert/delete with queries (use balanced BST or segment tree).

## Complexity & trade-offs

| Operation | Time | Space |
|-----------|------|-------|
| Sort + scan | O(n log n) | O(n) for result |

| Aspect | Merge Intervals | Activity Selection (Greedy) | Interval Tree |
|--------|-----------------|----------------------------|---------------|
| Solves | union of all overlaps | max set of mutually non-overlapping | which intervals contain a point |
| Sort by | start | end | N/A (tree structure) |
| Time | O(n log n) | O(n log n) | O(n log n) build, O(log n + k) query |
| Pick when | merge, insert, meeting rooms | non-overlapping count, min removals | dynamic point-stabbing queries |

## Pitfalls

- **Sort by start for merge**, not end. End matters for activity selection.
- Edge condition: `<=` vs `<` — decide if touching intervals `[1,3],[3,5]` count as overlapping (usually yes for merge, no for activity selection).
- Return type `int[][]` needs `toArray(new int[size][])` with correct size.
- For insert interval, the three-phase approach (before, merge, after) is cleaner than binary search + insert + merge.

## Canonical problems

| LeetCode | Problem | Difficulty |
|---:|---|---|
| 56 | Medium |
| 57 | Medium |
| 986 | Medium |
| 435 | Medium |

## Interview Q&A

(Senior Depth)

**Q: Merge Intervals vs Non-overlapping Intervals — why different sort keys?**
**A:** Merge wants to *combine* overlapping intervals. Sorting by start brings overlapping intervals together so they can be merged in one pass. Activity selection wants to *pick* a max subset of non-overlapping intervals. Sorting by end picks the interval that finishes earliest, leaving maximum room for the rest — the classic greedy proof.

**Q: Insert Interval (LC 57) — why is the three-phase approach better than binary search?**
**A:** Binary search finds insert position, but you still need to scan left and right for overlaps. The three-phase linear scan (add before, merge overlap, add after) is O(n) total, simpler, and handles all edge cases (new interval before all, after all, spanning multiple). Same asymptotic, less code.

**Q: What if intervals are [1,3], [3,5] — do they overlap?**
**A:** Depends on problem definition. Merge Intervals (LC 56): typically `current.start <= last.end` → overlap, so `[1,3]` and `[3,5]` merge to `[1,5]`. Activity Selection: typically `current.start >= last.end` → non-overlapping, so they *don't* overlap and both can be picked. Always clarify or state your assumption.

**Q: Meeting Rooms II (LC 253) — how does it relate?**
**A:** Min rooms = max concurrent meetings. Sweep line: split each interval into (start, +1) and (end, -1) events, sort by time (end before start at same time), scan and track running sum. Max sum = min rooms. Alternative: min-heap of end times, O(n log n). Both are interval patterns but use sweep line / heap, not merge.

## Flashcards

#flashcard
**Q:** What is the trigger keyword for Overlapping Intervals? :: **A:** merge intervals, insert interval, meeting rooms, non-overlapping intervals, interval intersection #flashcard

#flashcard
**Q:** Time/space complexity of Overlapping Intervals? :: **A:** Time: O(n log n) sort, Space: O(n) output / O(1) extra #flashcard

#flashcard
**Q:** When do you NOT use Overlapping Intervals? :: **A:** point queries (use segment tree), dynamic intervals (use interval tree) #flashcard

#flashcard
**Q:** Core Java 25 snippet for Overlapping Intervals? :: **A:** `Arrays.sort(a, (x,y)->x[0]-y[0]); for(int[] iv:a){ if(ans.isEmpty() || ans.getLast()[1]<iv[0]) ans.add(iv); else ans.getLast()[1]=Math.max(ans.getLast()[1], iv[1]); }` #flashcard

## Review tasks

- [ ] Explain recognition signals from memory 📅 2026-10-01
- [ ] Write the template from memory 📅 2026-10-03
- [ ] Solve one unseen problem without hints 📅 2026-10-07
- [ ] Explain the invariant aloud 📅 2026-10-14

## Related

- [[04_Intervals_Search/02 - Modified Binary Search|Modified Binary Search]] (search in intervals)
- [[07_Backtracking_DP/03 - Greedy|Greedy]] (activity selection is greedy)
- [[Java/07_DSA/Array]]
