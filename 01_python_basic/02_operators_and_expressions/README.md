# 📌 Topic 02: Operators & Expressions

## 📖 Introduction
An **operator** is a special symbol or keyword that carries out arithmetic, logical, or comparison operations on operands (variables or values). An **expression** is a combination of values, variables, and operators that evaluates to a single value.

---

## 🔑 Operator Categories

### 1. Arithmetic Operators
Used to perform standard mathematical calculations.

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division (Float) | `10 / 3` | `3.3333...` |
| `//` | Floor Division (Integer quotient) | `10 // 3` | `3` |
| `%` | Modulus (Remainder) | `10 % 3` | `1` |
| `**` | Exponentiation (Power) | `2 ** 4` | `16` |

```python
# Note behavior with negative numbers for floor division:
print(7 // 2)    # Output: 3
print(-7 // 2)   # Output: -4 (rounds toward negative infinity)
```

---

### 2. Comparison (Relational) Operators
Evaluate to a boolean value (`True` or `False`).

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `4 <= 5` | `True` |

```python
# Chained comparisons (Pythonic feature!)
x = 15
print(10 < x < 20)  # Output: True (Equivalent to: 10 < x and x < 20)
```

---

### 3. Logical Operators
Used to combine conditional statements.

| Operator | Description | Example |
|---|---|---|
| `and` | Returns `True` if both operands are truthy | `True and False` -> `False` |
| `or` | Returns `True` if at least one operand is truthy | `True or False` -> `True` |
| `not` | Inverts the boolean state | `not True` -> `False` |

#### ⚡ Short-Circuit Evaluation:
* In `A and B`, if `A` is falsy, Python returns `A` immediately without evaluating `B`.
* In `A or B`, if `A` is truthy, Python returns `A` immediately without evaluating `B`.

```python
# Python returns the actual evaluated operand, not just True/False:
print([] or "fallback")   # Output: "fallback"
print("hello" and "world") # Output: "world"
print(0 and 100)           # Output: 0
```

---

### 4. Identity Operators (`is` vs `==`)
* `==` checks for **value equality** (Do both objects have the same content?).
* `is` checks for **identity / reference equality** (Do both variables point to the same memory location?).

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)  # Output: True  (Same values)
print(list1 is list2)  # Output: False (Different memory objects)

# Best practice: Always compare with None using 'is'
var = None
if var is None:
    print("Variable is None")
```

---

### 5. Membership Operators (`in` and `not in`)
Tests whether a value exists within a sequence (string, list, tuple, set, dict).

```python
frameworks = ["Django", "FastAPI", "Flask"]
print("FastAPI" in frameworks)       # True
print("Ruby" not in frameworks)      # True

# Note on dictionaries: 'in' checks keys by default
student = {"name": "Rakesh", "age": 28}
print("name" in student)             # True
print(28 in student)                 # False (use student.values() instead)
```

---

### 6. Bitwise Operators
Operate directly on the binary representations of integers.

| Operator | Name | Example | Binary |
|---|---|---|---|
| `&` | Bitwise AND | `5 & 3` | `0101 & 0011 = 0001 (1)` |
| `\|` | Bitwise OR | `5 \| 3` | `0101 \| 0011 = 0111 (7)` |
| `^` | Bitwise XOR | `5 ^ 3` | `0101 ^ 0011 = 0110 (6)` |
| `~` | Bitwise NOT | `~5` | `-(5 + 1) = -6` |
| `<<` | Zero-fill Left Shift | `5 << 1` | `0101 << 1 = 1010 (10)` |
| `>>` | Signed Right Shift | `5 >> 1` | `0101 >> 1 = 0010 (2)` |

---

### 7. Operator Precedence (Highest to Lowest)
1. Parentheses: `()`
2. Exponentiation: `**`
3. Unary signs: `+x`, `-x`, `~x`
4. Multiplication, Division, Floor division, Modulus: `*`, `/`, `//`, `%`
5. Addition, Subtraction: `+`, `-`
6. Bitwise shifts: `<<`, `>>`
7. Bitwise AND: `&`
8. Bitwise XOR & OR: `^`, `|`
9. Comparisons, Identity & Membership: `==`, `!=`, `<`, `<=`, `>`, `>=`, `is`, `in`
10. Logical NOT: `not`
11. Logical AND: `and`
12. Logical OR: `or`

---

## ⚠️ Common Mistakes

```python
# Mistake: Using 'is' with literals or computed strings/numbers
x = 1000
y = 1000
# print(x is y)  # Unreliable across Python implementations/runtimes! Use == for values!

# Mistake: Operator precedence misunderstanding
result = 10 + 2 * 5  # Evaluates to 20, NOT 60! Use parentheses for clarity: (10 + 2) * 5
```

---

## 🧠 Top Interview Questions

1. **Q: What is the difference between `/` and `//` in Python 3?**
   * **A:** `/` always returns a `float` (true division), while `//` performs floor division (rounds down to the nearest integer) and preserves integer type if both operands are integers.

2. **Q: How does short-circuiting work in Python logical operators?**
   * **A:** Python evaluates from left to right. As soon as the outcome is determined (e.g., first operand of `or` is truthy, or first operand of `and` is falsy), evaluation terminates and the last evaluated operand is returned.

3. **Q: Why should you use `is None` instead of `== None`?**
   * **A:** `None` is a singleton in Python (only one instance exists in memory). `is` performs an identity check (`id(x) == id(None)`), which is faster and immune to custom `__eq__` operator overrides on objects.

---

## 💻 Practice Exercises
1. **Exercise 1:** Write a program that takes a number and checks if it is both divisible by 3 and 5 using logical operators.
2. **Exercise 2:** Implement a bitwise check to determine if an integer is even or odd using `& 1`.
