---
title: AI Memory Architecture
type: concept
category: Architect/13_AI-Architecture
difficulty: Hard
tags: [architecture, ai, memory]
---

# AI Memory Architecture

Separate memory by purpose.

| Memory | Purpose | Risk |
|---|---|---|
| Working context | current task | context limits |
| Episodic | prior interactions/events | stale or irrelevant data |
| Semantic | durable knowledge | access control |
| Procedural | reusable behavior | unsafe automation |

## Questions

- What should be forgotten?
- What is authoritative?
- How is memory corrected?
- What access controls apply?
## Memory selection

Do not persist information merely because it is available.

For each memory type define:

- owner and source of truth;
- retention period;
- write policy;
- retrieval policy;
- correction/deletion path;
- tenant/security boundary;
- freshness expectation.

Working context should not automatically become durable memory.

## Failure modes

Test stale memory, contradictory memory, unauthorized recall, accidental persistence and unbounded context growth.

## Evidence

Show a memory lifecycle from write → store → retrieve → validate → correct/delete, including access-control enforcement.
