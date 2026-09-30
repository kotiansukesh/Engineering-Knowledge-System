---
title: "Testcontainers"
category: "Java/12_Testing-Tooling"
tags: [java, testing, integration, testcontainers, docker]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
type: "note"
---

# Testcontainers

## Intent

Run integration tests against real disposable dependencies instead of relying on mocks for behavior that belongs to the dependency.

## Good Fit

- PostgreSQL/MySQL behavior;
- Kafka or messaging semantics;
- Redis integration;
- schema migration tests;
- database indexes and constraints;
- serialization or protocol compatibility.

## Example

```java
@Testcontainers
class RepositoryIT {
    @Container
    static PostgreSQLContainer<?> postgres =
        new PostgreSQLContainer<>("postgres:17");

    @Test
    void persistsAndReadsEntity() {
        // connect application to postgres.getJdbcUrl()
        // exercise the real repository
    }
}
```

Pin image versions and keep test data deterministic.

## Trade-off

Real dependencies increase test time and infrastructure requirements, but they catch failures that mocks cannot represent.

## Practice

- [ ] Add a PostgreSQL integration test.
- [ ] Run the same repository test against a real container and a unit-test double.
- [ ] Document what each test catches that the other does not.
