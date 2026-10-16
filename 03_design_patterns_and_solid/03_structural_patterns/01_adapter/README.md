# 📌 Structural Pattern 01: Adapter

## 📖 Intent
> *"Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces."* — Gang of Four

The Adapter acts as a translator or bridge between two incompatible APIs (e.g., converting legacy XML responses to modern JSON payloads).

```
┌─────────────────┐           ┌───────────────────┐           ┌───────────────────┐
│     Client      │ ───────>  │  Adapter (Wrapper)│ ───────>  │ Adaptee (Legacy)  │
│ Expects: JSON   │           │ Translates JSON   │           │ Expects: XML      │
└─────────────────┘           └───────────────────┘           └───────────────────┘
```

---

## 🛠️ Implementation in Python: Modernizing Legacy Payment Gateway

```python
from abc import ABC, abstractmethod

# 1. Target Interface expected by our modern application:
class ModernPaymentGateway(ABC):
    @abstractmethod
    def charge(self, user_id: str, amount_usd: float) -> dict:
        pass

# 2. Incompatible Adaptee (Old legacy 3rd-party banking library):
class LegacyBankSDK:
    def execute_wire_transfer(self, account_no: int, cents: int) -> str:
        # Incompatible signatures and units (expects integer cents, not USD float!)
        print(f"🏦 Legacy Bank: Transferred {cents} cents to account #{account_no}")
        return "SUCCESS_CODE_200"

# 3. The Adapter: Bridges ModernPaymentGateway to LegacyBankSDK
class BankSDKAdapter(ModernPaymentGateway):
    def __init__(self, legacy_sdk: LegacyBankSDK):
        self.legacy_sdk = legacy_sdk

    def charge(self, user_id: str, amount_usd: float) -> dict:
        # Translate modern parameters to legacy expectations:
        account_no = int(user_id.replace("USR-", ""))
        cents = int(amount_usd * 100)

        # Delegate to adaptee:
        status = self.legacy_sdk.execute_wire_transfer(account_no, cents)

        # Translate response back to client expectations:
        return {
            "status": "APPROVED" if status == "SUCCESS_CODE_200" else "FAILED",
            "amount_charged": amount_usd
        }

# 4. Client Code: Only interacts with ModernPaymentGateway
def process_customer_checkout(gateway: ModernPaymentGateway):
    result = gateway.charge("USR-98421", 49.99)
    print("Checkout Result:", result)

legacy_engine = LegacyBankSDK()
adapter = BankSDKAdapter(legacy_engine)
process_customer_checkout(adapter)
```

---

## 🧠 Top Interview Questions

1. **Q: What is the difference between an Object Adapter and a Class Adapter?**
   * **A:**
     * **Object Adapter**: Uses **Composition** (stores a reference to the adaptee instance inside `self.adaptee`). Highly flexible and works with any subclass of Adaptee.
     * **Class Adapter**: Uses **Multiple Inheritance** (subclasses both Target and Adaptee). Less common in Python because it couples the adapter to specific class hierarchies.
