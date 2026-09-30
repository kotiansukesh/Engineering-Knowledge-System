---
title: Architecture Cost Engineering
type: framework
category: Architect
tags: [architecture, cost, finops]
---

# Architecture Cost Engineering

Cost is an architecture constraint when it changes feasibility or operating behavior.

## Cost model

Estimate compute, database, cache, object storage, network/egress, messaging, observability, backups/DR, managed-service premiums, and operational/team burden.

## Unit economics

Prefer:

- cost / million requests
- cost / active user
- cost / transaction
- cost / GB stored
- cost / event processed

## Questions

1. What is the dominant cost driver?
2. What grows linearly?
3. What grows superlinearly?
4. What happens at 10× traffic?
5. Which reliability requirement increases cost?
6. Which managed service reduces operational burden enough to justify its premium?
7. Which assumption has the highest cost uncertainty?

## Evidence

Record assumptions and replace estimates with observed telemetry whenever possible.
