---
title: "AI Vault MOC"
category: "AI"
type: "root-MOC"
tags: [MOC, ai, llm, rag, agentic, production, kubernetes, governance]
created: "2026-09-29"
completed: false
reviewed: ""
sr-due: ""
---

# AI Vault — Map of Content

> **20-Week Roadmap** for LLM Engineering, RAG, Agentic AI, and Production ML interviews.
> Focus: Depth over breadth — build real systems, not just theory.

---

## 📊 Vault-Wide Progress

```dataviewjs
const all = dv.pages('"AI"').where(p => p.category && p.category.startsWith("AI/") && p.file.name != "README" && p.type !== "folder-MOC" && p.type !== "root-MOC");
const total = all.length;
const done = all.where(p => p.completed === true).length;
const pct = total ? Math.round(done/total*100) : 0;
const bar = (p, w=30) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w-Math.round(p/100*w));
dv.paragraph(`**Total: ${total} notes | Completed: ${done} | Remaining: ${total-done}** — \`${pct}%\``);
dv.paragraph(`\`${bar(pct)}\` **${pct}%**`);
if (total === done && total > 0) dv.paragraph(`🎉 *All notes completed!*`);
```

> **Fallback (if DataviewJS disabled):**
```dataview
TABLE WITHOUT ID
 length(rows) as "Total",
 length(filter(rows, (r) => r.completed)) as "Completed",
 length(filter(rows, (r) => !r.completed)) as "Remaining"
FROM "AI"
WHERE category AND category.startsWith("AI/") AND file.name != "README" AND type != "folder-MOC" AND type != "root-MOC"
GROUP BY true
```

---

## 📁 Folder Index & Progress

```dataview
TABLE WITHOUT ID
 file.link as "Folder",
 choice(category, category, "—") as "Category",
 length(rows.where(p => p.type != "folder-MOC" && p.type != "root-MOC")) as "Notes",
 length(rows.where(p => p.completed === true && p.type != "folder-MOC" && p.type != "root-MOC")) as "Done",
 round(length(rows.where(p => p.completed === true && p.type != "folder-MOC" && p.type != "root-MOC")) / length(rows.where(p => p.type != "folder-MOC" && p.type != "root-MOC")) * 100) + "%" as "Progress"
FROM "AI"
WHERE category AND category.startsWith("AI/") AND file.name = "README"
GROUP BY category
SORT category ASC
```

---

## 🎯 Spaced Repetition Status (All Notes)

```dataviewjs
const all = dv.pages('"AI"').where(p => p.category && p.category.startsWith("AI/") && p.file.name != "README" && p.type !== "folder-MOC" && p.type !== "root-MOC");
const stale = all.where(p => !p.reviewed || (dv.date("now") - dv.date(p.reviewed) > dv.duration({days: 7})));
const fresh = all.where(p => p.reviewed && (dv.date("now") - dv.date(p.reviewed) <= dv.duration({days: 7})));
const never = all.where(p => !p.reviewed);
dv.paragraph(`🟢 Fresh: **${fresh.length}** | 🟡 Stale: **${stale.length}** | 🔴 Never: **${never.length}**`);
dv.paragraph(`Next SR due: **${all.where(p => p["sr-due"]).sort(p => p["sr-due"])[0]?.["sr-due"] || "—"}**`);
```

---

## 📋 Study Plan & Dashboards

- [[Study-Plan.md|📅 20-Week Study Plan]] (in `99_Revision/`)
- [[Master Dashboard.md|📊 Master Dashboard]] (this vault)
- [[99_Revision/Interview Bank.md|🎤 Interview Bank]]
- [[99_Revision/Capstone Checklist.md|✅ Capstone Checklist]]
- [[99_Revision/Metrics Dashboard.md|📈 Metrics Dashboard]]

---

## 🗂️ Quick Navigation

### Phase 1: Foundations (Weeks 1-4)
- [[01_Fundamentals/README|01 Fundamentals]] — LLM internals, embeddings, tokenization, APIs, prompting, tool calling
- [[02_RAG-Engineering/README|02 RAG Engineering]] — RAG variants, enterprise search, agentic RAG, evaluation

### Phase 2: Agentic AI (Weeks 5-8)
- [[03_Agentic-AI/README|03 Agentic AI]] — Architectures, multi-agent, evaluation, production deployment

### Phase 3: Production Platform (Weeks 9-14)
- [[04_Production-Platform/README|04 Production Platform]] — Model serving, MLOps, data pipelines, monitoring, K8s
- [[05_Kubernetes-Operations/README|05 Kubernetes Operations]] — K8s for ML, Kubeflow, GPU scheduling, autoscaling

### Phase 4: Architecture, Governance & Interview (Weeks 15-20)
- [[06_Architecture-Governance/README|06 Architecture Governance]] — Model governance, compliance, risk management
- [[07_Cross-Cutting/README|07 Cross-Cutting]] — Security, privacy, ethics, observability, cost, routing, MCP

---

## 🔗 Cross-Vault Links

- **Vector DB** → [[Architect/10_System-Design-Interviews/DB-04-Vector-Databases]]
- **Model Serving** → [[Architect/10_System-Design-Interviews/BB-14-YouTube-Video-Streaming]]
- **Async Patterns** → [[Architect/10_System-Design-Interviews/ASYNC-01-Async-Patterns]]
- **Caching** → [[Architect/10_System-Design-Interviews/CACHE-02-Cache-Strategies]]
- **Rate Limiting** → [[Architect/10_System-Design-Interviews/BB-04-Rate-Limiter]]

---

## 📝 Note Template

- [[_templates/Unified-Note-Template.md|Unified Note Template]] — Standard structure for all notes

---

*Part of [[Architect/README|Architect MOC]] • Category: AI Root MOC*