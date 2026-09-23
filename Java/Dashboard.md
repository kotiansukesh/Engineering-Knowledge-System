---
title: "Java Dashboard"
category: dashboard
tags: [dashboard, java, spring, jvm, concurrency, progress, spaced-repetition]
created: 2026-09-26
completed: false
reviewed: ""
sr-due: ""
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---

# Java / Spring Dashboard

> Live tracking across all Java topics: Core Java, OOP, Collections, Concurrency, Spring, Design Patterns, DSA, Modern Java, Java 21 LTS, LLD. Tables update on reload. Pin this tab.

---

## Overall Progress

```dataviewjs
const vaults = ["Java/00_Java-25-Overview", "Java/01_Core-Java", "Java/02_OOP", "Java/03_Collections", "Java/04_Concurrency", "Java/05_Spring", "Java/06_Design-Patterns", "Java/07_DSA", "Java/08_Modern-Java", "Java/09_Java-21-LTS", "Java/10_LLD-Machine-Coding", "Java/99_Revision"];
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
  ["Java/01_Core-Java", "01 Core Java"],
  ["Java/02_OOP", "02 OOP"],
  ["Java/03_Collections", "03 Collections"],
  ["Java/04_Concurrency", "04 Concurrency"],
  ["Java/05_Spring", "05 Spring"],
  ["Java/06_Design-Patterns", "06 Design Patterns"],
  ["Java/07_DSA", "07 DSA"],
  ["Java/08_Modern-Java", "08 Modern Java"],
  ["Java/09_Java-21-LTS", "09 Java 21 LTS"],
  ["Java/10_LLD-Machine-Coding", "10 LLD/Machine Coding"],
  ["Java/99_Revision", "99 Revision"],
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
FROM "Java"
WHERE category AND file.name != "README" AND (!reviewed OR date(now)-reviewed > dur(7 days))
SORT reviewed ASC
LIMIT 30
```

---

## Spaced Repetition Due Today

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", "sr-due" as "Due", reviewed as "Last Reviewed"
FROM "Java"
WHERE category AND file.name != "README" AND "sr-due" AND date("sr-due") <= date(now)
SORT "sr-due" ASC
```

---

## Interview Banks (Quick Links)

- [[Java/99_Revision/Interview-Bank|Java Interview Bank]]
- [[Java/99_Revision/Interview Questions|Java Interview Questions]]

---

## Study Plan Tasks

```dataview
TASK WHERE !completed
FROM "Java/99_Revision/Study Plan"
GROUP BY file.link
```

---

## Java 25 Features Tracker

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", tags as "Tags", created as "Created"
FROM "Java"
WHERE tags AND (contains(tags, "java25") OR contains(tags, "jep"))
SORT created DESC
```

---

## Excalidraw Diagrams

Each note has a `## Diagram` section. For hand-drawn JVM/Memory/Concurrency diagrams:
1. Open any Java note
2. `Cmd+P` → `Excalidraw: New from template → Java Diagram`
3. Save as `<topic>-diagram.excalidraw.md` in same folder
4. Embed in note: `![[JVM Memory Model-diagram]]`

---

## Related

- [[README|Java MOC]]
- [[Master Dashboard|Global Dashboard]]
- [[_templates/Java Note Template.md|Java Note Template]]
- [[_templates/Java Diagram.excalidraw.md|Excalidraw Template]]

---

*Dataview required. Enable in Settings → Community plugins.*