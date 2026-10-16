# 📌 Topic 04: Strings & Formatting

## 📖 Introduction
In Python, strings (`str`) are **immutable sequences of Unicode characters**. Every string manipulation returns a *new* string object rather than modifying the original in-place.

```
Index:    0   1   2   3   4   5
Char:     P   y   t   h   o   n
Neg Idx: -6  -5  -4  -3  -2  -1
```

---

## 🔑 Core Concepts

### 1. Indexing & Slicing
Slicing syntax: `string[start:stop:step]` (stop is non-inclusive).

```python
text = "Python Programming"

# Positive and Negative Indexing
print(text[0])       # Output: 'P'
print(text[-1])      # Output: 'g'

# Slicing
print(text[0:6])     # Output: 'Python'
print(text[:6])      # Output: 'Python' (default start = 0)
print(text[7:])      # Output: 'Programming' (default stop = end)
print(text[::2])     # Output: 'Pto rgamn' (step by 2)

# Reversing a string (Idiomatic Python trick)
print(text[::-1])    # Output: 'gnimmargorP nohtyP'
```

---

### 2. Essential String Methods

```python
msg = "  Hello, Python World!  "

# Trimming whitespaces
print(msg.strip())            # "Hello, Python World!"
print(msg.lstrip())           # Trims left only
print(msg.rstrip())           # Trims right only

# Case manipulation
print("python".upper())       # "PYTHON"
print("PYTHON".lower())       # "python"
print("hello world".title())   # "Hello World"
print("hello world".capitalize()) # "Hello world"

# Searching & Counting
print(msg.find("Python"))     # Returns starting index (or -1 if not found)
print(msg.count("o"))         # Count occurrences: 3
print(msg.startswith("  He")) # True
print(msg.endswith("!  "))    # True

# Splitting and Joining (Extremely important!)
csv_data = "apple,banana,mango,orange"
fruits = csv_data.split(",")  # ['apple', 'banana', 'mango', 'orange']
print(fruits)

joined_str = " | ".join(fruits)
print(joined_str)             # "apple | banana | mango | orange"

# Replacement
print("I like Java".replace("Java", "Python")) # "I like Python"
```

---

### 3. String Formatting (The Evolution)

#### A. Old Style `%` Formatting (Avoid in modern code):
```python
name = "Rakesh"
"%s is teaching Python" % name
```

#### B. `str.format()` (Python 3.0+):
```python
"Welcome {} to {}!".format("Learner", "EduBroTech")
"Point: ({x}, {y})".format(x=10, y=20)
```

#### C. f-strings (PEP 498 - Modern Standard & Recommended):
Fast, readable, and evaluated at runtime:
```python
name = "Rakesh"
subscribers = 50000
pi = 3.14159265

# Inline variable & expression evaluation
print(f"Creator: {name.upper()}, Subscribers: {subscribers:,}")
# Output: Creator: RAKESH, Subscribers: 50,000

# Decimal precision formatting
print(f"Pi: {pi:.2f}")  # Output: Pi: 3.14

# Padding and alignment
print(f"{'Header':^20}") # Centered in 20 spaces
print(f"{42:05d}")       # Zero-padded: '00042'

# Debugging shorthand (Python 3.8+)
x = 25
print(f"{x=}")          # Output: x=25
```

---

### 4. Raw Strings & Escape Sequences
* Raw strings prefixed with `r` treat backslashes as literal characters (vital for regex & file paths).

```python
# Normal string interprets \n as newline
print("Line1\nLine2")

# Raw string ignores escape characters
regex_pattern = r"C:\new_folder\test.txt"
print(regex_pattern)  # Output: C:\new_folder\test.txt
```

---

## ⚠️ Common Pitfalls

```python
# Strings are IMMUTABLE: You cannot change a character by index!
s = "Hello"
# s[0] = "h"  # Raises TypeError: 'str' object does not support item assignment

# Correct way: Create a new string
s = "h" + s[1:]
```

---

## 🧠 Top Interview Questions

1. **Q: Why are strings immutable in Python?**
   * **A:**
     1. **Security**: Strings are used in file paths, network sockets, and database queries. Immutability guarantees they cannot be modified unexpectedly.
     2. **Hashing & Dict Keys**: Only immutable objects can be hashed. Because strings are immutable, they make safe dictionary keys and set members.
     3. **String Interning & Memory**: Python can reuse existing string instances in memory safely without fear of side-effects.

2. **Q: What is the time complexity of string concatenation `s += "a"` in a loop?**
   * **A:** In each iteration, a new string may be allocated, resulting in $O(N^2)$ overall complexity. Use `str.join()` with a list instead, which operates in $O(N)$ time.

3. **Q: How does `str.strip()` differ from `str.replace(" ", "")`?**
   * **A:** `strip()` only strips leading and trailing whitespaces. `replace(" ", "")` removes whitespaces from the entire string (including between words).

---

## 💻 Practice Exercises
1. **Exercise 1 (Palindrome Check):** Write a function `is_palindrome(s: str) -> bool` that checks if a string reads the same backwards, ignoring spaces and case.
2. **Exercise 2 (Word Frequency Counter):** Given a paragraph of text, split it into words, strip punctuation, convert to lowercase, and format the output using f-strings with aligned columns.
