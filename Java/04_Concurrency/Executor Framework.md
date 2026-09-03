---
title: "Executor Framework"
category: Concurrency
tags: [concurrency, executor, interview]
created: 2026-01-18
updated: 2026-09-02
---

# Executor Framework

> Part of [[README|Java MOC]] • `Concurrency` • Java 25 (LTS)

## 1. Summary


> In practice you probably only need one line now: Executors.newVirtualThreadPerTaskExecutor(). I used to tune pools, now I mostly don't. Still, scheduled tasks are the exception, they still run on platform threads.

The Executor Framework (`java.util.concurrent`, since Java 5) decouples *task submission* from *thread management*. Instead of `new Thread(r).start()`, you submit `Runnable`/`Callable` to an `ExecutorService` that handles threading, queuing, and lifecycle.

> Java 25 default: `Executors.newVirtualThreadPerTaskExecutor()`, one lightweight virtual thread per task, no pool tuning. Platform-thread pools (`newFixedThreadPool`, `newCachedThreadPool`) are now the exception (CPU-bound / legacy).

## 2. Why executors over raw threads?

1. Resource control, bounded or unbounded execution without manually creating/destroying `Thread` objects.
2. Decoupling, caller submits tasks; executor decides *how* to run them (pool, virtual thread, scheduled).
3. Lifecycle & queuing, `shutdown()`, `awaitTermination()`, rejection policies, `Future` results.
4. Virtual-thread scale, `newVirtualThreadPerTaskExecutor()` handles millions of concurrent blocking tasks with no queue saturation.

## 3. Core interfaces & classes

| Type | Role | Key method |
|---|---|---|
| `Executor` | Fire-and-forget | `execute(Runnable)` |
| `ExecutorService` | Lifecycle + `Future` | `submit()`, `invokeAll()`, `shutdown()` |
| `ScheduledExecutorService` | Delayed / periodic | `schedule()`, `scheduleAtFixedRate()` |
| `ThreadFactory` | Creates threads | `newThread(Runnable)` |
| `Executors` | Factory helpers | `newVirtualThreadPerTaskExecutor()`, `newFixedThreadPool(n)`, etc. |

Lifecycle: `RUNNING → SHUTDOWN (no new tasks, running tasks continue) → TERMINATED`. Call `shutdown()` or use try-with-resources (`ExecutorService` is `AutoCloseable` since Java 19).

## 4. Java 25 modernisation, virtual-thread-per-task

| Approach | Java 21 and before | Java 25 (LTS) default |
|---|---|---|
| IO-bound fan-out | `newFixedThreadPool(200)` + tuning + queue | `newVirtualThreadPerTaskExecutor()`, no tuning |
| Thread creation | `new Thread(r)` / `Executors.newCachedThreadPool()` | `Thread.ofVirtual().factory()` / `newThreadPerTaskExecutor(factory)` |
| Structured fan-out | `invokeAll()` / `CompletableFuture.allOf()` | `StructuredTaskScope` (preview, JEP 505), preferred for scoped tasks |
| Carrier pool | N/A | JVM `ForkJoinPool` sized to CPUs; `-Djdk.virtualThreadScheduler.parallelism=N` |

> StructuredTaskScope note (JEP 505, preview in Java 25): For *scoped* fan-out where subtasks share a deadline or must fail together, prefer `StructuredTaskScope.ShutdownOnFailure` / `ShutdownOnSuccess` over raw `ExecutorService.invokeAll()`. Executor remains correct for long-lived services / fire-and-forget. See [[Threads]] § Structured Concurrency.

```java

```

## 5. Vs Tables

### Executor types

| Executor | Thread model | Queue | When to use |
|---|---|---|---|
| `newVirtualThreadPerTaskExecutor()` | New virtual thread per task | None (direct) | Default for IO-bound, servers, fan-out, blocking calls |
| `newThreadPerTaskExecutor(Thread.ofVirtual().factory())` | Virtual, custom factory (naming) | None | Need custom `ThreadFactory` (names, `ThreadLocal` control) |
| `newFixedThreadPool(n)` | n platform threads | `LinkedBlockingQueue` (unbounded) | CPU-bound, strict concurrency cap, legacy |
| `newCachedThreadPool()` | Unbounded platform threads | `SynchronousQueue` | Short-lived bursts (legacy, prefer virtual) |
| `newSingleThreadExecutor()` | 1 platform thread | `LinkedBlockingQueue` | Ordered sequential execution |
| `newScheduledThreadPool(n)` | n platform threads | `DelayedWorkQueue` | Delays / periodic tasks (still platform-thread based) |
| `newWorkStealingPool()` | `ForkJoinPool` | Work-stealing queues | CPU-bound recursive tasks (`RecursiveTask`) |

### `submit()` vs `execute()` vs `invokeAll()`

| Method | Takes | Returns | Throws on failure |
|---|---|---|---|
| `execute(Runnable)` | `Runnable` | `void` | Uncaught via `UncaughtExceptionHandler` |
| `submit(Runnable/Callable)` | `Runnable`/`Callable` | `Future<T>` | `ExecutionException` on `get()` |
| `invokeAll(Collection<Callable>)` | Batch | `List<Future<T>>` | Per-future `ExecutionException` |
| `StructuredTaskScope.fork()` | `Callable` | `Subtask<T>` | `throwIfFailed()` propagates |

## 6. Code examples : Java 25

### 6a. Preferred: try-with-resources + virtual-thread-per-task

```java title="Java 25 - preferred default"
import java.util.concurrent.*;
import java.time.Duration;
// Executor — virtual-thread-per-task (Java 25 default)

public class ExecutorDemo {
// Entry point — classic form; Java 25 also allows void main()
    public static void main(String[] args) throws Exception {
        try (ExecutorService exec = Executors.newVirtualThreadPerTaskExecutor()) {
            Future<String> f1 = exec.submit(() -> {
                Thread.sleep(Duration.ofMillis(200));
                return "hello from " + Thread.currentThread();
            });
            Future<String> f2 = exec.submit(() -> "world");

            System.out.println(f1.get() + " " + f2.get());
        }
    }
}
```

### 6b. Custom virtual-thread factory (named threads)

```java title="Java 25 - named virtual threads"
import java.util.concurrent.*;
// Executor — virtual-thread-per-task (Java 25 default)

class NamedFactoryDemo {
    static void demo() throws Exception {
        ThreadFactory factory = Thread.ofVirtual()
                .name("worker-", 0)
                .factory();

        try (var exec = Executors.newThreadPerTaskExecutor(factory)) {
            var futures = java.util.stream.IntStream.range(0, 5)
                    .mapToObj(i -> exec.submit(() -> "task-" + i + " on " + Thread.currentThread()))
                    .toList();
            for (var f : futures) System.out.println(f.get());
        }
    }
}
```

### 6c. Fan-out: Executor vs StructuredTaskScope

```java title="Java 25 - Executor invokeAll vs StructuredTaskScope (preview)"
import java.util.List;
import java.util.concurrent.*;
// ExecutorFanOut — virtual-thread-per-task (Java 25 default)

class ExecutorFanOut {
    String fetchAll(ExecutorService exec) throws Exception {
        var tasks = List.<Callable<String>>of(
                () -> fetchUser(), () -> fetchOrder());
        List<Future<String>> futures = exec.invokeAll(tasks);
        return futures.get(0).get() + " | " + futures.get(1).get();
    }
    String fetchUser() throws InterruptedException { Thread.sleep(Duration.ofMillis(100)); return "alice"; }
    String fetchOrder() throws InterruptedException { Thread.sleep(Duration.ofMillis(150)); return "order-42"; }
}
// StructuredFanOut — virtual-thread-per-task (Java 25 default)

class StructuredFanOut {
    String fetchUser() throws InterruptedException { Thread.sleep(Duration.ofMillis(100)); return "alice"; }
    String fetchOrder() throws InterruptedException { Thread.sleep(Duration.ofMillis(150)); return "order-42"; }

    String handle() throws Exception {
        try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
            var u = scope.fork(this::fetchUser);
            var o = scope.fork(this::fetchOrder);
            scope.join();
            scope.throwIfFailed();
            return u.get() + " | " + o.get();
        }
    }
}
```

### 6d. Scheduled tasks (still platform-thread based)

```java title="Java 25 - scheduling"
import java.util.concurrent.*;
// Executor — virtual-thread-per-task (Java 25 default)

class ScheduledDemo {
    static void demo() throws Exception {
        try (var scheduler = Executors.newScheduledThreadPool(2)) {
            scheduler.schedule(() -> System.out.println("once after 500ms"),
                    500, TimeUnit.MILLISECONDS);
            var periodic = scheduler.scheduleAtFixedRate(
                    () -> System.out.println("tick " + Thread.currentThread()),
                    0, 1, TimeUnit.SECONDS);
            Thread.sleep(Duration.ofSeconds(3));
            periodic.cancel(false);
        }
    }
}
```

## 7. Interview Q&A

**Q: Why not `new Thread()` per request?** OS threads are ~MBs + kernel scheduling; unbounded creation causes OOM / thrashing. Executors bound or virtualise the cost. On Java 25 virtual threads make per-task threads cheap (~KBs) but you still want lifecycle management via `ExecutorService`.

**Q: `newFixedThreadPool` vs `newVirtualThreadPerTaskExecutor`?** Fixed pool caps *platform* threads and queues overflow; virtual-per-task creates a new virtual thread each submission and parks it cheaply on blocking IO, no queue, no tuning, scales to millions.

**Q: Do you need `shutdown()` with virtual-thread executor? Yes, but prefer try-with-resources**: `try (var exec = Executors.newVirtualThreadPerTaskExecutor()) { ... }`, `close()` calls `shutdown()` and awaits termination.

**Q: When to use `StructuredTaskScope` instead of `ExecutorService`?** When subtasks are *scoped* (share a deadline, must all succeed or cancel together). Executor is for long-lived / unbounded service pools; `StructuredTaskScope` is for structured fan-out with automatic cancellation and error propagation.

**Q: What happens if you submit after `shutdown()`?** `RejectedExecutionException`.

**Q: `execute()` vs `submit()`?** `execute` takes `Runnable` and returns nothing (exceptions go to handler); `submit` returns `Future` so you can `get()` the result or `ExecutionException`.

Q: How to handle exceptions from tasks? `Future.get()` wraps in `ExecutionException`; `CompletableFuture.exceptionally()`; `StructuredTaskScope.throwIfFailed()` rethrows the first failure.

## 8. Pitfalls & related

Pitfalls:
- Forgetting try-with-resources / `shutdown()` → leaked threads & JVM won't exit.
- Using `newFixedThreadPool` with unbounded `LinkedBlockingQueue` → OOM under load (virtual executor avoids this).
- Calling `Future.get()` without timeout → hangs forever; use `get(timeout, unit)`.
- Swallowing `InterruptedException` without `Thread.currentThread().interrupt()`.
- Using `newCachedThreadPool` for IO fan-out on Java 25, creates platform threads needlessly; use virtual.

Related:
- [[Threads]], lifecycle, virtual threads, JEP 491/505/506
- [[CompletableFuture]], async pipelines on virtual executors
- [[Locks and Synchronizers]], coordination primitives
- [[Concurrent Collections]], thread-safe data structures

## Practice
- [1115. Print Foobar Alternately](https://leetcode.com/problems/print-foobar-alternately/)
- [1226. The Dining Philosophers](https://leetcode.com/problems/the-dining-philosophers/)
- [1114. Print In Order](https://leetcode.com/problems/print-in-order/)


---
*Category: Concurrency • Part of [[README|Java MOC]] • Java 25*
