# 🔄 Behavioral Design Patterns in Python

## 📖 Introduction
Behavioral design patterns are concerned with **algorithms and the assignment of responsibilities between objects**. They characterize complex control flows that are difficult to follow at runtime, shifting your focus away from control flow to the way objects are interconnected.

---

## 🗺️ Patterns in this Section

| Pattern | Intent / Purpose | Real-World Use Case |
|---|---|---|
| **[01. Strategy](./01_strategy/)** | Define a family of algorithms, encapsulate each one, and make them interchangeable at runtime. | Payment methods, Sorting strategies, Compression algorithms, Discount calculators. |
| **[02. Observer](./02_observer/)** | Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified automatically. | Event emitters, Pub/Sub message buses, Stock price alert tickers, Model-View binding. |
| **[03. Command](./03_command/)** | Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations. | Undo/Redo in text editors, Background task queues (Celery-like), Macro recording. |
| **[04. State](./04_state/)** | Allow an object to alter its behavior when its internal state changes. The object will appear to change its class. | Order lifecycle (Pending -> Paid -> Shipped -> Delivered), TCP connection state. |
| **[05. Chain of Responsibility](./05_chain_of_responsibility/)** | Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. | HTTP middleware pipelines (Auth -> Logging -> Rate Limiter -> Handler). |
| **[06. Template Method & Mediator](./06_template_method_and_mediator/)** | Define algorithm skeletons (Template Method) and reduce chaotic dependencies between components (Mediator). | Data ETL processing pipelines, Chatroom / Air Traffic Control hubs. |
