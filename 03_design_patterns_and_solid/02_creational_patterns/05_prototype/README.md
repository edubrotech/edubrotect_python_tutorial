# 📌 Creational Pattern 05: Prototype

## 📖 Intent
> *"Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype."* — Gang of Four

Creating a new object directly via `__init__` can sometimes be computationally expensive (e.g. requires network calls, database lookups, or heavy rendering). The Prototype pattern solves this by **cloning an existing pre-configured object**.

---

## 🛠️ Implementation in Python: Game Character Spawner

```python
import copy
from typing import Dict

class Warrior:
    def __init__(self, name: str, weapon: str, armor: int, skills: list):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.skills = skills  # Nested mutable list!

    def clone(self, deep: bool = True) -> 'Warrior':
        """Clone this prototype instance"""
        if deep:
            # deepcopy duplicates all nested lists and mutable references!
            return copy.deepcopy(self)
        return copy.copy(self)

    def __repr__(self):
        return f"Warrior({self.name!r}, weapon={self.weapon!r}, armor={self.armor}, skills={self.skills})"

# Prototype Registry:
class CharacterRegistry:
    def __init__(self):
        self._prototypes: Dict[str, Warrior] = {}

    def register(self, name: str, prototype: Warrior):
        self._prototypes[name] = prototype

    def spawn(self, name: str, new_name: str) -> Warrior:
        proto = self._prototypes.get(name)
        if not proto:
            raise ValueError(f"Prototype '{name}' not found!")
        cloned = proto.clone(deep=True)
        cloned.name = new_name
        return cloned

# Setup base prototypes:
registry = CharacterRegistry()
registry.register("orc_grunt", Warrior("Grunt", weapon="Rusty Axe", armor=50, skills=["Smash", "Rage"]))
registry.register("elf_archer", Warrior("Archer", weapon="Elven Bow", armor=30, skills=["Snipe", "Eagle Eye"]))

# Spawning clones with customized names:
enemy1 = registry.spawn("orc_grunt", "Gorgash")
enemy2 = registry.spawn("orc_grunt", "Throk")
enemy2.skills.append("Shield Slam") # Does not mutate enemy1 or prototype!

print("Enemy 1:", enemy1)
print("Enemy 2:", enemy2)
```

---

## 🧠 Top Interview Questions

1. **Q: Why is `copy.deepcopy()` preferred over `copy.copy()` in the Prototype pattern?**
   * **A:** Shallow copy (`copy.copy()`) only duplicates the top-level container; any nested mutable structures (lists, dicts, child objects) share references. If clone A modifies a nested list, clone B and the original prototype would be unintentionally mutated. `copy.deepcopy()` recursively duplicates the entire object graph.
