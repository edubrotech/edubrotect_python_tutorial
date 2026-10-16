# 📌 Advanced Topic 02: Dunder (Magic) Methods & Operator Overloading

## 📖 Introduction
**Dunder methods** (short for **D**ouble **Under**score, e.g., `__init__`) are special methods in Python that allow custom classes to integrate seamlessly with built-in language features such as operators (`+`, `-`, `==`), indexing (`obj[key]`), iteration (`for item in obj`), and string conversion (`str(obj)`).

---

## 🔑 1. String Representation: `__str__` vs `__repr__`

* `__str__`: Intended for **end-users** (readable, user-friendly).
* `__repr__`: Intended for **developers / debugging** (unambiguous; ideally valid Python code to recreate the object).

```python
class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author} (${self.price:.2f})"

    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, author={self.author!r}, price={self.price!r})"

b = Book("Fluent Python", "Luciano Ramalho", 49.99)
print(str(b))   # 'Fluent Python' by Luciano Ramalho ($49.99)
print(repr(b))  # Book(title='Fluent Python', author='Luciano Ramalho', price=49.99)
```

---

## 📦 2. Emulating Containers: Sequence & Mapping Dunders

Implement custom collections that behave like native lists or dictionaries:

```python
class CourseCatalog:
    def __init__(self):
        self._courses = []

    def add_course(self, name: str):
        self._courses.append(name)

    # Enables len(catalog)
    def __len__(self) -> int:
        return len(self._courses)

    # Enables catalog[index] and slicing
    def __getitem__(self, index):
        return self._courses[index]

    # Enables catalog[index] = new_value
    def __setitem__(self, index, value):
        self._courses[index] = value

    # Enables "Python" in catalog
    def __contains__(self, item) -> bool:
        return item in self._courses

catalog = CourseCatalog()
catalog.add_course("Python Basics")
catalog.add_course("Advanced Python")

print("Total Courses:", len(catalog))     # Calls __len__ -> 2
print("First Course:", catalog[0])         # Calls __getitem__ -> Python Basics
print("Found?", "Advanced Python" in catalog) # Calls __contains__ -> True
```

---

## ➕ 3. Operator Overloading (Arithmetic & Comparison)

Enable standard math and relational operators on your custom objects:

```python
class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Addition: v1 + v2
    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    # Multiplication: v * scalar
    def __mul__(self, scalar: float) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)

    # Equality: v1 == v2
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y

    # Less than: v1 < v2 (based on magnitude)
    def __lt__(self, other: 'Vector2D') -> bool:
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

v1 = Vector2D(2, 3)
v2 = Vector2D(4, 5)
v3 = v1 + v2     # Calls __add__ -> Vector2D(6, 8)
print("v1 + v2 =", v3)
print("v1 * 3  =", v1 * 3)  # Calls __mul__ -> Vector2D(6, 9)
print("v1 == v2:", v1 == v2) # Calls __eq__  -> False
```

---

## 🔒 4. Hashing Custom Objects: `__hash__` & `__eq__`
To make your custom class objects usable as **dictionary keys** or inside **sets**, you must implement both `__hash__` and `__eq__`, and the object should be immutable:

```python
class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self): return self._x
    @property
    def y(self): return self._y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(10, 20)
p2 = Point(10, 20)

point_set = {p1, p2}
print("Set Size:", len(point_set)) # Output: 1 (p1 and p2 considered identical!)
```

---

## ⚡ 5. Callable Objects: `__call__`
Enables an instance of a class to be invoked like a regular function:

```python
class RateLimiter:
    def __init__(self, max_requests: int):
        self.max_requests = max_requests
        self.current_count = 0

    def __call__(self, user: str) -> bool:
        if self.current_count >= self.max_requests:
            print(f"❌ Rate limit exceeded for {user}!")
            return False
        self.current_count += 1
        print(f"✅ Allowed request #{self.current_count} for {user}")
        return True

limiter = RateLimiter(max_requests=2)
limiter("Alice")  # Calls __call__ -> Allowed #1
limiter("Alice")  # Allowed #2
limiter("Alice")  # Rate limit exceeded!
```

---

## 🔄 6. Object Instantiation: `__new__` vs `__init__`
* `__new__(cls, *args, **kwargs)`: Responsible for **creating** the instance in memory. Returns the newly created object.
* `__init__(self, *args, **kwargs)`: Responsible for **initializing** attributes on the already-created instance.

```python
# Implementing the Singleton Pattern with __new__
class DatabaseSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating brand new singleton instance...")
            cls._instance = super().__new__(cls)
        return cls._instance

db1 = DatabaseSingleton()
db2 = DatabaseSingleton()
print(db1 is db2)  # Output: True (Both point to exact same instance!)
```

---

## 🧠 Top Interview Questions

1. **Q: What is the fallback if `__str__` is not defined in a class?**
   * **A:** Python falls back to `__repr__`. If neither is defined, it inherits `object.__repr__`, which outputs `<ClassName object at 0x...>`.

2. **Q: If a class overrides `__eq__`, why does Python set `__hash__ = None` by default?**
   * **A:** In Python, objects that compare equal must have equal hash values. If you override `__eq__`, Python can no longer guarantee the hash contract, so it disables hashing by default unless you explicitly implement `__hash__`.

3. **Q: What is the difference between `__new__` and `__init__`?**
   * **A:** `__new__` is the actual creator of the object (returns the instance, receives `cls`), while `__init__` is an initializer (returns nothing, receives `self`).

---

## 💻 Practice Exercises
1. **Exercise 1 (Fraction Class):** Create a `Fraction(numerator, denominator)` class that implements `__str__`, `__add__`, `__eq__`, and simplifies fractions using `math.gcd`.
2. **Exercise 2 (Smart List):** Create a custom class that wraps a list and allows negative indexing beyond the length by wrapping around circularly using `__getitem__`.
