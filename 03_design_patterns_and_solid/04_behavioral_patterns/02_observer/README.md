# 📌 Behavioral Pattern 02: Observer (Pub/Sub)

## 📖 Intent
> *"Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically."* — Gang of Four

```
                              ┌─────────────────────────┐
                              │     Subject / Channel   │
                              ├─────────────────────────┤
                              │ + subscribe(observer)   │
                              │ + unsubscribe(observer) │
                              │ + notify(event_data)    │
                              └────────────┬────────────┘
                                           │ notifies all
                    ┌──────────────────────┼──────────────────────┐
                    ▼                      ▼                      ▼
           ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
           │ EmailSubscriber │    │  PushSubscriber │    │   DiscordBot    │
           └─────────────────┘    └─────────────────┘    └─────────────────┘
```

---

## 🛠️ Implementation in Python: YouTube Channel Notification Engine

```python
from abc import ABC, abstractmethod

# 1. Observer Interface
class Subscriber(ABC):
    @abstractmethod
    def update(self, channel_name: str, video_title: str) -> None:
        pass

# 2. Concrete Observers
class EmailSubscriber(Subscriber):
    def __init__(self, email: str):
        self.email = email

    def update(self, channel_name: str, video_title: str):
        print(f"📧 Email to {self.email}: New video on '{channel_name}': '{video_title}'!")

class MobilePushSubscriber(Subscriber):
    def __init__(self, device_id: str):
        self.device_id = device_id

    def update(self, channel_name: str, video_title: str):
        print(f"📱 Push Alert to Device [{self.device_id}]: {video_title} is LIVE on {channel_name}!")

# 3. Subject (Observable)
class YouTubeChannel:
    def __init__(self, name: str):
        self.name = name
        self._subscribers: list[Subscriber] = []

    def subscribe(self, subscriber: Subscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)
            print(f"✅ Added subscriber to {self.name}")

    def unsubscribe(self, subscriber: Subscriber):
        self._subscribers.remove(subscriber)
        print(f"❌ Removed subscriber from {self.name}")

    def upload_video(self, video_title: str):
        print(f"\n🎬 {self.name} uploaded: '{video_title}'!")
        print("🔔 Notifying all subscribers...")
        for sub in self._subscribers:
            sub.update(self.name, video_title)

# Usage:
channel = YouTubeChannel("EduBroTech")

sub1 = EmailSubscriber("rakesh@example.com")
sub2 = MobilePushSubscriber("Pixel_9_Pro")

channel.subscribe(sub1)
channel.subscribe(sub2)

channel.upload_video("Python Design Patterns in 20 Minutes")
```

---

## ⚠️ Memory Leak Warning: The "Lapsed Listener" Problem
In long-running Python servers, if subjects hold strong references to subscribers in a `list`, those subscriber objects can **never be garbage collected**, even if the rest of the application has dropped all references to them!

**The Idiomatic Python Fix**: Use `weakref.WeakSet`:
```python
import weakref

class WeakSubject:
    def __init__(self):
        # Automatically discards subscriber as soon as its strong references die!
        self._subscribers = weakref.WeakSet()
```

---

## 🧠 Top Interview Questions

1. **Q: What is the "Lapsed Listener" problem in the Observer Pattern?**
   * **A:** It occurs when an observer registers with a subject, but forgets to unregister. Because the subject holds a strong reference in its subscriber list, the observer is never garbage collected, causing a slow memory leak. In Python, this is solved cleanly using `weakref.WeakSet`.
