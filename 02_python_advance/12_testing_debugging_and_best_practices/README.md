# 📌 Advanced Topic 12: Testing, Debugging & Production Best Practices

## 📖 Introduction
Writing production software requires rigorous automated testing, robust structured logging, reproducible debugging, and strict type safety. This topic covers the industry-standard developer workflow used across top Python engineering teams.

---

## 🧪 1. Automated Testing with `pytest` & `unittest`

### `pytest` Essentials
`pytest` is the de-facto industry standard for Python testing due to its clean syntax and powerful fixture architecture:

```python
# test_calculator.py

def add(a: float, b: float) -> float:
    return a + b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Simple assertion (no self.assertEqual boilerplate needed!)
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# Testing exceptions:
import pytest

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# Parameterized testing:
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (5, 5, 10),
    (-2, 4, 2)
])
def test_add_parameterized(a, b, expected):
    assert add(a, b) == expected
```

### Pytest Fixtures (`@pytest.fixture`)
Fixtures provide a clean, modular way to manage test setup and teardown:

```python
import pytest

@pytest.fixture
def sample_user_data():
    # Setup phase
    data = {"id": 101, "name": "Rakesh", "role": "Admin"}
    yield data
    # Teardown / Cleanup phase executes after test finishes!
    data.clear()

def test_user_role(sample_user_data):
    assert sample_user_data["role"] == "Admin"
```

---

## 🎭 2. Mocking with `unittest.mock`
Isolate external dependencies (such as HTTP APIs, payment gateways, or databases) in tests:

```python
from unittest.mock import Mock, patch
import requests

def get_exchange_rate(currency: str) -> float:
    response = requests.get(f"https://api.fx.com/rate/{currency}")
    return response.json()["rate"]

# Mocking the requests.get call
@patch("requests.get")
def test_get_exchange_rate(mock_get):
    # Configuring the mock response
    mock_response = Mock()
    mock_response.json.return_value = {"rate": 83.25}
    mock_get.return_value = mock_response

    rate = get_exchange_rate("USD")
    assert rate == 83.25
    mock_get.assert_called_once_with("https://api.fx.com/rate/USD")
```

---

## 📝 3. Structured Logging (`logging` module)
Never use `print()` statements in production services. The `logging` module offers log levels, timestamps, process IDs, and output formatting:

```python
import logging

# Configure logger format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s]: %(message)s",
    handlers=[
        logging.StreamHandler(),                  # Console handler
        logging.FileHandler("app.log", mode="a")  # File handler
    ]
)

logger = logging.getLogger("BillingService")

logger.debug("Parsing transaction payload...")
logger.info("Payment processed successfully for customer #442.")
logger.warning("Database query took 1.25s (> 1.0s threshold).")
logger.error("Failed to connect to SMS notification gateway!")
```

---

## 🐞 4. Interactive Debugging (`breakpoint()` & `pdb`)
Python 3.7+ provides the built-in `breakpoint()` function to trigger the interactive Python Debugger (`pdb`):

```python
def process_data(items):
    total = 0
    for item in items:
        # Pauses execution and drops into interactive CLI debugger:
        # Commands: 'n' (next line), 's' (step in), 'c' (continue), 'p variable' (print)
        # breakpoint()
        total += item
    return total
```

---

## 🏷️ 5. Static Typing with `typing` & `mypy`

Python supports type hints (PEP 484) that are validated using static analysis tools like `mypy`:

```python
from typing import Optional, Union, Callable

def find_user(user_id: int) -> Optional[dict]:
    if user_id == 101:
        return {"id": 101, "name": "Rakesh"}
    return None

# Python 3.10+ union syntax (|)
def format_id(id_val: int | str) -> str:
    return str(id_val).zfill(6)
```

Run static type checking:
```bash
pip install mypy
mypy app/
```

---

## 🧠 Top Interview Questions

1. **Q: What is the difference between a Mock and a Stub?**
   * **A:** A **Stub** provides canned answers to calls made during tests without recording interactions. A **Mock** also records how many times it was called, with what arguments, allowing assertions on behavior (`assert_called_with()`).

2. **Q: Why is structured logging preferred over `print()` in production?**
   * **A:** `print()` lacks log severity levels (filtering), thread/process metadata, formatting flexibility, and destination multiplexing (directing errors to Sentry/cloud storage while outputting info to stdout).

---

## 💻 Practice Exercises
1. **Exercise 1 (Unit Test Suite):** Write a complete pytest test suite for a `ShoppingCart` class testing `add_item()`, `remove_item()`, `total_price()`, and negative quantity validation.
2. **Exercise 2 (Mocking Database Calls):** Write a function that reads a user record from a database and returns formatted JSON; write a unit test using `@patch` to mock the database query.
