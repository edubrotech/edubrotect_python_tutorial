# 📌 Behavioral Pattern 03: Command (Undo / Redo Architecture)

## 📖 Intent
> *"Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations."* — Gang of Four

```
┌──────────────────┐           ┌──────────────────┐           ┌──────────────────┐
│  Invoker (UI)    │ ───────>  │  Command (ABC)   │ ───────>  │Receiver (Document│
│ - history: list  │           │ + execute()      │           │ - content: str   │
│ + undo(), redo() │           │ + undo()         │           │ + write(), del() │
└──────────────────┘           └──────────────────┘           └──────────────────┘
```

---

## 🛠️ Implementation in Python: Text Editor with Undo / Redo

```python
from abc import ABC, abstractmethod

# 1. Receiver: The business object holding actual text state
class TextDocument:
    def __init__(self):
        self.text = ""

    def append(self, text_to_add: str):
        self.text += text_to_add

    def delete_last_n_chars(self, n: int):
        self.text = self.text[:-n]

    def __str__(self):
        return f"Document: '{self.text}'"

# 2. Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass

# 3. Concrete Command
class WriteTextCommand(Command):
    def __init__(self, document: TextDocument, text_to_insert: str):
        self.document = document
        self.text_to_insert = text_to_insert

    def execute(self):
        self.document.append(self.text_to_insert)

    def undo(self):
        self.document.delete_last_n_chars(len(self.text_to_insert))

# 4. Invoker: Tracks command execution and manages Undo/Redo stacks
class EditorHistory:
    def __init__(self):
        self._undo_stack: list[Command] = []
        self._redo_stack: list[Command] = []

    def execute(self, cmd: Command):
        cmd.execute()
        self._undo_stack.append(cmd)
        self._redo_stack.clear() # Clear redo history on new action

    def undo(self):
        if not self._undo_stack:
            print("⚠️ Nothing to undo!")
            return
        cmd = self._undo_stack.pop()
        cmd.undo()
        self._redo_stack.append(cmd)
        print("⏪ Action Undone!")

    def redo(self):
        if not self._redo_stack:
            print("⚠️ Nothing to redo!")
            return
        cmd = self._redo_stack.pop()
        cmd.execute()
        self._undo_stack.append(cmd)
        print("⏩ Action Redone!")

# Demonstration:
doc = TextDocument()
history = EditorHistory()

# User types words
history.execute(WriteTextCommand(doc, "Hello "))
history.execute(WriteTextCommand(doc, "World!"))
print(doc)  # Document: 'Hello World!'

# User presses Ctrl+Z (Undo)
history.undo()
print(doc)  # Document: 'Hello '

# User presses Ctrl+Y (Redo)
history.redo()
print(doc)  # Document: 'Hello World!'
```

---

## 🧠 Top Interview Questions

1. **Q: How does the Command Pattern enable delayed job execution in frameworks like Celery?**
   * **A:** By encapsulating all function parameters and execution targets into a serializable Command payload (e.g. JSON or pickle), jobs can be pushed to message brokers (RabbitMQ/Redis) and executed asynchronously by distributed worker processes.
