---
title: "Kubernetes Deployment"
category: "AI/05_Kubernetes-Operations"
tags: [ai, kubernetes, helm, deployment, probes]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-07"
type: concept
---

# Kubernetes Deployment

## Intent
Design a production deployment for AI services with safe rollout, health checks, resource controls, persistence boundaries, and observable scaling.

## Architecture
~~~~mermaid
flowchart TB
I[Ingress / Gateway] --> D[Deployment]
D --> P[Pods]
P --> S[Service]
D --> H[HPA / KEDA]
P --> M[Metrics + traces]
D --> R[Readiness]
D --> L[Liveness]
~~~~

## Deployment Boundary
Use Kubernetes Deployments for stateless application services and inference workers whose lifecycle is managed by the platform. Treat PostgreSQL, Redis, and other stateful dependencies as separate operational concerns unless there is a deliberate reason to operate them inside the cluster.

## Probe Semantics
- **Readiness:** should the pod receive traffic? It may depend on model loading or dependency readiness.
- **Liveness:** is the process stuck and should Kubernetes restart it? Do not use it as a generic dependency health check.
- **Startup:** does the process need time to initialize before liveness/readiness become meaningful?

For long-running model loading, startup/readiness configuration is often more important than aggressive liveness probes.

## Rollout Choices
| Decision | Safer default | When to change |
|---|---|---|
| Rollout | Rolling update | Blue/green or canary when blast radius is high |
| Scaling | HPA/custom metric | KEDA for queue/event-driven workloads |
| Configuration | Immutable versioned config | Dynamic config when change frequency requires it |
| Storage | External managed state | StatefulSet when operating state in-cluster is intentional |

## Failure Modes
1. Bad readiness probe → healthy capacity removed from service.
2. Liveness kills slow model initialization → restart loop.
3. Missing resource limits → noisy-neighbor/node pressure.
4. Rollout too fast → many replicas fail simultaneously.
5. No rollback signal → bad model/config remains live.
6. Unmanaged persistent data → restore/recovery becomes unclear.

## Evaluation
Test rollout recovery time, readiness correctness, restart rate, p95 latency, pod scheduling time, resource utilization, and rollback success.

## Practice
- [ ] Deploy a service with startup, readiness, and liveness probes.
- [ ] Inject a slow startup and verify no restart loop occurs.
- [ ] Perform a rolling update with one intentionally bad version.
- [ ] Verify rollback and observe traffic during the rollout.
- [ ] Add resource requests/limits and inspect scheduling behavior.

## Senior Interview Prompts
1. Why should readiness and liveness be separate?
2. When should a StatefulSet be used instead of a Deployment?
3. How do you prevent a rollout from taking down all capacity?
4. What signal should trigger rollback?
5. How does model-loading time affect probe design?

## Flashcards
#flashcard
**Q:** What is the difference between readiness and liveness? :: **A:** Readiness controls whether traffic should reach a pod; liveness determines whether the process should be restarted.

#flashcard
**Q:** Why can aggressive liveness probes be dangerous for AI services? :: **A:** Model loading or initialization can legitimately take time, so an overly short liveness threshold can create restart loops.

## Practice Tasks
- [ ] Rebuild the deployment from memory.
- [ ] Inject a failed rollout and execute rollback.
- [ ] Explain probe semantics aloud.
