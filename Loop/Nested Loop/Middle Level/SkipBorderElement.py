# Print 5x5 pattern but skip border element
for i in range (5):
    for j in range (5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            continue
        print("*", end=" ")
    print()
