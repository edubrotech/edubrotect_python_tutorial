# 🐍 EduBroTech Python Tutorial: From Zero to Hero (Basic to Advanced)

A structured, production-grade Python learning and reference repository designed to explain **Python functions, concepts, syntax, best practices, internal mechanics, and real-world architectures** in a simple, practical, and interview-focused way.

Whether you are watching the **YouTube video series**, preparing for technical interviews, or architecting backend services, this repository serves as your ultimate companion.

---

## 🎯 Repository Goals

* 📚 **Clear Explanations**: Function-by-function and concept-by-concept deep dives.
* 💡 **Runnable Code**: Practical, clean, tested examples with outputs.
* 🧠 **Interview Mastery**: Real questions, tricky outputs, and answers asked by top tech firms.
* ⚡ **Performance & Internals**: CPython memory architecture, reference counting, GIL, and `__slots__`.
* ⚠️ **Pitfall Prevention**: Common anti-patterns, beginner bugs, and idiomatic fixes.
* 📹 **YouTube Creator Ready**: Outlines, teaching points, and exercises tailored for video tutorials.

---

## 🗺️ Master Curriculum & Interactive Navigation

```
                               ┌─────────────────────────────┐
                               │     🐍 Python Learning      │
                               │           Roadmap           │
                               └──────────────┬──────────────┘
                                              │
                      ┌───────────────────────┴───────────────────────┐
                      ▼                                               ▼
          ┌────────────────────────┐                     ┌────────────────────────┐
          │   01. PYTHON BASICS    │                     │   02. PYTHON ADVANCE   │
          │  Foundations & Syntax  │                     │  OOP, Concurrency & GC │
          └────────────────────────┘                     └────────────────────────┘
```

---

### 🟢 [Part 1: Python Basics (`01_python_basic/`)](./01_python_basic/)

| # | Topic Name | Folder Link | Key Highlights |
|---|---|---|---|
| 01 | **Variables & Data Types** | [📂 `01_variables_and_data_types`](./01_python_basic/01_variables_and_data_types/) | Dynamic typing, primitive types, memory address (`id`), small integer caching, truthy/falsy |
| 02 | **Operators & Expressions** | [📂 `02_operators_and_expressions`](./01_python_basic/02_operators_and_expressions/) | Arithmetic, floor division (`//`), chained comparisons, logical short-circuiting, `is` vs `==`, bitwise |
| 03 | **Control Flow & Loops** | [📂 `03_control_flow`](./01_python_basic/03_control_flow/) | `if-elif-else`, ternary expressions, `match-case` (3.10+), `for`, `while`, loop `else` clause |
| 04 | **Strings & Formatting** | [📂 `04_strings_and_formatting`](./01_python_basic/04_strings_and_formatting/) | Slicing `[start:stop:step]`, immutability, string methods, modern f-strings, alignment, raw strings |
| 05 | **Type Casting & Console I/O** | [📂 `05_type_casting_and_io`](./01_python_basic/05_type_casting_and_io/) | Implicit vs explicit casting, `input()` handling, `print()` parameters (`sep`, `end`, `flush`) |
| 06 | **Functions & Variable Scope** | [📂 `06_functions`](./01_python_basic/06_functions/) | `def`, positional vs keyword, `*args`, `**kwargs`, LEGB scope rule, lambda, mutable default trap |
| 07 | **Basic Data Structures** | [📂 `07_basic_data_structures`](./01_python_basic/07_basic_data_structures/) | Lists, Tuples, Sets, Dictionaries, mutability, hashability, Big-O lookup comparison |
| 08 | **File Handling & Serialization** | [📂 `08_file_handling`](./01_python_basic/08_file_handling/) | Modes (`r`, `w`, `a`), `with` statement, line iteration, JSON & CSV serialization, `pathlib` |
| 09 | **Exception Handling** | [📂 `09_exception_handling`](./01_python_basic/09_exception_handling/) | `try-except-else-finally`, exception hierarchy, `raise ... from`, creating custom exceptions |

---

### 🚀 [Part 2: Python Advance (`02_python_advance/`)](./02_python_advance/)

| # | Topic Name | Folder Link | Key Highlights |
|---|---|---|---|
| 01 | **Object-Oriented Programming (OOP)** | [📂 `01_object_oriented_programming`](./02_python_advance/01_object_oriented_programming/) | Classes, `@classmethod`, `@staticmethod`, `@property`, inheritance, MRO, polymorphism, `abc.ABC` |
| 02 | **Dunder (Magic) Methods** | [📂 `02_dunder_and_magic_methods`](./02_python_advance/02_dunder_and_magic_methods/) | `__str__` vs `__repr__`, container dunders, operator overloading, `__call__`, `__new__` vs `__init__` |
| 03 | **Comprehensions & GenExpr** | [📂 `03_comprehensions`](./02_python_advance/03_comprehensions/) | List, Dict, Set comprehensions, generator expressions, `LIST_APPEND` bytecode speedup |
| 04 | **Iterators & Generators** | [📂 `04_iterators_and_generators`](./02_python_advance/04_iterators_and_generators/) | Iterator protocol (`__iter__`, `__next__`), `yield`, `yield from`, `.send()`, streaming pipelines |
| 05 | **Closures & Decorators** | [📂 `05_closures_and_decorators`](./02_python_advance/05_closures_and_decorators/) | Free variables, `@functools.wraps`, decorators with arguments, class decorators, caching & retry |
| 06 | **Context Managers** | [📂 `06_context_managers`](./02_python_advance/06_context_managers/) | Context protocol (`__enter__`, `__exit__`), exception suppression, `@contextmanager`, `ExitStack` |
| 07 | **Descriptors & Metaclasses** | [📂 `07_descriptors_and_metaclasses`](./02_python_advance/07_descriptors_and_metaclasses/) | Descriptors (`__get__`, `__set__`), dynamic classes with `type()`, custom metaclasses, `__init_subclass__` |
| 08 | **Slots & Memory Management** | [📂 `08_slots_and_memory_management`](./02_python_advance/08_slots_and_memory_management/) | `__slots__` 60%+ RAM savings, reference counting, cyclical GC (`gc` module), `weakref` |
| 09 | **Advanced Data Structures** | [📂 `09_advanced_data_structures`](./02_python_advance/09_advanced_data_structures/) | `collections` (`Counter`, `defaultdict`, `deque`, `namedtuple`), `heapq`, Stack, Linked List, BST |
| 10 | **Modules, Packages & Env** | [📂 `10_modules_packages_and_env`](./02_python_advance/10_modules_packages_and_env/) | `sys.path`, `__init__.py`, `__all__`, circular import fixes, `venv`, pip, `pyproject.toml` |
| 11 | **Concurrency & Parallelism** | [📂 `11_concurrency_and_parallelism`](./02_python_advance/11_concurrency_and_parallelism/) | GIL mechanics, Threading vs Multiprocessing vs AsyncIO, Event Loop, `TaskGroup` (3.11+) |
| 12 | **Testing, Debugging & Quality** | [📂 `12_testing_debugging_and_best_practices`](./02_python_advance/12_testing_debugging_and_best_practices/) | `pytest` fixtures, mocking external APIs, structured logging, `pdb` debugging, `mypy` typing |
| 13 | **Interview Questions & Projects** | [📂 `13_interview_questions_and_projects`](./02_python_advance/13_interview_questions_and_projects/) | Top 50 Interview Q&A, tricky outputs, 3 YouTube tutorial hands-on project architectures |

---

## 💻 How to Use This Repository

### 1. Clone the Repository
```bash
git clone https://github.com/edubrotech/edubrotect_python_tutorial.git
cd edubrotect_python_tutorial
```

### 2. Set Up a Clean Virtual Environment
```bash
python -m venv .venv

# On Windows:
.venv\Scripts\Activate.ps1

# On Linux / macOS:
source .venv/bin/activate
```

### 3. Navigate & Practice
Each folder contains a self-contained `README.md` with:
1. Conceptual theory & diagrams.
2. Complete runnable code snippets.
3. Common mistakes and pitfalls to avoid.
4. Top interview questions and answers.
5. Practice challenges with exercises.

---

## 🌟 Channel & Community
Created for **EduBroTech** YouTube programming tutorials. Happy Coding! 🚀
