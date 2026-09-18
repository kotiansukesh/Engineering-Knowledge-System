---
title: "AI Engineering, Master MOC"
type: MOC
tags: [MOC, ai, ai-platform, roadmap]
created: 2026-09-02
updated: 2026-09-02
weeks: "1-36"
hours_per_week: "10-15"
outcome: "Enterprise AI Platform + CKAD + iSAQB"
---
# AI Engineering, Master moc

> **36-week roadmap** (13+ years Java/backend → Staff/Principal AI Platform Engineer).
> One evolving platform, not 6 throwaway projects. Each phase hardens the same system.
> **2026 update:** MCP standard + reasoning models + Agentic/GraphRAG patched in via [[AI/00_Overview/2026 Trends Update|2026 Trends Update]], no phase move, just deeper build.
> Part of [[README|Vault MOC]] • [ Dashboard](Dashboard.html) • Certifications used to **reinforce** hands-on work, not replace it.

---

## Vault Overview

```dataviewjs
const pages = dv.pages('"AI"').where(p => p.category && p.file.name != "README");
const total = pages.length;
const completed = pages.where(p => p.completed).length;
const remaining = total - completed;
const pct = total ? Math.round(completed/total*100) : 0;
const bar = (p, w=20) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w-Math.round(p/100*w));
dv.paragraph(`**Total: ${total} notes | Completed: ${completed} | Remaining: ${remaining}** — \`${pct}% done\``);
dv.paragraph(`\`${bar(pct)}\` **${pct}%**`);
if (remaining === 0 && total > 0) dv.paragraph(`🎉 *All notes completed!*`);
```
> **Fallback:**
```dataview
TABLE WITHOUT ID
 length(rows) as "Total",
 length(filter(rows, (r) => r.completed)) as "Completed",
 length(filter(rows, (r) => !r.completed)) as "Remaining"
FROM "AI"
WHERE category AND file.name != "README"
GROUP BY true
```
---

## Progress, per Phase
```dataviewjsconst
 folders = [
 ["00_Overview", "00 Overview"],
 ["01_Fundamentals", "01 Fundamentals W1-4"],
 ["02_RAG-Engineering", "02 RAG W5-10"],
 ["03_Agentic-AI", "03 Agentic W11-16"],
 ["04_Production-Platform", "04 Production W17-24"],
 ["05_Kubernetes-Operations", "05 K8s Ops W25-30"],
 ["06_Architecture-Governance", "06 Arch/Gov W31-36"],
 ["07_Cross-Cutting", "07 Cross-Cutting"],
 ["99_Revision", "99 Revision"],
];
const bar = (p, w=14) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w - Math.round(p/100*w));
const rows = folders.map(([folder, label]) => {
 const pages = dv.pages(`"AI/${folder}"`).where(p => p.category && p.file.name != "README");
 const total = pages.length;
 const done = pages.where(p => p.completed).length;
 const pct = total ? Math.round(done/total*100) : 0;
 const stale = pages.where(p => !p.reviewed || (dv.date("now") - dv.date(p.reviewed)).days > 7).length;
 return [`[[AI/${folder}/README|${label}]]`, total, done, `${pct}%`, `\`${bar(pct)}\` ${pct}%`, stale ? `⚠ ${stale}` : ""];
});
dv.table(
 ["Phase", "Total", "Done", "%", "Progress", "Stale (>7d)"],
 rows
);
```
---

## 36-Week Timeline

| Phase | Weeks | Theme | Certification | Platform Evolution |
|-------|-------|-------|---------------|-------------------|
| **00** | — | [[AI/00_Overview/README\|Overview & Principles]] | — | Tech stack, weekly tracker, learning philosophy |
| **01** | 1–4 | [[AI/01_Fundamentals/README\|Fundamentals]] | *None* | `AI Backend Template` → FastAPI + LLM APIs + tools |
| **02** | 5–10 | [[AI/02_RAG-Engineering/README\|RAG Engineering]] | **Coursera C1** LLM Eng. with RAG + **C2** LLM Architectures | `Enterprise Document Search` — pgvector, hybrid search, citations, streaming |
| **03** | 11–16 | [[AI/03_Agentic-AI/README\|Agentic AI]] | **NUS-ISS** Architecting Agentic AI Solutions (4-day intensive) | `Enterprise AI Operations Platform` — 7 agents, human approval, memory, orchestration |
| **04** | 17–24 | [[AI/04_Production-Platform/README\|Production Platform]] | **Coursera C3–C7** Resilient Microservices → Integrate & Optimize | Harden platform: gRPC, Helm, autoscaling, Prometheus, OTel, resilience |
| **05** | 25–30 | [[AI/05_Kubernetes-Operations/README\|K8s Operations]] | **CKAD** (or CKA) | Deploy full stack on K8s: gateway, PG, Redis, vector DB, Kafka, Grafana |
| **06** | 31–36 | [[AI/06_Architecture-Governance/README\|Architecture & Governance]] | **iSAQB CPSA-A SWARC4AI** (3-day) | Governance, compliance, drift, MLOps, GenAI patterns, cost |
| **07** | *continuous* | [[AI/07_Cross-Cutting/README\|Cross-Cutting]] | — | MCP, eval, observability, security, cost, multi-model routing |
| **99** | — | [[AI/99_Revision/README\|Revision & Mock]] | — | Flashcards, capstone checklist, interview bank |

> **Principle:** Certifications reinforce building. No throwaway course projects, evolve **one platform** from Phase 1 → 6.

---

## Platform Evolution (Single System)
```W1-4
 AI Backend Template (FastAPI + LLM APIs + tool calling)
 ↓
W5-10 + RAG: Enterprise Document Search (pgvector, hybrid, citations)
 ↓
W11-16 + Agents: AI Operations Platform (7 agents, orchestration, memory)
 ↓
W17-24 harden: gRPC/Helm/autoscaling/Prometheus/OTel/resilience
 ↓
W25-30 deploy: K8s production (gateway, PG, Redis, vector DB, Kafka, observability)
 ↓
W31-36 govern: quality attributes, EU AI Act, drift, MLOps, enterprise integration
```
---

## Certification map

| Cert | Weeks | Format | Why Now | Work Submitted |
|------|-------|--------|---------|----------------|
| **Coursera C1: LLM Eng. with RAG** | 5–6 | Online | After fundamentals, validate RAG skills | Enterprise Document Search v1 |
| **Coursera C2: Design LLM Architectures** | 7–10 | Online | Compare architectures, RAG variants, cost | RAG variant experiments |
| **NUS-ISS Architecting Agentic AI** | 11–16 | 4-day intensive (Grad Cert module) | You already know agents/tools/MCP, shift to *ecosystem* thinking | AI Operations Platform |
| **Coursera C3–C7** | 17–24 | Online (5 courses) | Harden existing platform for production | Same platform + gRPC/Helm/K8s/monitoring |
| **CKAD / CKA** | 25–30 | Exam | Prove deployment & ops skills | Full K8s deployment |
| **iSAQB SWARC4AI** | 31–36 | 3-day (20+10 pts) | Formalize architecture after building | Final capstone with governance |

Details: [[AI/00_Overview/Certification Guide|Certification Guide]] • [[AI/00_Overview/Weekly Tracker|Weekly Tracker]]

---

## Cross-Cutting Concerns (Woven Throughout)

> Not a separate phase, integrate from Phase 2 onward. See [[AI/07_Cross-Cutting/README|07_Cross-Cutting]]

- [[AI/07_Cross-Cutting/01_MCP|MCP]] • [[AI/07_Cross-Cutting/02_AI Evaluation|AI Evaluation]] • [[AI/07_Cross-Cutting/03_LLM Observability|LLM Observability]] (Langfuse/Phoenix) • [[AI/07_Cross-Cutting/04_AI Security|AI Security]] • [[AI/07_Cross-Cutting/05_Cost Optimization|Cost Optimization]] • [[AI/07_Cross-Cutting/06_Multi-Model Routing|Multi-Model Routing]]

---

## Folder Index
```dataviewTABLE
 WITHOUT ID file.link as "Note", category as "Category", weeks as "Weeks"
FROM "AI"
WHERE category AND file.name != "README"
SORT file.path ASC
```
---

## ▶ Where to Start

1. Read [[AI/00_Overview/Roadmap Overview|Roadmap Overview]] → [[AI/00_Overview/Tech Stack|Tech Stack]] → [[AI/00_Overview/Learning Philosophy|Learning Philosophy]]
2. Open [[AI/01_Fundamentals/README|01_Fundamentals]], Weeks 1–4, no certs, build the backend template
3. Track weekly in [[AI/00_Overview/Weekly Tracker|Weekly Tracker]], set `completed: true` + `reviewed: YYYY-MM-DD` per note

*Structure mirrors [[Java/README|Java MOC]] + [[Coding Patterns/README|Coding Patterns]], numbered curriculum + `99_Revision` meta-folder.*
