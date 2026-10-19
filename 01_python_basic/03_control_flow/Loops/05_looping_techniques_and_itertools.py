"""
EduBroTech Python Tutorial Series
Topic: Modern Looping Techniques & itertools Superpowers
Author: Rakesh Singh Bajetha (EduBroTech)
"""

from itertools import zip_longest, cycle, islice, pairwise
try:
    from itertools import batched  # Python 3.12+
except ImportError:
    # Fallback for Python < 3.12
    def batched(iterable, n):
        it = iter(iterable)
        while batch := tuple(islice(it, n)):
            yield batch

print("=" * 60)
print("1. ENUMERATE: INDEX & VALUE TRACKING")
print("=" * 60)

cloud_services = ["AWS Lambda", "Azure Functions", "GCP Cloud Run", "Kubernetes"]
print("Cloud compute rankings:")
for rank, service in enumerate(cloud_services, start=1):
    print(f"Rank {rank}: {service}")

print("\n" + "=" * 60)
print("2. ZIP: PARALLEL LOCK-STEP ITERATION")
print("=" * 60)

headers = ["Name", "Department", "Salary"]
record  = ["Rakesh Bajetha", "Engineering", 125000]

employee_dict = {}
for key, val in zip(headers, record):
    employee_dict[key] = val
print("Constructed dictionary from zip:", employee_dict)

print("\n" + "=" * 60)
print("3. ZIP_LONGEST: HANDLING UNEVEN ITERABLES")
print("=" * 60)

teams = ["Alpha", "Bravo", "Charlie", "Delta"]
leads = ["Alice", "Bob"]

print("Pairing teams with leads (fill missing with 'Unassigned'):")
for team, lead in zip_longest(teams, leads, fillvalue="Unassigned"):
    print(f"  Team {team:7} -> Lead: {lead}")

print("\n" + "=" * 60)
print("4. REVERSED & SORTED ITERATION")
print("=" * 60)

versions = ["v1.0", "v1.2", "v2.0", "v2.1"]
print("Rollback sequence (reversed):", end=" ")
for ver in reversed(versions):
    print(ver, end=" -> ")
print("Base")

print("\n" + "=" * 60)
print("5. PAIRWISE ITERATION (PYTHON 3.10+)")
print("=" * 60)

# Computing price deltas across consecutive timestamps
stock_ticks = [100.5, 102.0, 101.5, 104.0, 103.5]
print("Consecutive Price Movement:")
for prev_price, curr_price in pairwise(stock_ticks):
    delta = curr_price - prev_price
    direction = "📈 UP" if delta > 0 else "📉 DOWN"
    print(f"  {prev_price:.1f} -> {curr_price:.1f} | Change: {delta:+.2f} ({direction})")

print("\n" + "=" * 60)
print("6. BATCHED ITERATION (CHUNKING DATA)")
print("=" * 60)

records = [f"ID_{i:03d}" for i in range(1, 11)]
batch_size = 3

print(f"Batching {len(records)} items into chunks of {batch_size}:")
for batch_idx, batch in enumerate(batched(records, batch_size), start=1):
    print(f"  Batch #{batch_idx}: {batch}")

print("\n" + "=" * 60)
print("7. ROUND-ROBIN TASK DISPATCHING WITH CYCLE")
print("=" * 60)

workers = ["Worker-1 (Node A)", "Worker-2 (Node B)", "Worker-3 (Node C)"]
worker_pool = cycle(workers)

jobs = ["Job_Alpha", "Job_Beta", "Job_Gamma", "Job_Delta", "Job_Epsilon"]

print("Dispatching incoming jobs round-robin:")
for job in jobs:
    assigned_worker = next(worker_pool)
    print(f"  {job:12} assigned to -> {assigned_worker}")
