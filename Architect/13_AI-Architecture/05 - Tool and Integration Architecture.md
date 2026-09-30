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
## Contract design

A production tool contract should define:

- typed input/output schema;
- authentication and authorization;
- idempotency semantics;
- timeout and cancellation behavior;
- retry policy;
- rate limits and quotas;
- audit events;
- validation of tool results;
- versioning and backward compatibility.

Authorization must be enforced by the tool/service boundary, not delegated to the model.

## Failure modes

Test duplicate requests, malformed arguments, unauthorized access, timeout, stale results, partial success and downstream retries.

## Evidence

Document one tool contract, one failure experiment and one ADR covering a consequential integration decision.
