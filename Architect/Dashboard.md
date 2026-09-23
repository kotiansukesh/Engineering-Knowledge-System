---
title: "Architect Dashboard"
category: dashboard
tags: [dashboard, architecture, system-design, adr, c4, progress, spaced-repetition]
created: 2026-09-26
completed: false
reviewed: ""
sr-due: ""
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---

# Software Architecture Dashboard

> Live tracking across all architecture topics: Foundations, Quality Attributes, Styles, Patterns, DDD, Data, APIs, Non-Functional, Governance, System Design Interviews. Tables update on reload. Pin this tab.

---

## Overall Progress

```dataviewjs
const vaults = ["Architect/00_Overview", "Architect/01_Architecture-Foundations", "Architect/02_Requirements-Quality-Attributes", "Architect/03_Architecture-Styles", "Architect/04_Design-Patterns-Building-Blocks", "Architect/05_DDD-Modeling", "Architect/06_Data-Architecture", "Architect/07_Integration-APIs", "Architect/08_NonFunctional-Ops", "Architect/09_Governance-Documentation", "Architect/10_System-Design-Interviews", "Architect/99_Revision"];
const rows = vaults.map(v => {
  const pages = dv.pages(`"${v}"`).where(p => p.category && p.file.name != "README");
  const tot = pages.length;
  const done = pages.where(p => p.completed).length;
  const pct = tot ? Math.round(done/tot*100) : 0;
  const stale = pages.where(p => !p.reviewed || (dv.date("now")-dv.date(p.reviewed)).days > 7).length;
  const due = pages.where(p => p["sr-due"] && dv.date(p["sr-due"]) <= dv.date("now")).length;
  return [`[[${v}/README|${v.split("/").pop()}]]`, tot, done, `${pct}%`, stale ? `⚠️ ${stale}` : "✅", due ? `🔴 ${due}` : "✅"];
});
dv.table(["Folder", "Total", "Done", "%", "Stale >7d", "SR Due"], rows);
```

---

## Topic Progress Breakdown

```dataviewjs
const folders = [
  ["Architect/01_Architecture-Foundations", "01 Foundations"],
  ["Architect/02_Requirements-Quality-Attributes", "02 Quality Attributes"],
  ["Architect/03_Architecture-Styles", "03 Arch Styles"],
  ["Architect/04_Design-Patterns-Building-Blocks", "04 Patterns/Blocks"],
  ["Architect/05_DDD-Modeling", "05 DDD Modeling"],
  ["Architect/06_Data-Architecture", "06 Data Architecture"],
  ["Architect/07_Integration-APIs", "07 Integration/APIs"],
  ["Architect/08_NonFunctional-Ops", "08 Non-Functional"],
  ["Architect/09_Governance-Documentation", "09 Governance"],
  ["Architect/10_System-Design-Interviews", "10 SysDesign Interviews"],
  ["Architect/99_Revision", "99 Revision"],
];

const bar = (p,w=12) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w-Math.round(p/100*w));
const rows = folders.map(([f,label]) => {
  const pages = dv.pages(`"${f}"`).where(p => p.category && p.file.name != "README");
  const tot = pages.length, don = pages.where(p=>p.completed).length;
  const pct = tot ? Math.round(don/tot*100) : 0;
  const stale = pages.where(p=> !p.reviewed || (dv.date("now")-dv.date(p.reviewed)).days > 7).length;
  return [`[[${f}/README|${label}]]`, tot, don, `${pct}%`, `\`${bar(pct)}\` ${pct}%`, stale ? `⚠️ ${stale}` : "✅"];
});
dv.table(["Topic", "Notes", "Done", "%", "Progress", "Stale >7d"], rows);
```

---

## Overdue Reviews (>7 Days or Never Reviewed)

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", reviewed as "Last Reviewed", date(now)-reviewed as "Days Ago"
FROM "Architect"
WHERE category AND file.name != "README" AND (!reviewed OR date(now)-reviewed > dur(7 days))
SORT reviewed ASC
LIMIT 30
```

---

## Spaced Repetition Due Today

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", "sr-due" as "Due", reviewed as "Last Reviewed"
FROM "Architect"
WHERE category AND file.name != "README" AND "sr-due" AND date("sr-due") <= date(now)
SORT "sr-due" ASC
```

---

## Interview Banks (Quick Links)

- [[Architect/10_System-Design-Interviews/Interview-Bank|System Design Interview Bank]]
- [[Architect/99_Revision/Interview-Bank|Revision Interview Bank]]

---

## Study Plan Tasks

```dataview
TASK WHERE !completed
FROM "Architect/00_Overview/Study Plan" OR "Architect/99_Revision/Study Plan"
GROUP BY file.link
```

---

## ADR Index (Architecture Decision Records)

```dataview
TABLE WITHOUT ID file.link as "ADR", category as "Category", tags as "Tags", created as "Created"
FROM "Architect"
WHERE tags AND contains(tags, "adr")
SORT created DESC
```

---

## Excalidraw Diagrams

Each note has a `## Diagram` section. For hand-drawn C4/Architecture diagrams:
1. Open any Architecture note
2. `Cmd+P` → `Excalidraw: New from template → Architecture Diagram`
3. Save as `<topic>-diagram.excalidraw.md` in same folder
4. Embed in note: `![[What-is-Architecture-diagram]]`

---

## Related

- [[README|Architect MOC]]
- [[Master Dashboard|Global Dashboard]]
- [[_templates/Arch-Note-Template.md|Architecture Note Template]]
- [[_templates/Architecture Diagram.excalidraw.md|Excalidraw Template]]

---

*Dataview required. Enable in Settings → Community plugins.*