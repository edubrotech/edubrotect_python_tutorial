"""
EduBroTech Python Tutorial Series
Topic: While Loops in Python - Features, Patterns & Best Practices
Author: Rakesh Singh Bajetha (EduBroTech)
"""

print("=" * 60)
print("1. BASIC CONDITION-CONTROLLED WHILE LOOP")
print("=" * 60)

# Counting up with a loop variable
count = 1
while count <= 5:
    print(f"Iteration #{count}")
    count += 1

print("\n" + "=" * 60)
print("2. SENTINEL-CONTROLLED LOOP (SIMULATED USER COMMAND STREAM)")
print("=" * 60)

# Simulating an input stream of commands
command_stream = ["status", "help", "metrics", "quit", "unreachable"]
stream_index = 0

while stream_index < len(command_stream):
    cmd = command_stream[stream_index]
    stream_index += 1
    
    if cmd == "quit":
        print("Sentinel command 'quit' received. Shutting down worker...")
        break
    print(f"Processing command: [{cmd}]")

print("\n" + "=" * 60)
print("3. WALRUS OPERATOR (:=) IN WHILE LOOPS (PYTHON 3.8+)")
print("=" * 60)

# The walrus operator (assignment expression) allows assigning and testing in one line
simulated_network_buffer = ["chunk_A", "chunk_B", "chunk_C", ""]  # "" simulates EOF

buffer_iter = iter(simulated_network_buffer)

# Traditional way: chunk = buffer.pop(); while chunk: ...
# Modern Pythonic way with walrus:
while (data_chunk := next(buffer_iter)) != "":
    print(f"Received buffer stream chunk: {data_chunk}")
print("End of Stream reached.")

print("\n" + "=" * 60)
print("4. RETRY WITH EXPONENTIAL BACKOFF PATTERN")
print("=" * 60)

import time

def mock_unstable_api_call(attempt: int) -> bool:
    """Simulates an API that fails twice before succeeding on attempt 3."""
    return attempt >= 3

max_retries = 5
attempt = 1
delay = 0.05  # Short delay for fast test execution
success = False

while attempt <= max_retries:
    print(f"Attempt {attempt}/{max_retries}: Calling remote service...")
    if mock_unstable_api_call(attempt):
        print(f"✅ Service responded successfully on attempt {attempt}!")
        success = True
        break
    print(f"❌ Failed. Backing off for {delay:.2f}s before retry...")
    time.sleep(delay)
    delay *= 2  # Exponential backoff
    attempt += 1

if not success:
    print("🚨 All retry attempts exhausted. Raising Alert.")

print("\n" + "=" * 60)
print("5. STATE FLAG CONTROL PATTERN")
print("=" * 60)

system_running = True
ticks = 0

while system_running:
    ticks += 1
    print(f"Heartbeat tick: {ticks}")
    if ticks >= 3:
        system_running = False
        print("Flag changed to False: Gracefully terminating loop.")
