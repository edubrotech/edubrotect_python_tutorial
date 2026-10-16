# 📌 Structural Pattern 04: Decorator (Object-Oriented Pattern)

## 📖 Intent
> *"Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality."* — Gang of Four

While Python has native syntax support for function decorators (`@my_decorator`), the classic **GoF Decorator Pattern** is an object-oriented structural pattern using object wrapping and composition.

```
┌─────────────────────────────────┐
│         Coffee (ABC)            │
├─────────────────────────────────┤
│ + get_cost(): float             │
│ + get_description(): str        │
└────────────────▲────────────────┘
                 │
       ┌─────────┴─────────┐
       │                   │
┌──────┴──────┐    ┌───────┴───────────────┐
│ SimpleCoffee│    │ CoffeeDecorator (Base)│
└─────────────┘    ├───────────────────────┤
                   │ - _decorated: Coffee  │
                   └──────────▲────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
             ┌──────┴───────┐    ┌──────┴───────┐
             │ MilkDecorator│    │SugarDecorator│
             └──────────────┘    └──────────────┘
```

---

## 🛠️ Implementation in Python: Customizable Beverage Ordering

```python
from abc import ABC, abstractmethod

# 1. Component Interface
class Coffee(ABC):
    @abstractmethod
    def get_cost(self) -> float: pass

    @abstractmethod
    def get_description(self) -> str: pass

# 2. Concrete Component
class SimpleCoffee(Coffee):
    def get_cost(self) -> float:
        return 2.00

    def get_description(self) -> str:
        return "Plain Espresso"

# 3. Base Decorator (Maintains reference to wrapped Coffee component)
class CoffeeDecorator(Coffee):
    def __init__(self, decorated_coffee: Coffee):
        self._decorated = decorated_coffee

    def get_cost(self) -> float:
        return self._decorated.get_cost()

    def get_description(self) -> str:
        return self._decorated.get_description()

# 4. Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._decorated.get_cost() + 0.50

    def get_description(self) -> str:
        return self._decorated.get_description() + " + Steamed Milk"

class VanillaDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._decorated.get_cost() + 0.75

    def get_description(self) -> str:
        return self._decorated.get_description() + " + Madagascar Vanilla"

class WhippedCreamDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._decorated.get_cost() + 0.90

    def get_description(self) -> str:
        return self._decorated.get_description() + " + Whipped Cream"

# Dynamic Composition at Runtime:
my_coffee = SimpleCoffee()
print(f"Base: {my_coffee.get_description()} -> ${my_coffee.get_cost():.2f}")

# Wrap with Milk:
my_coffee = MilkDecorator(my_coffee)

# Wrap with Vanilla:
my_coffee = VanillaDecorator(my_coffee)

# Wrap with Whipped Cream:
my_coffee = WhippedCreamDecorator(my_coffee)

print(f"Final Order: {my_coffee.get_description()} -> ${my_coffee.get_cost():.2f}")
# Output: Plain Espresso + Steamed Milk + Madagascar Vanilla + Whipped Cream -> $4.15
```

---

## 🧠 Top Interview Questions

1. **Q: Why use the Decorator Pattern instead of subclassing?**
   * **A:** Subclassing is static (compile-time) and leads to a **class explosion** (e.g. `EspressoWithMilk`, `EspressoWithMilkAndSugar`, `EspressoWithVanillaAndSugar` -> $2^N$ subclasses). The Decorator pattern allows combinations to be composed dynamically at runtime using only $N$ decorator classes.
