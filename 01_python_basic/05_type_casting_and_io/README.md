# 📌 Topic 05: Type Casting & Console I/O

## 📖 Introduction
Type casting (or type conversion) is the process of converting the value of one data type into another. Console I/O allows your Python program to interact with users via standard input (`stdin`) and standard output (`stdout`).

---

## 🔑 1. Type Casting in Python

### Implicit Type Conversion
Python automatically converts one data type to another without programmer intervention to prevent data loss:
```python
integer_val = 10      # int
float_val = 5.5       # float

# Python automatically converts integer_val to float before adding:
result = integer_val + float_val
print(result)         # Output: 15.5
print(type(result))   # Output: <class 'float'>
```

### Explicit Type Conversion (Type Casting)
Manually converting using Python's built-in conversion constructors:

| Function | Converts To | Example | Output |
|---|---|---|---|
| `int(x)` | Integer | `int("42")`, `int(9.99)` | `42`, `9` (truncates decimal!) |
| `float(x)`| Floating-point | `float("3.14")`, `float(10)` | `3.14`, `10.0` |
| `str(x)` | String | `str(100)`, `str(True)` | `'100'`, `'True'` |
| `bool(x)`| Boolean | `bool(1)`, `bool("")` | `True`, `False` |
| `list(x)`| List | `list("cat")` | `['c', 'a', 't']` |
| `tuple(x)`| Tuple | `tuple([1, 2])` | `(1, 2)` |
| `set(x)` | Unique Set | `set([1, 2, 2, 3])` | `{1, 2, 3}` |

```python
# Number bases conversion with int()
print(int("1010", 2))  # Binary to integer: 10
print(int("FF", 16))   # Hexadecimal to integer: 255
print(int("77", 8))    # Octal to integer: 63
```

---

## ⌨️ 2. User Input (`input()`)
The `input()` function prompts the user and **always returns a string (`str`)**.

```python
# Reading a string
name = input("Enter your name: ")

# Reading numbers requires explicit casting!
age = int(input("Enter your age: "))
salary = float(input("Enter monthly salary: "))

# Reading multiple values in a single line
# Example input: 10 20 30
nums = [int(x) for x in input("Enter 3 numbers: ").split()]
print("Sum:", sum(nums))

# Using map()
a, b = map(int, input("Enter two numbers: ").split())
```

---

## 🖥️ 3. Output Formatting (`print()`)

The signature of `print()`:
```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

### Parameters explained:
* `*objects`: Any number of values separated by commas.
* `sep`: Separator between items (default is single space `' '`).
* `end`: What to print at the end of the line (default is newline `'\n'`).
* `file`: Destination stream (default is standard output).
* `flush`: If `True`, forcibly flushes the output buffer immediately.

```python
# Custom separator
print("Python", "Java", "C++", sep=" | ")
# Output: Python | Java | C++

# Custom end (printing on same line)
for i in range(5):
    print(i, end=" -> ")
print("DONE")
# Output: 0 -> 1 -> 2 -> 3 -> 4 -> DONE

# Redirecting output to standard error
import sys
print("CRITICAL ERROR: Connection timeout!", file=sys.stderr)

# Buffer flushing (useful in progress bars / countdowns)
import time
for i in range(3, 0, -1):
    print(f"\rRestarting in {i}s...", end="", flush=True)
    time.sleep(1)
print("\nSystem restarted!")
```

---

## ⚠️ Common Pitfalls

```python
# Pitfall 1: Forgetting that input() returns str
num = input("Enter number: ")  # User enters: 5
# print(num + 10)  # TypeError: can only concatenate str (not "int") to str!

# Pitfall 2: int() with non-integer string representations
# int("3.14")  # ValueError: invalid literal for int() with base 10: '3.14'
# Fix: Convert to float first, then int:
print(int(float("3.14")))  # Output: 3
```

---

## 🧠 Top Interview Questions

1. **Q: Why does `int("3.14")` fail with ValueError, but `int(3.14)` succeeds?**
   * **A:** `int()` parses string literals strictly looking for base-10 digits without decimal points. Passing a float `3.14` directly invokes Python's C-level float-to-int conversion (`PyLong_FromDouble`), which cleanly truncates fractional digits.

2. **Q: What is the purpose of the `flush=True` parameter in `print()`?**
   * **A:** Standard output is buffered for efficiency. If writing to a console or network stream without a newline, messages may stay in the buffer. `flush=True` forces the runtime to write buffered characters to the destination device immediately.

---

## 💻 Practice Exercises
1. **Exercise 1 (Temperature Converter):** Write a script that prompts the user for temperature in Celsius (float), converts it to Fahrenheit ($F = C \times \frac{9}{5} + 32$), and prints with 2 decimal precision.
2. **Exercise 2 (Shopping Bill Generator):** Accept user items and prices in a single line, calculate total and GST (18%), and print a neat receipt using `sep` and f-strings.
