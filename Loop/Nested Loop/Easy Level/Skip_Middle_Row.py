# Print pattern but skip middle row using continue
for i in range(1, 6):
    if i == 3:
        continue
    for j in range(5):
        print("*", end="")
    print()