---
title: "Model Registry"
category: "AI/04_Production-Platform"
tags: [mlops, model-registry, lineage, versioning, governance]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-11"
type: concept
---

# Model Registry

## Intent
Use a registry as the control point for model artifacts, lineage, evaluation evidence, ownership, and promotion state.

## Model Record
A useful model version links:
**artifact → source commit → data version → configuration → evaluation results → environment → owner → approval → deployment history**

## Promotion
Prefer evidence-based states such as:
**candidate → validated → approved → deployed → retired**

Promotion should be a controlled decision, not merely a file copy.

## Registry vs Artifact Store
An artifact store holds bytes. A registry adds metadata, lineage, lifecycle state, and governance around those artifacts.

## Failure Modes
- Mutable artifact is overwritten → deployed model cannot be reproduced.
- Metadata is incomplete → lineage cannot be reconstructed.
- Approval is detached from exact version → wrong model gets promoted.
- Registry becomes the only source of truth while runtime configuration diverges.

## Practice
- [ ] Define a model-version schema.
- [ ] Register two versions with different evaluation results.
- [ ] Trace a production deployment back to source/data.
- [ ] Define promotion and retirement criteria.
- [ ] Simulate accidental promotion of an unapproved version and design the control.

## Senior Interview Prompts
1. What belongs in a model registry?
2. Why is an artifact store insufficient?
3. How do you guarantee deployment references an immutable version?
4. How should approval relate to model version?
5. What should happen when a deployed model is retired?
