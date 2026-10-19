"""
EduBroTech Python Tutorial Series
Topic: Loop Control Statements - break, continue, pass & Multi-level Break
Author: Rakesh Singh Bajetha (EduBroTech)
"""

print("=" * 60)
print("1. THE 'break' STATEMENT: EARLY TERMINATION")
print("=" * 60)

# Searching for target item; exit immediately when found
search_target = "TARGET_KEY"
keys = ["KEY_01", "KEY_02", "TARGET_KEY", "KEY_04", "KEY_05"]

for idx, key in enumerate(keys):
    if key == search_target:
        print(f"Target found at index {idx}! Breaking out of loop.")
        break
    print(f"Inspecting key: {key}")

print("\n" + "=" * 60)
print("2. THE 'continue' STATEMENT: SKIPPING ITERATIONS")
print("=" * 60)

# Skip invalid, null, or negative transactions
raw_inputs = [100, -5, None, 250, "invalid", 400]

print("Processing valid entries only:")
for item in raw_inputs:
    # Guard clauses using continue
    if item is None or not isinstance(item, (int, float)) or item < 0:
        print(f"  [SKIPPED] Invalid entry: {item}")
        continue
    print(f"  [PROCESSED] Clean amount: ${item}")

print("\n" + "=" * 60)
print("3. THE 'pass' STATEMENT: NO-OP PLACEHOLDER")
print("=" * 60)

# pass is syntactically required where Python expects a block but no action is needed
for i in range(5):
    if i == 2:
        pass  # TODO: Implement specialized telemetry tracking for step 2 in future release
    else:
        print(f"Executing step {i}")

print("\n" + "=" * 60)
print("4. HOW TO BREAK OUT OF MULTIPLE NESTED LOOPS CLEANLY")
print("=" * 60)

matrix = [
    [10, 20, 30],
    [40, 999, 60],
    [70, 80, 90]
]
target = 999

print("--- Technique A: Using a Flag Variable ---")
found = False
for r_idx, row in enumerate(matrix):
    for c_idx, val in enumerate(row):
        if val == target:
            print(f"Found {target} at row {r_idx}, col {c_idx}")
            found = True
            break
    if found:
        break

print("\n--- Technique B: Encapsulating in a Function with return (Recommended) ---")
def find_in_matrix(grid, val_to_find):
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == val_to_find:
                return (r, c)
    return None

coords = find_in_matrix(matrix, target)
print(f"Function return cleanly exited nested loops: Found at coords {coords}")

print("\n--- Technique C: Using itertools.product (Flattens 2 loops into 1) ---")
from itertools import product

for r, c in product(range(len(matrix)), range(len(matrix[0]))):
    if matrix[r][c] == target:
        print(f"Single break via itertools.product: Found at ({r}, {c})")
        break
