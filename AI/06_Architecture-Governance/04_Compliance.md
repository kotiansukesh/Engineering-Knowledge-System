---
title: "AI Compliance as Architecture Controls"
category: "AI/06_Architecture-Governance"
tags: [compliance, governance, privacy, security, audit, ai-act]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-16"
type: concept
---

# AI Compliance as Architecture Controls

## Intent
Translate legal, regulatory, contractual, and organizational requirements into **system controls, evidence, owners, and review triggers**. This note is an engineering framework, not legal advice.

## Core Model
**Jurisdiction + use case + data + role + risk → applicable obligations → control → evidence → owner → review**

Compliance is not a single checklist. Applicability depends on the system, deployment context, actors, data, sector, contracts, and jurisdiction.

## Control Map

| Concern | Architecture question | Example evidence |
|---|---|---|
| Data protection | What personal data enters, leaves, or is retained? | data map, retention policy, access logs, DPIA where applicable |
| Security | Who can invoke the model/tools and with what privileges? | IAM policy, audit logs, threat model |
| Transparency | What must users be told about AI involvement/output? | UI disclosure, model/system documentation |
| Human oversight | Which decisions require human review or override? | approval workflow, escalation logs |
| Traceability | Can a production outcome be reconstructed? | model/version/data/config lineage |
| Retention | What must be retained and for how long? | retention configuration and deletion evidence |
| Vendor risk | What happens to prompts/data at providers? | contract/DPA/security review |
| Incident response | What happens when a control fails? | runbook, incident record, notification workflow |

## EU AI Act — Versioned Knowledge

The EU AI Act is being applied progressively. As of **2 August 2026**, enforcement powers and several provisions apply; other obligations have later applicability dates. For example, the European Commission currently lists the Annex III high-risk rules as applying from **2 December 2027**, while some other provisions apply earlier. Do not encode a single "AI Act deadline" into architecture documentation. Re-check the official timeline before making a release decision. citeturn0search11

Architecture implication: maintain a **regulatory applicability record** containing jurisdiction, system classification/role, applicable provision, effective date, required control, evidence, owner, and review date.

## Privacy Engineering

For systems processing personal data, identify:
- purpose and lawful processing basis with the appropriate legal/privacy team
- data categories and sources
- retention/deletion behavior
- access and least privilege
- data transfer/provider boundaries
- training vs inference use
- logging exposure
- user rights and operational workflows where applicable

The EDPB publishes AI-specific data-protection guidance and notes that its LLM privacy-risk guidance complements rather than replaces a GDPR DPIA. citeturn0search12turn0search38

## NIST AI RMF Mapping

Use **Govern → Map → Measure → Manage** as an engineering lifecycle, not as a compliance checklist. NIST explicitly describes the framework as voluntary and context-dependent. citeturn0search0turn0search7

- **Govern:** policies, accountability, inventory, risk tolerance
- **Map:** context, intended use, impacts, stakeholders, limitations
- **Measure:** evaluations, metrics, uncertainty, testing evidence
- **Manage:** prioritize risks, choose responses, monitor and improve

## Failure Modes
1. Regulation copied into a checklist with no system control.
2. Control exists but has no evidence or owner.
3. Legal applicability is assumed from the model vendor rather than the actual deployment context.
4. Logs intended for audit accidentally retain sensitive prompts indefinitely.
5. A control is correct at launch but becomes stale after architecture/provider changes.
6. "Compliant" is treated as a permanent property instead of a time- and context-dependent assessment.

## Practice
- [ ] Build a compliance-control matrix for an enterprise RAG assistant.
- [ ] Identify personal-data flows and logging exposure.
- [ ] Map five requirements to concrete technical controls and evidence.
- [ ] Add effective/review dates to regulatory assumptions.
- [ ] Design a control-change review triggered by a model/provider change.
- [ ] Explain why a framework checklist cannot replace legal applicability analysis.

## Senior Interview Prompts
1. How do you turn a regulation into architecture controls?
2. What makes compliance evidence auditable?
3. Why should regulatory assumptions have effective dates?
4. How can observability become a privacy risk?
5. Where does legal interpretation end and engineering control design begin?
