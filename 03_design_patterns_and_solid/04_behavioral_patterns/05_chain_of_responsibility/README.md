# 📌 Behavioral Pattern 05: Chain of Responsibility

## 📖 Intent
> *"Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it."* — Gang of Four

This is the exact pattern that powers **web middleware pipelines** in frameworks like **Django, FastAPI, Express.js, and Flask**.

```
[ HTTP Request ]
       │
       ▼
┌──────────────────────┐
│  AuthMiddleware      │ ── (Invalid Token) ──> Return 401 Unauthorized
└──────────┬───────────┘
           │ (Valid)
           ▼
┌──────────────────────┐
│  RateLimitMiddleware │ ── (Too Many Requests) ──> Return 429 Too Many Requests
└──────────┬───────────┘
           │ (Allowed)
           ▼
┌──────────────────────┐
│  SanitizeMiddleware  │
└──────────┬───────────┘
           │
           ▼
[ Final API Controller ]
```

---

## 🛠️ Implementation in Python: Web API Request Middleware

```python
from abc import ABC, abstractmethod
from typing import Optional

# 1. Base Handler Interface
class MiddlewareHandler(ABC):
    def __init__(self):
        self._next_handler: Optional['MiddlewareHandler'] = None

    def set_next(self, handler: 'MiddlewareHandler') -> 'MiddlewareHandler':
        """Enables fluent chaining: h1.set_next(h2).set_next(h3)"""
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: dict) -> bool:
        """Process request or pass to next handler in chain."""
        if self._next_handler:
            return self._next_handler.handle(request)
        return True

# 2. Concrete Handlers
class AuthenticationMiddleware(MiddlewareHandler):
    def handle(self, request: dict) -> bool:
        token = request.get("headers", {}).get("Authorization")
        if not token or token != "Bearer SECRET_KEY":
            print("⛔ [401 Unauthorized]: Missing or invalid Authorization token!")
            return False
        print("✅ [Auth]: Token verified.")
        return super().handle(request)

class RateLimitingMiddleware(MiddlewareHandler):
    def handle(self, request: dict) -> bool:
        user_requests_count = request.get("user_request_count", 0)
        if user_requests_count > 100:
            print("⛔ [429 Too Many Requests]: Rate limit exceeded!")
            return False
        print("✅ [RateLimit]: Request within acceptable limits.")
        return super().handle(request)

class DataSanitizationMiddleware(MiddlewareHandler):
    def handle(self, request: dict) -> bool:
        body = request.get("body", "")
        if "<script>" in body.lower():
            print("⛔ [400 Bad Request]: XSS injection detected in payload!")
            return False
        print("✅ [Sanitize]: Payload safe.")
        return super().handle(request)

# 3. Assembling the Chain:
auth = AuthenticationMiddleware()
rate_limit = RateLimitingMiddleware()
sanitize = DataSanitizationMiddleware()

# Chain order: auth -> rate_limit -> sanitize
auth.set_next(rate_limit).set_next(sanitize)

# Test 1: Valid Request
print("--- Test 1: Valid Request ---")
valid_request = {
    "headers": {"Authorization": "Bearer SECRET_KEY"},
    "user_request_count": 15,
    "body": "Hello world"
}
auth.handle(valid_request)

# Test 2: Invalid Auth
print("\n--- Test 2: Invalid Auth ---")
bad_auth_request = {
    "headers": {"Authorization": "Bearer WRONG_KEY"},
    "user_request_count": 5,
    "body": "Hello"
}
auth.handle(bad_auth_request) # Fails at first link, stops chain immediately!
```

---

## 🧠 Top Interview Questions

1. **Q: How does Chain of Responsibility differ from Decorator?**
   * **A:**
     * In **Decorator**, every wrapper is executed, adding cumulative functionality to the response.
     * In **Chain of Responsibility**, any handler in the sequence has the power to **break the chain** and short-circuit execution without passing the request further.
