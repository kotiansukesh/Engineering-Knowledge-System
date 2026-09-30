---
title: "09 Advanced README"
category: "Coding Patterns/09_Advanced"
tags: [MOC, folder, advanced, optional]
created: "2026-09-29"
completed: false
reviewed: ""
sr-due: ""
---

# 09 Advanced Patterns (Optional)

> Part of [[README|Coding Patterns MOC]] • `Coding Patterns/09_Advanced`
> These patterns extend the core 20 and appear in harder problems / specific domains.
---

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
---

## Notes Index

```dataview
TABLE WITHOUT ID
 file.link as "Note",
 category as "Category",
 choice(completed, "✅", "⬜") as "Done",
 difficulty as "Difficulty",
 reviewed as "Last Reviewed",
 "sr-due" as "SR Due"
FROM "Coding Patterns/09_Advanced"
WHERE category AND file.name != "README"
SORT file.name ASC
```
---

## Quick Links

- [[README|← Back to Coding Patterns MOC]]
- [[Master Dashboard|📊 Master Dashboard]]
---

*Folder: Coding Patterns/09_Advanced • Part of [[README|Coding Patterns MOC]]*