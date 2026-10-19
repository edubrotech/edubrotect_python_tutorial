"""
EduBroTech Python Tutorial Series
Topic: Nested Loops, Matrix Traversal & Pattern Algorithms
Author: Rakesh Singh Bajetha (EduBroTech)
"""

print("=" * 60)
print("1. 2D MATRIX TRAVERSAL & DIAGONAL EXTRACTION")
print("=" * 60)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Row-by-row traversal:")
for r_idx, row in enumerate(matrix):
    for c_idx, val in enumerate(row):
        print(f"[{r_idx}][{c_idx}]={val}", end="  ")
    print()

print("\nExtracting primary diagonal:")
primary_diagonal = []
for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])
print("Primary Diagonal:", primary_diagonal)

print("\n" + "=" * 60)
print("2. MULTIPLICATION TABLE GRID (1 to 5)")
print("=" * 60)

for row in range(1, 6):
    for col in range(1, 6):
        print(f"{row * col:3}", end=" ")
    print()

print("\n" + "=" * 60)
print("3. CLASSIC INTERVIEW PATTERN PRINTING ALGORITHMS")
print("=" * 60)

height = 5

print("Pattern A: Right-Angled Star Triangle")
for i in range(1, height + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nPattern B: Inverted Star Triangle")
for i in range(height, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nPattern C: Centered Pyramid Pattern")
for i in range(1, height + 1):
    # Leading spaces
    for s in range(height - i):
        print(" ", end="")
    # Stars
    for star in range(2 * i - 1):
        print("*", end="")
    print()

print("\nPattern D: Floyd's Number Triangle")
current_num = 1
for i in range(1, height + 1):
    for j in range(i):
        print(f"{current_num:2}", end=" ")
        current_num += 1
    print()

print("\n" + "=" * 60)
print("4. CARTESIAN PRODUCT & GRID GENERATION")
print("=" * 60)

files = ["A", "B", "C"]
ranks = [1, 2, 3]

print("Generating 3x3 Chess Grid Coordinates:")
chessboard_squares = []
for f in files:
    for r in ranks:
        chessboard_squares.append(f"{f}{r}")
print("Squares:", chessboard_squares)
