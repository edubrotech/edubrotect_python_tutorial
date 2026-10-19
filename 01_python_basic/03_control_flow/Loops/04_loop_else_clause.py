"""
EduBroTech Python Tutorial Series
Topic: The Python Loop 'else' Clause - Superpower for Flag-Free Code
Author: Rakesh Singh Bajetha (EduBroTech)
"""

print("=" * 60)
print("1. THE FOR-ELSE CLAUSE: SEARCH WITHOUT BOOLEAN FLAGS")
print("=" * 60)

users_db = [
    {"id": 101, "username": "rakesh", "status": "active"},
    {"id": 102, "username": "priya",  "status": "active"},
    {"id": 103, "username": "kavita", "status": "pending"},
]

def search_user(target_username: str):
    print(f"\nSearching for '{target_username}'...")
    for user in users_db:
        if user["username"] == target_username:
            print(f"✅ Found user: ID={user['id']}, Status={user['status']}")
            break
    else:
        # Executes ONLY IF loop finished without encountering 'break'
        print(f"❌ User '{target_username}' not registered in database.")

search_user("priya")     # Hits break -> else is skipped
search_user("vikram")    # Exhausts loop -> else executes!

print("\n" + "=" * 60)
print("2. PRIME NUMBER TEST WITH FOR-ELSE")
print("=" * 60)

def check_prime(n: int) -> bool:
    if n < 2:
        print(f"{n} is NOT prime (less than 2).")
        return False
    
    # Check divisors up to square root of n
    limit = int(n ** 0.5) + 1
    for i in range(2, limit):
        if n % i == 0:
            print(f"{n} is NOT prime (divisible by {i}).")
            break
    else:
        print(f"⭐ {n} IS A PRIME NUMBER! (No divisors found)")
        return True
    return False

check_prime(29)  # Prime -> else executes
check_prime(35)  # Divisible by 5 -> break hits, else skipped

print("\n" + "=" * 60)
print("3. THE WHILE-ELSE CLAUSE: RETRY EXHAUSTION GUARD")
print("=" * 60)

def connect_to_database(max_attempts=3):
    attempt = 1
    server_online = False  # Simulating server down
    
    print(f"Initiating DB connection (Max {max_attempts} attempts):")
    while attempt <= max_attempts:
        print(f"  Attempt {attempt}: Connecting to host:5432...")
        if server_online:
            print("  Connection established successfully!")
            break
        attempt += 1
    else:
        # Runs ONLY if while loop condition became False without a break
        print("🚨 CRITICAL: Database connection attempts completely exhausted!")
        print("   Action: Alerting on-call DevOps engineer.")

connect_to_database()
