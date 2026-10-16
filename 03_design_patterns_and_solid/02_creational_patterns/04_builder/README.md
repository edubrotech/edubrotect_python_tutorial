# 📌 Creational Pattern 04: Builder

## 📖 Intent
> *"Separate the construction of a complex object from its representation so that the same construction process can create different representations."* — Gang of Four

The Builder pattern solves the **"Telescoping Constructor" anti-pattern**—constructors with 10+ positional and optional arguments where callers easily pass parameters in the wrong order.

---

## 🛠️ Implementation in Python: Fluent SQL Query Builder

```python
class SQLQuery:
    def __init__(self):
        self.table = ""
        self.columns = []
        self.where_clauses = []
        self.order_by_col = None
        self.limit_val = None

    def __str__(self):
        cols = ", ".join(self.columns) if self.columns else "*"
        query = f"SELECT {cols} FROM {self.table}"
        if self.where_clauses:
            query += " WHERE " + " AND ".join(self.where_clauses)
        if self.order_by_col:
            query += f" ORDER BY {self.order_by_col}"
        if self.limit_val is not None:
            query += f" LIMIT {self.limit_val}"
        return query + ";"

class SQLQueryBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._query = SQLQuery()
        return self

    def from_table(self, table: str):
        self._query.table = table
        return self  # Return self for Fluent Method Chaining!

    def select(self, *columns: str):
        self._query.columns.extend(columns)
        return self

    def where(self, condition: str):
        self._query.where_clauses.append(condition)
        return self

    def order_by(self, column: str):
        self._query.order_by_col = column
        return self

    def limit(self, count: int):
        self._query.limit_val = count
        return self

    def build(self) -> SQLQuery:
        if not self._query.table:
            raise ValueError("Query must specify a table!")
        constructed_query = self._query
        self.reset() # Ready for next build
        return constructed_query

# Fluent Usage:
builder = SQLQueryBuilder()
query = (
    builder.from_table("users")
           .select("id", "username", "email")
           .where("is_active = 1")
           .where("created_at > '2026-01-01'")
           .order_by("username ASC")
           .limit(10)
           .build()
)

print("Generated SQL:\n", query)
# Output: SELECT id, username, email FROM users WHERE is_active = 1 AND created_at > '2026-01-01' ORDER BY username ASC LIMIT 10;
```

---

## 🧠 Top Interview Questions

1. **Q: When is the Builder pattern needed in Python, given Python supports named keyword arguments and default values?**
   * **A:** While keyword arguments solve basic telescoping constructors, Builder is essential when:
     1. Object construction requires a multi-step sequence with validation at each stage.
     2. The object should be immutable once created (`build()` returns an immutable frozen instance).
     3. You want a domain-specific fluent API (like SQL query builders, pipeline builders, or HTTP request composers).
