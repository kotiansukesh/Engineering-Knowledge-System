---
title: "AI Dashboard"
category: dashboard
tags: [dashboard, ai, llm, rag, agents, progress, spaced-repetition]
created: 2026-09-26
completed: false
reviewed: ""
sr-due: ""
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---

# AI / LLM Engineering Dashboard

> Live tracking across all AI topics: Fundamentals, RAG, Agentic AI, Production, K8s, Governance. Tables update on reload. Pin this tab.

---

## Overall Progress

```dataviewjs
const vaults = ["AI/00_Overview", "AI/01_Fundamentals", "AI/02_RAG-Engineering", "AI/03_Agentic-AI", "AI/04_Production-Platform", "AI/05_Kubernetes-Operations", "AI/06_Architecture-Governance", "AI/07_Cross-Cutting", "AI/99_Revision"];
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
  ["AI/01_Fundamentals", "01 Fundamentals"],
  ["AI/02_RAG-Engineering", "02 RAG Engineering"],
  ["AI/03_Agentic-AI", "03 Agentic AI"],
  ["AI/04_Production-Platform", "04 Production Platform"],
  ["AI/05_Kubernetes-Operations", "05 K8s Operations"],
  ["AI/06_Architecture-Governance", "06 Arch Governance"],
  ["AI/07_Cross-Cutting", "07 Cross-Cutting"],
  ["AI/99_Revision", "99 Revision"],
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
FROM "AI"
WHERE category AND file.name != "README" AND (!reviewed OR date(now)-reviewed > dur(7 days))
SORT reviewed ASC
LIMIT 30
```

---

## Spaced Repetition Due Today

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", "sr-due" as "Due", reviewed as "Last Reviewed"
FROM "AI"
WHERE category AND file.name != "README" AND "sr-due" AND date("sr-due") <= date(now)
SORT "sr-due" ASC
```

---

## Interview Banks (Quick Links)

- [[AI/01_Fundamentals/Interview-Bank|AI Fundamentals Interview Bank]]
- [[AI/Interview-Bank|AI Master Interview Bank]]
- [[AI/99_Revision/Interview-Bank|Revision Interview Bank]]

---

## Study Plan Tasks

```dataview
TASK WHERE !completed
FROM "AI/99_Revision/Study Plan" OR "AI/00_Overview/Weekly Tracker"
GROUP BY file.link
```

---

## Excalidraw Diagrams

Each note has a `## Diagram` section with Mermaid. For hand-drawn style:
1. Open any AI note
2. `Cmd+P` → `Excalidraw: New from template → AI Diagram`
3. Save as `<topic>-diagram.excalidraw.md` in same folder
4. Embed in note: `![[LLM Fundamentals-diagram]]`

---

## Related

- [[README|AI MOC]]
- [[Master Dashboard|Global Dashboard]]
- [[_templates/AI Note Template.md|AI Note Template]]
- [[_templates/AI Diagram.excalidraw.md|Excalidraw Template]]

---

*Dataview required. Enable in Settings → Community plugins.*