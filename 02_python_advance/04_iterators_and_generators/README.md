# 📌 Advanced Topic 04: Iterators & Generators

## 📖 Introduction
Iterators and generators are at the heart of Python's memory-efficient data processing model. They allow programs to process massive (or even infinite) streams of data without loading everything into RAM all at once.

---

## 🔑 1. Iterable vs Iterator: The Core Distinction

* **Iterable**: An object capable of returning its members one at a time. It implements `__iter__()` which returns an iterator (e.g., `list`, `tuple`, `str`, `dict`).
* **Iterator**: An object that represents a stream of data. It implements:
  1. `__iter__()`: Returns itself.
  2. `__next__()`: Returns the next value in sequence, or raises `StopIteration` when exhausted.

```python
numbers = [10, 20, 30]

# numbers is an Iterable
print(hasattr(numbers, "__iter__"))  # True
print(hasattr(numbers, "__next__"))  # False

# Obtaining an Iterator from an Iterable:
it = iter(numbers)
print(hasattr(it, "__next__"))      # True

# Consuming values via next():
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# print(next(it)) # Raises StopIteration!
```

---

## 🛠️ 2. Writing a Custom Iterator Class

```python
class CountDown:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        # An iterator must return itself
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for count in CountDown(3):
    print(count, end=" ")
# Output: 3 2 1
```

---

## ⚡ 3. Generator Functions & `yield`

A generator is a special function that uses the `yield` keyword instead of `return`. When `yield` is encountered, Python **freezes the function's execution state**, yielding the value to the caller. When `next()` is called again, execution resumes immediately after the `yield` statement.

```python
def count_up_to(limit: int):
    count = 1
    while count <= limit:
        yield count
        count += 1

gen = count_up_to(3)
print(type(gen))  # <class 'generator'>
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
```

---

## 🔀 4. Subgenerator Delegation: `yield from`
`yield from <iterable>` delegates part of its operations to another generator or iterable cleanly:

```python
def chain_iterables(*iterables):
    for it in iterables:
        yield from it  # Automatically yields each item from 'it'

result = list(chain_iterables(["A", "B"], (1, 2), "XY"))
print(result)  # ['A', 'B', 1, 2, 'X', 'Y']
```

---

## 💬 5. Advanced Generator Control: `.send()`, `.throw()`, `.close()`

Generators can act as two-way data channels (coroutines):
* `.send(val)`: Resumes generator and sends a value into the `yield` expression.
* `.throw(typ)`: Raises an exception at the point where generator was paused.
* `.close()`: Terminates the generator by raising `GeneratorExit`.

```python
def accumulator():
    total = 0
    while True:
        # yield returns 'total' and receives 'value' sent via send()
        value = yield total
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)  # Prime the generator (advance to first yield) -> 0
print(acc.send(10))  # 10
print(acc.send(25))  # 35
print(acc.send(5))   # 40
acc.close()
```

---

## 🏗️ 6. Real-World Architecture: Streaming Data Pipeline
Processing a 10 GB log file using $O(1)$ memory by chaining generator stages:

```python
# Stage 1: File line producer
def read_log_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            yield line

# Stage 2: Filter for error entries
def filter_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line

# Stage 3: Parse timestamp and message
def parse_error_details(error_lines):
    for line in error_lines:
        parts = line.strip().split(" - ")
        yield {"timestamp": parts[0], "message": parts[1]}

# Composition: Memory-efficient streaming pipeline
# pipeline = parse_error_details(filter_errors(read_log_lines("production.log")))
# for entry in pipeline:
#     print(entry)
```

---

## 🧠 Top Interview Questions

1. **Q: What is the difference between `return` and `yield`?**
   * **A:** `return` exits the function permanently and destroys its local stack frame. `yield` pauses the function, preserves its entire state (local variables and instruction pointer), and yields a value, ready to resume on the next call.

2. **Q: Can an iterator be traversed more than once?**
   * **A:** No. Iterators are one-way data streams. Once exhausted (after raising `StopIteration`), they cannot be reset. To iterate again, you must create a new iterator from the iterable.

3. **Q: Why does a generator function not execute immediately when called?**
   * **A:** Calling a generator function merely instantiates and returns a generator object. No code inside the function body runs until the first call to `next()` or an iteration loop begins.

---

## 💻 Practice Exercises
1. **Exercise 1 (Infinite Prime Generator):** Write a generator function `infinite_primes()` that generates prime numbers indefinitely.
2. **Exercise 2 (Batched Chunker):** Implement a generator `batched(iterable, n)` that yields tuples of length `n` from any sequence.
