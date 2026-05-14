# Print triangle pattern but stop program when row becomes 4

for i in range(1, 6):

    if i == 4:
        break

    for j in range(i):
        print("*", end=" ")

    print()