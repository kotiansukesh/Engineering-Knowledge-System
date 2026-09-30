---
title: Architect Roles
type: note
category: Architect/01_Architecture-Foundations
difficulty: Beginner
completed: false
reviewed:
sr-due:
tags: [architecture, foundations, roles, enterprise]
---

# Architect Roles

## Purpose

Architect is a set of responsibilities, not necessarily a job title.

The same senior engineer can perform different architecture responsibilities depending on scope.

## Role dimensions

| Role | Primary scope | Typical decisions |
|---|---|---|
| Solution Architect | One solution/product | system shape, integrations, NFRs |
| Domain Architect | Business/domain area | boundaries, domain models, cross-system consistency |
| Platform Architect | Shared platform | capabilities, guardrails, developer experience |
| Enterprise Architect | Organization | capabilities, portfolio, standards, target state |
| Software Architect | Technical system | structures, dependencies, quality attributes |

These roles overlap. Avoid treating the labels as rigid organizational laws.

## Scope model

~~~text
Enterprise
    ↓
Domain / Capability
    ↓
Solution / Product
    ↓
Platform / Shared Services
    ↓
Implementation
~~~

A decision should be made at the lowest level that has enough context and authority, while respecting higher-level constraints.

## Architect responsibilities

An architect should be able to:

1. clarify ambiguous goals;
2. identify stakeholders and constraints;
3. quantify important requirements;
4. choose and communicate boundaries;
5. evaluate alternatives;
6. record significant decisions;
7. identify failure modes;
8. validate architecture with evidence;
9. guide evolution and migration;
10. communicate trade-offs to technical and non-technical audiences.

## Architect vs senior engineer

A senior engineer may optimize implementation within a boundary.

An architect additionally owns the consequences **across boundaries and over time**.

The distinction is responsibility and scope, not seniority hierarchy.

## Anti-patterns

- architect as diagram author;
- architect as technology gatekeeper;
- architect making decisions without teams;
- architecture board approving every implementation detail;
- separating architecture from production ownership.

## Practice

Take one real system and answer:

- What decisions belong to the solution level?
- Which belong to a platform?
- Which should remain with implementation teams?
- Which decisions require enterprise-level alignment?

## Practice tasks

- [ ] Map one system's decisions by scope
- [ ] Identify one decision that should be delegated
- [ ] Identify one decision requiring cross-domain alignment
- [ ] Explain the architect's responsibility in one minute
