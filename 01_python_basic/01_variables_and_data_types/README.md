# 📌 Topic 01: Variables & Data Types

## 📖 Introduction
In Python, variables are essentially **names (labels or references)** bound to objects stored in memory. Unlike C/C++ or Java, Python is **dynamically typed** — you do not need to declare variable types explicitly; the interpreter infers the type at runtime based on the assigned value.

```
┌──────────────┐          ┌───────────────────────┐
│ variable_name│ ───────> │  Object in Memory     │
│  "user_age"  │          │  Value: 25, Type: int │
└──────────────┘          └───────────────────────┘
```

---

## 🔑 Core Concepts

### 1. Declaring Variables & Naming Rules
* Must start with a letter (`a-z`, `A-Z`) or underscore (`_`).
* Cannot start with a digit.
* Can only contain alphanumeric characters and underscores (`a-z`, `0-9`, `_`).
* Variable names are **case-sensitive** (`age`, `Age`, and `AGE` are 3 different variables).
* Cannot use Python keywords (`def`, `class`, `if`, `while`, etc.).
* Convention: PEP 8 recommends `snake_case` for variable names (e.g., `student_name`, `total_price`).

```python
# Valid variable names
user_name = "Rakesh"
total_count = 100
_private_var = 42

# Invalid variable names (will raise SyntaxError)
# 1user = "error"     # Cannot start with number
# user-name = "error" # Hyphens not allowed
# class = "error"     # Cannot use reserved keyword
```

---

### 2. Primitive Built-in Data Types

| Data Type | Description | Example |
|---|---|---|
| `int` | Arbitrary precision integers | `x = 42`, `y = -1050` |
| `float` | Double precision floating-point numbers | `pi = 3.14159`, `price = 99.99` |
| `complex` | Complex numbers with real and imaginary parts | `z = 3 + 4j` |
| `str` | Textual data enclosed in quotes | `name = "Python 3"` |
| `bool` | Boolean truth values | `is_active = True`, `has_error = False` |
| `NoneType` | Represents the absence of a value or null state | `result = None` |

---

### 3. Checking Data Types and Memory Address

```python
# Checking type using type()
score = 98.5
print(type(score))  # Output: <class 'float'>

# Checking identity/memory address using id()
a = 10
b = 10
print(id(a) == id(b))  # Output: True (Small Integer Caching for -5 to 256)

# Type verification using isinstance()
print(isinstance(score, float))  # Output: True
print(isinstance(score, (int, float)))  # Output: True
```

---

### 4. Multiple Assignment & Unpacking

```python
# Assigning same value to multiple variables
x = y = z = 0

# Multiple assignment (tuple unpacking)
name, age, city = "Rakesh", 28, "Bengaluru"
print(f"Name: {name}, Age: {age}, City: {city}")

# Swapping two variables without a temporary variable
a = 10
b = 20
a, b = b, a
print(f"a = {a}, b = {b}")  # Output: a = 20, b = 10
```

---

### 5. The `None` Type and Truthy/Falsy Values
In Python, values can evaluate to `True` (Truthy) or `False` (Falsy) in a boolean context.

**Falsy values in Python:**
* `None`
* `False`
* Zero of any numeric type: `0`, `0.0`, `0j`
* Any empty sequence or collection: `""`, `[]`, `()`, `{}`, `set()`

```python
value = None
if not value:
    print("Value is None or empty!")  # This will print
```

---

## ⚠️ Common Pitfalls & Mistakes

1. **Confusing `=` (Assignment) with `==` (Equality Comparison):**
   ```python
   # Mistake:
   # if count = 10:  # SyntaxError
   # Correct:
   if count == 10:
       pass
   ```

2. **Accidentally shadowing built-in names:**
   ```python
   # Never do this:
   # list = [1, 2, 3]  # Shadows the built-in list() constructor
   # str = "hello"     # Shadows the built-in str() function
   ```

---

## 🧠 Top Interview Questions

1. **Q: Is Python statically typed or dynamically typed?**
   * **A:** Python is **dynamically typed** (types are checked at runtime) and **strongly typed** (you cannot perform operations between incompatible types without explicit conversion, e.g., `"age" + 5` raises `TypeError`).

2. **Q: What is small integer caching / integer interning in Python?**
   * **A:** CPython pre-allocates an array of integer objects for integers in the range `[-5, 256]`. When you assign an integer in this range, Python points to the existing pre-allocated memory object rather than creating a new one.

3. **Q: What is the difference between `type(x) == int` and `isinstance(x, int)`?**
   * **A:** `type(x) == int` only checks for the exact type, ignoring inheritance. `isinstance(x, int)` checks if `x` is an instance of `int` or any subclass derived from `int` (such as `bool`, because `bool` is a subclass of `int` in Python!).

---

## 💻 Practice Exercises

1. **Exercise 1:** Declare variables representing a student's `name` (str), `roll_no` (int), `marks_percentage` (float), and `passed` (bool). Print their values alongside their data types.
2. **Exercise 2:** Swap three variables `a = 5`, `b = 10`, `c = 15` such that `a` gets `c`, `b` gets `a`, and `c` gets `b` in a single line of Python code.
