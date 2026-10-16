# 📌 Advanced Topic 05: Closures & Decorators

## 📖 Introduction
Decorators are one of Python's most elegant and powerful architectural patterns. A **decorator** is a design pattern that allows you to dynamically alter, extend, or monitor the behavior of a callable (function or class) without modifying its original source code.

---

## 🔑 1. Functions as First-Class Citizens
In Python, functions can be:
1. Assigned to variables.
2. Passed as arguments to other functions.
3. Returned from other functions.
4. Stored in data structures.

```python
def shout(text):
    return text.upper()

# Passing function as an argument:
def execute_operation(func, value):
    return func(value)

print(execute_operation(shout, "hello python"))  # Output: HELLO PYTHON
```

---

## 🔒 2. Understanding Closures & Free Variables
A **closure** is a nested function that retains access to variables from its lexical enclosing scope, even after the outer function has finished executing and returned.

```python
def make_multiplier(factor: int):
    # 'factor' is a free variable in the enclosing scope
    def multiply(number: int) -> int:
        return number * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15

# Inspecting closure cells:
print(double.__closure__[0].cell_contents)  # Output: 2
```

---

## 🎨 3. Decorator Anatomy

The `@decorator` syntax is simply syntactic sugar for:
```python
func = decorator(func)
```

```python
import functools
import time

def execution_timer(func):
    # @functools.wraps preserves original function name, docstring, and annotations!
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        print(f"⏱️ '{func.__name__}' took {duration:.6f} seconds to run.")
        return result
    return wrapper

@execution_timer
def compute_heavy_task(n: int):
    """Computes sum of squares up to n."""
    return sum(i ** 2 for i in range(n))

compute_heavy_task(1_000_000)
print("Function Name:", compute_heavy_task.__name__) # Preserved: 'compute_heavy_task'
```

---

## ⚙️ 4. Decorators Accepting Arguments
To pass parameters to a decorator, you add an outer factory function (3 levels of nesting):

```python
def repeat(times: int):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(times=3)
def greet(name: str):
    print(f"Hello, {name}!")

greet("Rakesh")
# Prints "Hello, Rakesh!" 3 times
```

---

## 🏛️ 5. Class-Based Decorators
Using a class with `__call__` allows maintaining state cleanly across calls:

```python
class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count} to '{self.func.__name__}'")
        return self.func(*args, **kwargs)

@CallCounter
def ping_service():
    return "Pong"

ping_service()  # Call #1
ping_service()  # Call #2
```

---

## 🧱 6. Stacking Multiple Decorators
When chaining decorators:
```python
@decorator_one
@decorator_two
def my_func():
    pass
```
* **Wrapping order:** Bottom-Up (`decorator_two` wraps first, then `decorator_one`).
* **Execution order:** Top-Down (`decorator_one` executes first, then `decorator_two`).

---

## 💼 7. Real-World Production Decorators

### A. Automatic Retry with Exponential Backoff
```python
import time
import functools

def retry(max_attempts=3, delay=1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= 2
            raise RuntimeError(f"Function {func.__name__} failed after {max_attempts} attempts.")
        return wrapper
    return decorator
```

### B. Memoization / Caching
```python
def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n: int) -> int:
    if n < 2: return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(35):", fibonacci(35)) # Computes instantly!
```

---

## 🧠 Top Interview Questions

1. **Q: Why is `@functools.wraps` essential when writing decorators?**
   * **A:** Without `@wraps`, the decorated function loses its identity—its `__name__`, `__doc__`, and `__annotations__` are replaced by those of the inner `wrapper` function, breaking reflection, documentation tools, and debuggers.

2. **Q: How does Python preserve variables inside a closure when the enclosing scope has already returned?**
   * **A:** Python stores references to free variables in special `cell` objects within the nested function's `__closure__` tuple. Even though the stack frame is popped, the heap-allocated cell object keeps the referenced variable alive.

---

## 💻 Practice Exercises
1. **Exercise 1 (Role-Based Access Control):** Write an `@requires_role("ADMIN")` decorator that checks if `current_user.get("role") == "ADMIN"`, raising a `PermissionError` if unauthorized.
2. **Exercise 2 (Type Enforcer):** Write a decorator that validates argument types against the function's type annotations at runtime.
