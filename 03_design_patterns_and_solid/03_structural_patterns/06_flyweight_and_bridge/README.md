# 📌 Structural Pattern 06: Flyweight & Bridge Patterns

---

## 🪶 Part 1: The Flyweight Pattern

### 📖 Intent
> *"Use sharing to support large numbers of fine-grained objects efficiently."* — Gang of Four

When an application needs to create hundreds of thousands of objects (like particles, bullet projectiles, or text characters), RAM can be exhausted. Flyweight splits object state into:
* **Intrinsic State**: Constant, immutable data shared across all objects (e.g., textures, glyphs, color models).
* **Extrinsic State**: Unique, mutable data passed from outside (e.g., current $x, y$ coordinates).

### 🛠️ Python Implementation: Forest Particle Generator
```python
class TreeType:
    """Flyweight: Holds shared INTRINSIC state (Texture, Color)"""
    def __init__(self, name: str, color: str, texture: str):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x: int, y: int):
        # Operates using EXTRINSIC state (x, y) passed at runtime
        print(f"🌲 Rendering {self.color} {self.name} at coordinates ({x}, {y})")

class TreeFactory:
    """Flyweight Factory: Ensures identical intrinsic states are shared"""
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name: str, color: str, texture: str) -> TreeType:
        key = (name, color, texture)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
        return cls._tree_types[key]

class Tree:
    """Context object: Only stores small extrinsic coordinates + flyweight pointer"""
    def __init__(self, x: int, y: int, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def render(self):
        self.tree_type.draw(self.x, self.y)

# Spawning 100,000 trees using only 2 TreeType flyweight objects in RAM!
oak_type = TreeFactory.get_tree_type("Oak", "Green", "rough_bark.png")
pine_type = TreeFactory.get_tree_type("Pine", "DarkGreen", "needle_leaf.png")

forest = [Tree(i * 10, i * 20, oak_type) for i in range(50_000)]
forest.extend([Tree(i * 15, i * 25, pine_type) for i in range(50_000)])

print(f"Total trees planted: {len(forest):,}")
print(f"Total Flyweight objects stored in memory: {len(TreeFactory._tree_types)}")
# Output: 100,000 trees sharing exactly 2 Flyweights!
```

---

## 🌉 Part 2: The Bridge Pattern

### 📖 Intent
> *"Decouple an abstraction from its implementation so that the two can vary independently."* — Gang of Four

Instead of creating a Cartesian product of subclasses ($M$ abstractions $\times$ $N$ implementations = $M \times N$ classes), Bridge uses **composition** to separate high-level controls from device drivers.

```
       ABSTRACTION LAYER                 IMPLEMENTATION LAYER
   ┌───────────────────────┐           ┌───────────────────────┐
   │    RemoteControl      │ ────────> │      Device (ABC)     │
   ├───────────────────────┤           ├───────────────────────┤
   │ - device: Device      │           │ + enable(): void      │
   │ + toggle_power()      │           │ + disable(): void     │
   └───────────▲───────────┘           │ + set_volume(level)   │
               │                       └───────────▲───────────┘
   ┌───────────┴───────────┐                       │
   │  AdvancedRemoteControl│               ┌───────┴───────┐
   │  + mute()             │        ┌──────┴──────┐ ┌──────┴──────┐
   └───────────────────────┘        │   Sony TV   │ │Samsung Radio│
                                    └─────────────┘ └─────────────┘
```

### 🛠️ Python Implementation: Remotes & Devices
```python
from abc import ABC, abstractmethod

# 1. Implementation Interface
class Device(ABC):
    @abstractmethod
    def enable(self): pass
    @abstractmethod
    def disable(self): pass
    @abstractmethod
    def set_volume(self, percent: int): pass

# 2. Concrete Implementations
class SonyTV(Device):
    def enable(self): print("📺 Sony TV: Powered ON")
    def disable(self): print("📺 Sony TV: Powered OFF")
    def set_volume(self, percent: int): print(f"📺 Sony TV: Volume set to {percent}%")

class SamsungRadio(Device):
    def enable(self): print("📻 Samsung Radio: Audio ON")
    def disable(self): print("📻 Samsung Radio: Audio OFF")
    def set_volume(self, percent: int): print(f"📻 Samsung Radio: Volume set to {percent}%")

# 3. Abstraction: Remote Control
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device  # The Bridge

    def toggle_power(self):
        self.device.enable()

# 4. Refined Abstraction
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        print("🔇 Advanced Remote: Muting device!")
        self.device.set_volume(0)

# Changing remotes and devices independently:
tv = SonyTV()
remote = AdvancedRemoteControl(tv)
remote.toggle_power()
remote.mute()
```

---

## 🧠 Top Interview Questions

1. **Q: How does Flyweight relate to Python's internal string/integer interning?**
   * **A:** Python's small integer caching (-5 to 256) and string interning are native runtime implementations of the Flyweight pattern. Python shares identical immutable integer and string objects in memory instead of allocating new `PyObject` instances.
