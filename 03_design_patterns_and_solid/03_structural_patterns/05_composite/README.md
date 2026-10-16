# 📌 Structural Pattern 05: Composite

## 📖 Intent
> *"Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly."* — Gang of Four

```
                     ┌───────────────────────────┐
                     │  FileSystemItem (ABC)     │
                     ├───────────────────────────┤
                     │ + get_size(): int         │
                     │ + display(indent): void   │
                     └─────────────▲─────────────┘
                                   │
                   ┌───────────────┴───────────────┐
                   │                               │
        ┌──────────┴──────────┐         ┌──────────┴──────────┐
        │     File (Leaf)     │         │ Directory(Composite)│
        ├─────────────────────┤         ├─────────────────────┤
        │ - size: int         │         │ - children: list    │
        └─────────────────────┘         │ + add(item): void   │
                                        └─────────────────────┘
```

---

## 🛠️ Implementation in Python: Hierarchical File System

```python
from abc import ABC, abstractmethod

# 1. Base Component
class FileSystemItem(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_size_kb(self) -> float:
        """Returns total size of the item."""
        pass

    @abstractmethod
    def display(self, indent: int = 0) -> None:
        """Renders hierarchy tree."""
        pass

# 2. Leaf (Cannot have children)
class File(FileSystemItem):
    def __init__(self, name: str, size_kb: float):
        super().__init__(name)
        self.size_kb = size_kb

    def get_size_kb(self) -> float:
        return self.size_kb

    def display(self, indent: int = 0):
        print(f"{'  ' * indent}📄 {self.name} ({self.size_kb:.1f} KB)")

# 3. Composite (Contains child items: Files or other Directories)
class Directory(FileSystemItem):
    def __init__(self, name: str):
        super().__init__(name)
        self._children: list[FileSystemItem] = []

    def add(self, item: FileSystemItem):
        self._children.append(item)

    def remove(self, item: FileSystemItem):
        self._children.remove(item)

    def get_size_kb(self) -> float:
        # Uniform recursive calculation!
        return sum(child.get_size_kb() for child in self._children)

    def display(self, indent: int = 0):
        print(f"{'  ' * indent}📁 {self.name}/ (Total: {self.get_size_kb():.1f} KB)")
        for child in self._children:
            child.display(indent + 1)

# Building a complex tree:
root = Directory("my_project")
src = Directory("src")
docs = Directory("docs")

src.add(File("main.py", 12.5))
src.add(File("utils.py", 8.0))
docs.add(File("README.md", 4.2))

root.add(src)
root.add(docs)
root.add(File("requirements.txt", 1.1))

# Client code treats both individual files and entire directories uniformly:
root.display()
print(f"\nTotal Project Disk Usage: {root.get_size_kb():.2f} KB")
```

---

## 🧠 Top Interview Questions

1. **Q: What is the main benefit of the Composite Pattern?**
   * **A:** It simplifies client code. The client doesn't need to check `isinstance(item, Leaf)` or `isinstance(item, Composite)` with complex `if-else` branching; it treats individual objects and groups of objects identically through polymorphism.
