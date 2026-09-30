---
title: Fitness Functions and Architecture Runway
type: note
category: Architect/01_Architecture-Foundations
difficulty: Advanced
completed: false
reviewed:
sr-due:
tags: [architecture, foundations, fitness-functions, governance]
---

# Fitness Functions and Architecture Runway

## Purpose

Architecture needs feedback. Fitness functions turn important architectural properties into repeatable checks.

## Fitness function

**Property → Measurement → Threshold → Frequency → Owner → Action**

Examples:

- ArchUnit enforces dependency direction.
- Load tests verify p99 against an SLO.
- Recovery drills verify RTO.
- Security tests enforce policy.
- Cost telemetry checks cost per transaction.
- Contract tests protect event/API compatibility.

## Architecture runway

Architecture runway is the technical capability and structural preparation needed for near-term product evolution.

It should be driven by:

- known product needs;
- architectural risk;
- measured constraints;
- migration lead time.

It is **not** permission to build speculative infrastructure.

## Architecture drift

Drift occurs when implementation gradually violates intended architecture.

Detect it through:

- dependency analysis;
- runtime telemetry;
- configuration checks;
- security controls;
- operational metrics;
- architecture reviews.

## Practice

For a modular Spring Boot application define:

1. dependency fitness function;
2. performance fitness function;
3. security fitness function;
4. operational fitness function.

For each define threshold, owner and action on failure.

## Practice tasks

- [ ] Define four fitness functions
- [ ] Choose measurable thresholds
- [ ] Identify owners
- [ ] Identify one current drift risk
