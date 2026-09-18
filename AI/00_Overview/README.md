---
title: "00 Overview"
type: folder-MOC
tags: [MOC, overview]
---
# 00_Overview, Roadmap Meta

> How to use this vault. **Start here before Phase 01.** Now includes [[2026 Trends Update]], patch for MCP standard, reasoning models, Agentic RAG/GraphRAG.
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "AI/00_Overview"
WHERE file.name != "README"
SORT file.name ASC
```
| Note | Why read it | When |
|------|-------------|------|
| [[Roadmap Overview]] | 36-week phases, platform evolution | First |
| [[2026 Trends Update]] | MCP std, reasoning models, GraphRAG, delta on roadmap | Before Phase 02 |
| [[Tech Stack]] | Python/FastAPI/PG/pgvector/K8s/monitoring choices | Week 1 |
| [[Certification Guide]] | Coursera C1/C2/C3–C7, NUS-ISS, CKAD, iSAQB, order + caps | Week 5 |
| [[Weekly Tracker]] | Week-by-week Build/Study/Eval, check off | Weekly |
| [[Learning Philosophy]] | Build then certify, interview-ready Q&A | Anytime |

## Progress

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done"
FROM "AI/00_Overview"
WHERE category
SORT file.name ASC
```
[[README|← Back to AI MOC]]
