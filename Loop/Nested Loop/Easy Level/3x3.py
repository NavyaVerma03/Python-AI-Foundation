# Print 3x3 matrix but break outer loop if i == 3
for i in range(1, 5):
    if i == 3:
        break
    for j in range(1, 4):
        print(j, end="")
    print()