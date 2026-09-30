---
title: "03 Agentic Ai README"
category: "AI/03_Agentic-AI"
type: "folder-MOC"
tags: [MOC, folder]
created: "2026-09-27"
completed: false
reviewed: ""
sr-due: ""
---

# 03 Agentic AI

> **Enter this domain after basic LLM API, structured-output and retrieval foundations.**
>
> The default progression is **workflow → single agent → bounded delegation → multi-agent only when a measured decomposition justifies it**.

## Decision rule

Prefer the least autonomous mechanism that satisfies the requirement. Before adding an agent, compare it with a deterministic workflow. Before adding multiple agents, identify the concrete coordination benefit and the extra failure, latency, cost and observability burden.

> Part of [[README|AI MOC]] • `AI/03_Agentic-AI`

## Progress Overview

```dataviewjs
const category = dv.current().category;
const pages = dv.pages(`"${category}"`).where(p => p.category != null && p.file.name != "README");
const total = pages.length;
const done = pages.where(p => p.completed === true).length;
const pct = total ? Math.round(done/total*100) : 0;
const bar = (p, w=20) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w-Math.round(p/100*w));
dv.paragraph(`**Total: ${total} notes | Completed: ${done} | Remaining: ${total-done}** — \`${pct}%\``);
dv.paragraph(`\`${bar(pct)}\` **${pct}%**`);
if (total === done && total > 0) dv.paragraph(`🎉 *All notes completed!*`);
```

> **Fallback (if DataviewJS disabled):**
```dataview
TABLE WITHOUT ID
 length(rows) as "Total",
 length(filter(rows, (r) => r.completed)) as "Completed",
 length(filter(rows, (r) => !r.completed)) as "Remaining"
FROM "AI/03_Agentic-AI"
WHERE category AND file.name != "README"
GROUP BY true
```

## Notes Index

```dataview
TABLE WITHOUT ID
 file.link as "Note",
 category as "Category",
 choice(completed, "✅", "⬜") as "Done",
 difficulty as "Difficulty",
 reviewed as "Last Reviewed",
 "sr-due" as "SR Due"
FROM "AI/03_Agentic-AI"
WHERE category AND file.name != "README"
SORT file.name ASC
```

## Spaced Repetition Status

```dataview
TABLE WITHOUT ID
 file.link as "Note",
 reviewed as "Last Reviewed",
 "sr-due" as "Due",
 choice(!reviewed, "🔴 Never", choice(date(now)-reviewed > dur(7 days), "🟡 Stale", "🟢 Fresh")) as "Status"
FROM "AI/03_Agentic-AI"
WHERE category AND file.name != "README" AND (reviewed OR "sr-due")
SORT "sr-due" ASC
```

## Practice Tasks (from Notes)

```tasks
not done
path includes AI/03_Agentic-AI
sort by due
group by filename
limit 20
```


## Quick Links

- [[README|← Back to AI MOC]]
- [[Master Dashboard|📊 Master Dashboard]]

---

*Folder: AI/03_Agentic-AI • Part of [[README|AI MOC]]*