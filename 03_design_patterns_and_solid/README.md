# 🏛️ Module 03: Python Design Patterns & SOLID Principles

Welcome to the **Design Patterns & SOLID Principles** module of the **EduBroTech Python Tutorial Series**!

Writing Python code that works is only step one; writing code that is **maintainable, testable, decoupled, and extensible** is what separates junior coders from senior software engineers and software architects. This module covers the foundational **SOLID principles** and all classic **Gang of Four (GoF) Design Patterns** adapted to Pythonic idioms.

---

## 🗺️ Roadmap & Curriculum

```
┌────────────────────────────────────────────────────────────────────────┐
│               PYTHON DESIGN PATTERNS & SOLID ROADMAP                   │
├───────────────────────────────────┬────────────────────────────────────┤
│  01. SOLID Principles             │  02. Creational Patterns           │
│  - Single Responsibility (SRP)    │  - Singleton Pattern               │
│  - Open / Closed (OCP)            │  - Factory Method Pattern          │
│  - Liskov Substitution (LSP)      │  - Abstract Factory Pattern        │
│  - Interface Segregation (ISP)    │  - Builder Pattern                 │
│  - Dependency Inversion (DIP)     │  - Prototype Pattern               │
├───────────────────────────────────┼────────────────────────────────────┤
│  03. Structural Patterns          │  04. Behavioral Patterns           │
│  - Adapter Pattern                │  - Strategy Pattern                │
│  - Facade Pattern                 │  - Observer (Pub/Sub) Pattern      │
│  - Proxy Pattern                  │  - Command Pattern                 │
│  - Decorator Pattern (OOP)        │  - State Pattern                   │
│  - Composite Pattern              │  - Chain of Responsibility         │
│  - Bridge & Flyweight Patterns    │  - Template Method & Mediator      │
└───────────────────────────────────┴────────────────────────────────────┘
```

---

## 📑 Detailed Navigation Index

### 🛡️ [01. SOLID Principles (`01_solid_principles/`)](./01_solid_principles/)
* [📂 `01_single_responsibility/`](./01_solid_principles/01_single_responsibility/): SRP — One class, one reason to change.
* [📂 `02_open_closed/`](./01_solid_principles/02_open_closed/): OCP — Open for extension, closed for modification.
* [📂 `03_liskov_substitution/`](./01_solid_principles/03_liskov_substitution/): LSP — Subtypes must be substitutable for base types.
* [📂 `04_interface_segregation/`](./01_solid_principles/04_interface_segregation/): ISP — Many client-specific interfaces over one fat interface.
* [📂 `05_dependency_inversion/`](./01_solid_principles/05_dependency_inversion/): DIP — Depend upon abstractions, not concretions.

### 🏭 [02. Creational Patterns (`02_creational_patterns/`)](./02_creational_patterns/)
* [📂 `01_singleton/`](./02_creational_patterns/01_singleton/): Ensure a class has only one instance with a global point of access.
* [📂 `02_factory_method/`](./02_creational_patterns/02_factory_method/): Delegate instantiation logic to subclasses or factories.
* [📂 `03_abstract_factory/`](./02_creational_patterns/03_abstract_factory/): Create families of related or dependent objects without specifying concrete classes.
* [📂 `04_builder/`](./02_creational_patterns/04_builder/): Separate complex object construction from its representation (step-by-step assembly).
* [📂 `05_prototype/`](./02_creational_patterns/05_prototype/): Clone existing objects without depending on their concrete classes (`copy.deepcopy`).

### 🌉 [03. Structural Patterns (`03_structural_patterns/`)](./03_structural_patterns/)
* [📂 `01_adapter/`](./03_structural_patterns/01_adapter/): Allow incompatible interfaces to collaborate.
* [📂 `02_facade/`](./03_structural_patterns/02_facade/): Provide a simplified interface to a complex library or subsystem.
* [📂 `03_proxy/`](./03_structural_patterns/03_proxy/): Provide a surrogate or placeholder to control access, caching, or lazy loading.
* [📂 `04_decorator/`](./03_structural_patterns/04_decorator/): Dynamically attach additional responsibilities to objects via wrapping.
* [📂 `05_composite/`](./03_structural_patterns/05_composite/): Compose objects into tree structures to represent part-whole hierarchies.
* [📂 `06_flyweight_and_bridge/`](./03_structural_patterns/06_flyweight_and_bridge/): Shared memory optimization (Flyweight) and decoupling abstraction from implementation (Bridge).

### 🔄 [04. Behavioral Patterns (`04_behavioral_patterns/`)](./04_behavioral_patterns/)
* [📂 `01_strategy/`](./04_behavioral_patterns/01_strategy/): Define a family of interchangeable algorithms at runtime.
* [📂 `02_observer/`](./04_behavioral_patterns/02_observer/): Define a one-to-many subscription mechanism to notify multiple objects of state changes.
* [📂 `03_command/`](./04_behavioral_patterns/03_command/): Encapsulate requests as objects, enabling undo/redo and task queues.
* [📂 `04_state/`](./04_behavioral_patterns/04_state/): Allow an object to alter its behavior when its internal state changes.
* [📂 `05_chain_of_responsibility/`](./04_behavioral_patterns/05_chain_of_responsibility/): Pass requests along a chain of handlers until one processes it.
* [📂 `06_template_method_and_mediator/`](./04_behavioral_patterns/06_template_method_and_mediator/): Skeleton algorithm execution (Template Method) and centralized communication (Mediator).

---

## 💡 Why Design Patterns in Python?
Python's dynamic nature, first-class functions, and duck typing make some traditional GoF patterns simpler and more lightweight than in Java or C++. For example:
* **Strategy Pattern** is often implemented using simple first-class functions instead of full class hierarchies.
* **Singleton Pattern** can often be achieved through Python's module caching mechanism (`sys.modules`).
* **Decorator Pattern** has built-in language syntax support (`@decorator`).

Understanding both the classic OOP implementation and the idiomatic Pythonic equivalent is the key to writing clean, professional architecture.
