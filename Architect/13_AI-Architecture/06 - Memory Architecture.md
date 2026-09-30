---
title: AI Memory Architecture
type: note
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
