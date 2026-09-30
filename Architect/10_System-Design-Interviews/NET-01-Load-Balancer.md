---
title: Load Balancer
category: Architect/10_System-Design-Interviews
tags:
- company/amazon
- concept/interview-prep
- difficulty/medium
- horizontal-scaling
- layer4
- layer7
- load-balancer
- pattern/load-balancing
- pattern/system-design
- ssl-termination
created: '2026-09-27'
completed: false
difficulty: Medium
reviewed: '2026-09-15'
sr-due: '2026-09-22'
source: https://github.com/donnemartin/system-design-primer
excalidraw: Load-Balancer-Architecture.excalidraw.json
weeks: '2'
type: note

---











# Load Balancer

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 2
> 🎨 **Visual diagram:** Open Excalidraw template: 

## Intent

[![](/donnemartin/system-design-primer/raw/master/images/h81n9iK.png)](/donnemartin/system-design-primer/blob/master/images/h81n9iK.png)

## Why it Matters

- **Interview signal**: Entry point for any scalable system design
- **Production impact**: Single point of failure if not configured correctly
- **Core concept**: L4 vs L7, algorithms, health checks, SSL termination

[![](/donnemartin/system-design-primer/raw/master/images/h81n9iK.png)](/donnemartin/system-design-primer/blob/master/images/h81n9iK.png)
*[Source: Scalable system design patterns](http://horicky.blogspot.com/2010/10/scalable-system-design-patterns.html)*

Load balancers distribute incoming client requests to computing resources such as application servers and databases. In each case, the load balancer returns the response from the computing resource to the appropriate client. Load balancers are effective at:

- Preventing requests from going to unhealthy servers
- Preventing overloading resources
- Helping to eliminate a single point of failure
Load balancers can be implemented with hardware (expensive) or with software such as HAProxy.

Additional benefits include:

- **SSL termination** - Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations
  - Removes the need to install [X.509 certificates](https://en.wikipedia.org/wiki/X.509) on each server
- **Session persistence** - Issue cookies and route a specific client's requests to same instance if the web apps do not keep track of sessions
To protect against failures, it's common to set up multiple load balancers, either in active-passive or active-active mode.

Load balancers can route traffic based on various metrics, including:

- Random
- Least loaded
- Session/cookies
- [Round robin or weighted round robin](https://www.g33kinfo.com/info/round-robin-vs-weighted-round-robin-lb)
- Layer 4
- Layer 7



Layer 4 load balancers look at info at the transport layer to decide how to distribute requests. Generally, this involves the source, destination IP addresses, and ports in the header, but not the contents of the packet. Layer 4 load balancers forward network packets to and from the upstream server, performing [Network Address Translation (NAT)](https://web.archive.org/web/20240117134735/https://www.nginx.com/resources/glossary/layer-4-load-balancing/).

### Layer 7 load balancing

Layer 7 load balancers look at the application layer to decide how to distribute requests. This can involve contents of the header, message, and cookies. Layer 7 load balancers terminate network traffic, reads the message, makes a load-balancing decision, then opens a connection to the selected server. For example, a layer 7 load balancer can direct video traffic to servers that host videos while directing more sensitive user billing traffic to security-hardened servers.

At the cost of flexibility, layer 4 load balancing requires less time and computing resources than Layer 7, although the performance impact can be minimal on modern commodity hardware.

### Horizontal scaling

Load balancers can also help with horizontal scaling, improving performance and availability. Scaling out using commodity machines is more cost efficient and results in higher availability than scaling up a single server on more expensive hardware, called **Vertical Scaling**. It is also easier to hire for talent working on commodity hardware than it is for specialized enterprise systems.

#### Disadvantage(s): horizontal scaling

- Scaling horizontally introduces complexity and involves cloning servers
  - Servers should be stateless: they should not contain any user-related data like sessions or profile pictures
  - Sessions can be stored in a centralized data store such as a database (SQL, NoSQL) or a persistent cache (Redis, Memcached)
- Downstream servers such as caches and databases need to handle more simultaneous connections as upstream servers scale out

### Disadvantage(s): load balancer

- The load balancer can become a performance bottleneck if it does not have enough resources or if it is not configured properly.
- Introducing a load balancer to help eliminate a single point of failure results in increased complexity.
- A single load balancer is a single point of failure, configuring multiple load balancers further increases complexity.

### Source(s) and further reading

- [NGINX architecture](https://www.nginx.com/blog/inside-nginx-how-we-designed-for-performance-scale/)
- [HAProxy architecture guide](http://www.haproxy.org/download/1.2/doc/architecture.txt)
- [Scalability](https://web.archive.org/web/20220530193911/https://www.lecloud.net/post/7295452622/scalability-for-dummies-part-1-clones)
- [Wikipedia](https://en.wikipedia.org/wiki/Load_balancing_(computing))
- [Layer 4 load balancing](https://www.nginx.com/resources/glossary/layer-4-load-balancing/)
- [Layer 7 load balancing](https://www.nginx.com/resources/glossary/layer-7-load-balancing/)
- [ELB listener config](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html)

## Problems

### System Design Problem: Load Balancer

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Load Balancer - Client-Side with Resilience4j
// Production-ready client-side load balancing with circuit breaker

package com.architect.loadbalancer;

import io.github.resilience4j.circuitbreaker.CircuitBreaker;
import io.github.resilience4j.circuitbreaker.CircuitBreakerConfig;
import io.github.resilience4j.retry.Retry;
import io.github.resilience4j.retry.RetryConfig;
import io.github.resilience4j.timelimiter.TimeLimiter;
import io.github.resilience4j.timelimiter.TimeLimiterConfig;
import org.springframework.cloud.client.loadbalancer.reactive.ReactorLoadBalancerExchangeFilterFunction;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

import java.time.Duration;
import java.util.List;

@Service
public class ResilientServiceClient {

    private final WebClient webClient;
    private final CircuitBreaker circuitBreaker;
    private final Retry retry;
    private final TimeLimiter timeLimiter;

    public ResilientServiceClient(WebClient.Builder builder,
                                  ReactorLoadBalancerExchangeFilterFunction lbFunction) {
        // Circuit Breaker: fail fast when downstream is unhealthy
        this.circuitBreaker = CircuitBreaker.of("backend-service",
            CircuitBreakerConfig.custom()
                .failureRateThreshold(50)
                .waitDurationInOpenState(Duration.ofSeconds(30))
                .slidingWindowSize(10)
                .minimumNumberOfCalls(5)
                .permittedNumberOfCallsInHalfOpenState(3)
                .build());

        // Retry with exponential backoff
        this.retry = Retry.of("backend-retry",
            RetryConfig.custom()
                .maxAttempts(3)
                .waitDuration(Duration.ofMillis(100))
                .exponentialBackoffMultiplier(2)
                .retryExceptions(ConnectException.class, ReadTimeoutException.class)
                .build());

        // Timeout limiter
        this.timeLimiter = TimeLimiter.of("backend-timeout",
            TimeLimiterConfig.custom()
                .timeoutDuration(Duration.ofSeconds(5))
                .build());

        this.webClient = builder
            .baseUrl("lb://backend-service") // Spring Cloud LoadBalancer
            .filter(lbFunction)
            .filter((request, next) -> next.exchange(request)
                .transformDeferred(CircuitBreakerOperator.of(circuitBreaker))
                .transformDeferred(RetryOperator.of(retry))
                .transformDeferred(TimeLimiterOperator.of(timeLimiter))
                .onErrorResume(this::fallback))
            .build();
    }

    public Mono<UserResponse> getUser(String userId) {
        return webClient.get()
            .uri("/api/users/{id}", userId)
            .retrieve()
            .bodyToMono(UserResponse.class);
    }

    private Mono<UserResponse> fallback(Throwable ex) {
        // Return cached/stale data or default
        return Mono.just(UserResponse.cached());
    }
}

// Spring Cloud LoadBalancer custom rule - Least Connections
@Component
class LeastConnectionsRule implements ReactorServiceInstanceLoadBalancer {

    private final AtomicInteger[] connectionCounts;
    private final List<ServiceInstance> instances;

    @Override
    public Mono<Response<ServiceInstance>> choose(Request request) {
        return Mono.fromSupplier(() -> {
            ServiceInstance chosen = instances.stream()
                .min(Comparator.comparingInt(i -> connectionCounts[instances.indexOf(i)].get()))
                .orElseThrow();
            connectionCounts[instances.indexOf(chosen)].incrementAndGet();
            return new DefaultResponse(chosen);
        });
    }

    public void release(ServiceInstance instance) {
        connectionCounts[instances.indexOf(instance)].decrementAndGet();
    }
}
```
## When to Use / When NOT

| **Use When** | **Avoid When** |
|--------------|----------------|
| Building this system from scratch | Managed service covers need |
| Learning architecture patterns | Simple CRUD applications |
| Interview preparation | Requirements don't match |



## Trade-offs
| Dimension | This Approach | Alternative | Trade-off Rationale | Decision Rule |
|-----------|---------------|-------------|---------------------|---------------|
| Complexity | [TBD] | [TBD] | [TBD] | [TBD] |
| Operational Burden | [TBD] | [TBD] | [TBD] | [TBD] |
| Latency | [TBD] | [TBD] | [TBD] | [TBD] |
| Consistency | [TBD] | [TBD] | [TBD] | [TBD] |
| Cost at Scale | [TBD] | [TBD] | [TBD] | [TBD] |

## Vs Table

| Aspect | This Design | Managed Service | Decision Rule |
|--------|-------------|-----------------|---------------|
| Flexibility | Full | Limited | Need custom logic? → Self-host |
| Time to Market | Weeks | Hours | Prototype? → Managed |
| Cost at Scale | Optimizable | Fixed/marginal | High volume? → Self-host |

## Pitfalls

- Underestimating operational complexity
- Ignoring failure modes
- Not planning for 10x scale
- Skipping monitoring/alerting in MVP
- Premature optimization before measuring

## Interview Q&A (Senior Depth)

**Q1: Q1**
**A:** ('Design a load balancer from scratch. What are the key components?', '1) Health checker (active/passive, HTTP/TCP/gRPC). 2) Algorithm (round-robin, least-connections, least-time, consistent-hash, weighted). 3) Connection pool/state table. 4) SSL termination (hardware offload or software). 5) Layer 4 (TCP/UDP) vs Layer 7 (HTTP) routing. 6) HA setup: active-passive (VRRP) or active-active (anycast/ECMP). 7) Metrics: RED (rate, errors, duration) per backend.')

**Q2: Q2**
**A:** ('L4 vs L7 load balancing - when to use each?', 'L4: TCP/UDP, lower latency (~1ms), no HTTP parsing, no cookie affinity, no content routing. Use for: raw throughput, non-HTTP protocols, TLS passthrough. L7: HTTP-aware, path/host routing, cookie affinity, SSL termination, WAF, compression. Use for: microservices, API gateways, canary deployments. Most modern systems use both: L4 at edge, L7 per service.')

**Q3: Q3**
**A:** ('How do you handle session persistence without sticky sessions?', 'Stateless design: external session store (Redis, DB). JWT with short expiry + refresh tokens. Client-side affinity via consistent hashing (IP + user-agent). If sticky required: cookie-based (insert cookie), source IP hash (problematic behind NAT). Prefer stateless.')

**Q4: Q4**
**A:** ('What happens when a backend becomes unhealthy?', 'Active checks: remove from pool after N consecutive failures. Passive checks: track 5xx/timeout rate, eject if > threshold. Graceful drain: stop new connections, wait for in-flight (drain timeout). Circuit breaker: fast-fail before health check catches up. Slow-start: gradually add back after recovery.')

**Q5: Q5**
**A:** ('How do you scale the load balancer itself?', 'Horizontal: DNS round-robin, anycast IP, ECMP. Cloud: ALB/NLB/GCLB auto-scale. On-prem: HAProxy/Envoy cluster with keepalived/VRRP or BGP anycast. State sync: connection table replication (expensive) or stateless (prefer). Metrics: connections/sec, active connections, CPU, memory.')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is a load balancer? :: **A:** Distributes incoming requests across multiple backend servers #flashcard

#flashcard
**Q:** L4 vs L7 load balancing? :: **A:** L4: TCP/UDP, no HTTP parsing. L7: HTTP-aware, path routing, SSL termination, WAF #flashcard

#flashcard
**Q:** Common LB algorithms? :: **A:** Round-robin, Least Connections, Least Time, Consistent Hash, Weighted, IP Hash #flashcard

#flashcard
**Q:** What is SSL termination? :: **A:** Decrypt at LB, encrypt to backend. Removes cert management from backends #flashcard

#flashcard
**Q:** What is session persistence? :: **A:** Route same client to same backend (cookie, IP hash). Prefer stateless with Redis #flashcard

#flashcard
**Q:** Active vs Passive health checks? :: **A:** Active: LB sends probes. Passive: monitors real traffic (5xx, timeouts) #flashcard

#flashcard
**Q:** What is graceful drain? :: **A:** Stop new connections, wait for in-flight requests to complete before removing backend #flashcard

#flashcard
**Q:** What is circuit breaker? :: **A:** Fast-fail when error rate exceeds threshold, prevent cascade failures #flashcard

#flashcard
**Q:** How to scale the LB itself? :: **A:** DNS round-robin, anycast IP, ECMP, cloud managed (ALB/NLB/GCLB) #flashcard

#flashcard
**Q:** What is slow start? :: **A:** Gradually add recovered backend back to pool to avoid overwhelming it #flashcard

#flashcard
**Q:** What is connection pooling? :: **A:** Reuse backend connections to reduce handshake overhead #flashcard

#flashcard
**Q:** What is RED metrics? :: **A:** Rate, Errors, Duration - key metrics per backend #flashcard

#flashcard
**Q:** What is USE metrics? :: **A:** Utilization, Saturation, Errors - for resource monitoring #flashcard

#flashcard
**Q:** L4 vs L7 latency? :: **A:** L4: ~1ms. L7: ~2-5ms (HTTP parsing overhead) #flashcard

#flashcard
**Q:** When to use L4 vs L7? :: **A:** L4: raw throughput, non-HTTP, TLS passthrough. L7: microservices, canary, API gateway #flashcard
## Practice Tasks (Tasks Plugin)

- [ ] Explain the architecture from memory 📅 {date:YYYY-MM-DD, +1}
- [ ] Draw the system diagram without looking 📅 {date:YYYY-MM-DD, +3}
- [ ] Answer all Interview Q&A aloud 📅 {date:YYYY-MM-DD, +7}
- [ ] Review flashcards (Spaced Repetition) 📅 {date:YYYY-MM-DD, +1}

```tasks
not done
path includes 10_System-Design-Interviews
sort by due
limit 10
```

## Related

- [[Architect/10_System-Design-Interviews/README|System Design Interviews Folder]]
- [[Architect/03_Architecture-Styles/README|Architecture Styles]]
- [[Architect/08_NonFunctional-Ops/README|Non-Functional Requirements]]
- [[Architect/07_Integration-APIs/README|Integration Patterns]]

---

*Category: Architect/10_System-Design-Interviews • Part of [[README|MOC]]*