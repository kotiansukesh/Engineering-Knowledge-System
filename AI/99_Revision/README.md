---
title: "99 Revision — Mock & Cram"
type: folder-MOC
tags: [MOC, revision, interview]
---

# 99_Revision — Mock Interview & Cram

> Unnumbered meta-folder — not curriculum. Aggregates `## Interview Q&A` from `00..07`. Single source of truth stays in each note. Part of [[AI/README|AI MOC]]

---

## 📊 Revision Dashboard

```dataviewjs
const pages = dv.pages('"AI"').where(p => p.category && p.file.folder != "AI/99_Revision" && p.file.name != "README");
const total = pages.length;
const done = pages.where(p => p.completed).length;
const pct = total ? Math.round(done/total*100) : 0;
const bar = (p,w=20) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w-Math.round(p/100*w));
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
  dv.paragraph(`> *No \`sr-due\` / \`due\` dates found. Add \`sr-due: YYYY-MM-DD\` or \`reviewed:\` + SR plugin.*`);
}
```

> **Fallback:**
```dataview
TABLE WITHOUT ID
  length(rows) as "Total",
  length(filter(rows, (r) => r.completed)) as "Completed",
  length(filter(rows, (r) => !r.completed)) as "Remaining"
FROM "AI"
WHERE category AND file.folder != "AI/99_Revision" AND file.name != "README"
GROUP BY true
```

### SR Due — Cards / Notes due now

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done", coalesce(sr-due, due, reviewed) as "Due / Last Reviewed"
FROM "AI"
WHERE category AND file.folder != "AI/99_Revision" AND (sr-due OR due)
  AND date(coalesce(sr-due, due)) <= date(now)
SORT coalesce(sr-due, due) ASC
```

---

## 🗓️ 36-Week Cram Checklist

| Week | Focus | Daily Target |
|------|-------|--------------|
| **W1–4** Foundations | `01_Fundamentals` — Python, FastAPI, LLM APIs, prompts, structured outputs, tools | 1–2 notes/day + code the 4 projects |
| **W5–10** RAG | `02_RAG-Engineering` — C1/C2, pgvector, hybrid search, variants, cost | 1 note/day + eval table |
| **W11–16** Agentic | `03_Agentic-AI` — NUS-ISS, 7 agents, orchestration, memory, HITL | 1 note/day + capstone trace |
| **W17–24** Production | `04_Production-Platform` — gateway, TDD, Helm, gRPC, observability | 1 note/day + harden platform |
| **W25–30** K8s | `05_Kubernetes-Operations` — deploy full stack, CKAD drills | Mock exams |
| **W31–36** Governance | `06_Architecture-Governance` + `07_Cross-Cutting` — quality, compliance, drift, MLOps | ADRs + threat model |
| **Mock** | All phases | 15 Q&A/day whiteboard, weakest-folder revisit, SR sweep |

**How to track:** set `reviewed: YYYY-MM-DD` and `completed: true` in frontmatter. For SR, add `sr-due: YYYY-MM-DD`.

---

## All Notes — Index

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", weeks as "Weeks"
FROM "AI"
WHERE category AND file.folder != "AI/99_Revision"
SORT file.path ASC
```

## Progress — Have I revised?

```dataviewjs
const pages = dv.pages('"AI"').where(p => p.category && p.file.folder != "AI/99_Revision");
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

### Overdue — needs review (>7 days or never)

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", reviewed as "Last Reviewed", date(now) - reviewed as "Ago"
FROM "AI"
WHERE category AND file.folder != "AI/99_Revision" AND (!reviewed OR date(now) - reviewed > dur(7 days))
SORT reviewed ASC
LIMIT 20
```

---

## Capstone Review Gates

| Gate | Check |
|------|-------|
| Phase 02 | Enterprise Document Search — hybrid beats naive, citations verifiable, cost table done |
| Phase 03 | AI Operations Platform — 7 agents, HITL gate, audit log, memory |
| Phase 04 | Production hardening — Helm, HPA, gRPC, Prometheus, OTel, resilience all live |
| Phase 05 | K8s — full stack healthy, Grafana green, CKAD passed |
| Phase 06 | Governance — ADRs, quality scenarios, EU AI Act matrix, drift pipeline, threat model |

[[AI/README|← Back to AI MOC]]
