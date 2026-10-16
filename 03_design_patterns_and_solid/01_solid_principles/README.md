# 🛡️ SOLID Principles in Python

## 📖 Introduction
The **SOLID** principles are five design guidelines popularized by Robert C. Martin (Uncle Bob) to create software that is easy to maintain, extend, and understand over time.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        THE S.O.L.I.D. ACRONYM                          │
├─────┬─────────────────────────────────┬────────────────────────────────┤
│  S  │ Single Responsibility Principle │ A class should have only ONE   │
│     │ (SRP)                           │ reason to change.              │
├─────┼─────────────────────────────────┼────────────────────────────────┤
│  O  │ Open/Closed Principle           │ Software entities should be    │
│     │ (OCP)                           │ OPEN for extension, but CLOSED │
│     │                                 │ for modification.              │
├─────┼─────────────────────────────────┼────────────────────────────────┤
│  L  │ Liskov Substitution Principle   │ Subtypes must be substitutable │
│     │ (LSP)                           │ for their base types without   │
│     │                                 │ altering correctness.          │
├─────┼─────────────────────────────────┼────────────────────────────────┤
│  I  │ Interface Segregation Principle │ Clients should not be forced   │
│     │ (ISP)                           │ to depend on methods they do   │
│     │                                 │ not use.                       │
├─────┼─────────────────────────────────┼────────────────────────────────┤
│  D  │ Dependency Inversion Principle  │ High-level modules should not  │
│     │ (DIP)                           │ depend on low-level modules;   │
│     │                                 │ both should depend on          │
│     │                                 │ abstractions.                  │
└─────┴─────────────────────────────────┴────────────────────────────────┘
```

---

## 🗂️ Principle Modules

1. **[01_single_responsibility/](./01_single_responsibility/)**: Refactoring "God classes" into decoupled components (Business logic vs Persistence vs Presentation).
2. **[02_open_closed/](./02_open_closed/)**: Adding new payment providers or discount rules without modifying existing classes using polymorphism.
3. **[03_liskov_substitution/](./03_liskov_substitution/)**: Preventing broken subclass contracts (The Classic Square-Rectangle & Flying Bird traps).
4. **[04_interface_segregation/](./04_interface_segregation/)**: Splitting fat interfaces using Python's Abstract Base Classes (`abc.ABC`) and `typing.Protocol`.
5. **[05_dependency_inversion/](./05_dependency_inversion/)**: Inverting dependencies using Dependency Injection and abstract interfaces.
