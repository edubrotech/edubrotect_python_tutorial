"""
EduBroTech Python Tutorial Series
Topic: For Loops in Python - Features, Syntax & Usage
Author: Rakesh Singh Bajetha (EduBroTech)
"""

print("=" * 60)
print("1. ITERATING OVER SEQUENCES & COLLECTIONS")
print("=" * 60)

# Iterating over a list
frameworks = ["Django", "FastAPI", "Flask", "Pyramid"]
print("--- Iterating over List ---")
for framework in frameworks:
    print(f"Framework: {framework}")

# Iterating over a string (character by character)
print("\n--- Iterating over String ---")
word = "Python"
for char in word:
    print(f"Char: '{char}'", end=" | ")
print()

# Iterating over a tuple with multiple assignment unpacking
students = [("Rakesh", 95), ("Amit", 88), ("Sneha", 92)]
print("\n--- Unpacking in For Loop ---")
for name, score in students:
    print(f"Student: {name:7} | Score: {score}")

# Iterating over a dictionary (keys, values, items)
user_profile = {
    "username": "rakesh_dev",
    "role": "Cloud Architect",
    "city": "Bengaluru",
    "status": "Active"
}

print("\n--- Iterating over Dictionary (.items()) ---")
for key, value in user_profile.items():
    print(f"{key.capitalize():10}: {value}")

print("\n" + "=" * 60)
print("2. MASTERING range() FUNCTION")
print("=" * 60)

# range(stop): 0 up to stop-1
print("range(5):", list(range(5)))

# range(start, stop): start up to stop-1
print("range(10, 15):", list(range(10, 15)))

# range(start, stop, step): stepping by positive numbers
print("Even numbers (2 to 10):", list(range(2, 11, 2)))

# Negative step: counting backwards
print("Countdown (10 down to 1):", list(range(10, 0, -1)))

# Practical use case: calculating sum and average with range
total = 0
for n in range(1, 101):
    total += n
print(f"Sum of 1 to 100: {total} (Expected: 5050)")

print("\n" + "=" * 60)
print("3. REAL-WORLD DATA PROCESSING WITH FOR LOOPS")
print("=" * 60)

transactions = [
    {"tx_id": "TX101", "amount": 120.50, "type": "CREDIT"},
    {"tx_id": "TX102", "amount": 45.00,  "type": "DEBIT"},
    {"tx_id": "TX103", "amount": 350.75, "type": "CREDIT"},
    {"tx_id": "TX104", "amount": 80.20,  "type": "DEBIT"},
    {"tx_id": "TX105", "amount": 210.00, "type": "CREDIT"},
]

net_balance = 0.0
total_credit = 0.0
total_debit = 0.0

for tx in transactions:
    if tx["type"] == "CREDIT":
        net_balance += tx["amount"]
        total_credit += tx["amount"]
    elif tx["type"] == "DEBIT":
        net_balance -= tx["amount"]
        total_debit += tx["amount"]

print(f"Total Credit : ${total_credit:.2f}")
print(f"Total Debit  : ${total_debit:.2f}")
print(f"Net Balance  : ${net_balance:.2f}")
