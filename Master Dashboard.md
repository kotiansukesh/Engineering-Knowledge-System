---
title: "Master Dashboard"
category: overview
tags: [dashboard, master, progress, spaced-repetition]
created: 2026-09-23
completed: false
---

# Master Dashboard

> Live tracking across all 4 vaults: `Java/`, `Architect/`, `AI/`, `Coding Patterns/`. Tables update on reload. Pin this tab.

## Overall Progress

```dataviewjs
const vaults = ["Java", "Architect", "AI", "Coding Patterns"];
const rows = vaults.map(v => {
  const pages = dv.pages(`"${v}"`).where(p => p.category && p.file.name != "README");
  const tot = pages.length;
  const done = pages.where(p => p.completed).length;
  const pct = tot ? Math.round(done/tot*100) : 0;
  const stale = pages.where(p => !p.reviewed || (dv.date("now")-dv.date(p.reviewed)).days > 7).length;
  const due = pages.where(p => p["sr-due"] && dv.date(p["sr-due"]) <= dv.date("now")).length;
  return [`[[${v}/README|${v}]]`, tot, done, `${pct}%`, stale ? `⚠️ ${stale}` : "✅", due ? `🔴 ${due}` : "✅"];
});
dv.table(["Vault", "Total", "Done", "%", "Stale >7d", "SR Due"], rows);
```

## Per-Folder Breakdown

```dataviewjs
const folders = [
  ["Java/00_Java-25-Overview", "Java: 00 Overview"],
  ["Java/01_Core-Java", "Java: 01 Core"],
  ["Java/02_OOP", "Java: 02 OOP"],
  ["Java/03_Collections", "Java: 03 Collections"],
  ["Java/04_Concurrency", "Java: 04 Concurrency"],
  ["Java/05_Spring", "Java: 05 Spring"],
  ["Java/06_Design-Patterns", "Java: 06 Patterns"],
  ["Java/07_DSA", "Java: 07 DSA"],
  ["Java/08_Modern-Java", "Java: 08 Modern"],
  ["Java/09_Java-21-LTS", "Java: 09 Java 21"],
  ["Java/10_LLD-Machine-Coding", "Java: 10 LLD"],
  ["Java/99_Revision", "Java: 99 Revision"],
  ["Architect/00_Overview", "Arch: 00 Overview"],
  ["Architect/01_Architecture-Foundations", "Arch: 01 Foundations"],
  ["Architect/02_Requirements-Quality-Attributes", "Arch: 02 Qualities"],
  ["Architect/03_Architecture-Styles", "Arch: 03 Styles"],
  ["Architect/04_Design-Patterns-Building-Blocks", "Arch: 04 Patterns"],
  ["Architect/05_DDD-Modeling", "Arch: 05 DDD"],
  ["Architect/06_Data-Architecture", "Arch: 06 Data"],
  ["Architect/07_Integration-APIs", "Arch: 07 APIs"],
  ["Architect/08_NonFunctional-Ops", "Arch: 08 Ops"],
  ["Architect/09_Governance-Documentation", "Arch: 09 Governance"],
  ["Architect/10_System-Design-Interviews", "Arch: 10 SysDesign"],
  ["Architect/99_Revision", "Arch: 99 Revision"],
  ["AI/00_Overview", "AI: 00 Overview"],
  ["AI/01_Fundamentals", "AI: 01 Fundamentals"],
  ["AI/02_RAG-Engineering", "AI: 02 RAG"],
  ["AI/03_Agentic-AI", "AI: 03 Agentic"],
  ["AI/04_Production-Platform", "AI: 04 Production"],
  ["AI/05_Kubernetes-Operations", "AI: 05 K8s"],
  ["AI/06_Architecture-Governance", "AI: 06 Gov"],
  ["AI/07_Cross-Cutting", "AI: 07 Cross-Cutting"],
  ["AI/99_Revision", "AI: 99 Revision"],
  ["Coding Patterns/01_Array", "CP: Array"],
  ["Coding Patterns/02_LinkedList", "CP: LinkedList"],
  ["Coding Patterns/03_Stack_Heap", "CP: Stack/Heap"],
  ["Coding Patterns/04_Intervals_Search", "CP: Intervals"],
  ["Coding Patterns/05_Trees_Graphs", "CP: Trees/Graphs"],
  ["Coding Patterns/06_Matrix", "CP: Matrix"],
  ["Coding Patterns/07_Backtracking_DP", "CP: Backtrack/DP"],
  ["Coding Patterns/08_Bit_Manipulation", "CP: Bit Manipulation"],
];

const bar = (p,w=14) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w-Math.round(p/100*w));
const rows = folders.map(([f,label]) => {
  const pages = dv.pages(`"${f}"`).where(p => p.category && p.file.name != "README");
  const tot = pages.length, don = pages.where(p=>p.completed).length;
  const pct = tot ? Math.round(don/tot*100) : 0;
  const stale = pages.where(p=> !p.reviewed || (dv.date("now")-dv.date(p.reviewed)).days > 7).length;
  return [`[[${f}/README|${label}]]`, tot, don, `${pct}%`, `\`${bar(pct)}\` ${pct}%`, stale ? `⚠️ ${stale}` : "✅"];
});
dv.table(["Folder", "Total", "Done", "%", "Progress", "Stale >7d"], rows);
```

## Overdue Reviews (>7 Days or Never Reviewed)

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", reviewed as "Last Reviewed", date(now)-reviewed as "Days Ago"
FROM "Java" OR "Architect" OR "AI" OR "Coding Patterns"
WHERE category AND file.name != "README" AND (!reviewed OR date(now)-reviewed > dur(7 days))
SORT reviewed ASC
LIMIT 30
```

## Spaced Repetition Due Today

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", "sr-due" as "Due", reviewed as "Last Reviewed"
FROM "Java" OR "Architect" OR "AI" OR "Coding Patterns"
WHERE category AND file.name != "README" AND "sr-due" AND date("sr-due") <= date(now)
SORT "sr-due" ASC
```

## Review Timeline (All Vaults)

```dataviewjs
const pages = dv.pages('"Java" OR "Architect" OR "AI" OR "Coding Patterns"').where(p=>p.category && p.file.name!="README");
const rows = pages.map(p=>{
  const days = p.reviewed ? Math.floor((dv.date("now")-dv.date(p.reviewed)).days) : null;
  const ago = days===null?"— never —":days===0?"today":`${days}d ago`;
  const due = p["sr-due"];
  const dueStr = due? dv.date(due).toFormat("yyyy-MM-dd"):"—";
  const urgent = days===null?"🔴":days>14?"🟠":days>7?"🟡":"🟢";
  return [p.file.link, p.category, p.completed?"✅":"⬜", p.reviewed? p.reviewed.toFormat("yyyy-MM-dd"):"—", ago, dueStr, urgent];
}).sort(p=>p[4],'desc');
dv.table(["Note","Category","Done","Last Reviewed","Ago","SR Due","Urgency"], rows);
```

## Interview Banks (Quick Links)

- [[Java/99_Revision/Interview-Bank|Java Interview Bank]]
- [[Architect/99_Revision/Interview-Bank|Architect Interview Bank]]
- [[AI/01_Fundamentals/Interview-Bank|AI Fundamentals Interview Bank]]
- [[AI/Interview-Bank|AI Master Interview Bank]]
- [[Coding Patterns/Interview-Bank|Coding Patterns Interview Bank]]

## Study Plan Tasks

```dataview
TASK WHERE !completed
FROM "Java/99_Revision/Study Plan" OR "Architect/00_Overview/Study Plan - Architect" OR "AI/00_Overview/Weekly Tracker"
GROUP BY file.link
```

---

> **Dataview Required:** Enable `Settings → Community plugins → Dataview` for tables to render.
> **Pin this tab** — it's the landing page, not a reference note.