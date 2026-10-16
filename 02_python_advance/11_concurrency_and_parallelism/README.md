# 📌 Advanced Topic 11: Concurrency & Parallelism (Threading, Multiprocessing & AsyncIO)

## 📖 Introduction
Modern systems handle thousands of simultaneous requests and heavy computational workloads. Python offers three distinct concurrency paradigms: **Threading**, **Multiprocessing**, and **AsyncIO**. Choosing the right model depends on whether your workload is **I/O-Bound** or **CPU-Bound**.

```
┌────────────────────────────────────────────────────────────────────────┐
│                   CONCURRENCY vs PARALLELISM                           │
├───────────────────────────────────┬────────────────────────────────────┤
│  Concurrency (Dealing with many   │  Parallelism (Doing many things    │
│  things at once - Interleaved)    │  at the exact same physical time)  │
│  Examples: AsyncIO, Threading     │  Examples: Multiprocessing         │
└───────────────────────────────────┴────────────────────────────────────┘
```

---

## 🔒 1. The Global Interpreter Lock (GIL)

In CPython, the **GIL** is a mutual exclusion lock that prevents multiple native threads from executing Python bytecode at the same time.
* **Why it exists**: Memory management in CPython is not thread-safe (reference counts `ob_refcnt` could suffer race conditions and corrupt memory without the GIL).
* **Impact**:
  * **CPU-Bound Tasks**: Multithreading will **NOT** run on multiple CPU cores in Python. Use `multiprocessing` instead!
  * **I/O-Bound Tasks**: Multithreading works well because threads release the GIL while waiting for network responses, disk I/O, or `time.sleep()`.
* *Note on Python 3.13+*: PEP 703 introduces experimental free-threaded (no-GIL) Python builds!

---

## 🧵 2. Multithreading (`threading` & `ThreadPoolExecutor`)

Best for **I/O-bound** operations (e.g. web scraping, querying APIs, file downloads).

```python
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Race condition protection using Lock
counter = 0
counter_lock = threading.Lock()

def safe_increment():
    global counter
    for _ in range(100_000):
        with counter_lock:
            counter += 1

threads = [threading.Thread(target=safe_increment) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
print("Safe Counter with Lock:", counter) # Exactly 500,000

# High-Level ThreadPoolExecutor (Recommended)
def fetch_url(url: str) -> str:
    time.sleep(0.5) # Simulating network request latency
    return f"Response from {url}"

urls = [f"https://api.example.com/item/{i}" for i in range(5)]

with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(fetch_url, urls))
    print("Fetched results:", len(results))
```

---

## ⚡ 3. Multiprocessing (`multiprocessing` & `ProcessPoolExecutor`)

Best for **CPU-bound** workloads (e.g. video processing, cryptography, machine learning, heavy calculations). Each process has its own Python interpreter and memory space, bypassing the GIL entirely.

```python
import time
from concurrent.futures import ProcessPoolExecutor

def compute_heavy_factors(n: int) -> int:
    # CPU-intensive calculation
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += 1
    return count

numbers = [10_000_000 + i for i in range(4)]

if __name__ == "__main__":
    start = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(compute_heavy_factors, numbers))

    duration = time.perf_counter() - start
    print(f"Computed factors: {results} across cores in {duration:.2f}s")
```

---

## 🚀 4. Asynchronous Programming (`asyncio`)

AsyncIO uses **cooperative multitasking on a single thread** via an **Event Loop**. A task yields control using `await` when waiting for I/O, allowing other tasks to execute in the meantime.

```python
import asyncio
import time

async def fetch_user_data(user_id: int):
    print(f"Fetching user #{user_id}...")
    await asyncio.sleep(1) # Simulates non-blocking async network I/O
    print(f"User #{user_id} data received! ✅")
    return {"id": user_id, "status": "active"}

async def main():
    start_time = time.perf_counter()

    # Launching multiple coroutines concurrently with asyncio.gather
    users = await asyncio.gather(
        fetch_user_data(101),
        fetch_user_data(102),
        fetch_user_data(103)
    )

    elapsed = time.perf_counter() - start_time
    print(f"Fetched {len(users)} users in {elapsed:.2f} seconds!") # Takes ~1.0s, NOT 3.0s!

if __name__ == "__main__":
    asyncio.run(main())
```

### Modern Python 3.11+ `asyncio.TaskGroup`
Provides clean structured concurrency:
```python
async def modern_main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_user_data(1))
        task2 = tg.create_task(fetch_user_data(2))
    # Both tasks are guaranteed completed or canceled together on exception
    print("Tasks finished:", task1.result(), task2.result())
```

---

## 🎯 5. Decision Matrix: Which One Should I Use?

| Scenario | Recommended Approach | Reason |
|---|---|---|
| Web APIs, microservices, 10,000+ open sockets | **AsyncIO** | Extremely low memory overhead, fastest throughput for I/O |
| Scraping 50 websites, downloading files, simple scripts | **Threading / ThreadPoolExecutor** | Simpler synchronous-like code, handles blocking libraries |
| Heavy image processing, ML model inference, math calculations | **Multiprocessing / ProcessPoolExecutor** | Uses 100% of all available CPU cores, bypasses GIL |

---

## 🧠 Top Interview Questions

1. **Q: Why does a multi-threaded CPU-bound program in Python run SLOWER than a single-threaded one?**
   * **A:** Due to the GIL, only one thread can execute Python bytecode at any moment. Multiple CPU-bound threads fight for the GIL, resulting in high thread context-switching overhead and CPU cache thrashing without achieving true parallel execution.

2. **Q: What is the difference between `asyncio.create_task()` and calling an `async def` function directly?**
   * **A:** Calling an `async def` function returns a coroutine object without scheduling it. `asyncio.create_task(coro)` schedules the coroutine on the event loop immediately and returns a `Task` object that can be awaited or monitored.

3. **Q: What is a Race Condition and how do you prevent it in Python threading?**
   * **A:** A race condition occurs when multiple threads concurrently read and mutate shared mutable state, leading to inconsistent data. It is prevented using synchronization primitives like `threading.Lock` or `threading.RLock`.

---

## 💻 Practice Exercises
1. **Exercise 1 (Concurrent Web Checker):** Create a script using `ThreadPoolExecutor` that pings 10 popular websites and records their response status codes concurrently.
2. **Exercise 2 (Async Pipeline):** Write an `asyncio` script simulating an order processing pipeline where orders are validated, payment is processed, and email is dispatched concurrently.
