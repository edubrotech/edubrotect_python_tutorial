# 📌 Advanced Topic 07: Descriptors & Metaclasses

## 📖 Introduction
Descriptors and metaclasses are Python's deepest metaprogramming features. They power production-grade frameworks like **Django ORM, SQLAlchemy, Pydantic, and FastAPI**, allowing developers to intercept attribute access and customize class creation.

---

## 🔑 1. The Descriptor Protocol

A **descriptor** is an object attribute with "binding behavior", whose attribute access is overridden by methods in the descriptor protocol:

* `__get__(self, instance, owner=None)`: Read attribute.
* `__set__(self, instance, value)`: Write attribute.
* `__delete__(self, instance)`: Delete attribute.
* `__set_name__(self, owner, name)`: (Python 3.6+) Captures the variable name automatically.

### Data vs Non-Data Descriptors:
* **Data Descriptor**: Implements both `__get__` and `__set__` (or `__delete__`). Has higher precedence than the instance's `__dict__`.
* **Non-Data Descriptor**: Implements only `__get__` (e.g., standard methods and `@staticmethod`). If an attribute exists in the instance's `__dict__`, it overrides the non-data descriptor.

---

## 🛠️ 2. Practical Descriptor: Type-Checked Field Validator

```python
class PositiveNumber:
    def __set_name__(self, owner, name):
        # Automatically receives attribute name (e.g., 'price' or 'stock')
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"Value must be a positive number! Received: {value}")
        setattr(instance, self.private_name, value)

class Product:
    # Descriptors defined at class level
    price = PositiveNumber()
    stock = PositiveNumber()

    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price   # Triggers PositiveNumber.__set__
        self.stock = stock   # Triggers PositiveNumber.__set__

p = Product("Laptop", 1200.0, 15)
print(f"Product: {p.name}, Price: ${p.price}, Stock: {p.stock}")

# p.price = -500  # Raises ValueError: Value must be a positive number!
```

---

## 🧬 3. Metaclasses: The Class of a Class

In Python, **classes are objects too**. A metaclass is the "blueprint" that creates class objects.
* By default, all classes are instances of the built-in metaclass `type`.

```python
# Everything is an object, and classes are instances of 'type':
class Sample: pass
print(type(Sample))      # <class 'type'>
print(isinstance(Sample, type))  # True
```

### Dynamic Class Creation with `type()`
Syntax: `type(class_name, tuple_of_bases, dict_of_attributes)`

```python
# Creating a class dynamically at runtime:
def speak(self):
    return f"Hello, I am {self.name}!"

DynamicUser = type("DynamicUser", (object,), {"name": "Anonymous", "speak": speak})

user = DynamicUser()
print(user.name)     # Anonymous
print(user.speak())  # Hello, I am Anonymous!
```

---

## 🏗️ 4. Creating a Custom Metaclass
A metaclass inherits from `type` and overrides `__new__` to intercept class creation:

```python
class RequireDocumentationMeta(type):
    """Metaclass that enforces every class to have a non-empty docstring!"""
    def __new__(mcs, name, bases, attrs):
        if "__doc__" not in attrs or not attrs["__doc__"] or not attrs["__doc__"].strip():
            raise TypeError(f"Class '{name}' must have a valid docstring!")

        # Enforce all method names to be lowercase (snake_case):
        for attr_name, attr_val in attrs.items():
            if callable(attr_val) and not attr_name.startswith("__"):
                if not attr_name.islower():
                    raise TypeError(f"Method '{attr_name}' in class '{name}' must be lowercase snake_case!")

        return super().__new__(mcs, name, bases, attrs)

# Valid class definition
class GoodService(metaclass=RequireDocumentationMeta):
    """This service handles payment operations."""
    def process_order(self):
        pass

# Invalid class definition (uncomment to see TypeError at definition time!)
# class BadService(metaclass=RequireDocumentationMeta):
#     def ProcessOrder(self): # Fails casing check!
#         pass
```

---

## 🌟 5. The Modern Alternative: `__init_subclass__`
In Python 3.6+, you can customize subclass creation without writing a full metaclass:

```python
class PluginBase:
    registry = {}

    def __init_subclass__(cls, plugin_name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if plugin_name:
            cls.registry[plugin_name] = cls
            print(f"🔌 Registered plugin: '{plugin_name}' -> {cls.__name__}")

class AudioPlugin(PluginBase, plugin_name="audio"):
    pass

class VideoPlugin(PluginBase, plugin_name="video"):
    pass

print("Loaded plugins:", PluginBase.registry)
```

---

## 🧠 Top Interview Questions

1. **Q: What is the attribute lookup order in Python when descriptors are present?**
   * **A:**
     1. Data Descriptor on the class.
     2. Instance `__dict__`.
     3. Non-Data Descriptor on the class.
     4. Class `__dict__` (normal class attributes).
     5. Base classes (MRO traversal).
     6. `__getattr__` fallback method.

2. **Q: When should you use a Metaclass vs `__init_subclass__`?**
   * **A:** Prefer `__init_subclass__` for simple subclass registration, validation, and configuration. Use a Metaclass only when you need deep customization of the class creation process (e.g. controlling attribute namespace via `__prepare__` or modifying class attributes before the class object exists).

---

## 💻 Practice Exercises
1. **Exercise 1 (StringLength Descriptor):** Write a descriptor `StringLength(min_len, max_len)` that validates that an assigned string's length is within bounds.
2. **Exercise 2 (Auto-Registering Metaclass):** Create a metaclass `AutoSerializerMeta` that automatically injects a `.to_dict()` method into any class that uses it.
