---
title: "Java , Master MOC"
type: MOC
category: "root"
tags: [MOC, java, interview-prep]
created: 2026-09-02
updated: 2026-09-23
pattern: 0
difficulty: Easy
completed: false
reviewed:
sr-due:
---

# Java , Master MOC

> Consolidated from `Interview Prep/` → `Java/` on 2026-09-02.
> **Java 8 to 25 LTS (Sep 2025) , 191 notes, 12 folders (00 to 10 + 99_Revision)** , all searchable via global `[[wikilinks]]`.
> **Start here:** [[00_Java-25-Overview/README|00 Overview]] → [[00_Java-25-Overview/LTS Evolution 8 to 25|LTS Evolution 8 to 25]] → [[09_Java-21-LTS/README|09 Java 21 LTS ]] → [[00_Java-25-Overview/Java 25 Roadmap|Roadmap]] → [[99_Revision/Study Plan|Study Plan]]. Vault root is `obsidian/`.

---

## Vault Overview

```dataviewjs
const pages = dv.pages('"Java"').where(p => p.category && p.file.name != "README");
const total = pages.length;
const completed = pages.where(p => p.completed).length;
const remaining = total - completed;
const pct = total ? Math.round(completed/total*100) : 0;
const bar = (p, w=20) => {
 const f = Math.round(p/100*w);
 return "█".repeat(f) + "░".repeat(w-f);
};
dv.paragraph(`**Total: ${total} notes | Completed: ${completed} | Remaining: ${remaining}** — \`${pct}% done\``);
dv.paragraph(`\`${bar(pct)}\` **${pct}%**`);
if (remaining === 0 && total > 0) dv.paragraph(`🎉 *All notes completed!*`);
```
> **Fallback** (if `dataviewjs` is disabled):
```dataview
TABLE WITHOUT ID
 length(rows) as "Total",
 length(filter(rows, (r) => r.completed)) as "Completed",
 length(filter(rows, (r) => !r.completed)) as "Remaining"
FROM "Java"
WHERE category AND file.name != "README"
GROUP BY true
```

---

## Progress , per Folder

```dataviewjs
const folders = [
 ["00_Java-25-Overview", "00 Java 25 Overview ⭐"],
 ["01_Core-Java", "01 Core-Java"],
 ["01_Core-Java/Types", "Types"],
 ["01_Core-Java/Types/Nested", "Nested Types"],
 ["02_OOP", "02 OOP"],
 ["02_OOP/Inheritance", "Inheritance Types"],
 ["03_Collections", "03 Collections"],
 ["03_Collections/List", "List Implementations"],
 ["03_Collections/Set", "Set Implementations"],
 ["04_Concurrency", "04 Concurrency"],
 ["05_Spring", "05 Spring"],
 ["06_Design-Patterns", "06 Design-Patterns"],
 ["06_Design-Patterns/Creational", "Creational Patterns"],
 ["06_Design-Patterns/Structural", "Structural Patterns"],
 ["06_Design-Patterns/Behavioral", "Behavioral Patterns"],
 ["06_Design-Patterns/Extra", "Extra Patterns"],
 ["07_DSA", "07 DSA"],
 ["08_Modern-Java", "08 Modern Java (8→25) ⭐"],
 ["09_Java-21-LTS", "09 Java 21 LTS ⭐"],
 ["10_LLD-Machine-Coding", "10 LLD Machine Coding"],
 ["99_Revision", "99 Revision"],
];
const bar = (p, w=14) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w - Math.round(p/100*w));
const rows = folders.map(([folder, label]) => {
 const pages = dv.pages(`"Java/${folder}"`).where(p => p.category && p.file.name != "README");
 const total = pages.length;
 const done = pages.where(p => p.completed).length;
 const pct = total ? Math.round(done/total*100) : 0;
 // avg days since reviewed
 const reviewedDates = pages.where(p => p.reviewed).map(p => dv.date(p.reviewed));
 let avgDays = "—";
 if (reviewedDates.length) {
  const now = dv.date("now");
  const avg = Math.round(reviewedDates.map(d => (now - d).days).array().reduce((a,b)=>a+b,0) / reviewedDates.length);
  avgDays = `${avg}d`;
 }
 const stale = pages.where(p => !p.reviewed || (dv.date("now") - dv.date(p.reviewed)).days > 7).length;
 return [`[[Java/${folder}/README|${label}]]`, total, done, `${pct}%`, `\`${bar(pct)}\` ${pct}%`, avgDays, stale ? `⚠️ ${stale}` : "✅"];
});
dv.table(
 ["Folder", "Total", "Done", "%", "Progress", "Avg. Since Review", "Stale (>7d)"],
 rows
);
// Overall vault bar
const all = dv.pages('"Java"').where(p => p.category && p.file.name != "README");
const tot = all.length, don = all.where(p => p.completed).length;
const opct = tot ? Math.round(don/tot*100) : 0;
const obar = (p,w=28) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w-Math.round(p/100*w));
dv.paragraph(`\n**Overall Vault:** \`${obar(opct)}\` **${opct}%** — ${don}/${tot} completed`);
```
> **Fallback** (no JS):
```dataview
TABLE WITHOUT ID
 file.folder as "Folder",
 length(rows) as "Total",
 length(filter(rows, (r) => r.completed)) as "Done",
 round(length(filter(rows, (r) => r.completed)) / length(rows) * 100) + "%" as "Complete %",
 choice(any(filter(rows, (r) => r.completed)), "has progress", "—") as "Progress"
FROM "Java"
WHERE category AND file.name != "README"
GROUP BY file.folder
SORT file.folder ASC
```

---

## Structure , how to use

| Folder | What's Inside | Count | When to Use |
|--------|---------------|-------|-------------|
| [[Java/00_Java-25-Overview/README\|00_Java-25-Overview]] | [[Java 25 Roadmap]], [[Whats New in Java 25]], [[99_Revision/Study Plan\|Study Plan]], [[Interview Strategy]], [[Dashboard\|Dashboard]] | 5 | **Start here , plan + Java 25 delta** |
| [[Java/01_Core-Java/README\|01_Core-Java]] | `Classes`, `Interface`, `Method Overload`, + 15 `Types/` (Abstract, POJO, Singleton, Wrapper, Object, Nested…) | 18 | Java language basics |
| [[Java/02_OOP/README\|02_OOP]] | `00 - OOP Overview`, 4 pillars (Abstraction, Encapsulation, Inheritance, Polymorphism) + 5 inheritance types | 10 | OOP interview |
| [[Java/03_Collections/README\|03_Collections]] | `Collection` + `List/` (ArrayList, LinkedList, Vector, Stack), `Set/` (HashSet, TreeSet, SortedSet), `Map`, `Queue` | 12 | Collections framework |
| [[Java/08_Modern-Java/README\|08_Modern-Java]] | **Records, Sealed, Pattern Matching, SequencedCollection, Virtual Threads (JEP 491), ScopedValue (JEP 506), Compact Headers (JEP 450)** | 8 | **Java 8→25 , "What's new?"** |
| [[Java/09_Java-21-LTS/README\|09_Java-21-LTS]] | **Java 21 LTS , Virtual Threads JEP 444, Sequenced 431, Record Patterns 440, Switch 441, Generational ZGC 439, FFM 442, _(plus 430/443/445 previews)_** | 10 | **Java 21 LTS interview must-know** |
| [[Java/04_Concurrency/README\|04_Concurrency]] | `Threads` (virtual threads deep), `Executor`, `CompletableFuture`, `Locks`, `Atomics` | 7 | Concurrency (Loom) |
| [[Java/05_Spring/README\|05_Spring]] | `Spring Framework`, `Spring Core`, `DI`, `Security`, `Transaction` + Boot 3.5 + virtual threads | 9 | Spring |
| [[Java/06_Design-Patterns/README\|06_Design-Patterns]] | 22 GoF patterns (Creational 5 + Structural 7 + Behavioral 10) + 2 Extra (DAO, DI) | 29 | Design patterns |
| [[Java/07_DSA/README\|07_DSA]] | `Array`, `Linked List`, `Singly/Doubly`, `Stack`, `Queue`, `HashMap`, `Trees` + [[Coding Patterns/README\|Coding Patterns]] 20 | 11 | DSA fundamentals |
| [[Java/99_Revision/README\|99_Revision]] | [[99_Revision/Study Plan\|Study Plan]], [[99_Revision/Interview-Bank\|Interview Bank]] + Dashboard | 3 | Mock interview / cram |
| `_attachments/` | 22 images (all `Pasted image …png`) | , | Assets |

> **New in this update (Java 25):** Added `00_Java-25-Overview` (roadmap + whats-new + 6-week plan) and `08_Modern-Java` (8 notes covering every LTS-relevant feature 8→25). `Dashboard` + `00_Java-25-Overview/Dashboard.md` track `completed: true` live.

> **Reading paths:**
> - **Java 25 fast-track:** `00 Overview` → `08 Modern Java` → `04 Concurrency` → `Whats New` 60-sec answer
> - *Core → OOP → Collections* → Java SE mastery
> - *Concurrency → Spring → Design Patterns* → Backend interview
> - *DSA → Collections → _attachments diagrams* → Problem solving

---

## Progress , Review Status

### ⏰ Overdue , not Reviewed in 7+ Days

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", reviewed as "Last Reviewed", date(now) - reviewed as "Days Ago"
FROM "Java"
WHERE category AND file.name != "README" AND (!reviewed OR date(now) - reviewed > dur(7 days))
SORT reviewed ASC
```

### Recently Reviewed (Last 7 Days)

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done", reviewed as "Last Reviewed", date(now) - reviewed as "Ago"
FROM "Java"
WHERE category AND file.name != "README" AND reviewed AND date(now) - reviewed <= dur(7 days)
SORT reviewed DESC
```

### Remaining , not yet Completed

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", choice(completed, "✅", "⬜") as "Done"
FROM "Java"
WHERE category AND file.name != "README" AND !completed
SORT category ASC, file.name ASC
```

### Review Timeline , Days Since Reviewed (Dataviewjs)

```dataviewjs
const pages = dv.pages('"Java"').where(p => p.category && p.file.name != "README");
const rows = pages
 .map(p => {
 const days = p.reviewed ? Math.floor((dv.date("now") - dv.date(p.reviewed)).days) : null;
 const status = p.completed ? "✅" : "⬜";
 const when = p.reviewed ? p.reviewed.toFormat("yyyy-MM-dd") : "— never —";
 const ago = days === null ? "—" : (days === 0 ? "today" : `${days}d ago`);
 const urgency = days === null ? "🔴" : days > 14 ? "🔴" : days > 7 ? "🟡" : "🟢";
 return [p.file.link, p.category, status, when, ago, urgency];
 })
 .sort(p => p[4], 'desc');
dv.table(["Note", "Category", "Done", "Last Reviewed", "Ago", "Urgency"], rows);
```
> **Fallback** (no JS):
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", choice(completed, "✅", "⬜") as "Done", reviewed as "Last Reviewed"
FROM "Java"
WHERE category AND file.name != "README"
SORT reviewed DESC
```

---

## Quick Navigation , all Notes

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "Java"
WHERE file.name != "README"
SORT category ASC, file.name ASC
```

---

## How this was Restructured

- **Before:** Flat, duplicate `Interview Prep/` and `Java/` (both had `.obsidian/` sub-vaults, duplicated `DSA/`, scattered `Types/` with typo `SiIngly-linked`).
- **After:** Single `Java/` vault, 8 numbered folders, nested `Types/Nested/`, `Inheritance/`, `List/`, `Set/`. Typos fixed (`Singly Linked List`, `TreeSet`), parenthesized filenames cleaned (`Hybrid Inheritance`), stray `.obsidian` removed.
- **Frontmatter added** to all 64 notes (`title, category, tags`) , enables dataview.
- **Images consolidated** to `Java/_attachments/` (22 from `Interview Prep/Assets/img` + 1 from `Java/Resources/img`).
- **Links:** Wikilinks like `[[Single Inheritance]]` still resolve globally , no broken links. Images use vault-wide `![[Pasted image …]]`.

---

## Revision Checklist

- [ ] Core: Can you explain `Object` vs `Wrapper` vs `POJO` vs `Singleton`?
- [ ] OOP: 4 pillars + 5 inheritance types (esp. multiple/hybrid via interfaces) + `sealed`?
- [ ] Collections: `ArrayList` vs `LinkedList` vs `Vector`; `HashSet` vs `TreeSet`; `SequencedCollection.getFirst()` vs `get(0)`?
- [ ] Modern (Java 25): `record` vs `class`, `ScopedValue` vs `ThreadLocal`, `synchronized` pinning (JEP 491), compact headers?
- [ ] Concurrency: Thread lifecycle + virtual threads + `StructuredTaskScope` + `CompletableFuture`?
- [ ] Spring: IoC/DI/AOP + `spring.threads.virtual.enabled=true` + `@Transactional` proxy pitfall?
- [ ] Patterns: 22 GoF , problem/solution/benefits for each?
- [ ] DSA: Height/traversal of trees, `Heap` vs `Tree`, 20 Coding Patterns?

---

## 🆕 Java 25 , Added 2026-09-03

- `[[00_Java-25-Overview/README|00 Overview]]` , roadmap, whats-new (JEP 506/505/450/507/513/491), 6-week plan
- `[[08_Modern-Java/README|08 Modern Java]]` , 8 notes: Records, Sealed, Pattern Matching (JEP 507), SequencedCollection, Virtual Threads, ScopedValue, Flexible Constructors/Module Imports, Compact Headers
- `Dashboard` , [[00_Java-25-Overview/Dashboard|Dataview Dashboard]] + [[Dashboard.html|HTML Dashboard]] (interactive, localStorage `+1`/`-1`)
- **How to track:** `completed: true` + `reviewed: YYYY-MM-DD` per note → MOC bars + Dashboard + `99_Revision` overdue. Study Plan checkboxes → `TASK` progress.

---

## Next Steps

- Add `completed: true` frontmatter to notes you've revised , the folder READMEs show dataview progress.
- Delete `Interview Prep/` after verifying in Obsidian Graph View (see `Interview Prep/_MOVED.md`).
- **Mock loop:** Weekly — 3 questions from [[99_Revision/Interview-Bank|Interview Bank]] + 1 system-design drill from Master Dashboard's SR Due list.

*Created 2026-09-02 • Vault: `obsidian/Java`*