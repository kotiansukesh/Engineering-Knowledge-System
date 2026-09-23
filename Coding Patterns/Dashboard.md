---
title: "Coding Patterns Dashboard"
category: dashboard
tags: [dashboard, coding-patterns, progress, spaced-repetition, leetcode]
created: 2026-09-26
completed: false
---

# Coding Patterns Dashboard

> Live tracking for all 21 DSA patterns with LeetCode problems, spaced repetition, and practice tracking.

---

## Pattern Progress Overview

```dataviewjs
const folders = [
  ["Coding Patterns/01_Array", "01 Array"],
  ["Coding Patterns/02_LinkedList", "02 LinkedList"],
  ["Coding Patterns/03_Stack_Heap", "03 Stack/Heap"],
  ["Coding Patterns/04_Intervals_Search", "04 Intervals/Search"],
  ["Coding Patterns/05_Trees_Graphs", "05 Trees/Graphs"],
  ["Coding Patterns/06_Matrix", "06 Matrix"],
  ["Coding Patterns/07_Backtracking_DP", "07 Backtrack/DP"],
  ["Coding Patterns/08_Bit_Manipulation", "08 Bit Manipulation"],
];

const bar = (p, w = 12) => "█".repeat(Math.round(p / 100 * w)) + "░".repeat(w - Math.round(p / 100 * w));
const rows = [];

for (const [f, label] of folders) {
  const pages = dv.pages(`"${f}"`).where(p => p.category && p.file.name != "README");
  const tot = pages.length;
  const done = pages.where(p => p.completed).length;
  const pct = tot ? Math.round(done / tot * 100) : 0;
  const stale = pages.where(p => !p.reviewed || (dv.date("now") - dv.date(p.reviewed)).days > 7).length;
  const due = pages.where(p => p["sr-due"] && dv.date(p["sr-due"]) <= dv.date("now")).length;
  
  // Count total LeetCode problems in this folder
  let totalProblems = 0;
  let solvedProblems = 0;
  for (const pg of pages) {
    if (pg.leetcode && Array.isArray(pg.leetcode)) {
      totalProblems += pg.leetcode.length;
    }
    if (pg["problems-solved"] && Array.isArray(pg["problems-solved"])) {
      solvedProblems += pg["problems-solved"].length;
    }
  }
  
  rows.push([
    `[[${f}/README|${label}]]`,
    tot,
    done,
    `${pct}%`,
    `\`${bar(pct)}\` ${pct}%`,
    totalProblems,
    solvedProblems,
    stale ? `⚠️ ${stale}` : "✅",
    due ? `🔴 ${due}` : "✅"
  ]);
}

dv.table(["Pattern", "Notes", "Done", "%", "Progress", "LC Problems", "Solved", "Stale >7d", "SR Due"], rows);
```

---

## All LeetCode Problems by Pattern

```dataviewjs
const folders = [
  ["Coding Patterns/01_Array", "01 Array"],
  ["Coding Patterns/02_LinkedList", "02 LinkedList"],
  ["Coding Patterns/03_Stack_Heap", "03 Stack/Heap"],
  ["Coding Patterns/04_Intervals_Search", "04 Intervals/Search"],
  ["Coding Patterns/05_Trees_Graphs", "05 Trees/Graphs"],
  ["Coding Patterns/06_Matrix", "06 Matrix"],
  ["Coding Patterns/07_Backtracking_DP", "07 Backtrack/DP"],
  ["Coding Patterns/08_Bit_Manipulation", "08 Bit Manipulation"],
];

const allProblems = [];

for (const [f, label] of folders) {
  const pages = dv.pages(`"${f}"`).where(p => p.category && p.file.name != "README");
  for (const pg of pages) {
    if (pg.leetcode && Array.isArray(pg.leetcode)) {
      for (const pid of pg.leetcode) {
        // Check if this problem is marked solved
        const solved = pg["problems-solved"] && pg["problems-solved"].includes(pid);
        const solvedDate = pg["problems-solved-dates"] && pg["problems-solved-dates"][pid];
        
        allProblems.push({
          pattern: label,
          note: pg.file.link,
          problem: pid,
          title: `LC ${pid}`, // Will be enhanced if we have title mapping
          difficulty: pg.difficulty || "—",
          solved: solved ? "✅" : "⬜",
          solvedDate: solvedDate || "—",
          srDue: pg["sr-due"] ? dv.date(pg["sr-due"]).toFormat("yyyy-MM-dd") : "—"
        });
      }
    }
  }
}

// Sort by pattern, then problem number
allProblems.sort((a, b) => {
  if (a.pattern !== b.pattern) return a.pattern.localeCompare(b.pattern);
  return parseInt(a.problem) - parseInt(b.problem);
});

dv.table(
  ["Pattern", "Note", "Problem", "Difficulty", "Solved", "Solved Date", "SR Due"],
  allProblems.map(p => [p.pattern, p.note, p.problem, p.difficulty, p.solved, p.solvedDate, p.srDue])
);
```

---

## Problems Due for Review (Spaced Repetition)

```dataview
TABLE WITHOUT ID
  file.link as "Pattern Note",
  category as "Category",
  "sr-due" as "Due Date",
  reviewed as "Last Reviewed",
  "problems-solved" as "Problems Solved"
FROM "Coding Patterns"
WHERE category
  AND file.name != "README"
  AND "sr-due"
  AND date("sr-due") <= date(now)
SORT "sr-due" ASC
```

---

## Stale Patterns (>7 Days Since Review)

```dataview
TABLE WITHOUT ID
  file.link as "Pattern Note",
  category as "Category",
  reviewed as "Last Reviewed",
  date(now) - reviewed as "Days Ago"
FROM "Coding Patterns"
WHERE category
  AND file.name != "README"
  AND (!reviewed OR date(now) - reviewed > dur(7 days))
SORT reviewed ASC
```

---

## Practice Tasks (Tasks Plugin)

```dataview
TASK WHERE !completed
FROM "Coding Patterns"
GROUP BY file.link
```

---

## Weekly Practice Plan

| Day | Focus | Target |
|-----|-------|--------|
| Mon | Array patterns (Prefix Sum, Two Pointers, Sliding Window, Frequency) | 3 problems |
| Tue | LinkedList + Stack/Heap | 2 patterns × 1-2 problems |
| Wed | Intervals/Search + Trees/Graphs | 2 patterns × 1-2 problems |
| Thu | Matrix + Backtracking/DP | 2 patterns × 1-2 problems |
| Fri | Greedy + Bit Manipulation | 2 patterns × 1-2 problems |
| Sat | **Timed Mock**: 5 random Q&A + 1 LeetCode Medium | Timed |
| Sun | Review misses, update `reviewed` + `sr-due` | All due |

---

## Quick Actions

- [ ] **Create new pattern note** → Use `Pattern Template` in `_templates/`
- [ ] **Mark problem solved** → Add to `problems-solved` array in frontmatter with date
- [ ] **Set SR due** → After solving: `sr-due = today + 3d` (first), then +7, +14, +30, +90
- [ ] **Run weekly review** → Open this dashboard, check "SR Due" and "Stale" columns

---

## Excalidraw Diagrams

Each pattern note has a `## Diagram` section with Mermaid. For hand-drawn style:
1. Open any pattern note
2. `Cmd+P` → `Excalidraw: New drawing in folder`
3. Save as `<pattern-name>-diagram.excalidraw.md` in same folder
4. Embed in note: `![[Sliding Window-diagram]]`

---

## Related

- [[README|20 DSA Patterns Overview]]
- [[Interview-Bank|Interview Question Bank]]
- [[Cheat Sheet|Quick Reference]]
- [[Master Dashboard|Global Dashboard]]
- [[_templates/Pattern Template.md|Pattern Template]]

---

*Dataview required. Enable in Settings → Community plugins.*