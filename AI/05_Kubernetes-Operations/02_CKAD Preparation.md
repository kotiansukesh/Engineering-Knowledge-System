---
title: "CKAD Preparation"
category: kubernetes
tags: [ai, ckad, cka, kubernetes, certification]
weeks: "28-30"
created: 2026-09-02
completed: false
---

# CKAD Preparation — Weeks 28–30

> Part of [[README|05_Kubernetes-Operations]] • `kubernetes`

## Intent

Earn **CKAD** (or **CKA**) to validate deployment and operational skills after 25 weeks of building.

## CKAD vs CKA

| Cert | Focus | Pick When |
|------|-------|-----------|
| **CKAD** | App-centric: manifests, config, services, troubleshooting | You deploy AI services (recommended) |
| **CKA** | Cluster admin: networking, storage, security, internals | Leaning platform/infra |

## Study Plan (W28–30)

| Week | Focus |
|------|-------|
| 28 | Prometheus + Grafana dashboards, mock exams |
| 29 | Troubleshooting (killer.sh / killerkoda), timed drills |
| 30 | **Exam** + post-exam hardening |

## CKAD Exam Tips

- Imperative `kubectl` (`--dry-run=client -o yaml`) — speed matters.
- Know: pods, deployments, services, ingress, config/secrets, probes, resources, jobs/cronjobs, HPA.
- Practice in `killer.sh` — 2-hour timed environment.

## Success Criteria

- Full platform `kubectl apply` from repo → all pods healthy; dashboards green; exam passed.

## Related

- [[01_Kubernetes Deployment]] • [[AI/00_Overview/Certification Guide|Certification Guide]]

---
*Category: kubernetes*
