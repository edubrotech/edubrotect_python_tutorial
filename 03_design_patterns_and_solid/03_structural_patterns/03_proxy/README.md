# 📌 Structural Pattern 03: Proxy

## 📖 Intent
> *"Provide a surrogate or placeholder for another object to control access to it."* — Gang of Four

A Proxy controls access to the original object, allowing you to perform operations before or after the request gets through to the original target (e.g., lazy loading, authorization, caching, or logging).

```
┌──────────────────┐           ┌──────────────────┐           ┌──────────────────┐
│      Client      │ ───────>  │   Proxy Object   │ ───────>  │   Real Subject   │
│                  │           │ (Auth / Cache /  │           │ (Heavy DB / I/O) │
│                  │           │  Lazy Loading)   │           │                  │
└──────────────────┘           └──────────────────┘           └──────────────────┘
```

---

## 🛠️ Implementation in Python: Virtual Proxy (Lazy Loading) & Caching

```python
from abc import ABC, abstractmethod
import time

# 1. Subject Interface
class DatabaseReport(ABC):
    @abstractmethod
    def display(self) -> None: pass

# 2. Real Subject: Extremely expensive to instantiate!
class HeavyDatabaseReport(DatabaseReport):
    def __init__(self, query_id: str):
        self.query_id = query_id
        self._load_heavy_dataset_from_disk()

    def _load_heavy_dataset_from_disk(self):
        print(f"⏳ Connecting to cluster & loading 500MB dataset for '{self.query_id}'...")
        time.sleep(1.0) # Simulating heavy I/O
        self.data = [f"Record_{i}" for i in range(100_000)]
        print("✅ Heavy dataset loaded into memory!")

    def display(self):
        print(f"📊 Displaying report for {self.query_id}: {len(self.data)} records analyzed.")

# 3. Virtual & Caching Proxy: Defers heavy loading until display() is explicitly called!
class LazyReportProxy(DatabaseReport):
    def __init__(self, query_id: str, user_role: str):
        self.query_id = query_id
        self.user_role = user_role
        self._real_report: HeavyDatabaseReport = None

    def display(self):
        # 1. Protection Check (Authorization)
        if self.user_role != "ADMIN":
            print(f"⛔ Access Denied: User role '{self.user_role}' cannot view this report.")
            return

        # 2. Virtual Proxy Check (Lazy Initialization on demand)
        if self._real_report is None:
            print("🔍 Proxy: First access detected. Initializing real heavy object...")
            self._real_report = HeavyDatabaseReport(self.query_id)

        # 3. Delegate to Real Subject
        self._real_report.display()

# Instantiating the proxy is instantaneous (no heavy I/O yet!):
proxy = LazyReportProxy("ANNUAL_FINANCES_2026", user_role="ADMIN")
print("Proxy instantiated without memory spike.\n")

# Heavy load only happens when display() is actually invoked:
proxy.display()
```

---

## 🧠 Top Interview Questions

1. **Q: How does a Proxy differ from a Decorator?**
   * **A:**
     * A **Decorator** dynamically adds *new behaviors or responsibilities* to an object without modifying its core functionality.
     * A **Proxy** controls *access* to an object (lifecycle, permissions, caching, lazy loading) without altering the interface or adding new domain features.
