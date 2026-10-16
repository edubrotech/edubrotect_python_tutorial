# 📌 Topic 03: Control Flow & Loops

## 📖 Introduction
Control flow dictates the order in which statements are evaluated and executed. Python supports conditional branching (`if-elif-else`, `match-case`) and looping constructs (`for`, `while`) with rich control directives (`break`, `continue`, `pass`, `else`).

---

## 🔑 1. Conditional Statements

### `if`, `elif`, `else`
```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Your Grade: {grade}")  # Output: Your Grade: B
```

### Ternary Operator (Conditional Expression)
A concise one-liner for assigning values conditionally:
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult
```

### Match-Case Statement (Python 3.10+)
Python's powerful structural pattern matching:
```python
def http_status(code: int) -> str:
    match code:
        case 200:
            return "OK - Request Succeeded"
        case 400:
            return "Bad Request - Client Error"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:
            return "Server Error"
        case _:
            return "Unknown Status Code"

print(http_status(404))  # Output: Not Found
```

---

## 🔁 2. Loops in Python

### The `for` Loop & `range()`
In Python, `for` loops iterate over iterable objects (not simple index counters like C/Java):
```python
# range(start, stop, step) - note: stop is non-inclusive!
for num in range(2, 10, 2):
    print(num, end=" ")
# Output: 2 4 6 8
```

#### Iterating with `enumerate()` and `zip()`:
```python
# enumerate provides both index and item
languages = ["Python", "Golang", "Rust"]
for index, lang in enumerate(languages, start=1):
    print(f"{index}. {lang}")

# zip pairs elements from multiple iterables
names = ["Alice", "Bob", "Charlie"]
scores = [95, 88, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

---

### The `while` Loop
Repeats as long as a condition remains `True`:
```python
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Blast off! 🚀")
```

---

## 🛑 3. Loop Control Statements

| Statement | Purpose |
|---|---|
| `break` | Immediately terminates the enclosing loop |
| `continue` | Skips the rest of the current iteration and jumps to the next iteration |
| `pass` | Null statement / placeholder where syntax requires code but no action is needed |

```python
for n in range(1, 10):
    if n % 2 == 0:
        continue  # Skip even numbers
    if n > 7:
        break     # Stop loop once n exceeds 7
    print(n, end=" ")
# Output: 1 3 5 7
```

---

## 🌟 4. The Loop `else` Clause (Secret Python Superpower!)
Both `for` and `while` loops can have an optional `else` block.
* **Rule:** The `else` block executes **ONLY IF** the loop terminates normally (without hitting a `break` statement).

```python
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} is divisible by {i}")
            break
    else:
        # Executes only if loop finished without breaking!
        print(f"{n} is a Prime Number!")
        return True
    return False

is_prime(17)  # Output: 17 is a Prime Number!
```

---

## ⚠️ Common Pitfalls

1. **Accidental Infinite Loops:** Forgetting to update the loop condition counter inside `while`.
2. **Modifying a list while iterating over it:**
   ```python
   # Dangerous:
   numbers = [1, 2, 3, 4, 5]
   for n in numbers:
       if n % 2 == 0:
           numbers.remove(n)  # Skips elements due to shifted indices!

   # Safe solution: Iterate over a copy or use list comprehension
   numbers = [n for n in numbers if n % 2 != 0]
   ```

---

## 🧠 Top Interview Questions

1. **Q: When does the `else` clause of a `for` or `while` loop execute?**
   * **A:** It executes when the loop completes all iterations naturally without encountering a `break` statement or an unhandled exception.

2. **Q: What is the difference between `pass`, `continue`, and `break`?**
   * **A:** `pass` does nothing (placeholder); `continue` skips the remainder of the current iteration; `break` exits the loop entirely.

3. **Q: What makes Python's `match-case` more powerful than a traditional `switch`?**
   * **A:** Python's `match-case` supports structural pattern matching, including destructuring lists/dictionaries, class patterns, and guards (`case x if x > 0:`).

---

## 💻 Practice Exercises
1. **Exercise 1 (FizzBuzz):** Print numbers 1 to 50. For multiples of 3, print "Fizz", for 5 print "Buzz", and for both print "FizzBuzz".
2. **Exercise 2 (Search with Loop Else):** Write a script searching for a user in a list of names. If found, break and print "Found"; if not found after iterating through the entire list, use loop `else` to print "User not registered".
