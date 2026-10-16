# 📌 Advanced Topic 10: Modules, Packages & Virtual Environments

## 📖 Introduction
Modularization is the cornerstone of building maintainable software architectures. In Python, modules allow code separation into independent files, while packages organize modules into hierarchical directory namespaces.

```
project_root/
│
├── package_a/
│   ├── __init__.py           # Marks directory as regular Python package
│   ├── module_one.py
│   └── subpackage/
│       ├── __init__.py
│       └── helpers.py
│
├── requirements.txt          # Frozen project dependencies
└── main.py                   # Project entry point
```

---

## 🔍 1. How Python Finds & Loads Modules (`sys.path`)

When you execute `import my_module`, Python performs these 3 steps:
1. **Cache Check (`sys.modules`)**: Inspects `sys.modules` to see if the module was already loaded in this session. If found, returns the cached module object immediately.
2. **Finders**: Searches through directories listed in `sys.path` in strict order:
   - Current working directory (or script directory).
   - `PYTHONPATH` environment variable directories.
   - Standard library directories.
   - `site-packages` (third-party pip installed libraries).
3. **Loaders**: Compiles the source into bytecode (`.pyc` in `__pycache__`), executes the module body top-to-bottom, and binds it to `sys.modules`.

```python
import sys

# Inspecting search paths:
for idx, path in enumerate(sys.path):
    print(f"{idx}: {path}")

# Programmatically injecting a path (use cautiously!):
# sys.path.insert(0, "/path/to/custom/libs")
```

---

## 📦 2. Packages, `__init__.py` & `__all__`

### The Role of `__init__.py`:
* Initializes package-level state and configures public exports.
* Controls what is exposed when a user runs `from package import *`.

```python
# package_a/__init__.py

from .module_one import clean_data, process_order

# __all__ limits what 'from package_a import *' imports:
__all__ = ["clean_data", "process_order"]
```

---

## 🔄 3. Absolute vs Relative Imports

* **Absolute Import** (Preferred): Specifies path from the project root.
  ```python
  from myproject.services.auth import verify_token
  ```
* **Relative Import**: Uses dot notation relative to current module location.
  ```python
  from . import sibling_module
  from ..core.config import DATABASE_URL
  ```

---

## 🚀 4. Understanding `if __name__ == '__main__':`

Every Python module has a built-in variable `__name__`:
* If executed directly from the terminal (`python script.py`), `__name__` is set to `"__main__"`.
* If imported into another file (`import script`), `__name__` is set to the module's file name (`"script"`).

```python
# math_utils.py

def add(a, b):
    return a + b

# Only executes when run directly as a script (e.g. for self-testing or CLI):
if __name__ == "__main__":
    print("Testing math_utils directly:")
    assert add(2, 3) == 5
    print("All tests passed! ✅")
```

---

## ⚡ 5. Circular Imports: Root Cause & Fixes

**The Problem**: Module A imports Module B, and Module B imports Module A at top-level. When Module A is executing its top-level lines, it halts to import Module B, which halts to import Module A, finding an incompletely initialized Module A object!

**The Solutions**:
1. **Refactor**: Extract shared logic or types into a third independent module `common.py` (Best Practice).
2. **Deferred / Inside-Function Import**: Move the import inside the specific function that uses it so it executes only when called.
3. **Type Hint Only Guard**: Use `typing.TYPE_CHECKING`:
   ```python
   from typing import TYPE_CHECKING
   if TYPE_CHECKING:
       from module_b import ClassB  # Evaluated by static linters/mypy only, not at runtime!
   ```

---

## 🌐 6. Virtual Environments & Modern Packaging

### Creating a Virtual Environment with `venv`:
```bash
# Create virtual environment in '.venv' folder
python -m venv .venv

# Activate on Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Activate on Linux/macOS:
source .venv/bin/activate

# Install dependencies:
pip install requests fastapi uvicorn

# Freeze dependencies:
pip freeze > requirements.txt

# Install from requirements:
pip install -r requirements.txt
```

---

## 🧠 Top Interview Questions

1. **Q: What is the purpose of `sys.modules` in Python?**
   * **A:** It is a dictionary acting as Python's global module cache. Any previously imported module is stored there. Subsequent imports simply retrieve the cached reference without re-executing the module code.

2. **Q: What is the difference between a Regular Package and a Namespace Package?**
   * **A:** A regular package contains an `__init__.py` file. A namespace package (PEP 420) does not require `__init__.py` and can span multiple directories across different physical locations on `sys.path`.

3. **Q: How does `__all__` influence imports?**
   * **A:** `__all__` is a list of string identifiers that specifies exactly which symbols are exported when a client uses wildcard import `from module import *`.

---

## 💻 Practice Exercises
1. **Exercise 1 (Modular CLI):** Create a mini 2-package project with a `core` package (utility math functions) and an `app` package (CLI interface) with proper `__init__.py` exports.
2. **Exercise 2 (Circular Import Debugging):** Intentionally construct a circular import scenario between two modules and resolve it using both a shared submodule refactoring and an in-function import.
