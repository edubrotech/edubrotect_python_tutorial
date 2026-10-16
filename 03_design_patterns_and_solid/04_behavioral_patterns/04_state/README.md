# 📌 Behavioral Pattern 04: State

## 📖 Intent
> *"Allow an object to alter its behavior when its internal state changes. The object will appear to change its class."* — Gang of Four

The State pattern is the object-oriented implementation of a **Finite State Machine (FSM)**. It cleans up massive, fragile `if-elif-else` conditionals that check status flags before every action.

```
                  ┌─────────────────────────────────────────┐
                  │                 Context                 │
                  │              (OrderObject)              │
                  ├─────────────────────────────────────────┤
                  │ - state: OrderState                     │
                  │ + set_state(state): void                │
                  │ + pay(): void                           │
                  │ + ship(): void                          │
                  └────────────────────┬────────────────────┘
                                       │ delegates to current state
                                       ▼
                  ┌─────────────────────────────────────────┐
                  │            OrderState (ABC)             │
                  ├─────────────────────────────────────────┤
                  │ + pay(order): void                      │
                  │ + ship(order): void                     │
                  │ + cancel(order): void                   │
                  └──────┬─────────────┼─────────────┬──────┘
                         │             │             │
        ┌────────────────▼───┐  ┌──────▼──────┐  ┌───▼────────────────┐
        │    PendingState    │  │  PaidState  │  │    ShippedState    │
        └────────────────────┘  └─────────────┘  └────────────────────┘
```

---

## 🛠️ Implementation in Python: E-Commerce Order Lifecycle

```python
from abc import ABC, abstractmethod

# Forward reference
class Order: pass

# 1. State Interface
class OrderState(ABC):
    @abstractmethod
    def pay(self, order: 'Order') -> None: pass

    @abstractmethod
    def ship(self, order: 'Order') -> None: pass

    @abstractmethod
    def cancel(self, order: 'Order') -> None: pass

# 2. Concrete States
class PendingState(OrderState):
    def pay(self, order: 'Order'):
        print("💳 Payment accepted! Transitioning to PAID state.")
        order.set_state(PaidState())

    def ship(self, order: 'Order'):
        print("❌ Cannot ship: Order has not been paid yet!")

    def cancel(self, order: 'Order'):
        print("🛑 Order canceled by customer.")
        order.set_state(CanceledState())

class PaidState(OrderState):
    def pay(self, order: 'Order'):
        print("⚠️ Order is already paid!")

    def ship(self, order: 'Order'):
        print("🚚 Package dispatched to logistics courier! Transitioning to SHIPPED.")
        order.set_state(ShippedState())

    def cancel(self, order: 'Order'):
        print("💸 Payment refunded. Order canceled.")
        order.set_state(CanceledState())

class ShippedState(OrderState):
    def pay(self, order: 'Order'):
        print("⚠️ Order is already paid and in transit!")

    def ship(self, order: 'Order'):
        print("⚠️ Package is already on its way!")

    def cancel(self, order: 'Order'):
        print("❌ Cannot cancel order that is already in transit with courier!")

class CanceledState(OrderState):
    def pay(self, order): print("❌ Cannot pay for a canceled order.")
    def ship(self, order): print("❌ Cannot ship a canceled order.")
    def cancel(self, order): print("⚠️ Order is already canceled.")

# 3. Context
class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self._state: OrderState = PendingState() # Initial state

    def set_state(self, new_state: OrderState):
        self._state = new_state

    # Delegating behaviors directly to the active state:
    def pay(self): self._state.pay(self)
    def ship(self): self._state.ship(self)
    def cancel(self): self._state.cancel(self)

# Simulation:
order = Order("ORD-5501")

order.ship()    # ❌ Cannot ship: Order has not been paid yet!
order.pay()     # 💳 Payment accepted! Transitioning to PAID state.
order.ship()    # 🚚 Package dispatched to logistics courier! Transitioning to SHIPPED.
order.cancel()  # ❌ Cannot cancel order that is already in transit with courier!
```

---

## 🧠 Top Interview Questions

1. **Q: What is the difference between Strategy Pattern and State Pattern?**
   * **A:**
     * **Strategy Pattern**: The client actively chooses which strategy algorithm to use; strategies typically don't know about each other.
     * **State Pattern**: The states automatically trigger transitions between each other based on incoming actions, modifying the context's internal behavior transparently.
