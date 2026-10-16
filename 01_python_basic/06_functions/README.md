# 📌 Topic 06: Functions & Variable Scope

## 📖 Introduction
A function is an organized, reusable block of code designed to perform a single, related action. Functions promote the **DRY (Don't Repeat Yourself)** principle, improve modularity, and make applications easy to test and debug.

---

## 🔑 1. Function Definition & Docstrings

```python
def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    :param length: Length of the rectangle
    :param width: Width of the rectangle
    :return: Area as a float
    """
    return length * width

# Accessing function metadata
print(calculate_area(10, 5))         # Output: 50.0
print(calculate_area.__doc__)        # Prints the docstring
```

---

## ⚙️ 2. Function Arguments & Parameters

### A. Positional vs Keyword Arguments
```python
def greet(name: str, greeting: str):
    return f"{greeting}, {name}!"

# Positional arguments (order matters)
print(greet("Rakesh", "Hello"))

# Keyword arguments (order does not matter)
print(greet(greeting="Namaste", name="Rakesh"))
```

### B. Default Arguments
```python
def connect(host="localhost", port=5432):
    return f"Connecting to {host}:{port}"

print(connect())              # Uses defaults: localhost:5432
print(connect("192.168.1.1")) # Overrides host: 192.168.1.1:5432
```

### C. Arbitrary Arguments: `*args` and `**kwargs`
* `*args`: Collects extra positional arguments into a **tuple**.
* `**kwargs`: Collects extra keyword arguments into a **dictionary**.

```python
def order_food(customer: str, *items, **metadata):
    print(f"Customer: {customer}")
    print(f"Items ordered: {items}")         # tuple: ('Pizza', 'Burger', 'Coke')
    print(f"Metadata: {metadata}")           # dict: {'table': 5, 'priority': 'High'}

order_food("Alice", "Pizza", "Burger", "Coke", table=5, priority="High")
```

### D. Positional-Only (`/`) & Keyword-Only (`*`) Parameters (Python 3.8+)
```python
def configure(host, port, /, timeout=30, *, secure=True):
    # host and port MUST be positional (before /)
    # secure MUST be keyword-only (after *)
    # timeout can be either
    return f"{host}:{port} (timeout={timeout}, secure={secure})"

# Valid call:
print(configure("api.example.com", 443, 60, secure=True))

# Invalid calls:
# configure(host="api.example.com", 443)  # TypeError!
# configure("api.example.com", 443, 60, False) # TypeError!
```

---

## 🌐 3. Scope & The LEGB Rule
Python resolves variable names in this exact hierarchy:
1. **L**ocal: Defined inside the current function.
2. **E**nclosing: Defined in outer/enclosing functions (nested scope).
3. **G**lobal: Defined at top-level module scope.
4. **B**uilt-in: Pre-defined Python names (`len`, `print`, `int`, etc.).

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # Prints: local
    inner()
    print(x)      # Prints: enclosing

outer()
print(x)          # Prints: global
```

### Modifying Scopes: `global` and `nonlocal`
```python
counter = 0

def increment_global():
    global counter
    counter += 1

def outer_closure():
    val = 10
    def inner_closure():
        nonlocal val
        val += 5
        return val
    return inner_closure()

print(outer_closure())  # Output: 15
```

---

## ⚡ 4. Anonymous (Lambda) Functions
Small, one-line functions with no name, created using the `lambda` keyword:
`lambda arguments: expression`

```python
square = lambda x: x ** 2
print(square(6))  # Output: 36

# Frequently used in sorting:
students = [("Rakesh", 92), ("Alice", 85), ("Bob", 98)]
students.sort(key=lambda item: item[1], reverse=True)
print(students)  # [('Bob', 98), ('Rakesh', 92), ('Alice', 85)]
```

---

## 🔄 5. Higher-Order Functions (`map`, `filter`, `reduce`)
A higher-order function is a function that takes another function as an argument or returns one.

```python
numbers = [1, 2, 3, 4, 5, 6]

# map(): transforms every element
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)  # [2, 4, 6, 8, 10, 12]

# filter(): filters elements matching condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)      # [2, 4, 6]

# reduce(): accumulates elements into single value
from functools import reduce
total_product = reduce(lambda acc, x: acc * x, numbers)
print("Product:", total_product)  # 720
```

---

## 🔁 6. Recursion
A function calling itself until reaching a base condition:

```python
def factorial(n: int) -> int:
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

---

## ⚠️ The Notorious Mutable Default Argument Bug!

```python
# 🚨 DANGEROUS MISTAKE:
def add_item(item, target_list=[]):
    target_list.append(item)
    return target_list

print(add_item("Apple"))   # ['Apple']
print(add_item("Banana"))  # ['Apple', 'Banana'] -> OOPS! Default list is shared!

# ✅ CORRECT IDIOMATIC FIX:
def add_item_safe(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list
```
**Why?** In Python, default arguments are evaluated **once at function definition time**, not every time the function is called!

---

## 🧠 Top Interview Questions

1. **Q: Explain the LEGB rule with an example.**
   * **A:** LEGB defines Python's name resolution order: Local -> Enclosing -> Global -> Built-in. Python searches each scope sequentially until it finds the variable or raises a `NameError`.

2. **Q: Why should you never use `[]` or `{}` as a default argument?**
   * **A:** Default arguments are created once when the function is defined. If you mutate a mutable default argument, that mutation persists across all future calls that omit the parameter.

3. **Q: What is the difference between `*args` and `**kwargs`?**
   * **A:** `*args` packs arbitrary positional arguments into a `tuple`, while `**kwargs` packs arbitrary keyword arguments into a `dict`.

---

## 💻 Practice Exercises
1. **Exercise 1 (Fibonacci Generator):** Implement a recursive function with memoization to find the $n$-th Fibonacci number.
2. **Exercise 2 (Config Parser):** Write a function that accepts required `app_name` and `version` as positional-only arguments, and arbitrary feature flags as `**kwargs`, returning a formatted dictionary.
