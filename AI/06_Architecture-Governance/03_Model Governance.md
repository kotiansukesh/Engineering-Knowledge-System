---
title: "Model Governance"
category: "AI/06_Architecture-Governance"
tags: [governance, model-lifecycle, audit, risk]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-06"
type: concept
---

# Model Governance

## Intent
Create traceability and control across model selection, evaluation, approval, deployment, monitoring, incident response, and retirement.

## Lifecycle
~~~~mermaid
flowchart LR
I[Inventory] --> R[Risk classification] --> E[Evaluation] --> A[Approval] --> D[Deploy] --> M[Monitor] --> X[Incident / change] --> Q[Retire]
~~~~

## Governance Record
For every production model or provider configuration capture:
- owner and business purpose
- model/version/provider identifier
- intended use and prohibited use
- data sources and important restrictions
- evaluation results and known limitations
- security/privacy review
- approval evidence
- deployment configuration
- monitoring metrics and thresholds
- incident history and retirement trigger

## Decision Rule
Governance depth should follow risk and impact. A low-impact internal summarizer does not need the same approval path as a system making consequential decisions or executing external actions.

## Real Trade-offs
| Control | Lightweight | Strong control | Choose based on |
|---|---|---|---|
| Approval | Team owner | Independent review | impact and regulatory/security exposure |
| Evaluation | Offline test set | Offline + adversarial + human review | risk of failure |
| Change management | Version tag | Formal approval + rollback | reversibility and impact |
| Audit | Operational logs | Evidence package | accountability requirements |

## Failure Modes
1. Unknown model version → immutable deployment metadata.
2. Evaluation not reproducible → version data, prompts, tools, model configuration.
3. Approval bypass → deployment policy gate.
4. Vendor/model change breaks quality → continuous regression evaluation.
5. No retirement criteria → define expiry/review date.

## Evidence
Governance is useful only if an auditor or engineer can reconstruct **what ran, why it was approved, what evidence supported it, and what happened afterward**.

## Practice
- [ ] Create a model inventory entry.
- [ ] Define a risk class and required approvals.
- [ ] Build a reproducible evaluation record.
- [ ] Simulate a model-version change and regression gate.
- [ ] Write a retirement trigger.

## Senior Interview Prompts
1. What belongs in a model inventory?
2. How does governance differ for a third-party API versus a self-hosted model?
3. How do you prevent undocumented model changes?
4. What evidence should exist before production approval?
5. How should governance respond to an incident?

## Flashcards
#flashcard
**Q:** What is the core purpose of model governance? :: **A:** Traceable control over model lifecycle decisions, evidence, risk, deployment, monitoring, and retirement.
