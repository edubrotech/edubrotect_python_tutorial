# 📌 Topic 08: File Handling & Serialization

## 📖 Introduction
File handling allows Python programs to persist data to disk and read external files. Python provides intuitive built-in file operations along with standard library modules like `pathlib`, `json`, and `csv`.

---

## 🔑 1. The `open()` Function & File Modes

```python
file = open("sample.txt", mode="r", encoding="utf-8")
```

| Mode | Name | Description |
|---|---|---|
| `'r'` | Read (Default) | Opens file for reading. Raises `FileNotFoundError` if missing. |
| `'w'` | Write | Opens for writing. **Truncates (erases)** file if it exists, creates if not. |
| `'a'` | Append | Opens for writing. Appends data to end of file without erasing. |
| `'x'` | Exclusive Creation | Creates new file. Raises `FileExistsError` if file already exists. |
| `'b'` | Binary | Binary mode (e.g., `'rb'`, `'wb'`) for images, PDFs, audio. |
| `'+'` | Read/Write | Update mode (e.g., `'r+'`, `'w+'`). |

---

## 🛡️ 2. The `with` Statement (Context Manager)
**Best Practice:** Always use the `with` statement. It automatically flushes and closes the file descriptor even if an error occurs!

```python
# Writing to a file safely
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Welcome to Python File Handling!\n")
    f.write("Line 2: Always use with statement.\n")
# File is automatically closed here!
```

---

## 📖 3. Reading Files Efficiently

```python
# 1. Reading entire content into memory (Use for small files only!)
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 2. Reading line-by-line (Memory Efficient - Recommended for large files!)
with open("notes.txt", "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, start=1):
        print(f"Line {line_num}: {line.strip()}")

# 3. Reading lines into a list
with open("notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
```

### File Cursor: `tell()` and `seek()`
```python
with open("notes.txt", "r", encoding="utf-8") as f:
    print("Initial position:", f.tell())  # 0
    chunk = f.read(10)                    # Read first 10 characters
    print("New position:", f.tell())      # 10
    f.seek(0)                             # Reset cursor back to start
    print("After seek(0):", f.tell())     # 0
```

---

## 📦 4. Working with JSON (`json` module)

```python
import json

data = {
    "project": "EduBroTech Python Tutorial",
    "version": 3.12,
    "modules": ["basics", "advanced", "concurrency"],
    "is_published": True
}

# Writing JSON to file (Serialization: dump)
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

# Reading JSON from file (Deserialization: load)
with open("config.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print("Loaded JSON:", loaded_data["project"])

# In-memory JSON string conversion
json_str = json.dumps(data)         # dict -> JSON string
parsed_dict = json.loads(json_str)  # JSON string -> dict
```

---

## 📊 5. Working with CSV (`csv` module)

```python
import csv

# Writing CSV using DictWriter
users = [
    {"name": "Rakesh", "role": "Instructor", "city": "Bengaluru"},
    {"name": "Aman", "role": "Student", "city": "Delhi"}
]

with open("users.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["name", "role", "city"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(users)

# Reading CSV using DictReader
with open("users.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} ({row['role']}) from {row['city']}")
```

---

## 🗂️ 6. Modern File Paths with `pathlib.Path`

```python
from pathlib import Path

# Constructing paths safely across Windows/Linux/macOS
base_dir = Path.cwd()
target_file = base_dir / "data" / "output.txt"

# Creating parent directories if they don't exist
target_file.parent.mkdir(parents=True, exist_ok=True)

# Quick read and write without open() boilerplate
target_file.write_text("Hello from Pathlib!", encoding="utf-8")
print(target_file.read_text(encoding="utf-8"))

# Checking existence and properties
print("Exists:", target_file.exists())
print("Is File:", target_file.is_file())
print("File Extension:", target_file.suffix)
```

---

## ⚠️ Common Pitfalls

```python
# Pitfall 1: Forgetting encoding="utf-8"
# On Windows, default encoding might be cp1252, causing UnicodeDecodeError on emojis or special characters!
# Always specify encoding="utf-8"!

# Pitfall 2: Forgetting newline="" in csv on Windows
# Causes extra blank lines between rows!
```

---

## 🧠 Top Interview Questions

1. **Q: Why is iterating over the file object `for line in f:` preferred over `f.readlines()`?**
   * **A:** `f.readlines()` loads the entire file into memory as a list of strings at once, which will cause an `OutOfMemoryError` on gigabyte-sized files. Iterating over `f` uses a lazy generator buffer, reading one line at a time in $O(1)$ memory.

2. **Q: What is the difference between `json.dump()` and `json.dumps()`?**
   * **A:** `json.dump(obj, file)` writes the serialized JSON directly into an open file-like stream. `json.dumps(obj)` serializes the object into a Python `str` in memory.

3. **Q: How does `with open(...)` prevent resource leaks?**
   * **A:** The `with` statement utilizes the Context Management protocol (`__enter__` and `__exit__`). Even if an unhandled exception is raised during file read/write, Python guarantees that `__exit__` will be called, closing the underlying OS file descriptor.

---

## 💻 Practice Exercises
1. **Exercise 1 (Log Counter):** Write a script that reads a simulated server log file line-by-line and counts how many times "ERROR", "WARNING", and "INFO" appear.
2. **Exercise 2 (JSON Merger):** Given two JSON files containing configurations, write a script to merge them and save the result into a new JSON file formatted with 4 spaces indent.
