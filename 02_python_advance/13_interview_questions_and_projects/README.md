# 📌 Advanced Topic 13: Top Interview Questions & Production Projects

## 📖 Introduction
This module consolidates the most critical Python interview questions asked by Tier-1 product companies and startups, alongside complete production-ready project architectures ideal for YouTube coding tutorials and portfolio showcases.

---

## 🧠 Part 1: Tricky Output-Based Interview Questions

### 1. Late Binding Closures in Loops
```python
def create_multipliers():
    return [lambda x: i * x for i in range(4)]

for multiplier in create_multipliers():
    print(multiplier(2), end=" ")
# What is the output?
# Output: 6 6 6 6 (NOT 0 2 4 6!)
```
**Explanation:** Python's closures bind to the variable `i`, not its value at the time the lambda was defined. By the time the functions run, the loop has completed and `i == 3`. To fix this, use default arguments to bind values eagerly: `lambda x, i=i: i * x`.

---

### 2. Mutating a List inside a Tuple
```python
t = (1, 2, [3, 4])
try:
    t[2] += [5]
except TypeError:
    print("TypeError raised!")

print("Tuple contents:", t)
# What is the output?
# Output:
# TypeError raised!
# Tuple contents: (1, 2, [3, 4, 5])
```
**Explanation:** The `+=` operator executes `extend()` on the list (which succeeds and mutates the list in-place), and *then* attempts to reassign the result back to `t[2]`. The tuple assignment raises a `TypeError`, but the list in memory was already mutated!

---

### 3. Identity vs Value Equality with Small Integers
```python
a = 256
b = 256
print(a is b)  # True (Small integer cache: -5 to 256)

x = 257
y = 257
print(x is y)  # False (in interactive REPL) or True (in same code block due to compiler const folding)
```

---

## 💼 Part 2: Top Senior Python Interview Questions

| # | Question | Key Answer Summary |
|---|---|---|
| 1 | **What is the GIL and why can't it just be removed?** | The Global Interpreter Lock ensures CPython's reference counting is thread-safe without fine-grained locks. Removing it introduces substantial overhead for single-threaded scripts (though PEP 703 introduces optional free-threading in 3.13+). |
| 2 | **Explain the difference between `deepcopy` and `copy`.** | Shallow copy (`copy.copy()`) creates a new container but inserts references to the original nested objects. Deep copy (`copy.deepcopy()`) recursively duplicates all nested objects. |
| 3 | **How does Python handle memory deallocation?** | Deterministic reference counting reclaims memory immediately when `ob_refcnt == 0`. An auxiliary generational cyclical garbage collector (`gc` module) detects and reclaims circular reference islands. |
| 4 | **What is Method Resolution Order (MRO)?** | The order in which Python searches parent classes for a method, computed via the C3 Linearization algorithm. |
| 5 | **How does `asyncio` differ from multi-threading?** | Multi-threading uses OS preemptive scheduling where the OS switches threads. `asyncio` uses cooperative multitasking on a single thread where coroutines voluntarily yield control at `await` points. |

---

## 🛠️ Part 3: Production Tutorial Projects (YouTube Ready)

### 🚀 Project 1: Asynchronous Service Health Monitor & Pinger
* **Concepts Used**: `asyncio`, `aiohttp` (or `urllib`), `dataclasses`, Async context managers.
* **Problem Statement**: Monitor a list of 50 microservice endpoints concurrently, check response latency and HTTP status, and record failures.

```python
import asyncio
import time
from dataclasses import dataclass

@dataclass
class HealthReport:
    url: str
    status: int
    latency_ms: float
    is_healthy: bool

async def check_endpoint(url: str) -> HealthReport:
    start = time.perf_counter()
    # Simulated async network request
    await asyncio.sleep(0.2)
    latency = (time.perf_counter() - start) * 1000
    return HealthReport(url=url, status=200, latency_ms=latency, is_healthy=True)

async def run_monitor():
    urls = [f"https://service-{i}.internal.net/health" for i in range(10)]
    results = await asyncio.gather(*(check_endpoint(u) for u in urls))
    for r in results:
        print(f"[{'ONLINE' if r.is_healthy else 'OFFLINE'}] {r.url} - {r.latency_ms:.2f}ms")

if __name__ == "__main__":
    asyncio.run(run_monitor())
```

---

### 🚀 Project 2: High-Performance Log Streaming & Analytics Engine
* **Concepts Used**: Generators (`yield`), `collections.Counter`, regular expressions, file streaming.
* **Problem Statement**: Parse a multi-gigabyte server log file with zero memory spike, extracting error frequencies, top IP addresses, and hourly traffic spikes.

---

### 🚀 Project 3: In-Memory Key-Value Cache with TTL & LRU Eviction
* **Concepts Used**: `collections.OrderedDict`, `@property`, `threading.Lock`, custom context managers.
* **Problem Statement**: Build a thread-safe Redis-like in-memory cache supporting `set(key, val, ttl_seconds)`, `get(key)`, and automatic eviction of least recently used keys when exceeding capacity.

---

## 📹 YouTube Creator Guide (Video Outline Tips)
* **Hook (0:00 - 0:45)**: State the exact real-world problem (e.g. *"Why did this Python microservice run out of memory in production?"*).
* **The "Naive" Approach (0:45 - 2:30)**: Show the beginner solution with for-loops and explain why it fails at scale.
* **Deep Architectural Dive (2:30 - 6:00)**: Introduce the advanced Python primitive (Generators, `__slots__`, or AsyncIO) with memory/time graphs.
* **Live Coding Walkthrough (6:00 - 15:00)**: Implement the optimized solution step-by-step with terminal validation.
* **Interview Question & Wrap-up (15:00 - end)**: Quiz the audience and link to this GitHub repository.
