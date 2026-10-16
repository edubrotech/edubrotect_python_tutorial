# 📌 SOLID 03: Liskov Substitution Principle (LSP)

## 📖 Definition
> *"If $S$ is a subtype of $T$, then objects of type $T$ may be replaced with objects of type $S$ without altering any of the desirable properties of the program (correctness, task performed, etc.)."* — Barbara Liskov

A derived subclass must be completely substitutable for its base class without breaking client expectations or raising unexpected exceptions.

---

## ❌ Violation 1: The Classic Square-Rectangle Problem

In mathematics, a square is a rectangle. But in object-oriented programming, modeling a Square as a subclass of a Rectangle violates LSP:

```python
# 🚨 VIOLATION OF LSP:
class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    @property
    def width(self): return self._width
    @width.setter
    def width(self, val): self._width = val

    @property
    def height(self): return self._height
    @height.setter
    def height(self, val): self._height = val

    def get_area(self) -> float:
        return self._width * self._height

class Square(Rectangle):
    # Overriding setters to keep sides equal:
    @Rectangle.width.setter
    def width(self, val):
        self._width = val
        self._height = val

    @Rectangle.height.setter
    def height(self, val):
        self._width = val
        self._height = val

# Client function expecting standard Rectangle behavior:
def resize_and_verify(rect: Rectangle):
    rect.width = 10
    rect.height = 5
    # For ANY genuine rectangle, area should be 10 * 5 = 50:
    assert rect.get_area() == 50, f"Expected 50, but got {rect.get_area()}!"

# Works for Rectangle:
resize_and_verify(Rectangle(2, 3))  # Passes!

# FAILS for Square:
# resize_and_verify(Square(2, 2))   # AssertionError: Expected 50, but got 25!
# Square CANNOT substitute for Rectangle!
```

---

## ❌ Violation 2: The Ostrich / Flying Bird Problem

```python
# 🚨 VIOLATION OF LSP:
class Bird:
    def fly(self):
        print("Flying high in the sky!")

class Ostrich(Bird):
    def fly(self):
        # Breaks contract by raising an error for an expected method!
        raise NotImplementedError("Ostriches cannot fly!")

def make_bird_fly(bird: Bird):
    bird.fly() # Crashes if passed an Ostrich!
```

---

## ✅ Refactored Solution: Correct Hierarchy & Abstraction

Separate contracts so subtypes never inherit methods they cannot legitimately fulfill:

```python
from abc import ABC, abstractmethod

# Common abstraction for all birds
class Bird(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def move(self):
        pass

# Specialized capability interfaces / base classes
class FlyingBird(Bird):
    def move(self):
        print(f"{self.name} is flying through the air! 🦅")

class FlightlessBird(Bird):
    def move(self):
        print(f"{self.name} is running swiftly across the ground! 🪶")

# Concrete implementations:
class Eagle(FlyingBird): pass
class Ostrich(FlightlessBird): pass

def let_birds_move(birds: list[Bird]):
    for bird in birds:
        # Guaranteed safe substitution: every bird knows how to move()!
        bird.move()

let_birds_move([Eagle("Bald Eagle"), Ostrich("African Ostrich")])
```

---

## 📋 Rules of Thumb for LSP
1. **Never throw unexpected exceptions** in subclass methods (e.g., `raise NotImplementedError` in an overridden method is a red flag of an LSP violation).
2. **Preconditions cannot be strengthened** in a subtype (a subclass cannot demand stricter validation than the parent).
3. **Postconditions cannot be weakened** in a subtype (a subclass must return at least what the parent promised).

---

## 🧠 Top Interview Questions

1. **Q: Why is "A Square IS-A Rectangle" considered an OOP antipattern?**
   * **A:** While mathematically true, behavioral contracts differ. A Rectangle has independent degrees of freedom for width and height; a Square forces coupling between them. A client mutating width on a Rectangle assumes height is unchanged; substituting a Square breaks this invariant.

2. **Q: What is the relationship between LSP and Polymorphism?**
   * **A:** Polymorphism allows a variable of a parent type to hold an instance of a child type. LSP ensures that doing so is **semantically safe** and doesn't introduce hidden bugs or crash the application.
