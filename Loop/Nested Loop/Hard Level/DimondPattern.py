# Print diamond pattern but skip center line

n = 5

for i in range(n):

    if i == n // 2:
        continue

    for j in range(n - i - 1):
        print(" ", end="")

    for j in range(2 * i + 1):
        print("*", end="")

    print()