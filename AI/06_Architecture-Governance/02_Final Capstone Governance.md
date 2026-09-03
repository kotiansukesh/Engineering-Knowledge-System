---
title: "Final Capstone — Governed Platform"
category: governance
tags: [ai, capstone, governance, mlops, drift]
weeks: "35-36"
created: 2026-09-02
completed: false
type: project
---

# Final Capstone — Governed Platform (Weeks 35–36)

> Part of [[README|06_Architecture-Governance]] • `project` • The same platform, now **governed**.

## Intent

Incorporate iSAQB concerns into [[AI/03_Agentic-AI/Enterprise AI Operations Platform|AI Operations Platform]] rather than adding features — demonstrate architectural maturity.

## Required Additions

- [ ] **ADRs** for key decisions (vector DB choice, agent framework, model routing, MCP adoption)
- [ ] **Quality attribute scenarios** (security, scalability, explainability, sustainability) with measurable responses
- [ ] **Compliance matrix:** GDPR + EU AI Act obligations → platform controls (audit logs, HITL, data lineage)
- [ ] **MLOps pipeline:** embedding versioning, drift detection (data/concept), rollback plan
- [ ] **Threat model:** prompt injection, secret leakage, supply-chain, sandboxing (link [[AI/07_Cross-Cutting/04_AI Security|Security]])
- [ ] **Cost & Green IT** report: tokens, GPU, energy — with optimization levers
- [ ] **Enterprise integration** diagram: how this platform plugs into existing Java/Spring estate

## Success Criteria

- Reviewer can trace every AI decision to an ADR, a quality scenario, and a compliance control.

## Related

- [[01_SWARC4AI Syllabus]] • [[AI/99_Revision/README|99_Revision]] • [[AI/07_Cross-Cutting/README|Cross-Cutting]]

---
*Category: governance*
