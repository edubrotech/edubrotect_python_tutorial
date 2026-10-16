# 📌 Advanced Topic 09: Advanced Data Structures & `collections`

## 📖 Introduction
Beyond Python's primitive lists and dictionaries, the standard library provides specialized high-performance container datatypes in the `collections` and `heapq` modules. Understanding these—alongside implementing classical data structures from scratch—is essential for algorithm design and systems programming.

---

## 🧰 1. The `collections` Module

### A. `Counter` (Multiset Frequency Analysis)
```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)

print(counts)                    # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print("Top 2 most common:", counts.most_common(2)) # [('apple', 3), ('banana', 2)]

# Multiset math
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print("Combined:", c1 + c2)      # Counter({'a': 4, 'b': 3})
```

### B. `defaultdict` (Automatic Default Value on Missing Keys)
```python
from collections import defaultdict

# Grouping words by their first letter
grouped = defaultdict(list)
for word in ["python", "perl", "java", "javascript", "c++"]:
    grouped[word[0]].append(word)

print(dict(grouped))
# {'p': ['python', 'perl'], 'j': ['java', 'javascript'], 'c': ['c++']}
```

### C. `deque` (Fast Double-Ended Queue: $O(1)$ Both Ends)
* Python lists have $O(N)$ cost when popping or inserting at index 0. `deque` has $O(1)$ amortized cost at both ends.

```python
from collections import deque

dq = deque(maxlen=3) # Fixed maxlen automatically evicts oldest on overflow!
dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)  # 1 is automatically evicted!
print(dq)     # deque([2, 3, 4], maxlen=3)

dq.appendleft(10)
print(dq.pop())      # Pops right: 4
print(dq.popleft())  # Pops left: 10
```

### D. `namedtuple` (Memory-Lean Tuple with Named Fields)
```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y", "z"])
p = Point(10, 20, 30)

print(f"X: {p.x}, Y: {p.y}, Z: {p.z}")
print(p[0])  # Still supports index access like regular tuple
```

---

## 🏔️ 2. Priority Queues with `heapq` (Min-Heap)
Python implements binary min-heaps in $O(\log N)$ time:

```python
import heapq

numbers = [20, 1, 15, 8, 3]
heapq.heapify(numbers)  # In-place converts list into min-heap in O(N)
print("Heapified:", numbers)  # Root numbers[0] is guaranteed smallest: 1

heapq.heappush(numbers, 0)
smallest = heapq.heappop(numbers)
print("Smallest element popped:", smallest)  # 0

# Finding N largest or smallest in O(N log K):
print("Top 2 Largest:", heapq.nlargest(2, numbers))
```

---

## 🏗️ 3. Classical Data Structures Built from Scratch

### A. Stack (LIFO: Last In, First Out)
```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        return self._items[-1] if self._items else None

    def is_empty(self):
        return len(self._items) == 0
```

### B. Singly Linked List
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def to_list(self):
        items = []
        curr = self.head
        while curr:
            items.append(curr.data)
            curr = curr.next
        return items

ll = LinkedList()
ll.insert_at_head(30)
ll.insert_at_head(20)
ll.insert_at_head(10)
print("Linked List:", ll.to_list())  # [10, 20, 30]
```

### C. Binary Search Tree (BST)
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_node(self.root, val)

    def _insert_node(self, current, val):
        if val < current.val:
            if not current.left:
                current.left = TreeNode(val)
            else:
                self._insert_node(current.left, val)
        else:
            if not current.right:
                current.right = TreeNode(val)
            else:
                self._insert_node(current.right, val)

    def inorder(self, node, result=None):
        if result is None: result = []
        if node:
            self.inorder(node.left, result)
            result.append(node.val)
            self.inorder(node.right, result)
        return result

bst = BinarySearchTree()
for n in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(n)
print("BST In-Order Sorted:", bst.inorder(bst.root))
# [20, 30, 40, 50, 60, 70, 80]
```

---

## 🧠 Top Interview Questions

1. **Q: Why should you use `collections.deque` instead of `list` for a FIFO Queue?**
   * **A:** In a Python `list`, removing the first element (`list.pop(0)`) requires shifting all subsequent $N-1$ elements in memory, which is $O(N)$ time complexity. `collections.deque` is implemented as a doubly linked list of blocks, providing true $O(1)$ operations from both ends.

2. **Q: How does `heapq` implement priority queues?**
   * **A:** It uses standard Python lists organized as a 0-indexed binary heap array where `heap[k] <= heap[2*k + 1]` and `heap[k] <= heap[2*k + 2]` for all $k$.

---

## 💻 Practice Exercises
1. **Exercise 1 (Valid Parentheses with Stack):** Write a function using a `Stack` to validate if a string containing parentheses `'()[]{}'` is balanced.
2. **Exercise 2 (LRU Cache with OrderedDict):** Implement a Least Recently Used (LRU) Cache with capacity $K$ using `collections.OrderedDict`.
