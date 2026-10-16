# 📌 Creational Pattern 03: Abstract Factory

## 📖 Intent
> *"Provide an interface for creating families of related or dependent objects without specifying their concrete classes."* — Gang of Four

Where **Factory Method** creates a single product, **Abstract Factory** creates an entire **family of coordinated products** (e.g., UI widgets matching a specific visual theme, or database engines providing connection, cursor, and transaction objects).

---

## 🛠️ Implementation in Python: Cross-Platform UI Component Family

```python
from abc import ABC, abstractmethod

# 1. Abstract Products
class Button(ABC):
    @abstractmethod
    def render(self) -> str: pass

class Checkbox(ABC):
    @abstractmethod
    def toggle(self) -> str: pass

# 2. Concrete Products for Light Theme Family
class LightButton(Button):
    def render(self) -> str: return "🔘 [Light Button] with white background"

class LightCheckbox(Checkbox):
    def toggle(self) -> str: return "☑️ [Light Checkbox] checked"

# 3. Concrete Products for Dark Theme Family
class DarkButton(Button):
    def render(self) -> str: return "⚫ [Dark Button] with neon border"

class DarkCheckbox(Checkbox):
    def toggle(self) -> str: return "⬛ [Dark Checkbox] checked"

# 4. Abstract Factory Interface
class GUIThemeFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox: pass

# 5. Concrete Factories
class LightThemeFactory(GUIThemeFactory):
    def create_button(self) -> Button: return LightButton()
    def create_checkbox(self) -> Checkbox: return LightCheckbox()

class DarkThemeFactory(GUIThemeFactory):
    def create_button(self) -> Button: return DarkButton()
    def create_checkbox(self) -> Checkbox: return DarkCheckbox()

# 6. Client Code: Completely agnostic of concrete theme classes!
class Application:
    def __init__(self, factory: GUIThemeFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render_ui(self):
        print(self.button.render())
        print(self.checkbox.toggle())

# Client selects theme via environment/config:
current_mode = "dark"
factory = DarkThemeFactory() if current_mode == "dark" else LightThemeFactory()
app = Application(factory)
app.render_ui()
```

---

## 🧠 Top Interview Questions

1. **Q: What is the main difference between Factory Method and Abstract Factory?**
   * **A:**
     * **Factory Method** uses inheritance to create a **single** product (`create_button()`).
     * **Abstract Factory** uses composition to create **families of related products** (`create_button()`, `create_checkbox()`, `create_window()`) that are guaranteed to work together harmoniously.

2. **Q: When should you use Abstract Factory in backend engineering?**
   * **A:** When building multi-cloud SDKs (e.g., AWS factory producing S3 storage, SQS queues, and DynamoDB vs GCP factory producing GCS, Pub/Sub, and Bigtable) where mixing components from different families would cause system errors.
