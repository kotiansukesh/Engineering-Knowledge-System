---
title: "07 Cross-Cutting Concerns"
type: folder-MOC
tags: [MOC, cross-cutting]
---

# 07_Cross-Cutting — Continuous (Woven Throughout)

> Not a phase — integrate from Phase 02 onward. Part of [[AI/README|AI MOC]]

These 6 topics are **underemphasized in certs** but increasingly required in production AI platforms. Address them as you build.

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "AI/07_Cross-Cutting"
WHERE file.name != "README"
SORT file.name ASC
```

## Progress

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done"
FROM "AI/07_Cross-Cutting"
WHERE category
SORT file.name ASC
```

| Concern | Integrate From | Core Tooling |
|---------|---------------|--------------|
| [[01_MCP\|MCP]] | Phase 02 | MCP servers + clients |
| [[02_AI Evaluation\|AI Evaluation]] | Phase 02 | Golden sets, LLM-as-judge, Phoenix |
| [[03_LLM Observability\|LLM Observability]] | Phase 03 | Langfuse / Arize Phoenix, OTel |
| [[04_AI Security\|AI Security]] | Phase 03 | Injection defenses, secrets, sandboxing |
| [[05_Cost Optimization\|Cost Optimization]] | Phase 02 | Semantic cache, batching, routing |
| [[06_Multi-Model Routing\|Multi-Model Routing]] | Phase 02 | Dynamic routing (latency/capability/cost) |

[[AI/06_Architecture-Governance/README|← 06_Governance]] • [[AI/README|AI MOC]]
