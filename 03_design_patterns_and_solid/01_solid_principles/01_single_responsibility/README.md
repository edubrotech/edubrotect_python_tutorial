# 📌 SOLID 01: Single Responsibility Principle (SRP)

## 📖 Definition
> *"A class should have one, and only one, reason to change."* — Robert C. Martin

Every class or module should be responsible for **a single part of the functionality**, and that responsibility should be entirely encapsulated by the class.

---

## ❌ Violation Example: The "God Object" Antipattern

Here is a `UserManager` that violates SRP by taking on 4 distinct responsibilities:
1. User registration business logic
2. Password validation
3. Database persistence
4. Sending transactional emails

```python
# 🚨 VIOLATION OF SRP:
class UserManager:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def validate_password(self):
        # Responsibility 1: Validation
        if len(self.password) < 8:
            raise ValueError("Password must be at least 8 characters!")

    def save_to_database(self):
        # Responsibility 2: Database Persistence
        print(f"Connecting to DB and saving user {self.username}...")

    def send_welcome_email(self):
        # Responsibility 3: Email Notification / SMTP
        print(f"Connecting to SMTP server and emailing {self.email}...")

# If email provider changes, we change UserManager.
# If database engine changes, we change UserManager.
# If validation rules change, we change UserManager.
# Too many reasons to change!
```

---

## ✅ Refactored Pythonic Solution: Decoupled Responsibilities

```python
from dataclasses import dataclass

# 1. Domain Model: Holds data only
@dataclass
class User:
    username: str
    email: str
    password: str

# 2. Validator: One reason to change -> Validation rules change
class UserValidator:
    @staticmethod
    def validate(user: User):
        if len(user.password) < 8:
            raise ValueError("Password must be at least 8 characters long!")
        if "@" not in user.email:
            raise ValueError("Invalid email address format!")

# 3. Repository: One reason to change -> Database/Storage tech changes
class UserRepository:
    def save(self, user: User):
        print(f"💾 Saving user '{user.username}' to PostgreSQL database.")

# 4. Email Service: One reason to change -> Notification system changes
class EmailNotificationService:
    def send_welcome(self, user: User):
        print(f"📧 Sending welcome email to {user.email} via SendGrid.")

# 5. Application Orchestrator / Service
class RegistrationService:
    def __init__(self, validator: UserValidator, repo: UserRepository, emailer: EmailNotificationService):
        self.validator = validator
        self.repo = repo
        self.emailer = emailer

    def register_user(self, user: User):
        self.validator.validate(user)
        self.repo.save(user)
        self.emailer.send_welcome(user)
        print("✅ User registration completed successfully!")

# Usage:
user = User("rakesh", "rakesh@edubrotech.com", "SecurePassword123")
service = RegistrationService(UserValidator(), UserRepository(), EmailNotificationService())
service.register_user(user)
```

---

## 🎯 Advantages of SRP
1. **Easy Unit Testing**: You can test `UserValidator` or `UserRepository` in complete isolation without setting up mock SMTP servers.
2. **Low Coupling**: Changing your database engine from PostgreSQL to MongoDB will never touch or risk breaking your email sending logic.
3. **High Reusability**: `EmailNotificationService` can now be reused by `PasswordResetService`, `BillingService`, etc.

---

## 🧠 Top Interview Questions

1. **Q: Does Single Responsibility mean a class can only have one method?**
   * **A:** Absolutely not. A class can have multiple methods as long as all of them serve a **single coherent responsibility** (e.g. a `UserRepository` may have `get_by_id`, `save`, `delete`, and `update`, all serving data persistence).

2. **Q: How do you identify an SRP violation in existing code?**
   * **A:** Watch for "God classes", classes with names ending in generic terms like `Manager` or `Controller` that import completely unrelated modules (e.g. database drivers, SMTP clients, and HTTP templates all in one file).
