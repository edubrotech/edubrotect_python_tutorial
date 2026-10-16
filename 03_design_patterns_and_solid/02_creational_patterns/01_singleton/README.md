# 📌 Creational Pattern 01: Singleton

## 📖 Intent
> *"Ensure a class only has one instance, and provide a global point of access to it."* — Gang of Four

```
┌─────────────────────────────────┐
│        SingletonClass           │
├─────────────────────────────────┤
│ - _instance: SingletonClass     │
├─────────────────────────────────┤
│ + __new__(cls): SingletonClass  │
│ + business_logic(): void        │
└─────────────────────────────────┘
```

---

## 🛠️ Implementation Approaches in Python

### 1. Overriding `__new__` (Standard OOP Approach)
```python
class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("🔌 Establishing new physical database connection...")
            cls._instance = super().__new__(cls)
        return cls._instance

db1 = DatabaseConnection()
db2 = DatabaseConnection()
print("Same instance?", db1 is db2)  # Output: True
```

---

### 2. Thread-Safe Singleton with Double-Checked Locking
In multithreaded environments, multiple threads could concurrently check `_instance is None` and create multiple objects.

```python
import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                # Double-check inside lock
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

---

### 3. Metaclass-Based Singleton (Cleanest & Most Reusable)
```python
class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

# Any class using this metaclass becomes a thread-safe singleton!
class AppConfig(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {"env": "production", "debug": False}

cfg1 = AppConfig()
cfg2 = AppConfig()
print("Metaclass singleton identical?", cfg1 is cfg2)  # True
```

---

### 4. The Monostate (Borg) Pattern (Shared State, Different Identities)
Proposed by Alex Martelli: Instead of enforcing single instance identity, enforce that **all instances share the same `__dict__` state**:

```python
class BorgConfig:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

b1 = BorgConfig()
b2 = BorgConfig()
b1.api_key = "SECRET_123"

print("Shared state in b2:", b2.api_key)  # SECRET_123
print("Same object identity?", b1 is b2) # False (Different instances, shared state!)
```

---

### 5. The Pythonic Way: Python Modules ARE Singletons!
In Python, any file imported via `import config` is executed **only once** by CPython and cached in `sys.modules`.
```python
# config.py
DATABASE_URL = "postgres://user:pass@localhost:5432/db"
APP_NAME = "EduBroTech"

# client.py
import config  # Guaranteed singleton by Python import system!
```

---

## 🧠 Top Interview Questions

1. **Q: Why is Singleton often called an "anti-pattern"?**
   * **A:** It introduces global mutable state, makes automated unit tests difficult (tests can bleed state into one another), and hides dependencies instead of explicitly declaring them via Dependency Injection.

2. **Q: What is the difference between classic Singleton and Monostate (Borg)?**
   * **A:** Classic Singleton enforces **identity equality** (`a is b`). Monostate allows multiple instances to exist but forces them to share the **same attribute dictionary** (`a.__dict__ is b.__dict__`).
