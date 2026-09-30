---
title: Failure Injection Lab
type: practice
category: Architect
tags: [architecture, reliability, chaos, practice]
---

# Failure Injection Lab

The objective is not to name resilience patterns. The objective is to reason about blast radius, degraded behavior, detection and recovery.

## Standard injections

| Injection | Questions |
|---|---|
| Database unavailable | What remains writable? What is cached? How is recovery reconciled? |
| Queue unavailable | Do producers block, buffer or degrade? What is the durability boundary? |
| Duplicate delivery | Is the business operation idempotent? Where is the dedupe key? |
| Hot partition | How is skew detected and relieved? |
| Network partition | What consistency guarantees are sacrificed? |
| Region failure | What are the RTO/RPO and failover path? |
| Dependency timeout | What prevents cascading failure? |
| Bad deployment | How is rollback detected and executed? |
| Replication lag | Which reads become unsafe? |
| Storage corruption | How are backups validated and restored? |

## Failure record

~~~yaml
failure:
blast_radius:
detection:
user_impact:
degraded_mode:
data_loss:
recovery:
reconciliation:
evidence_needed:
redesign_trigger:
~~~

## Rule

Every architecture should answer:

1. What fails first?
2. How do we detect it?
3. What does the user experience?
4. What remains correct?
5. How do we recover?
6. What evidence would cause redesign?
