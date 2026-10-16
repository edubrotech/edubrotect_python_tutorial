# 📌 SOLID 02: Open/Closed Principle (OCP)

## 📖 Definition
> *"Software entities (classes, modules, functions) should be open for extension, but closed for modification."* — Bertrand Meyer

You should be able to **add new features or behaviors** to a system without modifying existing, tested, and deployed source code.

---

## ❌ Violation Example: The Cascading `if-elif` Ladder

```python
# 🚨 VIOLATION OF OCP:
class PaymentProcessor:
    def process_payment(self, payment_type: str, amount: float):
        if payment_type == "credit_card":
            print(f"Charging ${amount} via Credit Card Gateway...")
        elif payment_type == "paypal":
            print(f"Redirecting to PayPal for ${amount}...")
        elif payment_type == "upi":
            print(f"Generating UPI QR Code for INR {amount}...")
        else:
            raise ValueError(f"Unsupported payment type: {payment_type}")

# ⚠️ Every time the business wants to add ApplePay, Crypto, or Razorpay:
# 1. We MUST modify PaymentProcessor.
# 2. We risk introducing regressions in CreditCard or PayPal!
# 3. We violate OCP!
```

---

## ✅ Refactored Pythonic Solution: Polymorphic Extension

Use an Abstract Base Class (`abc.ABC`) to define a common interface. New payment methods **extend** the system as new classes without modifying existing ones:

```python
from abc import ABC, abstractmethod

# 1. Open interface: Defines contract
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        """Process transaction. Must be implemented by concrete providers."""
        pass

# 2. Existing concrete implementations:
class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float) -> bool:
        print(f"💳 Charging ${amount:.2f} to Card ending in {self.card_number[-4:]}")
        return True

class PayPalPayment(PaymentMethod):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> bool:
        print(f"🅿️ Routing ${amount:.2f} payment through PayPal account: {self.email}")
        return True

class UPIPayment(PaymentMethod):
    def __init__(self, vpa_id: str):
        self.vpa_id = vpa_id

    def pay(self, amount: float) -> bool:
        print(f"📱 Processing UPI transfer of INR {amount:.2f} via VPA: {self.vpa_id}")
        return True

# 3. Processor: CLOSED for modification! It never needs to change!
class PaymentProcessor:
    def execute_transaction(self, method: PaymentMethod, amount: float):
        print("Initiating transaction...")
        success = method.pay(amount)
        if success:
            print("Transaction complete! Receipt dispatched. ✅\n")

# 4. EXTENSION: Adding Crypto payment without changing a single line above!
class CryptoPayment(PaymentMethod):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> bool:
        print(f"₿ Transferring crypto equivalent of ${amount:.2f} to {self.wallet_address}")
        return True

# Usage:
processor = PaymentProcessor()
processor.execute_transaction(CreditCardPayment("4111222233334444"), 150.00)
processor.execute_transaction(CryptoPayment("0x71C...38A"), 500.00)
```

---

## 🎯 Advantages of OCP
1. **Zero Regression Risk**: Adding new features will not break existing, tested business code.
2. **Pluggable Architecture**: New plugins or strategies can be added dynamically at runtime.

---

## 🧠 Top Interview Questions

1. **Q: How is OCP achieved in object-oriented programming?**
   * **A:** Primarily through **Abstraction, Inheritance, and Polymorphism** (or Composition with Strategy Pattern). By depending on abstract interfaces rather than concrete implementations, new behaviors are added by supplying new subclasses or callables without touching existing caller code.

2. **Q: Does OCP mean code should never be modified?**
   * **A:** No. If there is a bug or requirement change in existing logic, of course you modify the existing code. OCP specifically applies to adding *new features or behaviors*.
