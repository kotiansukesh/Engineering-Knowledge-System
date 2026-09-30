---
title: "Feature Store"
category: "AI/04_Production-Platform"
tags: [feature-store, online-offline, point-in-time, mlops]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-13"
type: concept
---

# Feature Store

## Intent
Understand when a feature store solves a real consistency/reuse problem and when ordinary data services are simpler.

## Core Model
A feature store typically separates:
- feature definitions and ownership
- offline historical storage for training
- online low-latency serving
- transformation/materialization
- lineage and freshness metadata

## Critical Invariant
**Training-time features must represent only information available at prediction time.**

Point-in-time correctness prevents leakage from future data into historical training examples.

## When It Helps
- many models reuse common features
- online and offline feature consistency matters
- feature ownership/lineage needs centralization
- low-latency feature retrieval is required

## When It Adds Unnecessary Complexity
- one model with simple transformations
- features can be computed cheaply at request time
- no shared feature ownership problem
- latency requirements do not justify an online store

## Failure Modes
- training/serving skew
- stale materialized features
- point-in-time leakage
- online/offline schema mismatch
- cache/storage outage

## Practice
- [ ] Define one feature with offline and online representations.
- [ ] Construct a leakage example and fix it.
- [ ] Measure feature freshness and online latency.
- [ ] Decide whether a feature store is justified for a small service.
- [ ] Document the ownership and lineage model.

## Senior Interview Prompts
1. What problem does a feature store actually solve?
2. Explain point-in-time correctness.
3. How does training-serving skew happen?
4. When would you not introduce a feature store?
5. What availability guarantees should online features have?
