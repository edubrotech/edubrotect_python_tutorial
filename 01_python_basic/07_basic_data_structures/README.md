# 📌 Topic 07: Basic Data Structures (List, Tuple, Set, Dictionary)

## 📖 Introduction
Python provides 4 essential built-in collection data structures. Choosing the right data structure directly impacts the **performance, memory usage, and readability** of your code.

```
┌──────────────────────────────────────────────────────────────┐
│                    PYTHON COLLECTIONS                        │
├──────────────┬──────────────┬────────────────┬───────────────┤
│    List      │    Tuple     │      Set       │  Dictionary   │
│  [1, 2, 3]   │   (1, 2)     │   {1, 2, 3}    │  {'a': 1}     │
│ Mutable      │ Immutable    │ Mutable        │ Mutable       │
│ Ordered      │ Ordered      │ Unordered*     │ Key-Ordered*  │
│ Duplicates   │ Duplicates   │ Unique Only    │ Unique Keys   │
└──────────────┴──────────────┴────────────────┴───────────────┘
* In Python 3.7+, dictionaries preserve insertion order.
```

---

## 🔑 1. Lists (`list`)
A mutable, ordered sequence of heterogeneous elements.

```python
# Creation
fruits = ["apple", "banana", "cherry"]

# Adding elements
fruits.append("orange")         # Adds to end: O(1)
fruits.insert(1, "mango")        # Inserts at index 1: O(N)
fruits.extend(["grape", "kiwi"]) # Appends multiple elements

# Removing elements
removed_item = fruits.pop()      # Removes and returns last item: O(1)
fruits.remove("banana")          # Removes first occurrence by value: O(N)

# Sorting and Reversing
fruits.sort()                    # In-place Timsort: O(N log N)
fruits.reverse()                 # In-place reversal: O(N)

print("Final fruits:", fruits)
```

---

## 🔒 2. Tuples (`tuple`)
An immutable, ordered sequence of elements. Tuples are faster than lists, consume less memory, and can be used as dictionary keys.

```python
# Creation (note: single-element tuple requires trailing comma!)
point = (10, 20)
single_element = (42,) # tuple
not_a_tuple = (42)     # int!

# Tuple Unpacking
x, y = point
print(f"X: {x}, Y: {y}")

# Extended unpacking with *
first, *middle, last = (1, 2, 3, 4, 5)
print(f"first: {first}, middle: {middle}, last: {last}")
# Output: first: 1, middle: [2, 3, 4], last: 5
```

---

## 🎯 3. Sets (`set` & `frozenset`)
An unordered collection of **unique, hashable elements**. Backed by a hash table with average **$O(1)$ lookup, insertion, and deletion**.

```python
# Creation
tags = {"python", "coding", "tutorial", "python"}
print(tags)  # Duplicates removed: {'python', 'coding', 'tutorial'}

# Mathematical Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union (A | B):", a | b)                 # {1, 2, 3, 4, 5, 6}
print("Intersection (A & B):", a & b)          # {3, 4}
print("Difference (A - B):", a - b)            # {1, 2}
print("Symmetric Diff (A ^ B):", a ^ b)        # {1, 2, 5, 6}

# frozenset: Immutable version of set (can be used as dict key)
frozen = frozenset([1, 2, 3])
```

---

## 🗂️ 4. Dictionaries (`dict`)
An associative mapping of unique keys to arbitrary values. Backed by a highly optimized hash table with **$O(1)$ average complexity**.

```python
user = {
    "id": 101,
    "name": "Rakesh",
    "role": "Lead Engineer",
    "active": True
}

# Safe access with get() (avoids KeyError)
email = user.get("email", "not_provided@example.com")
print("Email:", email)

# setdefault(): Inserts key with default value if not present
user.setdefault("skills", []).append("Python")

# Iterating over dictionary
for key, value in user.items():
    print(f"{key}: {value}")

# Merging dictionaries (Python 3.9+ union operator |)
defaults = {"theme": "dark", "notifications": True}
user_prefs = {"notifications": False, "font_size": 14}
final_config = defaults | user_prefs
print("Final Config:", final_config)
# Output: {'theme': 'dark', 'notifications': False, 'font_size': 14}
```

---

## 📊 Time Complexity Comparison (Big-O)

| Operation | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Access by Index / Key | $O(1)$ | $O(1)$ | N/A | $O(1)$ avg |
| Append / Insert | $O(1)$ / $O(N)$ | N/A | $O(1)$ avg | $O(1)$ avg |
| Membership check (`x in S`) | $O(N)$ | $O(N)$ | **$O(1)$ avg** | **$O(1)$ avg (keys)** |
| Deletion | $O(N)$ | N/A | $O(1)$ avg | $O(1)$ avg |

---

## ⚠️ Common Pitfalls

```python
# Pitfall 1: Modifying a mutable item inside a tuple
t = (1, 2, [3, 4])
t[2].append(5)  # Works! The list inside the tuple IS mutable!
# t[2] = [3, 4, 5]  # Raises TypeError: 'tuple' does not support assignment

# Pitfall 2: Using unhashable types as dictionary keys or set elements
# my_dict = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
# Fix: Use tuple instead
my_dict = {(1, 2): "value"}  # Valid!
```

---

## 🧠 Top Interview Questions

1. **Q: What is "hashability" and why can't lists be used as dictionary keys?**
   * **A:** An object is hashable if it has a hash value that never changes during its lifetime (`__hash__()`) and can be compared to other objects (`__eq__()`). Since lists are mutable, their contents can change, which would corrupt the dictionary hash table bucket lookup.

2. **Q: How does Python's `set` achieve $O(1)$ lookup time?**
   * **A:** Python sets use a hash table. When checking `x in my_set`, Python calculates `hash(x)` to directly compute the index of the bucket in memory, avoiding a linear scan through the elements.

3. **Q: What is the difference between `dict.get(key)` and `dict[key]`?**
   * **A:** `dict[key]` raises a `KeyError` if the key does not exist. `dict.get(key, default)` returns `None` (or a specified default value) without raising an error.

---

## 💻 Practice Exercises
1. **Exercise 1 (Remove Duplicates Preserving Order):** Given a list with duplicate elements, remove duplicates while strictly preserving the original order (hint: compare `list(set(l))` vs using a dictionary).
2. **Exercise 2 (Group Anagrams):** Given a list of words `["eat", "tea", "tan", "ate", "nat", "bat"]`, group the anagrams together using a dictionary.
