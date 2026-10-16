# 📌 Advanced Topic 06: Context Managers & The `with` Statement

## 📖 Introduction
A **Context Manager** is a Python construct that simplifies resource management by ensuring that setup and teardown actions are executed deterministically. Whether opening files, acquiring threading locks, or opening database connections, context managers guarantee that resources are cleanly released.

---

## 🔑 1. The Context Management Protocol

Any object that implements the following two methods is a Context Manager:
1. `__enter__(self)`: Prepares the resource. The return value is bound to the target variable after the `as` keyword.
2. `__exit__(self, exc_type, exc_val, exc_tb)`: Executes cleanup. Handles exceptions that occurred inside the `with` block.

```
       with ContextManager() as resource:
                 │
                 ├──> 1. __enter__() is called
                 │    Value returned assigned to 'resource'
                 │
                 ├──> 2. Code inside 'with' block executes
                 │
                 └──> 3. __exit__() is ALWAYS called
                      (Even if an exception was raised!)
```

---

## 🛠️ 2. Class-Based Custom Context Manager

```python
import time

class BenchmarkTimer:
    def __init__(self, label: str):
        self.label = label
        self.start_time = None

    def __enter__(self):
        print(f"⏱️ Starting [{self.label}]...")
        self.start_time = time.perf_counter()
        return self  # Bound to the 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start_time
        print(f"🏁 Finished [{self.label}] in {elapsed:.6f} seconds.")

        if exc_type is not None:
            print(f"⚠️ Exception detected during execution: {exc_val}")
            # Returning True suppresses the exception; Returning False/None propagates it!
            return False

with BenchmarkTimer("Heavy Computation") as timer:
    total = sum(i ** 2 for i in range(2_000_000))
```

---

## 🛑 3. Suppressing Exceptions in `__exit__`
If `__exit__` returns `True`, Python **suppresses** the exception and continues execution past the `with` block:

```python
class IgnoreSpecificError:
    def __init__(self, error_type):
        self.error_type = error_type

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type, self.error_type):
            print(f"Handled and suppressed: {exc_val}")
            return True  # Suppresses exception!
        return False

with IgnoreSpecificError(ZeroDivisionError):
    val = 10 / 0  # Does not crash program!

print("Execution continued smoothly!")
```

---

## ⚡ 4. Generator-Based Context Managers (`@contextmanager`)
The `contextlib.contextmanager` decorator turns a simple generator function into a context manager without writing a full class:

```python
from contextlib import contextmanager
import os

@contextmanager
def temporary_working_directory(new_path: str):
    original_cwd = os.getcwd()
    try:
        os.chdir(new_path)
        yield new_path  # Code inside 'with' runs while yielded here
    finally:
        # Cleanup guaranteed even on error
        os.chdir(original_cwd)

# Usage:
# with temporary_working_directory("/tmp") as temp_dir:
#     print("Currently in:", os.getcwd())
# print("Restored to:", os.getcwd())
```

---

## 🧰 5. Essential `contextlib` Utilities

### A. `contextlib.suppress` (Clean error ignoring)
```python
from contextlib import suppress
import os

# Instead of try... except FileNotFoundError: pass
with suppress(FileNotFoundError):
    os.remove("non_existent_file.tmp")
```

### B. `contextlib.ExitStack` (Dynamic multiple context managers)
Useful when the number of context managers is only known at runtime:
```python
from contextlib import ExitStack

file_paths = ["file1.txt", "file2.txt"]
# with ExitStack() as stack:
#     files = [stack.enter_context(open(fname, "w")) for fname in file_paths]
#     files[0].write("Data 1")
#     files[1].write("Data 2")
# All dynamically opened files are safely closed!
```

---

## 🧠 Top Interview Questions

1. **Q: What arguments does `__exit__` take and what does returning `True` do?**
   * **A:** It takes 3 arguments: `exc_type` (Exception class), `exc_val` (Exception instance), and `exc_tb` (Traceback object). Returning `True` suppresses the exception so it won't propagate outside the `with` block.

2. **Q: How does `@contextmanager` work under the hood?**
   * **A:** It wraps a generator function into a class implementing `__enter__` and `__exit__`. In `__enter__`, it calls `next()` to advance to the `yield` statement. In `__exit__`, it resumes the generator via `next()` or `.throw()` to run code in the `finally` block.

---

## 💻 Practice Exercises
1. **Exercise 1 (Database Transaction Manager):** Write a context manager `DatabaseTransaction(connection)` that calls `connection.commit()` on success, or `connection.rollback()` if an exception occurs in `__exit__`.
2. **Exercise 2 (Stdout Redirector):** Implement a context manager that captures all `print()` outputs inside its block and stores them in a list instead of printing to screen.
