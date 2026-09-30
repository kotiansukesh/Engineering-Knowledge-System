---
title: Capstone Checklist
category: Architect/99_Revision
tags:
- capstone
- checklist
- design-review
- difficulty/easy
created: 2026-09-03
completed: false
reviewed: '2026-08-31'
sr-due: '2026-09-03'
difficulty: Easy
excalidraw: ''
source: ''
type: note
weeks: ''

---





## Why it Matters

A design is not done when it works; it's done when it survives review. This checklist is the pre-submission gate, the questions a senior reviewer or interviewer will ask anyway, answered before they're asked, so "done" means evidence rather than intention.

## Diagram

```mermaid
graph TD
 D[Draft design] --> G{Gate checklist}
 G -->|Scope & quality| S[C1/C2, scenarios, fitness]
 G -->|Data & integration| DA[SOT per entity, contracts, migration]
 G -->|NFRs| N[SLOs, security, resilience, cost]
 G -->|Operate & govern| O[GitOps, ADRs, compliance evidence]
 S --> R[Review-ready: every box cites an artifact]
 DA --> R
 N --> R
 O --> R
 R --> ADR[Gaps become ADRs or follow-up tasks]
```

## Code

```yaml

## When to use / NOT

- **Use:** before calling any design complete — tick every box, and treat an unticked one as a follow-up task or an ADR, not an omission.
- **Use:** in interview practice as the closing structure for a system-design answer: scope → data → NFRs → operate. It makes a 40-minute answer cover what a senior panel scores on.
- **Use:** as a review checklist in real design reviews — it converts "looks fine" into a list of evidence.

**When NOT:** do not treat it as a document to fill in once — it is a gate that runs per design decision, and a checked box from six months ago is not evidence about the system today. Do not tick from memory: each item should cite an artifact (diagram, ADR, dashboard link, Helm value), because un-cited checks are how designs pass review and fail in production.


## Vs

| Companion | Difference |
|---|---|
| [[Interview-Bank]] | Questions to answer; this is the design gate those answers must satisfy |
| [[Case-Studies]] | Applied designs *under constraint*; this is the generic gate they all pass |
| [[../09_Governance-Documentation/03_Review-Process-RFC\|Review/RFC]] | The social process around the checklist — who reviews, who decides |



## Trade-offs
| Dimension | This Approach | Alternative | Trade-off Rationale | Decision Rule |
|-----------|---------------|-------------|---------------------|---------------|
| Complexity | [TBD] | [TBD] | [TBD] | [TBD] |
| Operational Burden | [TBD] | [TBD] | [TBD] | [TBD] |
| Latency | [TBD] | [TBD] | [TBD] | [TBD] |
| Consistency | [TBD] | [TBD] | [TBD] | [TBD] |
| Cost at Scale | [TBD] | [TBD] | [TBD] | [TBD] |

## Pitfalls

- Ticking boxes without citing an artifact — cite the ADR, dashboard, or manifest.
- Completeness over priority: a fully checked list with no top-3 risks named is still not a design.
- One-time use — re-run it per design decision, and supersede stale passes.

## Interview Q&A

**Q: How do you know when a design is "done"?**
A: When each gate section has cited evidence and the remaining gaps are owned — a C1/C2 pair, quality scenarios with measures, named fitness functions, a state map with a justified consistency choice, versioned contracts with idempotency stated, a migration plan with rollback, SLOs with burn-rate alerts, security controls, resilience plus a named chaos test, a unit-cost metric, GitOps with canary and pinned images, ADRs for the irreversible calls, and a compliance scope with an evidence location. Anything unticked is either an ADR or a task with an owner — that's what makes it done rather than merely drawn.

**Q: Which box do candidates most often leave empty in a system-design interview?**
A: The rollback/migration plan and the cost model. Candidates design the steady state and forget the transition — expand-migrate-contract, backfill, and a rollback path — and they never name a unit-cost metric. Those two are what separate a senior answer from a mid-level one, and they're cheap to add if you hold 5 minutes for them at the end.

**Q: A reviewer says your design "looks reasonable". Is it done?**
A: Not until "looks reasonable" becomes specific evidence: run the checklist and ask which box gave them confidence. A vague approval doesn't survive an incident, and the checklist's job is exactly to replace impressions with artifacts.

**Q: How is this different from a definition-of-done checklist?**
A: Scope and consequences. A DoD covers a ticket (merged, tested, documented); this covers a *design decision* — data ownership, consistency stance, failure modes, compliance scope — the things that outlive the ticket and show up in the next ADR, the next audit, or the next incident review.


## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core concept of Capstone Checklist? :: **A:** [Key algorithm/architecture pattern] #flashcard

#flashcard
**Q:** When do you apply Capstone Checklist? :: **A:** [Trigger scenarios and context] #flashcard

#flashcard
**Q:** What is the primary trade-off in Capstone Checklist? :: **A:** [Main tension: e.g., consistency vs latency] #flashcard

#flashcard
**Q:** What breaks first at scale in Capstone Checklist? :: **A:** [Primary bottleneck: e.g., coordination, hot keys, replication lag] #flashcard

#flashcard
**Q:** How do you handle failures in Capstone Checklist? :: **A:** [Retry, circuit breaker, fallback, graceful degradation] #flashcard

#flashcard
**Q:** What are the key metrics to monitor for Capstone Checklist? :: **A:** [RED: rate, errors, duration; USE: utilization, saturation, errors] #flashcard

#flashcard
**Q:** How does Capstone Checklist scale to 10x? :: **A:** [Sharding, read replicas, async processing, caching layers] #flashcard

#flashcard
**Q:** What is the consistency model for Capstone Checklist? :: **A:** [Strong/eventual/causal - justify with use case] #flashcard

#flashcard
**Q:** How do you test Capstone Checklist? :: **A:** [Contract tests, chaos engineering, load tests, fault injection] #flashcard

#flashcard
**Q:** What is the operational cost of Capstone Checklist? :: **A:** [Team expertise, tooling, on-call burden, migration risk] #flashcard

#flashcard
**Q:** When would you NOT use Capstone Checklist? :: **A:** [Managed service covers need, simple CRUD, team lacks maturity] #flashcard

#flashcard
**Q:** What is the key design decision in Capstone Checklist? :: **A:** [The irreversible choice that defines the architecture] #flashcard

#flashcard
**Q:** How do you migrate to Capstone Checklist? :: **A:** [Strangler fig, dual-write, canary, feature flags] #flashcard

#flashcard
**Q:** What security considerations for Capstone Checklist? :: **A:** [AuthZ, encryption, audit, secrets management] #flashcard

#flashcard
**Q:** How do you debug Capstone Checklist in production? :: **A:** [Structured logging, correlation IDs, distributed tracing, SLO alerts] #flashcard


## Practice Tasks (Tasks Plugin)
- [ ] Explain the architecture from memory 📅 {{date:YYYY-MM-DD, +1}}
- [ ] Draw the system diagram without looking 📅 {{date:YYYY-MM-DD, +3}}
- [ ] Answer all Interview Q&A aloud 📅 {{date:YYYY-MM-DD, +7}}
- [ ] Review flashcards (Spaced Repetition) 📅 {{date:YYYY-MM-DD, +1}}

```tasks
not done
path includes Architect/99_Revision
sort by due
limit 10
```

## Related

- [[Interview-Bank]] · [[Case-Studies]] · [[../09_Governance-Documentation/03_Review-Process-RFC\|Review/RFC]]
- Inputs: [[../02_Requirements-Quality-Attributes/Quality-Scenarios\|Quality Scenarios]] · [[../02_Requirements-Quality-Attributes/Fitness-Functions\|Fitness Functions]] · [[../09_Governance-Documentation/02_ADRs\|ADRs]]
- NFRs: [[../08_NonFunctional-Ops/03_Performance-SLOs\|SLOs]] · [[../08_NonFunctional-Ops/05_Cloud-K8s-Deploy-Helm\|K8s Deploy]]

# CI-side evidence of a passed gate (the checklist's automated twin):

boundary-test: # ArchUnit / Spring Modulith verify in CI
 modules: [order, inventory, payment]
 rule: no cross-module access to *.internal
load-gate: # k6/Gatling, scenario from Quality-Scenarios
 script: checkout_p99_300ms_500rps.js
 fail_on: p(99) > 300
security-scan: # OWASP dep-check + gitleaks + image CVE
 block_on: HIGH
deploy: # Helm + canary + probes + PDB, pinned images
 strategy: canary
 rollback_on: slo_burn_rate > 14.4
```

# Capstone Checklist, Design Gate

Tick before calling any design done (`completed: true` only when all pass).

## Scope & Quality

- [ ] C1 context + C2 containers drawn (actors, boundaries, protocols)
- [ ] Quality scenarios written (stimulus→response→measure) + top-3 risks
- [ ] Fitness functions named (what fails the build?)

## Data & Integration

- [ ] State map: system-of-record per entity; consistency choice (CAP/PACELC) justified
- [ ] Contracts versioned (REST/OAS or proto); idempotency + ordering stated
- [ ] Migration plan: expand-migrate-contract + rollback + backfill

## NFRs

- [ ] SLOs (p50/p95/p99 + availability) + burn-rate alerts + dashboard link
- [ ] Security: OAuth scopes, secrets mgmt, PII encryption/redaction
- [ ] Resilience: breaker/bulkhead/fallback + chaos test named
- [ ] Cost: unit-cost metric + rightsizing/HPA-KEDA story

## Operate & Govern

- [ ] Helm + GitOps + canary + probes/PDBs; image pin + CVE gate
- [ ] ADRs for irreversible calls; RFC link; runbook + GameDay date
- [ ] Compliance scope named (PCI/SOC2/DPDP) with evidence location
```dataview
TASK FROM "Architect/99_Revision/Capstone-Checklist" WHERE !completed
```