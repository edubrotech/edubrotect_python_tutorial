# 📌 Behavioral Pattern 01: Strategy

## 📖 Intent
> *"Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it."* — Gang of Four

```
┌────────────────────────────────┐            ┌────────────────────────────────┐
│      OrderContext              │            │     DiscountStrategy (ABC)     │
├────────────────────────────────┤ ─────────> ├────────────────────────────────┤
│ - strategy: DiscountStrategy   │            │ + calculate(total): float      │
│ + calculate_final_bill(): float│            └───────────────▲────────────────┘
└────────────────────────────────┘                            │
                                             ┌────────────────┴────────────────┐
                                      ┌──────┴──────┐                   ┌──────┴──────┐
                                      │ VIPDiscount │                   │FlashDiscount│
                                      └─────────────┘                   └─────────────┘
```

---

## 🛠️ Implementation in Python

### 1. The Classic OOP Strategy Pattern
```python
from abc import ABC, abstractmethod

# 1. Strategy Interface
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total_amount: float) -> float:
        pass

# 2. Concrete Strategies
class RegularCustomerDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total * 0.95  # 5% off

class VIPCustomerDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total * 0.80  # 20% off

class FestiveSeasonDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total * 0.70  # 30% off

# 3. Context
class ShoppingCart:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy
        self.items = []

    def add_item(self, price: float):
        self.items.append(price)

    def checkout(self) -> float:
        raw_total = sum(self.items)
        final_bill = self.strategy.apply_discount(raw_total)
        print(f"Subtotal: ${raw_total:.2f} -> Discounted Total: ${final_bill:.2f}")
        return final_bill

# Changing strategy dynamically at runtime:
cart = ShoppingCart(strategy=RegularCustomerDiscount())
cart.add_item(100.0)
cart.checkout()

# Switch strategy dynamically:
cart.strategy = VIPCustomerDiscount()
cart.checkout()
```

---

## 🐍 2. The Pythonic Strategy: First-Class Functions
In Python, because **functions are first-class citizens**, you often don't need a formal abstract class hierarchy for strategies! A simple `Callable` works wonders:

```python
from typing import Callable

# Strategies defined as simple functions:
def regular_discount(total: float) -> float:
    return total * 0.95

def vip_discount(total: float) -> float:
    return total * 0.80

class PythonicCart:
    def __init__(self, discount_fn: Callable[[float], float] = lambda x: x):
        self.discount_fn = discount_fn
        self.total = 100.0

    def get_final_total(self) -> float:
        return self.discount_fn(self.total)

cart = PythonicCart(vip_discount)
print("Pythonic Strategy Bill:", cart.get_final_total())  # $80.0
```

---

## 🧠 Top Interview Questions

1. **Q: How does Python simplify the Gang of Four Strategy Pattern?**
   * **A:** In languages like Java or C++, a strategy requires declaring an `interface` and instantiating multiple concrete classes. In Python, any function or lambda can act as a strategy, allowing the context to simply store a function reference.
