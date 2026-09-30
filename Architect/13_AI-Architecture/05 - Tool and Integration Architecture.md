---
title: AI Tool and Integration Architecture
type: note
category: Architect/13_AI-Architecture
difficulty: Hard
tags: [architecture, ai, integration]
---

# AI Tool and Integration Architecture

Tools turn model output into system actions, so they require normal distributed-system controls.

## Required properties

- explicit schemas
- authorization
- idempotency
- timeouts
- rate limits
- auditability
- bounded retries
- result validation

## Rule

Treat an AI tool call as an untrusted request crossing a system boundary.
