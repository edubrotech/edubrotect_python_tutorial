# 📌 SOLID 04: Interface Segregation Principle (ISP)

## 📖 Definition
> *"Clients should not be forced to depend upon interfaces that they do not use."* — Robert C. Martin

Avoid "fat", bloated interfaces that combine multiple distinct concerns. It is better to have many small, client-specific interfaces than one massive general-purpose interface.

---

## ❌ Violation Example: The Bloated "All-in-One" Machine Interface

```python
from abc import ABC, abstractmethod

# 🚨 VIOLATION OF ISP:
class SmartMachine(ABC):
    @abstractmethod
    def print_document(self, doc): pass

    @abstractmethod
    def scan_document(self, doc): pass

    @abstractmethod
    def fax_document(self, doc): pass

    @abstractmethod
    def staple_document(self, doc): pass

# A modern office enterprise copier can do all 4:
class EnterpriseCopier(SmartMachine):
    def print_document(self, doc): print("Printing document...")
    def scan_document(self, doc): print("Scanning document...")
    def fax_document(self, doc): print("Faxing document...")
    def staple_document(self, doc): print("Stapling document...")

# A cheap desk printer CANNOT scan, fax, or staple!
class CheapDeskPrinter(SmartMachine):
    def print_document(self, doc):
        print("Printing document...")

    def scan_document(self, doc):
        # Forced to implement method it does not support!
        raise NotImplementedError("This device cannot scan!")

    def fax_document(self, doc):
        raise NotImplementedError("This device cannot fax!")

    def staple_document(self, doc):
        pass # Empty dummy method
```

---

## ✅ Refactored Pythonic Solution: Granular Role Interfaces

Split the bloated interface into atomic role-based interfaces (or Protocols):

```python
from abc import ABC, abstractmethod

# 1. Granular Role Interfaces:
class Printer(ABC):
    @abstractmethod
    def print_document(self, doc: str): pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self, doc: str) -> str: pass

class FaxMachine(ABC):
    @abstractmethod
    def fax_document(self, doc: str, number: str): pass

# 2. Cheap printer only implements Printer:
class CheapDeskPrinter(Printer):
    def print_document(self, doc: str):
        print(f"🖨️ CheapDeskPrinter printing: {doc}")

# 3. All-in-one copier implements multiple role interfaces via Multiple Inheritance:
class EnterpriseCopier(Printer, Scanner, FaxMachine):
    def print_document(self, doc: str):
        print(f"🖨️ EnterpriseCopier printing: {doc}")

    def scan_document(self, doc: str) -> str:
        print(f"📄 EnterpriseCopier scanning: {doc}")
        return f"Scanned: {doc}"

    def fax_document(self, doc: str, number: str):
        print(f"📠 EnterpriseCopier faxing {doc} to {number}")

# 4. Consumer functions depend ONLY on the capability they actually need:
def print_invoice(device: Printer, invoice_text: str):
    # This function only cares that 'device' can print!
    device.print_document(invoice_text)

print_invoice(CheapDeskPrinter(), "Invoice #1001")
print_invoice(EnterpriseCopier(), "Invoice #1002")
```

---

## 🌟 Modern Python Approach: `typing.Protocol` (Duck Typing with Type Checking)

In modern Python (3.8+), you don't even need explicit inheritance; you can use **Structural Subtyping** with `typing.Protocol`:

```python
from typing import Protocol

class Printable(Protocol):
    def print_document(self, doc: str) -> None:
        ...

def handle_printing(item: Printable, text: str):
    item.print_document(text)
```
Any class with a matching `print_document` signature automatically satisfies `Printable` without subclassing!

---

## 🧠 Top Interview Questions

1. **Q: How does Python support Interface Segregation without a formal `interface` keyword like Java or C#?**
   * **A:** Python uses:
     1. Abstract Base Classes (`abc.ABC`) with `@abstractmethod`.
     2. Multiple inheritance / Mixin classes.
     3. Modern `typing.Protocol` (PEP 544) for structural type checking (compile/lint time interface contracts).

2. **Q: What is the smell or symptom of an ISP violation?**
   * **A:** When subclasses implement methods with `pass`, `return None`, or `raise NotImplementedError`, it indicates the base interface is too wide for all its implementers.
