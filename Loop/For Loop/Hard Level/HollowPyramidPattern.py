# Hollow pyramid pattern
n = int(input("Enter rows: "))

for i in range(1, n + 1):
    # spaces
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")

    print()