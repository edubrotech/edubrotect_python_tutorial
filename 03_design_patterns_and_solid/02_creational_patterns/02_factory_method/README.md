# 📌 Creational Pattern 02: Factory Method

## 📖 Intent
> *"Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses."* — Gang of Four

```
┌───────────────────────────┐           ┌───────────────────────────┐
│     Notification (ABC)    │           │    NotificationCreator    │
├───────────────────────────┤           ├───────────────────────────┤
│ + send(msg): void         │           │ + create_notification()   │
└─────────────▲─────────────┘           │ + notify_user(msg): void  │
              │                         └─────────────▲─────────────┘
      ┌───────┴───────┐                               │
      │               │                               │
┌─────┴─────┐   ┌─────┴─────┐                   ┌─────┴──────────────┐
│   Email   │   │    SMS    │                   │ EmailCreator / SMS │
└───────────┘   └───────────┘                   └────────────────────┘
```

---

## 🛠️ Implementation in Python

```python
from abc import ABC, abstractmethod

# 1. Product Interface
class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass

# 2. Concrete Products
class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"📧 Sending EMAIL: {message}")

class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"📱 Sending SMS: {message}")

class PushNotification(Notification):
    def send(self, message: str) -> None:
        print(f"🔔 Sending PUSH ALERT: {message}")

# 3. Creator (Factory Method)
class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        """The Factory Method"""
        pass

    def notify(self, message: str):
        # Uses the factory method to create the product, then operates on it:
        notification = self.create_notification()
        notification.send(message)

# 4. Concrete Creators
class EmailNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return EmailNotification()

class SMSNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return SMSNotification()

# Usage:
def client_code(creator: NotificationCreator, msg: str):
    creator.notify(msg)

client_code(EmailNotificationCreator(), "Welcome to Python Tutorials!")
client_code(SMSNotificationCreator(), "Your OTP is 9482")
```

---

## 🐍 The Lightweight Pythonic Alternative: Registry / Dict Factory
In Python, functions and classes are first-class objects. A dictionary dispatch table is often much cleaner than deep subclass hierarchies:

```python
class NotificationFactory:
    _registry = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification
    }

    @classmethod
    def register(cls, channel: str, notification_class):
        cls._registry[channel.lower()] = notification_class

    @classmethod
    def get_notification(cls, channel: str) -> Notification:
        target_class = cls._registry.get(channel.lower())
        if not target_class:
            raise ValueError(f"Unknown notification channel: {channel}")
        return target_class()

# Usage:
sender = NotificationFactory.get_notification("email")
sender.send("Clean Pythonic Factory!")
```

---

## 🧠 Top Interview Questions

1. **Q: When should you use Factory Method over simple direct instantiation?**
   * **A:** When the exact type and dependencies of the object to create cannot be anticipated beforehand (e.g., determined by config files, user input, or environment variables) or when you want to decouple creation logic from business logic.

2. **Q: How does Factory Method support the Open/Closed Principle?**
   * **A:** You can introduce new product classes and corresponding creator classes without modifying any existing client code.
