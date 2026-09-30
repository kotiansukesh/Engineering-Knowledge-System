---
title: "JUnit 5"
category: "Java/12_Testing-Tooling"
tags: [java, testing, junit5]
created: "2026-09-30"
completed: false
difficulty: "Medium"
type: concept
---

# JUnit 5

## Intent

Use tests to specify observable behavior and protect refactoring, not to maximize line coverage.

## Structure

```java
class PricingServiceTest {

    @Test
    void appliesDiscountForEligibleCustomer() {
        var service = new PricingService();

        var result = service.priceFor(new Customer(true), 100);

        assertEquals(90, result);
    }
}
```

Prefer tests that have one clear behavior and meaningful failure messages.

## Useful JUnit Features

- parameterized tests for input partitions;
- nested tests for related behavior;
- lifecycle hooks only when they clarify setup;
- tags to separate test categories;
- assertions that describe the contract.

## What to Test

Prioritize invariants, boundaries, failure behavior, concurrency behavior, serialization contracts, and integration points. Do not equate high coverage with high confidence.

## Practice

- [ ] Convert one happy-path test into boundary and failure tests.
- [ ] Add a parameterized test for an input partition.
- [ ] Remove a test that only duplicates implementation details.
