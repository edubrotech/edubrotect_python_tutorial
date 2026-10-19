"""
EduBroTech Python Tutorial Series
Topic: CPython Loop Internals, Iterator Protocol & Common Traps
Author: Rakesh Singh Bajetha (EduBroTech)
"""

import dis
import time

print("=" * 60)
print("1. UNDER THE HOOD: CPYTHON ITERATOR PROTOCOL")
print("=" * 60)

# A for loop in Python is syntax sugar for iter(), next(), and StopIteration
sample_list = ["Alpha", "Beta", "Gamma"]

# Manual simulation of what Python interpreter does under the hood:
print("Simulating Python 'for' loop manually:")
iterator = iter(sample_list)  # Calls sample_list.__iter__()
while True:
    try:
        item = next(iterator) # Calls iterator.__next__()
        print(f"  Underlying VM fetched: {item}")
    except StopIteration:
        print("  StopIteration exception caught. Loop finished cleanly!")
        break

print("\n" + "=" * 60)
print("2. BYTECODE DISASSEMBLY OF A FOR LOOP (dis module)")
print("=" * 60)

def loop_example():
    for x in [1, 2]:
        pass

# Displaying CPython bytecode instructions (GET_ITER, FOR_ITER)
print("CPython Bytecode instructions:")
dis.dis(loop_example)

print("\n" + "=" * 60)
print("3. PITFALL #1: MUTATING A LIST WHILE ITERATING (INDEX SKIPPING BUG)")
print("=" * 60)

# Buggy code: Attempting to remove even numbers while looping directly
bad_numbers = [1, 2, 2, 3, 4, 5]
print("Original list:", bad_numbers)

for num in bad_numbers:
    if num % 2 == 0:
        bad_numbers.remove(num)

print("Result after faulty loop:", bad_numbers)
print("Notice the second '2' was SKIPPED! Because removing shifts the index forward.")

# The Idiomatic Fix: Use a list comprehension or iterate over a shallow copy
fix_numbers = [1, 2, 2, 3, 4, 5]
clean_numbers = [n for n in fix_numbers if n % 2 != 0]
print("Result with list comprehension fix:", clean_numbers)

print("\n" + "=" * 60)
print("4. PITFALL #2: MUTATING A DICTIONARY DURING ITERATION")
print("=" * 60)

session_cache = {
    "user_1": "active",
    "user_2": "expired",
    "user_3": "expired",
    "user_4": "active"
}

# Modifying directly raises: RuntimeError: dictionary changed size during iteration
# Safe fix: Iterate over a static snapshot of the keys using list()
print("Evicting expired sessions safely:")
for user_id in list(session_cache.keys()):
    if session_cache[user_id] == "expired":
        del session_cache[user_id]
        print(f"  Evicted: {user_id}")
print("Active sessions remaining:", session_cache)

print("\n" + "=" * 60)
print("5. PITFALL #3: LATE-BINDING CLOSURES IN LOOPS")
print("=" * 60)

# Buggy: Functions created in a loop bind the variable name, not the current value
faulty_multipliers = [lambda x: x * i for i in range(4)]
print("Faulty closures calling multiplier(2):", [f(2) for f in faulty_multipliers])
print("All returned 6! Because 'i' finished at 3 when invoked.")

# Fixed: Use default parameter value to bind at definition time
correct_multipliers = [lambda x, current_i=i: x * current_i for i in range(4)]
print("Fixed closures calling multiplier(2):", [f(2) for f in correct_multipliers])

print("\n" + "=" * 60)
print("6. PERFORMANCE: LIST COMPREHENSION VS FOR LOOP APPEND")
print("=" * 60)

N = 200_000

# Benchmark for loop + append
start_loop = time.perf_counter()
res_loop = []
for i in range(N):
    res_loop.append(i * 2)
end_loop = time.perf_counter()
loop_time = (end_loop - start_loop) * 1000

# Benchmark list comprehension (optimized in C bytecode via LIST_APPEND)
start_comp = time.perf_counter()
res_comp = [i * 2 for i in range(N)]
end_comp = time.perf_counter()
comp_time = (end_comp - start_comp) * 1000

print(f"For Loop + Append  Time : {loop_time:.2f} ms")
print(f"List Comprehension Time : {comp_time:.2f} ms")
print(f"Speedup                 : {loop_time / comp_time:.2f}x faster with Comprehension!")
