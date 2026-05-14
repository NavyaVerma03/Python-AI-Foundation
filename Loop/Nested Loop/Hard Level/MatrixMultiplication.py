# Print multiplication matrix but skip diagonal elements

for i in range(1, 6):

    for j in range(1, 6):

        if i == j:
            continue

        print(i * j, end=" ")

    print()