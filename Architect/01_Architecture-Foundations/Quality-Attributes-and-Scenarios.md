---
title: Quality Attributes and Scenarios
type: concept
category: Architect/01_Architecture-Foundations
difficulty: Intermediate
completed: false
reviewed:
sr-due:
tags: [architecture, foundations, quality-attributes, NFR]
---

# Quality Attributes and Scenarios

## Purpose

Quality attributes describe **how** a system behaves under conditions. They become useful only when translated into measurable scenarios.

## Common qualities

Availability, reliability, performance, scalability, security, modifiability, operability, observability, recoverability, durability, consistency and cost efficiency.

These qualities can conflict. Architecture is largely the work of managing those conflicts.

## Scenario format

**Source → Stimulus → Environment → Artifact → Response → Measure**

Example:

> During loss of one availability zone, checkout remains available with **RTO ≤ 5 minutes** and **no acknowledged orders lost**.

## Weak vs useful

| Weak | Useful |
|---|---|
| "Highly available" | "After one-zone loss, checkout recovers within 5 minutes" |
| "Scalable" | "At 2× forecast peak, p99 remains below 300 ms" |
| "Secure" | "Unauthorized tenant access is rejected and audited" |
| "Fast" | "Search p95 remains below 200 ms for the defined workload" |

## NFR vs constraint

A **quality requirement** describes desired behavior.

A **constraint** limits the solution space.

Examples:

- NFR: p99 < 200 ms
- Constraint: data must remain in a specified region
- NFR: RTO < 30 minutes
- Constraint: must integrate with an existing payment provider

## Scenario review

A scenario should answer:

1. Who/what generates the stimulus?
2. Under what environment?
3. Which artifact is affected?
4. What response is required?
5. How is success measured?
6. What test or telemetry provides evidence?

## Practice

Rewrite "scalable", "secure", "reliable", "fast" and "cheap" as measurable scenarios.

Then identify the architecture decision each scenario influences.

## Practice tasks

- [ ] Write five quality scenarios
- [ ] Identify one quality conflict for each
- [ ] Attach one architecture decision to each
- [ ] Define how each requirement will be tested
