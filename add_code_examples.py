#!/usr/bin/env python3
"""
Add real Spring Boot 3.5 / Java 25 code examples for top 20 patterns.
"""

import yaml
import re
from pathlib import Path

TARGET = Path('/Users/sukesh/Documents/GitHub/Obsidian/Architect/10_System-Design-Interviews')

CODE_EXAMPLES = {
    'FND-04-CAP-Theorem.md': '''```java
// Java 25 / Spring Boot 3.5: CAP Theorem - Tunable Consistency Client
// Demonstrates how to configure consistency level per operation

package com.architect.cap;

import org.springframework.data.cassandra.core.CassandraTemplate;
import org.springframework.data.cassandra.core.query.Query;
import org.springframework.data.cassandra.core.query.ConsistencyLevel;
import org.springframework.stereotype.Service;
import reactor.core.publisher.Mono;

@Service
public class TunableConsistencyService {

    private final CassandraTemplate cassandraTemplate;

    public TunableConsistencyService(CassandraTemplate cassandraTemplate) {
        this.cassandraTemplate = cassandraTemplate;
    }

    // Strong consistency (CP) - for financial transactions
    public Mono<User> getUserStrongConsistency(String userId) {
        Query query = Query.query(where("id").is(userId))
            .consistencyLevel(ConsistencyLevel.QUORUM); // R + W > N
        return cassandraTemplate.selectOne(query, User.class);
    }

    // Eventual consistency (AP) - for user profile reads
    public Mono<User> getUserEventualConsistency(String userId) {
        Query query = Query.query(where("id").is(userId))
            .consistencyLevel(ConsistencyLevel.ONE); // Low latency, may be stale
        return cassandraTemplate.selectOne(query, User.class);
    }

    // Per-operation consistency based on business context
    public Mono<Account> transferFunds(TransferRequest req) {
        return cassandraTemplate.getSession()
            .executeReactive(
                "BEGIN BATCH " +
                "UPDATE accounts SET balance = balance - ? WHERE id = ? IF balance >= ?; " +
                "UPDATE accounts SET balance = balance + ? WHERE id = ?; " +
                "APPLY BATCH;",
                req.amount(), req.fromAccount(), req.amount(),
                req.amount(), req.toAccount()
            )
            .map(result -> result.one().getBool("[applied]"))
            .filter(applied -> applied)
            .switchIfEmpty(Mono.error(new InsufficientFundsException()));
    }
}

// Configuration for different consistency profiles
@Configuration
class CassandraConsistencyConfig {

    @Bean
    public CassandraClusterFactoryBean cluster() {
        CassandraClusterFactoryBean cluster = new CassandraClusterFactoryBean();
        cluster.setContactPoints("cassandra-1,cassandra-2,cassandra-3");
        cluster.setPort(9042);
        cluster.setConsistencyLevel(ConsistencyLevel.LOCAL_QUORUM); // Default
        return cluster;
    }
}
```''',
    
    'NET-01-Load-Balancer.md': '''```java
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
```''',

    'DB-05-Sharding.md': '''```java
// Java 25 / Spring Boot 3.5: Sharding - Consistent Hashing Router with Vitess
// Production sharding router with virtual nodes and hotspot handling

package com.architect.sharding;

import com.google.common.hash.Hashing;
import org.springframework.stereotype.Component;

import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;

@Component
public class ConsistentHashShardRouter {

    private static final int VIRTUAL_NODES = 150;
    private final TreeMap<Long, String> ring = new TreeMap<>();
    private final Map<String, ShardInfo> shards = new ConcurrentHashMap<>();
    private final Map<String, AtomicInteger> hotKeyCounters = new ConcurrentHashMap<>();

    public void addShard(String shardId, String host, int port, int weight) {
        ShardInfo info = new ShardInfo(shardId, host, port, weight);
        shards.put(shardId, info);
        
        // Add virtual nodes proportional to weight
        int vnodes = VIRTUAL_NODES * weight;
        for (int i = 0; i < vnodes; i++) {
            String virtualKey = shardId + "-vn-" + i;
            long hash = Hashing.murmur3_128().hashString(virtualKey, StandardCharsets.UTF_8).asLong();
            ring.put(hash, shardId);
        }
    }

    public void removeShard(String shardId) {
        shards.remove(shardId);
        ring.values().removeIf(v -> v.equals(shardId));
    }

    public String getShard(String key) {
        if (ring.isEmpty()) throw new IllegalStateException("No shards available");
        
        long hash = Hashing.murmur3_128().hashString(key, StandardCharsets.UTF_8).asLong();
        Map.Entry<Long, String> entry = ring.ceilingEntry(hash);
        String shardId = (entry != null) ? entry.getValue() : ring.firstEntry().getValue();
        
        // Hotspot detection: if key accessed > threshold, route to dedicated cache
        AtomicInteger counter = hotKeyCounters.computeIfAbsent(key, k -> new AtomicInteger(0));
        if (counter.incrementAndGet() > 10000) { // Threshold
            return getShard(key + "-hot"); // Separate cache shard
        }
        
        return shardId;
    }

    public List<String> getShardsForRange(String startKey, String endKey) {
        long startHash = Hashing.murmur3_128().hashString(startKey, StandardCharsets.UTF_8).asLong();
        long endHash = Hashing.murmur3_128().hashString(endKey, StandardCharsets.UTF_8).asLong();
        
        return ring.subMap(startHash, true, endHash, true)
            .values()
            .stream()
            .distinct()
            .toList();
    }

    // Bounded load consistent hashing (Google-style)
    public String getShardWithBoundedLoad(String key, int maxLoadPerShard) {
        String primary = getShard(key);
        AtomicInteger load = shards.get(primary).currentLoad();
        
        if (load.get() < maxLoadPerShard) {
            load.incrementAndGet();
            return primary;
        }
        
        // Find next shard with capacity
        return ring.tailMap(Hashing.murmur3_128()
                .hashString(key, StandardCharsets.UTF_8).asLong())
            .values()
            .stream()
            .filter(s -> shards.get(s).currentLoad().get() < maxLoadPerShard)
            .findFirst()
            .orElse(primary); // Fallback
    }

    record ShardInfo(String id, String host, int port, int weight) {
        AtomicInteger currentLoad = new AtomicInteger(0);
    }
}

// Spring Data Sharding Configuration
@Configuration
@EnableJpaRepositories(basePackages = "com.architect.sharding.repository")
class ShardingConfig {

    @Bean
    public ShardingDataSource shardingDataSource(ConsistentHashShardRouter router) {
        Map<String, DataSource> shardDataSources = new HashMap<>();
        router.getShards().forEach((id, info) -> {
            HikariDataSource ds = new HikariDataSource();
            ds.setJdbcUrl("jdbc:postgresql://" + info.host() + ":" + info.port() + "/shard_" + id);
            ds.setUsername("shard_user");
            ds.setPassword("secret");
            shardDataSources.put(id, ds);
        });
        
        return new ShardingDataSource(shardDataSources, router);
    }
}
```''',

    'CACHE-02-Cache-Strategies.md': '''```java
// Java 25 / Spring Boot 3.5: Multi-Level Cache with Caffeine (L1) + Redis (L2)
// Production cache with write-through, cache-aside, and invalidation

package com.architect.cache;

import com.github.benmanes.caffeine.cache.Caffeine;
import org.springframework.cache.CacheManager;
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.cache.caffeine.CaffeineCacheManager;
import org.springframework.data.redis.cache.RedisCacheConfiguration;
import org.springframework.data.redis.cache.RedisCacheManager;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.stereotype.Service;

import java.time.Duration;
import java.util.Map;

@Service
public class MultiLevelCacheService {

    private final CacheManager l1CacheManager; // Caffeine (in-process)
    private final CacheManager l2CacheManager; // Redis (distributed)
    private final RedisTemplate<String, Object> redisTemplate;

    public MultiLevelCacheService(CaffeineCacheManager l1, 
                                  RedisCacheManager l2,
                                  RedisTemplate<String, Object> redis) {
        this.l1CacheManager = l1;
        this.l2CacheManager = l2;
        this.redisTemplate = redis;
    }

    // Cache-Aside with L1/L2 fallback
    public <T> T get(String key, Class<T> type, java.util.function.Supplier<T> loader) {
        // L1: In-process (microsecond latency)
        var l1Cache = l1CacheManager.getCache("l1");
        T value = l1Cache.get(key, type);
        if (value != null) return value;

        // L2: Redis (millisecond latency)
        var l2Cache = l2CacheManager.getCache("l2");
        value = l2Cache.get(key, type);
        if (value != null) {
            l1Cache.put(key, value); // Populate L1
            return value;
        }

        // Miss: load from source
        value = loader.get();
        put(key, value);
        return value;
    }

    // Write-Through: write to both L1, L2, and DB
    public void put(String key, Object value) {
        var l1Cache = l1CacheManager.getCache("l1");
        var l2Cache = l2CacheManager.getCache("l2");
        
        l1Cache.put(key, value);
        l2Cache.put(key, value);
        
        // Async DB write (fire-and-forget with completion callback)
        CompletableFuture.runAsync(() -> persistToDb(key, value))
            .exceptionally(ex -> {
                // Invalidate on DB failure
                l1Cache.evict(key);
                l2Cache.evict(key);
                return null;
            });
    }

    // Event-driven invalidation via Redis pub/sub
    public void invalidate(String key) {
        l1CacheManager.getCache("l1").evict(key);
        l2CacheManager.getCache("l2").evict(key);
        
        // Publish invalidation event to other instances
        redisTemplate.convertAndSend("cache:invalidate", key);
    }

    // Cache tags for group invalidation
    public void invalidateByTag(String tag) {
        Set<String> keys = redisTemplate.opsForSet().members("cache:tag:" + tag);
        if (keys != null) {
            keys.forEach(this::invalidate);
            redisTemplate.delete("cache:tag:" + tag);
        }
    }

    private void persistToDb(String key, Object value) {
        // DB write logic
    }
}

// Configuration
@Configuration
@EnableCaching
class CacheConfig {

    @Bean
    public CaffeineCacheManager l1CacheManager() {
        CaffeineCacheManager manager = new CaffeineCacheManager("l1");
        manager.setCaffeine(Caffeine.newBuilder()
            .maximumSize(10_000)
            .expireAfterWrite(Duration.ofMinutes(5))
            .recordStats());
        return manager;
    }

    @Bean
    public RedisCacheManager l2CacheManager(RedisConnectionFactory factory) {
        RedisCacheConfiguration config = RedisCacheConfiguration.defaultCacheConfig()
            .entryTtl(Duration.ofHours(1))
            .disableCachingNullValues();
        return RedisCacheManager.builder(factory)
            .cacheDefaults(config)
            .build();
    }

    @Bean
    public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory factory) {
        RedisTemplate<String, Object> template = new RedisTemplate<>();
        template.setConnectionFactory(factory);
        template.setKeySerializer(new StringRedisSerializer());
        template.setValueSerializer(new GenericJackson2JsonRedisSerializer());
        return template;
    }
}
```''',

    'ASYNC-02-Message-Queues.md': '''```java
// Java 25 / Spring Boot 3.5: Kafka - Exactly-Once Semantics with Transactional Producer
// Production Kafka configuration for exactly-once processing

package com.architect.messaging;

import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.common.serialization.StringSerializer;
import org.springframework.kafka.core.DefaultKafkaProducerFactory;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.core.ProducerFactory;
import org.springframework.kafka.transaction.KafkaTransactionManager;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.HashMap;
import java.util.Map;

@Service
public class ExactlyOnceOrderService {

    private final KafkaTemplate<String, OrderEvent> kafkaTemplate;
    private final OrderRepository orderRepository;

    public ExactlyOnceOrderService(KafkaTemplate<String, OrderEvent> kafkaTemplate,
                                   OrderRepository orderRepository) {
        this.kafkaTemplate = kafkaTemplate;
        this.orderRepository = orderRepository;
    }

    // Exactly-once: DB write + Kafka send in single transaction
    @Transactional
    public void createOrder(Order order) {
        // 1. Persist to database
        Order saved = orderRepository.save(order);

        // 2. Send to Kafka (same transaction via KafkaTransactionManager)
        OrderEvent event = OrderEvent.created(saved.getId(), saved.getUserId(), saved.getTotal());
        kafkaTemplate.send("orders", saved.getId(), event);
        
        // 3. Send to another topic atomically
        InventoryEvent invEvent = InventoryEvent.reserve(saved.getItems());
        kafkaTemplate.send("inventory", saved.getId(), invEvent);
    }

    // Idempotent consumer with deduplication
    @KafkaListener(topics = "orders", groupId = "order-processor",
                   containerFactory = "kafkaListenerContainerFactory")
    @Transactional
    public void processOrder(ConsumerRecord<String, OrderEvent> record) {
        String orderId = record.key();
        
        // Deduplication: check if already processed
        if (processedEventRepository.existsByEventId(record.headers()
                .lastHeader("event-id").value())) {
            return; // Already processed
        }

        OrderEvent event = record.value();
        processOrderInternal(event);
        
        // Record processed event ID
        processedEventRepository.save(new ProcessedEvent(record.headers()
            .lastHeader("event-id").value()));
    }

    private void processOrderInternal(OrderEvent event) {
        // Business logic
    }
}

// Producer Factory with Exactly-Once
@Configuration
class KafkaProducerConfig {

    @Bean
    public ProducerFactory<String, OrderEvent> producerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "kafka-1:9092,kafka-2:9092,kafka-3:9092");
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, JsonSerializer.class);
        
        // Exactly-once settings
        props.put(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG, true); // Idempotent producer
        props.put(ProducerConfig.ACKS_CONFIG, "all"); // Wait for all ISR
        props.put(ProducerConfig.RETRIES_CONFIG, Integer.MAX_VALUE);
        props.put(ProducerConfig.MAX_IN_FLIGHT_REQUESTS_PER_CONNECTION, 5);
        props.put(ProducerConfig.TRANSACTIONAL_ID_CONFIG, "order-service-${spring.application.instance-id}");
        
        // Performance
        props.put(ProducerConfig.LINGER_MS_CONFIG, 5);
        props.put(ProducerConfig.BATCH_SIZE_CONFIG, 16384);
        props.put(ProducerConfig.COMPRESSION_TYPE_CONFIG, "zstd");
        
        return new DefaultKafkaProducerFactory<>(props);
    }

    @Bean
    public KafkaTemplate<String, OrderEvent> kafkaTemplate(ProducerFactory<String, OrderEvent> pf) {
        KafkaTemplate<String, OrderEvent> template = new KafkaTemplate<>(pf);
        template.setDefaultTopic("orders");
        return template;
    }

    @Bean
    public KafkaTransactionManager<String, OrderEvent> transactionManager(
            ProducerFactory<String, OrderEvent> pf) {
        return new KafkaTransactionManager<>(pf);
    }
}
```''',
}

def update_note_code(file_path: Path, code: str):
    """Update a note's Code / Example section with real implementation."""
    content = file_path.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return False
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    fm = yaml.safe_load(parts[1]) or {}
    body = parts[2]
    
    # Replace Code / Example section
    new_code_section = f"## Code / Example\n\n{code}\n\n"
    
    if "## Code / Example" in body:
        pattern = r'## Code / Example.*?(?=\n## |\Z)'
        body = re.sub(pattern, new_code_section.rstrip(), body, flags=re.DOTALL)
    else:
        # Add after Problems section
        if "## Problems" in body:
            body = body.replace("## Problems", new_code_section + "## Problems")
        else:
            body += "\n\n" + new_code_section
    
    new_fm = "---\n" + yaml.dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False) + "---\n"
    file_path.write_text(new_fm + body, encoding='utf-8')
    return True

def main():
    updated = 0
    for filename, code in CODE_EXAMPLES.items():
        file_path = TARGET / filename
        if not file_path.exists():
            print(f"  MISSING: {filename}")
            continue
        
        if update_note_code(file_path, code):
            print(f"  UPDATED: {filename}")
            updated += 1
        else:
            print(f"  FAILED: {filename}")
    
    print(f"\nTotal updated: {updated}")

if __name__ == "__main__":
    main()