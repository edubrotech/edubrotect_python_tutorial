# 📌 Behavioral Pattern 06: Template Method & Mediator Patterns

---

## 📐 Part 1: The Template Method Pattern

### 📖 Intent
> *"Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure."* — Gang of Four

Adheres to the famous **Hollywood Principle**: *"Don't call us, we'll call you."* The base class controls the overall algorithm workflow, calling hook and abstract methods implemented in subclasses.

### 🛠️ Python Implementation: Data Mining & ETL Pipeline
```python
from abc import ABC, abstractmethod

class DataMinerPipeline(ABC):
    def mine(self, file_path: str):
        """The Template Method: Defines strict sequence of execution steps"""
        raw_data = self.open_file(file_path)
        extracted = self.extract_data(raw_data)
        cleaned = self.clean_data(extracted)
        self.save_to_database(cleaned)
        self.close_file(raw_data)
        print("✅ Pipeline execution completed successfully!\n")

    # Invariant steps (common to all formats):
    def open_file(self, path: str):
        print(f"📂 Opening file stream: {path}")
        return f"Stream({path})"

    def clean_data(self, data):
        print(f"🧹 Sanitizing and formatting extracted records...")
        return [f"Cleaned_{d}" for d in data]

    def save_to_database(self, cleaned_data):
        print(f"💾 Persisting {len(cleaned_data)} records to PostgreSQL.")

    def close_file(self, stream):
        print(f"🔒 Closed file stream: {stream}")

    # Variant step: Must be implemented by specialized subclass!
    @abstractmethod
    def extract_data(self, raw_data_stream) -> list:
        pass

# Specialized subclasses:
class PDFDataMiner(DataMinerPipeline):
    def extract_data(self, raw_data_stream) -> list:
        print("📄 Parsing binary PDF font tables and page bounding boxes...")
        return ["Invoice_#401", "Total_$500.00"]

class CSVDataMiner(DataMinerPipeline):
    def extract_data(self, raw_data_stream) -> list:
        print("📊 Splitting comma-separated rows and parsing header cells...")
        return ["Row_1_Data", "Row_2_Data", "Row_3_Data"]

# Execution:
csv_miner = CSVDataMiner()
csv_miner.mine("sales_q3.csv")
```

---

## 🤝 Part 2: The Mediator Pattern

### 📖 Intent
> *"Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently."* — Gang of Four

Instead of every component needing direct references to every other component (creating a tangled spaghetti network of $N \times (N-1)$ connections), all components communicate through a **centralized Mediator**.

```
TANGLED DIRECT COUPLING (Bad):         CLEAN MEDIATOR PATTERN (Good):
     [ User A ] ─── [ User B ]                   [ User A ]      [ User B ]
         │     ╲   ╱     │                            ╲            ╱
         │      ╳        │                             ▼          ▼
         │     ╱   ╲     │                       ┌─────────────────────┐
     [ User C ] ─── [ User D ]                   │      ChatMediator   │
                                                 └─────────────────────┘
                                                       ▲          ▲
                                                      ╱            ╲
                                                 [ User C ]      [ User D ]
```

### 🛠️ Python Implementation: Chatroom Communication Hub
```python
class ChatMediator:
    """The Centralized Hub"""
    def __init__(self):
        self._colleagues: list['User'] = []

    def register(self, user: 'User'):
        self._colleagues.append(user)
        user.mediator = self

    def send_message(self, sender: 'User', message: str):
        # Broadcast message to all other users without sender needing direct references:
        for colleague in self._colleagues:
            if colleague != sender:
                colleague.receive(sender.name, message)

class User:
    def __init__(self, name: str):
        self.name = name
        self.mediator: ChatMediator = None

    def send(self, message: str):
        print(f"💬 {self.name} posts: '{message}'")
        self.mediator.send_message(self, message)

    def receive(self, sender_name: str, message: str):
        print(f"   📥 [{self.name}'s Screen] {sender_name}: {message}")

# Assembly:
hub = ChatMediator()
rakesh = User("Rakesh")
priya = User("Priya")
rahul = User("Rahul")

hub.register(rakesh)
hub.register(priya)
hub.register(rahul)

rakesh.send("Welcome team to EduBroTech!")
```

---

## 🧠 Top Interview Questions

1. **Q: What is the Hollywood Principle and which pattern embodies it?**
   * **A:** *"Don't call us, we'll call you"* defines the **Template Method** pattern. High-level base classes control the execution sequence and invoke low-level subclass hooks, rather than low-level subclasses controlling the flow.

2. **Q: How does Mediator differ from Observer?**
   * **A:**
     * **Observer** establishes a one-way broadcast from one subject to many subscribers.
     * **Mediator** coordinates bidirectional, multi-party communication between peers, centralizing complex business workflows in one place.
