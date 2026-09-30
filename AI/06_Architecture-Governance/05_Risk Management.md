---
title: "AI Risk Management"
category: "AI/06_Architecture-Governance"
tags: [risk-management, threat-modeling, red-teaming, incident-response]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-07"
type: "note"
---

# AI Risk Management

## Intent
Turn AI risks into explicit scenarios with owners, controls, residual risk, monitoring, and response plans.

## Risk Loop
**Identify → analyze → control → test → monitor → respond → learn**

## Threat Categories
| Category | Example | Control examples |
|---|---|---|
| Security | prompt injection, tool abuse | isolation, authorization, red-team tests |
| Privacy | sensitive-data leakage | minimization, access control, redaction |
| Reliability | hallucination, tool failure | grounding, validation, fallback |
| Safety | harmful output/action | policy controls, approval, escalation |
| Operational | provider outage/cost spike | quotas, fallback, budgets |
| Governance | undocumented change | inventory, approval, audit trail |

## Risk Register Entry
Every material risk should record: **scenario, affected asset/user, likelihood, impact, existing controls, residual risk, owner, detection signal, response, review date**.

## Decision Rule
Prioritize by impact and exploitability, but do not hide high-impact low-frequency risks. Irreversible actions deserve stronger preventive controls than reversible informational responses.

## Failure Modes
1. Risk list without owners → assign accountable owner.
2. Red team disconnected from production threats → derive cases from architecture and incidents.
3. Controls tested only once → continuously replay important attack cases.
4. Residual risk undocumented → record accepted risk and expiry/review date.
5. Incident response starts from scratch → maintain playbooks and evidence paths.

## Practice
- [ ] Threat-model an agent with three tools.
- [ ] Create five concrete abuse cases.
- [ ] Map each to preventive and detective controls.
- [ ] Run a red-team replay and record residual risk.
- [ ] Write an incident playbook for one high-impact failure.

## Senior Interview Prompts
1. How do you threat-model an agent differently from a normal API?
2. What makes an AI risk scenario actionable?
3. Which controls should be preventive versus detective?
4. How do you handle accepted residual risk?
5. How should incidents feed back into evaluation and architecture?

## Flashcards
#flashcard
**Q:** What makes an AI risk entry actionable? :: **A:** A concrete scenario with impact, controls, owner, detection signal, response, residual risk, and review date.
