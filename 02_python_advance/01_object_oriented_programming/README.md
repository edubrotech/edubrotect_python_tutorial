# 📌 Advanced Topic 01: Object-Oriented Programming (OOP) Deep Dive

## 📖 Introduction
Object-Oriented Programming (OOP) is a paradigm based on the concept of "objects" containing data (attributes) and code (methods). In Python, everything is an object (including functions, modules, and classes themselves).

```
┌────────────────────────────────────────────────────────┐
│                   CLASS: BankAccount                   │
├────────────────────────────────────────────────────────┤
│ Class Variables:    bank_name = "Global Reserve"       │
├────────────────────────────────────────────────────────┤
│ Instance Attributes: account_number, balance, owner    │
├────────────────────────────────────────────────────────┤
│ Methods:            deposit(), withdraw(), get_summary│
└────────────────────────────────────────────────────────┘
```

---

## 🔑 1. Classes, Objects & The Constructor

```python
class Student:
    # Class Variable (Shared across all instances!)
    school_name = "EduBroTech Academy"

    def __init__(self, name: str, roll_number: int):
        # Instance Variables (Unique to each instance!)
        self.name = name
        self.roll_number = roll_number

    def display_info(self):
        return f"Student: {self.name} (Roll #{self.roll_number}) at {self.school_name}"

s1 = Student("Rakesh", 101)
s2 = Student("Pooja", 102)

print(s1.display_info())
print(s2.display_info())
```

---

## ⚙️ 2. Instance vs Class vs Static Methods

| Method Type | Decorator | First Argument | Use Case |
|---|---|---|---|
| **Instance Method** | None | `self` | Manipulates instance state |
| **Class Method** | `@classmethod` | `cls` | Manipulates class state or factory / alternative constructors |
| **Static Method** | `@staticmethod` | None | Utility functions with no access to instance or class state |

```python
class User:
    total_users = 0

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        User.total_users += 1

    # Instance method
    def send_welcome_email(self):
        return f"Email sent to {self.email}"

    # Class method as an alternative constructor (Factory)
    @classmethod
    def from_csv_string(cls, csv_text: str):
        username, email = csv_text.split(",")
        return cls(username.strip(), email.strip())

    # Static method (utility)
    @staticmethod
    def is_valid_email(email: str) -> bool:
        return "@" in email and "." in email

# Creating user via standard constructor
u1 = User("rakesh", "rakesh@edubrotech.com")

# Creating user via classmethod factory
u2 = User.from_csv_string("priya, priya@example.com")

# Using staticmethod
print(User.is_valid_email("test@domain.com"))  # True
print(f"Total Users: {User.total_users}")       # 2
```

---

## 🛡️ 3. Encapsulation & `@property` (Getters/Setters)

Python does not have true `private` keywords, but uses conventions:
* `_name`: Protected (internal use convention; warning to developers).
* `__name`: Private (triggers **Name Mangling** to `_ClassName__name` to prevent accidental override).

```python
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self._department = "Engineering"
        self.__salary = salary  # Mangled to _Employee__salary

    @property
    def salary(self) -> float:
        """Getter for salary"""
        return self.__salary

    @salary.setter
    def salary(self, value: float):
        """Setter with validation"""
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        self.__salary = value

    @salary.deleter
    def salary(self):
        """Deleter"""
        print("Salary attribute deleted!")
        del self.__salary

emp = Employee("Rakesh", 85000.0)
print(emp.salary)       # Calls getter: 85000.0
emp.salary = 95000.0    # Calls setter
# emp.salary = -100     # Raises ValueError!
```

---

## 🧬 4. Inheritance & `super()`

```python
class Vehicle:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return f"{self.brand} {self.model} engine started."

class ElectricCar(Vehicle):
    def __init__(self, brand: str, model: str, battery_capacity_kwh: int):
        super().__init__(brand, model)  # Calls parent constructor cleanly
        self.battery_capacity_kwh = battery_capacity_kwh

    # Method Overriding & Extension
    def start_engine(self):
        base_message = super().start_engine()
        return f"{base_message} (Silent electric motor engaged! ⚡)"

tesla = ElectricCar("Tesla", "Model 3", 75)
print(tesla.start_engine())
```

---

## 🔀 5. Multiple Inheritance & Method Resolution Order (MRO)
Python uses the **C3 Linearization Algorithm** to determine the exact order in which base classes are searched:

```python
class A:
    def ping(self):
        print("Ping from A")

class B(A):
    def ping(self):
        print("Ping from B")

class C(A):
    def ping(self):
        print("Ping from C")

class D(B, C):
    pass

d = D()
d.ping()  # Output: Ping from B

# Inspecting MRO:
print([cls.__name__ for cls in D.mro()])
# Output: ['D', 'B', 'C', 'A', 'object']
```

---

## 🦆 6. Polymorphism & Duck Typing
*"If it walks like a duck and quacks like a duck, it's a duck."* Python doesn't require explicit interfaces for polymorphism:

```python
class PDFExporter:
    def export(self, data):
        return f"Exporting {data} as PDF document"

class CSVExporter:
    def export(self, data):
        return f"Exporting {data} as CSV spreadsheet"

def export_report(exporter, data):
    # Polymorphic call: accepts any object that implements .export()
    print(exporter.export(data))

export_report(PDFExporter(), "Sales Data")
export_report(CSVExporter(), "Sales Data")
```

---

## 🏛️ 7. Abstract Base Classes (`abc.ABC`)
Enforce contracts and prevent direct instantiation of incomplete base classes:

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Must be implemented by subclasses"""
        pass

    @abstractmethod
    def refund_payment(self, transaction_id: str) -> bool:
        pass

class StripePayment(PaymentGateway):
    def process_payment(self, amount: float) -> bool:
        print(f"Stripe charged: ${amount}")
        return True

    def refund_payment(self, transaction_id: str) -> bool:
        print(f"Stripe refunded txn: {transaction_id}")
        return True

# gateway = PaymentGateway() # TypeError: Can't instantiate abstract class!
stripe = StripePayment()
stripe.process_payment(99.0)
```

---

## 🧠 Top Interview Questions

1. **Q: What is Name Mangling in Python?**
   * **A:** Any identifier in a class prefixed with two leading underscores (e.g. `__salary`) is textually transformed by Python to `_ClassName__salary`. This prevents accidental collisions in derived subclasses.

2. **Q: What is the difference between `@classmethod` and `@staticmethod`?**
   * **A:** `@classmethod` receives the class object (`cls`) as its first argument and can access/modify class state. `@staticmethod` receives neither `self` nor `cls`; it behaves like an isolated plain function scoped inside the class namespace.

3. **Q: How does Python resolve the Diamond Problem in Multiple Inheritance?**
   * **A:** Python uses C3 Linearization to construct a deterministic Method Resolution Order (MRO). You can view the order via `Class.mro()` or `Class.__mro__`.

---

## 💻 Practice Exercises
1. **Exercise 1 (Bank Hierarchy):** Implement an abstract class `Account` with abstract methods `deposit()` and `withdraw()`, and concrete subclasses `SavingsAccount` (with interest calculation) and `CurrentAccount` (with overdraft limit).
2. **Exercise 2 (MRO Analysis):** Create a diamond inheritance hierarchy and print `mro()`, demonstrating how `super()` calls traverse cooperative inheritance.
