# 📌 Advanced Topic 03: Comprehensions (List, Dict, Set & GenExpr)

## 📖 Introduction
Comprehensions provide a concise, readable, and highly expressive syntax for constructing new sequences and collections from existing iterables. In CPython, comprehensions are executed at C-speed using specialized bytecode instructions (`LIST_APPEND`), making them significantly faster than manual `for` loops.

---

## 🔑 1. List Comprehensions

Syntax: `[expression for item in iterable if condition]`

```python
# Traditional loop:
squares = []
for x in range(1, 6):
    if x % 2 == 0:
        squares.append(x ** 2)

# Equivalent List Comprehension:
squares = [x ** 2 for x in range(1, 6) if x % 2 == 0]
print("Squares:", squares)  # [4, 16]

# Using ternary if-else within comprehension:
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]
print("Labels:", labels)    # ['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

---

## 🗂️ 2. Dictionary Comprehensions

Syntax: `{key_expression: value_expression for item in iterable if condition}`

```python
names = ["Rakesh", "Bob", "Pooja", "Alex"]

# Creating name-to-length lookup map
name_lengths = {name: len(name) for name in names if len(name) > 3}
print("Lengths:", name_lengths)
# Output: {'Rakesh': 6, 'Pooja': 5, 'Alex': 4}

# Inverting a dictionary (swapping keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print("Inverted:", inverted)  # {1: 'a', 2: 'b', 3: 'c'}
```

---

## 🎯 3. Set Comprehensions

Syntax: `{expression for item in iterable if condition}`

```python
words = ["apple", "BANANA", "Cherry", "apple", "banana"]

# Collect unique lowercase words
unique_words = {word.lower() for word in words}
print("Unique words:", unique_words)  # {'apple', 'banana', 'cherry'}
```

---

## ⚡ 4. Generator Expressions (Lazy Evaluation)

A generator expression uses **parentheses `()`** instead of brackets `[]`. It yields items one by one on demand rather than allocating the entire sequence in memory:

```python
import sys

# List comprehension: Eagerly creates 1,000,000 numbers in memory
list_comp = [x ** 2 for x in range(1_000_000)]
print(f"List size in RAM: {sys.getsizeof(list_comp):,} bytes") # ~8.4 MB

# Generator expression: Generates values lazily on the fly
gen_expr = (x ** 2 for x in range(1_000_000))
print(f"GenExpr size in RAM: {sys.getsizeof(gen_expr):,} bytes") # ~200 bytes!

# Passing generator expression directly to sum() or any():
total = sum(x ** 2 for x in range(100))
print("Sum of squares:", total)
```

---

## 🔄 5. Nested Comprehensions & Flattening

```python
# Flattening a 2D matrix:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Order follows natural for-loop nesting order:
# for row in matrix: for val in row: yield val
flattened = [val for row in matrix for val in row]
print("Flattened:", flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Matrix Transpose:
transposed = [[row[i] for row in matrix] for i in range(3)]
print("Transposed:", transposed)
# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

---

## 🚀 6. Performance: Why are Comprehensions Faster?

Under the hood in CPython:
* A standard loop with `.append()` requires looking up the `append` method on the list object in every iteration and making a Python function call.
* List comprehensions compile down to the C-level opcode `LIST_APPEND`, avoiding attribute lookup and function call overhead entirely.

```python
import timeit

loop_time = timeit.timeit("""
res = []
for i in range(1000):
    res.append(i * 2)
""", number=10000)

comp_time = timeit.timeit("""
res = [i * 2 for i in range(1000)]
""", number=10000)

print(f"Loop time: {loop_time:.4f}s vs Comprehension time: {comp_time:.4f}s")
# Comprehension is typically 25% - 40% faster!
```

---

## ⚠️ When NOT to Use Comprehensions

1. **When side effects are involved:** Do not use list comprehensions simply to call a function (`[print(x) for x in items]`). Use a plain `for` loop.
2. **Excessive nesting:** Nesting beyond 2 levels degrades readability dramatically. Apply the Zen of Python: *"Readability counts"*.

---

## 🧠 Top Interview Questions

1. **Q: What is the syntactic difference between a list comprehension and a generator expression?**
   * **A:** Brackets `[...]` produce an in-memory eager `list`. Parentheses `(...)` produce a lazy, memory-efficient `generator` iterator that computes elements on-demand.

2. **Q: How does scoping work in Python 3 comprehensions?**
   * **A:** In Python 3, comprehensions have their own local function-like scope. Iteration variables do not leak into the surrounding scope (in Python 2, the loop variable leaked into the global namespace).

---

## 💻 Practice Exercises
1. **Exercise 1 (Matrix Multiplication Prep):** Given two lists `A = [1, 2, 3]` and `B = ['x', 'y']`, write a list comprehension to generate all pairs `[(1, 'x'), (1, 'y'), ...]`.
2. **Exercise 2 (Dictionary Filter):** Given a dictionary of student grades `{'Alice': 88, 'Bob': 58, 'Charlie': 94, 'David': 45}`, create a dict comprehension containing only students who passed (`grade >= 60`) with their grade mapped to `"Pass"`.
