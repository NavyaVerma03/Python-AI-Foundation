# Multiplication table but skip multiples of 5 using continue
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j

        if result % 5 == 0:
            continue

        print(result, end=" ")
    print()