---
title: "AI Architecture Governance Study Map"
category: "AI/06_Architecture-Governance"
tags: [ai, architecture, governance, certification, isaqb]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-17"
type: "study-map"
---

# AI Architecture Governance Study Map

## Purpose
Use architecture-governance frameworks as a study map for turning AI quality, lifecycle, security, compliance, and sustainability concerns into architecture decisions and evidence.

> This note is a learning aid, not a claim that any certification syllabus or framework requires every item below.

## Governance Reasoning Loop

**Context → stakeholders → quality/risk drivers → applicable requirements → architecture decision → control → evidence → monitoring → review**

## Core Study Areas

### 1. Quality Attributes
Practice writing measurable scenarios for:
- latency
- availability
- reliability
- security
- privacy
- scalability
- cost
- observability
- modifiability
- sustainability

### 2. AI Lifecycle
Connect:
**data → model/provider → evaluation → deployment → monitoring → incident → retirement**

### 3. Governance
Define:
- accountable owner
- decision authority
- risk tolerance
- approval gates
- evidence repository
- review cadence
- exception process

### 4. Architecture Decisions
Every significant decision should record:
**context → drivers → alternatives → decision → consequences → evidence → review trigger**

### 5. Compliance Engineering
Do not memorize regulations as isolated facts. Practice:
**requirement → applicability → control → evidence → owner → review date**

### 6. Sustainability
Treat energy/cost as architecture concerns where relevant. Measure useful work rather than relying on infrastructure consumption alone.

## Framework Comparison

| Framework / approach | Primary role | Useful architecture output |
|---|---|---|
| AI RMF | risk-management structure | Govern/Map/Measure/Manage evidence |
| Enterprise architecture method | organizational alignment | capabilities, principles, target architecture |
| Security/privacy frameworks | control definition | safeguards, responsibilities, evidence |
| Regulatory requirements | binding obligations where applicable | required controls and records |

NIST describes AI RMF 1.0 as voluntary and organizes it around Govern, Map, Measure, and Manage. citeturn0search2turn0search9

## Practice
- [ ] Take one RAG system and create its quality-attribute scenarios.
- [ ] Produce five ADRs from real architecture decisions.
- [ ] Build a risk register and map each risk to a control.
- [ ] Create a compliance evidence matrix.
- [ ] Defend one architecture decision in a 10-minute review.

## Flashcards
#flashcard
**Q:** What is the governance loop? :: **A:** Context → drivers/requirements → decision → control → evidence → monitoring → review.

#flashcard
**Q:** Is NIST AI RMF a mandatory regulation? :: **A:** No. NIST describes AI RMF as voluntary guidance; legal and contractual obligations must be assessed separately. citeturn0search9

## Review
Use this note to prepare for architecture reviews; do not treat it as a substitute for the authoritative framework or certification provider material.
