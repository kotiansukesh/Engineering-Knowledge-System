---
title: "03 Agentic AI"
type: folder-MOC
tags: [MOC, agents, nus-iss]
weeks: "11-16"
---

# 03_Agentic-AI — Weeks 11–16 · NUS-ISS Architecting Agentic AI Solutions

> From "building an agent" to **designing an enterprise agent ecosystem**. Part of [[AI/README|AI MOC]]

**Certification:** **NUS-ISS Architecting Agentic AI Solutions** — 4-day intensive (~32h), Grad Cert in Architecting AI Systems  
**Prereqs by W11:** agents, tools, [[AI/07_Cross-Cutting/01_MCP|MCP]], workflows, RAG, orchestration  
**Platform evolution:** [[Enterprise AI Operations Platform]] — capstone beyond a chatbot

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", weeks as "Weeks"
FROM "AI/03_Agentic-AI"
WHERE file.name != "README"
SORT file.name ASC
```

## Progress

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done"
FROM "AI/03_Agentic-AI"
WHERE category
SORT file.name ASC
```

## This Phase Shifts

| Before (Phase 02) | After (Phase 03) |
|-------------------|------------------|
| Single RAG pipeline | 7-agent ecosystem with orchestration |
| Tool = search | Tools via [[AI/07_Cross-Cutting/01_MCP\|MCP]] + domain tools |
| No memory | Short/long-term memory + audit logs |

[[AI/02_RAG-Engineering/README|← 02_RAG]] • Next: [[AI/04_Production-Platform/README|04_Production]]
