---
title: "Revision — Mock Interview Bank"
type: folder-MOC
tags: [MOC, revision, interview-prep]
---

# 99_Revision — Mock Interview Bank

> Unnumbered meta-folder — not curriculum. Aggregates `## Interview Q&A` from `01..07` via Dataview. Single source of truth stays in each topic note. **Java 25:** Q&A in `07_DSA` now references `record Node`, `SequencedCollection`, pattern matching, and Compact Object Headers (JEP 450) — search `Java 25` across vault.

---

## 📊 Revision Dashboard

```dataviewjs
const pages = dv.pages('"Java"').where(p => p.category && p.file.folder != "Java/99_Revision" && p.file.name != "README");
const total = pages.length;
const done = pages.where(p => p.completed).length;
const pct = total ? Math.round(done/total*100) : 0;
const bar = (p,w=20) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w-Math.round(p/100*w));

// SR scheduling fields: sr-due / sr-interval / sr-ease / due — support both conventions
const srPages = pages.where(p => p["sr-due"] || p.due || p["sr-interval"] || p.reviewed);
const srDueCount = pages.where(p => {
  const d = p["sr-due"] || p.due;
  if (!d) return false;
  return dv.date(d) <= dv.date("now");
}).length;
const srUpcoming = pages
  .where(p => p["sr-due"] || p.due)
  .map(p => ({ link: p.file.link, due: dv.date(p["sr-due"] || p.due), name: p.file.name }))
  .sort(p => p.due, 'asc');
const nextDue = srUpcoming.length ? srUpcoming[0] : null;
const overdue = pages.where(p => !p.reviewed || (dv.date("now") - dv.date(p.reviewed)).days > 7).length;

dv.paragraph(`**Total: ${total} notes | Completed: ${done} | Remaining: ${total - done}** — \`${bar(pct)}\` **${pct}%**`);
dv.paragraph(`| 🔁 **SR Due:** ${srDueCount} | ⏭️ **Next Due:** ${nextDue ? nextDue.link + " → " + nextDue.due.toFormat("yyyy-MM-dd") : "— none scheduled —"} | ⚠️ **Overdue (>7d):** ${overdue} |`);
if (srUpcoming.length) {
  dv.paragraph(`**Upcoming SR queue (next 5):**`);
  dv.table(["Note", "Due"], srUpcoming.slice(0,5).map(p => [p.link, p.due.toFormat("yyyy-MM-dd")]));
} else {
  dv.paragraph(`> *No \`sr-due\` / \`due\` dates found. Add \`sr-due: 2026-09-10\` or \`reviewed:\` + SR plugin to enable spaced-repetition tracking.*`);
}
```

> **Fallback** (if `dataviewjs` disabled):

```dataview
TABLE WITHOUT ID
  length(rows) as "Total",
  length(filter(rows, (r) => r.completed)) as "Completed",
  length(filter(rows, (r) => !r.completed)) as "Remaining"
FROM "Java"
WHERE category AND file.folder != "Java/99_Revision" AND file.name != "README"
GROUP BY true
```

### SR Due — Cards / Notes due now

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done", coalesce(sr-due, due, reviewed) as "Due / Last Reviewed"
FROM "Java"
WHERE category AND file.folder != "Java/99_Revision" AND (sr-due OR due)
  AND date(coalesce(sr-due, due)) <= date(now)
SORT coalesce(sr-due, due) ASC
```

### Next Due — Upcoming schedule

```dataview
TABLE WITHOUT ID file.link as "Note", coalesce(sr-due, due) as "Due", date(coalesce(sr-due, due)) - date(now) as "In"
FROM "Java"
WHERE category AND file.folder != "Java/99_Revision" AND (sr-due OR due)
SORT coalesce(sr-due, due) ASC
LIMIT 10
```

---

## 🗓️ 30-Day Plan

> Structured revision calendar — one pass over the full vault in 30 days. Pair with SR due above.

| Week | Days | Focus | Daily Target |
|------|------|-------|--------------|
| **W1 — Foundations** | 1–4 | `01_Core-Java` — Classes, Interface, Types (Abstract/POJO/Singleton/Wrapper/Object/Nested) | 4–5 notes/day → mark `completed: true` |
| | 5–7 | `02_OOP` — 4 pillars + 5 inheritance types (focus multiple/hybrid via interfaces) + [[Polymorphism]] | 3 notes/day + write 5 Q&A answers from memory |
| **W2 — Data** | 8–11 | `03_Collections` — Collection/List/Set/Map/Queue; ArrayList vs LinkedList vs Vector; HashSet vs TreeSet | 3 notes/day + diagram `_attachments` |
| | 12–14 | `07_DSA` — Array/Linked Lists/Stack/Queue/HashMap/Trees/Graph/Heap; Java 25 records & SequencedCollection | 3 notes/day + 2 LeetCode easy per day |
| **W3 — Backend** | 15–17 | `04_Concurrency` — Threads lifecycle, 4 creation ways, 7 issues, Locks, Executor, CompletableFuture | 2–3 notes/day + code a deadlock demo |
| | 18–22 | `05_Spring` — Framework/Core/Boot/MVC/Data JPA/Security/Transaction; IoC/DI/AOP + propagation | 1–2 notes/day + trace Security filter chain |
| **W4 — Patterns + Mock** | 23–27 | `06_Design-Patterns` — 22 GoF: Creational 5 + Structural 7 + Behavioral 10 + Extra (DAO/DI) | 4–5 patterns/day — whiteboard intent |
| | 28–30 | **Full mock** — `[[Interview Questions]]` index → timed Q&A, weakest-folder revisit, SR due sweep | 15 Q&A/day + re-review overdue (>7d) |

**How to track:** set `reviewed: YYYY-MM-DD` and `completed: true` in frontmatter each day. For SR, add `sr-due: YYYY-MM-DD` (or use the *Spaced Repetition* plugin's `!` scheduling on `## Interview Q&A` flashcards). The dashboard above counts due automatically.

- **Today's focus →** check *SR Due* and *Overdue* tables above, then pick the next row in this plan.
- **Full index →** [[Interview Questions]] — live dataview of every Q&A source note.
- **Vault progress →** [[README|Java MOC — Progress Bars]]

---

## All Notes — Index

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "Java"
WHERE category AND file.folder != "Java/99_Revision"
SORT file.path ASC
```
> **Dataview note — Java 25:** `07_DSA` notes updated Sep 2025 for Java 25 (records, Sequenced collections, pattern matching, Compact Object Headers). Filter `WHERE contains(file.text, "Java 25")` to audit coverage.

## Progress — Have I revised?

```dataviewjs
const pages = dv.pages('"Java"').where(p => p.category && p.file.folder != "Java/99_Revision");
const rows = pages
  .map(p => {
    const days = p.reviewed ? Math.floor((dv.date("now") - dv.date(p.reviewed)).days) : null;
    const ago = days === null ? "— never —" : (days === 0 ? "today" : `${days}d ago`);
    const due = p["sr-due"] || p.due;
    const dueStr = due ? dv.date(due).toFormat("yyyy-MM-dd") : "—";
    const urgent = days === null ? "🔴" : days > 14 ? "🔴" : days > 7 ? "🟡" : "🟢";
    return [p.file.link, p.completed ? "✅" : "⬜", p.reviewed ? p.reviewed.toFormat("yyyy-MM-dd") : "—", ago, dueStr, urgent];
  })
  .sort(p => p[3], 'desc');
dv.table(["Note", "Done", "Last Reviewed", "Ago", "SR Due", "Urgency"], rows);
```

> **Fallback** (no JS):

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done", reviewed as "Last Reviewed"
FROM "Java"
WHERE category AND file.folder != "Java/99_Revision"
SORT reviewed DESC
```

### Overdue — needs review (>7 days or never)

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", reviewed as "Last Reviewed", date(now) - reviewed as "Ago"
FROM "Java"
WHERE category AND file.folder != "Java/99_Revision" AND (!reviewed OR date(now) - reviewed > dur(7 days))
SORT reviewed ASC
LIMIT 20
```

## How to use

1. **Daily:** study `01_Core-Java` → `07_DSA` in order — Q&A lives *in* each note.
2. **Cram:** open `Interview Questions.md` in this folder — it's a live Dataview index of every Q&A.
3. **Track:** set `completed: true` and `reviewed: 2026-09-03` in frontmatter when done — tables above turn ✅. For SR, add `sr-due: 2026-09-10`.

[[README|← Back to Java MOC]]
