---
title: Dashboard
category: overview
tags: [architect, dashboard]
created: 2026-09-03
completed: false
---

# Dashboard

## Overall progress
```dataviewjs
const pages = dv.pages('"Architect"').where(p => p.completed !== undefined);
const done = pages.where(p => p.completed).length;
dv.paragraph(`**Overall: ${done}/${pages.length} (${pages.length ? Math.round(done/pages.length*100) : 0}%)**`);
```

## By folder
```dataviewjs
const folders = ["00_Overview","01_Architecture-Foundations","02_Requirements-Quality-Attributes"];
for (const f of folders) {
  const pages = dv.pages(`"${f}"`).where(p => p.completed !== undefined);
  const done = pages.where(p => p.completed).length;
  const pct = pages.length ? Math.round(done/pages.length*100) : 0;
  dv.paragraph(`**${f}**: ${done}/${pages.length} — ${pct}%`);
}
```

## Overdue / incomplete
```dataview
TABLE file.mtime AS Modified
FROM "Architect"
WHERE completed = false
SORT file.mtime ASC
LIMIT 20
```

## Open tasks
```dataview
TASK WHERE !completed
SORT file.mtime ASC
LIMIT 30
```
