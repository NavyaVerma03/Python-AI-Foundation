# Nested loop: Print coordinates (i, j) and break if i == j
for i in range(1, 5):
    for j in range(1, 5):
        if i == j:
            break
        print(f"({i},{j})", end=" ")
    print()