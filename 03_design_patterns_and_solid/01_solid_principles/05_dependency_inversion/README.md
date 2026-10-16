# 📌 SOLID 05: Dependency Inversion Principle (DIP)

## 📖 Definition
> *1. High-level modules should not depend upon low-level modules. Both should depend on abstractions.*  
> *2. Abstractions should not depend upon details. Details should depend on abstractions.* — Robert C. Martin

In traditional software design, high-level policy components directly instantiate and depend on low-level utility components (like database drivers, disk I/O, or third-party APIs). DIP **inverts this relationship** using interfaces or abstractions.

```
TRADITIONAL COUPLING (Bad):
[ High-Level: OrderService ] ─────────> [ Low-Level: MySQLDatabase ]
(Direct dependency on concrete implementation)

DEPENDENCY INVERSION (Good):
[ High-Level: OrderService ] ─────────> [ Abstraction: DatabaseInterface ]
                                                       ▲
                                                       │
                                        [ Low-Level: MySQLDatabase ]
```

---

## ❌ Violation Example: Direct Hardcoded Dependencies

```python
# 🚨 VIOLATION OF DIP:
class MySQLDatabase:
    def insert(self, record):
        print(f"Executing SQL: INSERT INTO orders VALUES ({record});")

class TwilioSMS:
    def send_sms(self, phone, msg):
        print(f"Dispatching SMS to {phone} via Twilio Gateway: {msg}")

class OrderService:
    def __init__(self):
        # HARDCODED CONCRETIONS! High-level OrderService is coupled to MySQL and Twilio!
        self.db = MySQLDatabase()
        self.notifier = TwilioSMS()

    def create_order(self, order_id: str, phone: str):
        # Business logic:
        self.db.insert(order_id)
        self.notifier.send_sms(phone, f"Order {order_id} confirmed!")

# Problems:
# 1. Impossible to unit test OrderService without spinning up MySQL and hitting Twilio API!
# 2. Cannot switch to MongoDB or Slack without modifying OrderService source code.
```

---

## ✅ Refactored Pythonic Solution: Dependency Injection

Define abstractions (`ABC`), and inject concrete dependencies through the constructor:

```python
from abc import ABC, abstractmethod

# 1. Abstractions (Contracts)
class Database(ABC):
    @abstractmethod
    def save(self, data: dict) -> None: pass

class NotificationSender(ABC):
    @abstractmethod
    def notify(self, recipient: str, message: str) -> None: pass

# 2. Low-level concrete implementations
class PostgresDatabase(Database):
    def save(self, data: dict) -> None:
        print(f"🐘 PostgreSQL: Stored order {data['id']}")

class MongoDatabase(Database):
    def save(self, data: dict) -> None:
        print(f"🍃 MongoDB: Inserted document {data['id']}")

class EmailNotification(NotificationSender):
    def notify(self, recipient: str, message: str) -> None:
        print(f"📧 Email dispatched to {recipient}: {message}")

class SlackNotification(NotificationSender):
    def notify(self, recipient: str, message: str) -> None:
        print(f"💬 Slack alert sent to #{recipient}: {message}")

# 3. High-level module depends ONLY on abstractions
class OrderService:
    def __init__(self, db: Database, notifier: NotificationSender):
        # Dependencies INJECTED via constructor
        self.db = db
        self.notifier = notifier

    def checkout(self, order_id: str, customer_contact: str):
        order_data = {"id": order_id, "status": "CONFIRMED"}
        self.db.save(order_data)
        self.notifier.notify(customer_contact, f"Your order {order_id} has been placed!")

# Usage in Production:
prod_service = OrderService(db=PostgresDatabase(), notifier=EmailNotification())
prod_service.checkout("ORD-9021", "rakesh@edubrotech.com")

# Usage in Testing (Zero network or DB overhead!):
class MockDatabase(Database):
    def __init__(self): self.saved = []
    def save(self, data): self.saved.append(data)

class MockNotifier(NotificationSender):
    def __init__(self): self.messages = []
    def notify(self, recipient, message): self.messages.append((recipient, message))

def test_order_checkout():
    mock_db = MockDatabase()
    mock_notifier = MockNotifier()
    test_service = OrderService(db=mock_db, notifier=mock_notifier)

    test_service.checkout("TEST-01", "test@test.com")
    assert len(mock_db.saved) == 1
    assert mock_notifier.messages[0][1] == "Your order TEST-01 has been placed!"
    print("Test passed with 100% test isolation! ✅")

test_order_checkout()
```

---

## ⚡ DIP in Modern Python: FastAPI Dependency Injection
Modern frameworks like **FastAPI** implement DIP natively using `Depends`:

```python
# FastAPI architectural pattern
# from fastapi import Depends, FastAPI

# def get_db_session() -> Database:
#     return PostgresDatabase()

# @app.post("/orders")
# def create_order(db: Database = Depends(get_db_session)):
#     db.save(...)
```

---

## 🧠 Top Interview Questions

1. **Q: What is the difference between Inversion of Control (IoC), Dependency Inversion (DIP), and Dependency Injection (DI)?**
   * **A:**
     * **DIP** is the high-level **architectural design principle** (depend on abstractions).
     * **IoC** is a broad **paradigm** where the framework controls the program flow rather than custom code.
     * **DI** is a concrete **design pattern and implementation technique** used to supply dependencies to an object from the outside (via constructor or method arguments).

2. **Q: How does DIP make code more testable?**
   * **A:** By decoupling high-level services from concrete databases, file systems, or network endpoints, you can effortlessly inject fast, memory-only Mock objects during automated unit testing without needing live external infrastructure.
