# Skip printing even numbers inside nested loop
for i in range(1, 4):
    for j in range(1, 6):
        if j % 2 == 0:
            continue
        print(j, end="")
    print()