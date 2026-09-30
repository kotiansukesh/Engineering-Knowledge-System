---
title: "Master Dashboard"
category: overview
tags: [dashboard, master, progress, spaced-repetition]
created: 2026-09-23
completed: false
---

# Master Dashboard

> Live tracking across the four top-level learning domains: `Java/`, `Architect/`, `AI/`, and `Coding Patterns/`. These are folders inside this single vault, not separate vaults. Tables update on reload. Pin this tab.

## 🧭 Knowledge System Control Plane

**Learning:** Understand → Build → Measure → Break → Decide → Explain → Review → Redesign

| Control | Purpose |
|---|---|
| [[00 - Knowledge System/Knowledge Model]] | note types and quality model |
| [[00 - Knowledge System/Learning Graph]] | prerequisites and cross-domain relationships |
| [[Evidence/README]] | implementations, benchmarks, failures, ADRs and evaluations |
| [[Build Lab/README]] | portfolio systems and capstone progression |
| [[00 - Knowledge System/10x Exercises]] | 1× / 10× / 100× redesign reasoning |
| [[00 - Knowledge System/Failure Engineering]] | deliberate failure analysis |
| [[00 - Knowledge System/Decision Notes]] | reusable engineering decisions |
| [[00 - Knowledge System/Agent Workflow]] | AI-assisted repository operating loop |
| [[00 - Knowledge System/Maintenance Guide]] | freshness and cleanup cadence |

### Evidence pipeline

**Knowledge → Practice → Evidence → Capability**

A completion checkbox is not mastery. Prefer an implementation, measurement, failure experiment, decision record or independent defense.

## Overall Progress — One Vault

```dataviewjs
const vaults = ["Java", "Architect", "AI", "Coding Patterns"];
const rows = vaults.map(v => {
  const pages = dv.pages(`"${v}"`).where(p => p.category != null && p.file.name != "README");
  const tot = pages.length;
  const done = pages.where(p => p.completed === true).length;
  const pct = tot ? Math.round(done/tot*100) : 0;
  const stale = pages.where(p => !p.reviewed || (dv.date("now")-dv.date(p.reviewed)).days > 7).length;
  const due = pages.where(p => p["sr-due"] && dv.date(p["sr-due"]) <= dv.date("now")).length;
  return [`[[${v}/README|${v}]]`, tot, done, `${pct}%`, stale ? `⚠️ ${stale}` : "✅", due ? `🔴 ${due}` : "✅"];
});
dv.table(["Vault", "Total", "Done", "%", "Stale >7d", "SR Due"], rows);
```

## 🏁 Current Sprint Phase (Auto-Calculated)

```dataviewjs
const startDate = dv.date("2026-09-28"); // Program start
const now = dv.date("now");
const weeksElapsed = Math.floor((now - startDate).days / 7);

const phases = {
  "Java": [
    {phase: "Core Java", weeks: "1-6", start: 1, end: 6},
    {phase: "Spring Ecosystem", weeks: "7-12", start: 7, end: 12},
    {phase: "Patterns + DSA", weeks: "13-18", start: 13, end: 18},
    {phase: "Advanced + Interview", weeks: "19-24", start: 19, end: 24}
  ],
  "Architect": [
    {phase: "Foundations", weeks: "1-3", start: 1, end: 3},
    {phase: "Styles + Patterns", weeks: "4-7", start: 4, end: 7},
    {phase: "Advanced Architecture", weeks: "8-13", start: 8, end: 13},
    {phase: "Ops + SysDesign Interviews", weeks: "14-18", start: 14, end: 18}
  ],
  "AI": [
    {phase: "Foundations + RAG", weeks: "1-4", start: 1, end: 4},
    {phase: "Agentic AI", weeks: "5-8", start: 5, end: 8},
    {phase: "Production Platform", weeks: "9-14", start: 9, end: 14},
    {phase: "Gov + Capstone + Interview", weeks: "15-20", start: 15, end: 20}
  ],
  "Coding Patterns": [
    {phase: "Arrays + Strings", weeks: "1-4", start: 1, end: 4},
    {phase: "Trees + Graphs", weeks: "5-9", start: 5, end: 9},
    {phase: "DP + Backtracking", weeks: "10-14", start: 10, end: 14},
    {phase: "Mastery + Interview", weeks: "15-20", start: 15, end: 20}
  ]
};

const rows = Object.entries(phases).map(([vault, vaultPhases]) => {
  let currentPhase = vaultPhases[0];
  for (const p of vaultPhases) {
    if (weeksElapsed + 1 >= p.start && weeksElapsed + 1 <= p.end) {
      currentPhase = p;
      break;
    }
  }
  const weekInPhase = (weeksElapsed + 1) - currentPhase.start + 1;
  const phaseLength = currentPhase.end - currentPhase.start + 1;
  const progressInPhase = Math.max(0, Math.min(100, Math.round((weekInPhase / phaseLength) * 100)));
  const bar = "█".repeat(Math.max(0, Math.round(progressInPhase/10))) + "░".repeat(10 - Math.max(0, Math.round(progressInPhase/10)));
  return [`[[${vault}/README|${vault}]]`, `Week ${weeksElapsed + 1}`, currentPhase.phase, `${currentPhase.weeks}`, `${bar} ${progressInPhase}%`];
});

dv.table(["Vault", "Program Week", "Current Phase", "Phase Weeks", "Phase Progress"], rows);
```

## Per-Domain Breakdown

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
  ["Architect/11_Real-World-Case-Studies", "Arch: 11 Case Studies"],
  ["Architect/99_Revision", "Arch: 99 Revision"],
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
  ["Coding Patterns/99_Revision", "CP: 99 Revision"],
];

const bar = (p,w=14) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w-Math.round(p/100*w));
const rows = folders.map(([f,label]) => {
  const pages = dv.pages(`"${f}"`).where(p => p.category != null && p.file.name != "README");
  const tot = pages.length, don = pages.where(p=>p.completed === true).length;
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

## Last Reviewed Dashboard (All Domains)

```dataviewjs
const pages = dv.pages('"Java" OR "Architect" OR "AI" OR "Coding Patterns"').where(p=>p.category != null && p.file.name!="README" && p.reviewed);
const buckets = { "Today": 0, "1-3d": 0, "4-7d": 0, "8-14d": 0, "15-30d": 0, "30+d": 0 };
pages.forEach(p => {
  const days = Math.floor((dv.date("now") - dv.date(p.reviewed)).days);
  if (days === 0) buckets["Today"]++;
  else if (days <= 3) buckets["1-3d"]++;
  else if (days <= 7) buckets["4-7d"]++;
  else if (days <= 14) buckets["8-14d"]++;
  else if (days <= 30) buckets["15-30d"]++;
  else buckets["30+d"]++;
});
const total = pages.length || 1;
const rows = Object.entries(buckets).map(([k,v]) => [k, v, "█".repeat(Math.round(v/total*30))]);
dv.table(["Recency", "Count", "Distribution"], rows);
```

## Review Timeline (All Domains)

```dataviewjs
const pages = dv.pages('"Java" OR "Architect" OR "AI" OR "Coding Patterns"').where(p=>p.category != null && p.file.name!="README");
const rows = pages.map(p=>{
  const days = p.reviewed ? Math.floor((dv.date("now")-dv.date(p.reviewed)).days) : null;
  const ago = days===null?"— never —":days===0?"today":`${days}d ago`;
  const due = p["sr-due"];
  const dueStr = due? dv.date(due).toFormat("yyyy-MM-dd"):"—";
  const urgent = days===null?"🔴":days>14?"🟠":days>7?"🟡":"🟢";
  return [p.file.link, p.category || "—", p.completed===true?"✅":"⬜", p.reviewed? p.reviewed.toFormat("yyyy-MM-dd"):"—", ago, dueStr, urgent];
}).sort(p=>p[4],'desc');
dv.table(["Note","Category","Done","Last Reviewed","Ago","SR Due","Urgency"], rows);
```

## Interview Banks (Quick Links)

- [[Java/99_Revision/Interview Questions|Java Interview Bank]]
- [[Architect/99_Revision/Capstone-Checklist|Architect Capstone Checklist]]
- [[AI/99_Revision/Interview Bank|AI Interview Bank]]
- [[Coding Patterns/99_Revision/Study-Plan|Coding Patterns Study Plan]]

---

## Study Plan Tasks

```dataview
TASK WHERE !completed
FROM "Java/99_Revision/Study-Plan" OR "Architect/99_Revision/Study-Plan" OR "AI/99_Revision/Study-Plan" OR "Coding Patterns/99_Revision/Study-Plan"
GROUP BY file.link
```

## 🎯 This Week's Focus (Auto-Calculated)

```dataviewjs
const now = dv.date("now");
const weekStart = now.minus({days: now.day}); // Monday
const weekEnd = weekStart.plus({days: 6}); // Sunday

const plans = [
  ["Java", "Java/99_Revision/Study-Plan"],
  ["Architect", "Architect/99_Revision/Study-Plan"],
  ["AI", "AI/99_Revision/Study-Plan"],
  ["Coding Patterns", "Coding Patterns/99_Revision/Study-Plan"]
];

for (const [vault, path] of plans) {
  const page = dv.page(path);
  if (!page || !page.file?.tasks) continue;
  
  const tasks = page.file.tasks
    .filter(t => !t.completed && t.due)
    .filter(t => {
      const due = dv.date(t.due);
      return due >= weekStart && due <= weekEnd;
    })
    .sort(t => dv.date(t.due).toMillis());
  
  if (tasks.length > 0) {
    dv.paragraph(`### ${vault} (${tasks.length} tasks this week)`);
    const rows = tasks.slice(0, 8).map(t => [
      t.text,
      dv.date(t.due).toFormat("EEE M/d"),
      t.section ? `[[${page.file.path}|${t.section}]]` : ""
    ]);
    dv.table(["Task", "Due", "Section"], rows);
  }
}
```

## 📅 Weekly Calendar View

```dataviewjs
const now = dv.date("now");
const weekStart = now.minus({days: now.day});
const days = [];
for (let i = 0; i < 7; i++) {
  days.push(weekStart.plus({days: i}));
}

const studyPlanPaths = [
  "Java/99_Revision/Study-Plan",
  "Architect/99_Revision/Study-Plan",
  "AI/99_Revision/Study-Plan",
  "Coding Patterns/99_Revision/Study-Plan"
];

const allTasks = dv.pages(studyPlanPaths.join(' OR '))
  .flatMap(p => p.file?.tasks || [])
  .filter(t => !t.completed && t.due)
  .map(t => ({
    text: t.text,
    due: dv.date(t.due),
    vault: t.path.split("/")[0]
  }))
  .filter(t => t.due >= weekStart && t.due <= weekStart.plus({days: 13}));

const rows = days.map(d => {
  const dayTasks = allTasks.filter(t => t.due.toFormat("yyyy-MM-dd") === d.toFormat("yyyy-MM-dd"));
  return [
    d.toFormat("ccc M/d"),
    dayTasks.filter(t => t.vault === "Java").length,
    dayTasks.filter(t => t.vault === "Architect").length,
    dayTasks.filter(t => t.vault === "AI").length,
    dayTasks.filter(t => t.vault === "Coding Patterns").length,
    dayTasks.map(t => `• ${t.text}`).join("\n")
  ];
});

dv.table(["Day", "Java", "Architect", "AI", "Coding Patterns", "Tasks"], rows);
```

---

> **Dataview Required:** Enable `Settings → Community plugins → Dataview` for tables to render.
> **Pin this tab** — it's the landing page, not a reference note.