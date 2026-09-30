---
title: "ML Data Pipeline"
category: "AI/04_Production-Platform"
tags: [data-pipeline, etl, streaming, lineage, mlops]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-12"
type: "note"
---

# ML Data Pipeline

## Intent
Design data flows that preserve correctness, freshness, lineage, and recoverability from source to training or inference.

## Batch vs Streaming
| Need | Batch | Streaming |
|---|---|---|
| Freshness | minutes/hours | seconds/sub-seconds |
| Operational complexity | lower | higher |
| Replay | straightforward | requires durable event/log design |
| Typical fit | training/periodic features | real-time inference features/events |

Choose based on freshness and recovery requirements, not fashion.

## Pipeline Contract
Every stage should make explicit:
- schema
- ownership
- freshness expectation
- quality checks
- partitioning/keying
- retry behavior
- lineage
- retention

## Failure Modes
- Schema change breaks downstream consumers.
- Duplicate delivery creates duplicate training examples/events.
- Late data changes aggregates.
- Partial pipeline success creates inconsistent snapshots.
- Backfill changes historical results without versioning.

## Practice
- [ ] Design a batch training-data pipeline.
- [ ] Add schema compatibility checks.
- [ ] Simulate duplicate and late events.
- [ ] Design a replay/backfill procedure.
- [ ] Trace one dataset to its source and downstream model.

## Senior Interview Prompts
1. When is streaming unnecessary?
2. How do you make data processing idempotent?
3. How should late-arriving data be handled?
4. What makes a dataset reproducible?
5. How does lineage help incident response?
