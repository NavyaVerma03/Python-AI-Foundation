# Find first pair (i, j) where i*j equals target

target = 12
found = False

for i in range(1, 10):

    for j in range(1, 10):

        if i * j == target:
            print(i, j)
            found = True
            break

    if found:
        break