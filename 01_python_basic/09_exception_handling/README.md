# 📌 Topic 09: Exception Handling

## 📖 Introduction
An **exception** is an error that occurs during the execution of a program (at runtime), disrupting the normal flow of instructions. Exception handling allows developers to intercept errors gracefully and prevent application crashes.

```
┌──────────────────────────────────────────────┐
│                    try:                      │
│            [Risky code execution]            │
└──────────────────────┬───────────────────────┘
                       │
         Did an exception occur?
         /                     \
       YES                     NO
        ▼                       ▼
┌──────────────┐         ┌──────────────┐
│   except:    │         │    else:     │
│ [Handle it]  │         │ [Success path]│
└───────┬──────┘         └──────┬───────┘
        │                       │
        └───────────┬───────────┘
                    ▼
          ┌───────────────────┐
          │     finally:      │
          │ [Always runs:     │
          │  Cleanup/Close]   │
          └───────────────────┘
```

---

## 🔑 1. The `try-except-else-finally` Lifecycle

```python
def divide_numbers(a: float, b: float) -> None:
    try:
        result = a / b
    except ZeroDivisionError as err:
        print(f"❌ Error Caught: Cannot divide by zero! ({err})")
    except TypeError as err:
        print(f"❌ Error Caught: Invalid data types provided! ({err})")
    else:
        # Executes ONLY IF no exception occurred in the try block!
        print(f"✅ Calculation Successful: {a} / {b} = {result}")
    finally:
        # ALWAYS executes regardless of whether an exception occurred or not!
        print("🔄 Cleanup: Calculation attempt finished.\n")

divide_numbers(10, 2)  # Hits 'else' and 'finally'
divide_numbers(10, 0)  # Hits 'except ZeroDivisionError' and 'finally'
```

---

## 🌳 2. Python Exception Hierarchy
All built-in exceptions inherit from `BaseException`. You should almost always catch `Exception` (or specific subclasses), never `BaseException`, to allow `KeyboardInterrupt` and `SystemExit` to stop the script normally.

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── ValueError
    ├── TypeError
    ├── FileNotFoundError (subclass of OSError)
    └── RuntimeError
```

---

## 🚀 3. Raising Exceptions & Exception Chaining

### Raising built-in exceptions
```python
def validate_age(age: int):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer!")
    if age < 0 or age > 120:
        raise ValueError(f"Invalid age {age}. Must be between 0 and 120.")
    return True
```

### Exception Chaining with `raise ... from`
Preserves the original root cause context:
```python
class DatabaseConnectionError(Exception):
    """Custom exception for database errors."""
    pass

def connect_to_database():
    try:
        import socket
        # Simulating low-level network failure
        raise ConnectionRefusedError("Port 5432 unreachable")
    except ConnectionRefusedError as original_error:
        # Chain original error to high-level application error
        raise DatabaseConnectionError("Failed to connect to database cluster") from original_error
```

---

## 🛠️ 4. Creating Custom Exceptions
Create domain-specific exceptions by inheriting from Python's built-in `Exception`:

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance: float, amount: float):
        super().__init__(f"Cannot withdraw ${amount:.2f}. Current balance is ${balance:.2f}.")
        self.balance = balance
        self.amount = amount

class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

account = BankAccount(100.0)
try:
    account.withdraw(150.0)
except InsufficientFundsError as e:
    print(f"Transaction Denied: {e}")
```

---

## ⚠️ Anti-Patterns & Common Mistakes

```python
# 🚨 1. Bare Except (Catches EVERYTHING, including Ctrl+C and exit!)
try:
    risky_operation()
except:  # NEVER DO THIS!
    pass

# 🚨 2. Catching and silently swallowing exceptions (Silent Failures)
try:
    do_something()
except Exception:
    pass  # Makes debugging impossible!

# ✅ Proper way: Catch specific exceptions and log them
import logging
try:
    risky_operation()
except SpecificError as e:
    logging.error("Operation failed: %s", e)
```

---

## 🧠 Top Interview Questions

1. **Q: When does the `else` block execute in a `try-except` structure?**
   * **A:** The `else` block runs **only if no exceptions were raised** in the `try` block. It is useful for code that should only run on success without accidentally catching errors that might happen inside it.

2. **Q: Why does `finally` execute even after a `return` statement in `try`?**
   * **A:** Python's execution model prioritizes guaranteed resource cleanup. When a `return` is encountered in a `try` block, Python preserves the return value, executes the `finally` block, and then completes the function return.

3. **Q: What is exception chaining (`from e`) and why is it useful?**
   * **A:** Exception chaining allows you to raise a high-level application exception while preserving the underlying root-cause traceback via the `__cause__` attribute.

---

## 💻 Practice Exercises
1. **Exercise 1 (Safe Input Evaluator):** Write a function `safe_int_input(prompt: str, retries: int = 3)` that keeps asking the user for a valid integer if a `ValueError` is encountered, up to a maximum number of retries.
2. **Exercise 2 (Custom API Error):** Create an exception hierarchy `APIError` with subclasses `UnauthorizedError (401)`, `NotFoundError (404)`, and `InternalServerError (500)`.
