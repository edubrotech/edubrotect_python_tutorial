# 🏭 Creational Design Patterns in Python

## 📖 Introduction
Creational design patterns deal with **object creation mechanisms**, trying to create objects in a manner suitable to the situation. They provide flexibility in deciding which objects need to be created for a given case, while hiding the creation logic from the caller.

---

## 🗺️ Patterns in this Section

| Pattern | Intent / Purpose | Real-World Use Case |
|---|---|---|
| **[01. Singleton](./01_singleton/)** | Ensure a class has only one instance and provide a global point of access to it. | Database connection pool, Configuration manager, Logger. |
| **[02. Factory Method](./02_factory_method/)** | Provide an interface for creating objects in a superclass, but allow subclasses to alter the type of objects that will be created. | Document parsers (JSON, XML, CSV), Payment gateway selector. |
| **[03. Abstract Factory](./03_abstract_factory/)** | Provide an interface for creating families of related or dependent objects without specifying their concrete classes. | Multi-platform UI widgets (Windows Button/Checkbox vs Mac Button/Checkbox). |
| **[04. Builder](./04_builder/)** | Separate the construction of a complex object from its representation so that the same construction process can create different representations. | SQL query builder, HTTP request composer, Pizza/Car assembly. |
| **[05. Prototype](./05_prototype/)** | Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype. | Game entity cloning (enemies, bullets), snapshot state duplicating. |
