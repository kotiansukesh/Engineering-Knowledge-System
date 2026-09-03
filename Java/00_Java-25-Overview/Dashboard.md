---
title: "Dashboard — Progress"
category: overview
tags: [dashboard, java25, tracker]
created: 2026-09-03
completed: false
---

# Dashboard — Java 25 Progress

> Live tracking for `Java/` — 00..08 + 99_Revision. Tick `completed: true` in any note's frontmatter or the Study Plan checkboxes; these tables update instantly. Open as pinned tab.

## Overall

```dataviewjs
const pages = dv.pages('"Java"').where(p => p.category && p.file.name != "README");
const total = pages.length;
const done = pages.where(p => p.completed).length;
const pct = total ? Math.round(done/total*100) : 0;
const bar = (p,w=20) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w-Math.round(p/100*w));
dv.paragraph(`**Total: ${total} notes | Completed: ${done} | Remaining: ${total-done}** — \`${bar(pct)}\` **${pct}%**`);
if (!total) dv.paragraph("> No notes with `category` yet. Check frontmatter.");
```

```dataview
TABLE WITHOUT ID
  length(rows) as "Total",
  length(filter(rows, (r) => r.completed)) as "Completed",
  length(filter(rows, (r) => !r.completed)) as "Remaining"
FROM "Java"
WHERE category AND file.name != "README"
GROUP BY true
```

## By Folder

```dataviewjs
const folders = [
  ["00_Java-25-Overview","00 Overview (8→25)"],
  ["01_Core-Java","01 Core-Java"],
  ["02_OOP","02 OOP"],
  ["03_Collections","03 Collections"],
  ["04_Concurrency","04 Concurrency"],
  ["05_Spring","05 Spring"],
  ["06_Design-Patterns","06 Patterns"],
  ["07_DSA","07 DSA"],
  ["08_Modern-Java","08 Modern (8→25)"],
  ["09_Java-21-LTS","09 Java 21 LTS"],
  ["99_Revision","99 Revision"],
];
const bar = (p,w=14) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w-Math.round(p/100*w));
const rows = folders.map(([f,label]) => {
  const pages = dv.pages(`"Java/${f}"`).where(p => p.category && p.file.name != "README");
  const tot = pages.length, don = pages.where(p=>p.completed).length;
  const pct = tot ? Math.round(don/tot*100) : 0;
  const stale = pages.where(p=> !p.reviewed || (dv.date("now")-dv.date(p.reviewed)).days > 7).length;
  return [`[[Java/${f}/README|${label}]]`, tot, don, `${pct}%`, `\`${bar(pct)}\` ${pct}%`, stale ? `⚠️ ${stale}` : "✅"];
});
dv.table(["Folder","Total","Done","%","Progress","Stale >7d"], rows);
const all = dv.pages('"Java"').where(p=>p.category && p.file.name!="README");
dv.paragraph(`\n**Overall:** \`${bar(all.where(p=>p.completed).length/all.length*100 || 0,28)}\` **${all.length?Math.round(all.where(p=>p.completed).length/all.length*100):0}%** — ${all.where(p=>p.completed).length}/${all.length}`);
```

```dataview
TABLE WITHOUT ID file.folder as "Folder", length(rows) as "Total", length(filter(rows, (r)=>r.completed)) as "Done"
FROM "Java"
WHERE category AND file.name != "README"
GROUP BY file.folder
SORT file.folder ASC
```

## Overdue (>7 days or never reviewed)

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", reviewed as "Last Reviewed", date(now)-reviewed as "Ago"
FROM "Java"
WHERE category AND file.name != "README" AND (!reviewed OR date(now)-reviewed > dur(7 days))
SORT reviewed ASC
LIMIT 20
```

## Recently Reviewed (≤7d)

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed,"✅","⬜") as "Done", reviewed as "Last Reviewed", date(now)-reviewed as "Ago"
FROM "Java"
WHERE category AND file.name != "README" AND reviewed AND date(now)-reviewed <= dur(7 days)
SORT reviewed DESC
```

## Remaining

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", choice(completed,"✅","⬜") as "Done"
FROM "Java"
WHERE category AND file.name != "README" AND !completed
SORT category ASC, file.name ASC
```

## Review Timeline

```dataviewjs
const pages = dv.pages('"Java"').where(p=>p.category && p.file.name!="README");
const rows = pages.map(p=>{
  const days = p.reviewed ? Math.floor((dv.date("now")-dv.date(p.reviewed)).days) : null;
  const ago = days===null?"— never —": days===0?"today":`${days}d ago`;
  const due = p["sr-due"]||p.due;
  const dueStr = due? dv.date(due).toFormat("yyyy-MM-dd"):"—";
  const urgent = days===null?"🔴":days>14?"🔴":days>7?"🟡":"🟢";
  return [p.file.link, p.category, p.completed?"✅":"⬜", p.reviewed? p.reviewed.toFormat("yyyy-MM-dd"):"—", ago, dueStr, urgent];
}).sort(p=>p[4],'desc');
dv.table(["Note","Category","Done","Last Reviewed","Ago","SR Due","Urgency"], rows);
```

## Tasks — Study Plan

```dataview
TASK
FROM "Java/00_Java-25-Overview/Study Plan - Java 25"
GROUP BY file.link
```

## Quick Links

- [[Java/00_Java-25-Overview/README|00 Overview]] • [[Java/00_Java-25-Overview/LTS Evolution 8 to 25|LTS Evolution 8→25]] • [[Java/00_Java-25-Overview/Study Plan - Java LTS 8 to 25|Study Plan 8→25]]
- [[Java/00_Java-25-Overview/Java 8 LTS Overview|Java 8]] • [[Java/00_Java-25-Overview/Java 11 LTS Overview|Java 11]] • [[Java/00_Java-25-Overview/Java 17 LTS Overview|Java 17]] • [[Java/09_Java-21-LTS/README|09 Java 21 LTS]] • [[Java/00_Java-25-Overview/Whats New in Java 25|Whats New 25]]
- [[Java/99_Revision/README|99 Revision]] • [[Java/99_Revision/Interview Questions|Interview Q Bank]] • [[Java/README|Java MOC]]

> **Links not opening?** In Obsidian: ensure `Settings → Community plugins → Dataview` is **enabled** (required for the tables above). Then `Ctrl/Cmd+O` → type `Dashboard` → pin it. For this Markdown Dashboard file, open via `Obsidian → File → Open vault → /Users/sukesh/documents/github/obsidian` then navigate to `Java/00_Java-25-Overview/Dashboard.md`.

---
*Category: overview • dashboard*
