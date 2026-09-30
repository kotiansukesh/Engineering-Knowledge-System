---
title: "AI Master Dashboard"
category: "AI"
type: "dashboard"
tags: [dashboard, dataview, tasks, ai]
created: "2026-09-30"
completed: false
reviewed: ""
sr-due: ""
---

# AI Master Dashboard

## Today's Review Queue

```dataviewjs
const today = dv.date("today");
const notes = dv.pages('"AI"')
  .where(p => p.category && p.category.startsWith("AI/"))
  .where(p => !["README","folder-MOC","root-MOC","dashboard","study-plan"].includes(p.type));
const due = notes.where(p => p["sr-due"] && dv.date(p["sr-due"]) <= today);
dv.table(["Note","Area","Due"], due.sort(p => p["sr-due"]).map(p => [p.file.link,p.category,p["sr-due"]]));
if (!due.length) dv.paragraph("✅ No scheduled AI reviews are due today.");
```

## Progress by Area

```dataview
TABLE WITHOUT ID
  file.link AS "Area",
  length(rows) AS "Notes",
  length(filter(rows, (r) => r.completed = true)) AS "Done",
  round(length(filter(rows, (r) => r.completed = true)) / length(rows) * 100) + "%" AS "Progress"
FROM "AI"
WHERE type = "folder-MOC"
GROUP BY category
SORT category ASC
```

## Practice Tasks

```tasks
not done
path includes AI
sort by due
limit 30
```

## Stale Notes (>14 days)

```dataviewjs
const today = dv.date("today");
const notes = dv.pages('"AI"')
  .where(p => p.category && p.category.startsWith("AI/"))
  .where(p => !["README","folder-MOC","root-MOC","dashboard","study-plan"].includes(p.type));
const stale = notes.where(p => !p.reviewed || (today - dv.date(p.reviewed) > dv.duration({days:14})));
dv.table(["Note","Last Reviewed","Difficulty"], stale.sort(p => p.reviewed || "").map(p => [p.file.link,p.reviewed || "Never",p.difficulty || "—"]));
```

## Navigation

- [[README|AI MOC]]
- [[99_Revision/Study-Plan.md|Study Plan]]
- [[00 - AI Engineering Decision Framework|Decision Framework]]
- [[00 - AI Practice Engine|Practice Engine]]
- [[99_Revision/Interview Bank.md|Interview Bank]]
- [[99_Revision/Capstone Checklist.md|Capstone Checklist]]

---

*This dashboard tracks evidence, not just note completion.*
