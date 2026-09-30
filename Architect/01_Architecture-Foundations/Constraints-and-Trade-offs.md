---
title: Constraints and Trade-offs
type: concept
category: Architect/01_Architecture-Foundations
difficulty: Intermediate
completed: false
reviewed:
sr-due:
tags: [architecture, foundations, constraints, trade-offs]
---

# Constraints and Trade-offs

## Purpose

Good architecture does not maximize every quality. It satisfies important constraints while making compromises explicit.

## Constraint hierarchy

1. **Hard:** cannot be violated
2. **Required:** must normally be satisfied
3. **Target:** desired but negotiable
4. **Preference:** team or technology preference

This prevents preferences from masquerading as requirements.

## Trade-off process

~~~text
Constraint
   ↓
Candidate options
   ↓
Benefits
   ↓
Costs + risks
   ↓
Reversibility
   ↓
Evidence
   ↓
Decision
~~~

## Decision matrix

| Dimension | Option A | Option B | Evidence |
|---|---|---|---|
| Latency | | | |
| Consistency | | | |
| Availability | | | |
| Cost | | | |
| Complexity | | | |
| Team capability | | | |
| Migration risk | | | |

Do not invent precision by scoring uncertain assumptions as exact numbers.

## Reversibility

Cheap-to-reverse decisions can be tested.

Expensive-to-reverse decisions deserve:

- more evidence;
- prototypes/spikes;
- explicit assumptions;
- migration planning;
- review triggers.

## Common errors

- technology-first design;
- cargo-cult microservices;
- optimizing average instead of tail latency;
- ignoring operational cost;
- treating all requirements as equally important;
- hiding trade-offs instead of recording them.

## Practice

Compare modular monolith vs microservices under:

1. small team, moderate scale;
2. multiple autonomous teams;
3. strict independent deployment.

The architecture should change when the constraints change.

## Practice tasks

- [ ] Separate requirements from preferences
- [ ] Build one trade-off matrix
- [ ] Identify the least reversible decision
- [ ] State what evidence would change the decision
