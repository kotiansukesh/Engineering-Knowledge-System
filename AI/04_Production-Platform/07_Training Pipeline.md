---
title: "Training Pipeline"
category: "AI/04_Production-Platform"
tags: [mlops, training, pipelines, reproducibility, checkpoints]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-09"
type: concept
---

# Training Pipeline

## Intent
Build reproducible training workflows whose inputs, code, configuration, artifacts, and evaluation results can be traced and rerun.

## Pipeline
**Data snapshot → validation → preprocessing → training → checkpoint → evaluation → registration → approval**

~~~~mermaid
flowchart LR
D[Versioned data] --> V[Validation]
V --> T[Training]
T --> C[Checkpoint]
C --> E[Evaluation]
E --> R[Registry]
R --> A[Approval]
~~~~

## Reproducibility Contract
Record:
- dataset/version and preprocessing code
- source commit
- dependency/runtime versions
- training configuration and random seeds where meaningful
- model artifact/checkpoint
- evaluation dataset and metrics
- hardware/runtime information when relevant

## Reliability
Checkpoint long-running jobs so failures do not require restarting from zero. Make pipeline steps idempotent where possible and separate immutable artifacts from mutable orchestration state.

## Trade-offs
| Decision | Option A | Option B | Driver |
|---|---|---|---|
| Orchestration | managed workflow | Kubernetes-native workflow | platform ownership |
| Checkpoint frequency | frequent | infrequent | recovery time vs storage/overhead |
| Data processing | batch | streaming | freshness vs operational complexity |
| HPO | broad search | constrained search | budget vs exploration |

## Failure Modes
- Data version is missing → results cannot be reproduced.
- Checkpoint is corrupted/incompatible → recovery fails.
- Training job retries duplicate side effects → storage or registry corruption.
- Evaluation uses a different dataset → misleading comparison.
- Pipeline succeeds technically but model quality regresses → quality gate missing.

## Practice
- [ ] Define a reproducibility manifest.
- [ ] Kill a training job and resume from checkpoint.
- [ ] Make a pipeline step idempotent.
- [ ] Add a model-quality gate before registration.
- [ ] Trace one model artifact back to its data and source commit.

## Senior Interview Prompts
1. What makes a training pipeline reproducible?
2. Where should checkpointing occur?
3. How do you make retries safe?
4. What belongs in a model lineage record?
5. Why is pipeline success not equivalent to model success?
