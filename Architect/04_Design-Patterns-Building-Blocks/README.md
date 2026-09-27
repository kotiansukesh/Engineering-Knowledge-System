---
title: "04 Design Patterns Building Blocks README"
category: "Architect/04_Design-Patterns-Building-Blocks"
type: "folder-MOC"
tags: [MOC, folder]
created: "2026-09-27"
completed: false
reviewed: ""
sr-due: ""
---

# 04 Design Patterns Building Blocks

> Part of [[README|Architect MOC]] • `Architect/04_Design-Patterns-Building-Blocks`

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
FROM "Architect/04_Design-Patterns-Building-Blocks"
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
FROM "Architect/04_Design-Patterns-Building-Blocks"
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
FROM "Architect/04_Design-Patterns-Building-Blocks"
WHERE category AND file.name != "README" AND (reviewed OR "sr-due")
SORT "sr-due" ASC
```

## Practice Tasks (from Notes)

```tasks
not done
path includes Architect/04_Design-Patterns-Building-Blocks
sort by due
group by filename
limit 20
```

> ⚠️ **Template Note:** The `Architect/04_Design-Patterns-Building-Blocks` placeholder above is replaced by the generate script (`python3 generate_folder_readmes.py`). The template file itself will show a Tasks error — this is expected. Generated README files have the actual folder path and work correctly.

## Quick Links

- [[README|← Back to Architect MOC]]
- [[Master Dashboard|📊 Master Dashboard]]

---

*Folder: Architect/04_Design-Patterns-Building-Blocks • Part of [[README|Architect MOC]]*