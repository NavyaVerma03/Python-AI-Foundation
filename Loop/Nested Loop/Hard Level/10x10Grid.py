# Print 1-100 in 10x10 grid and stop if number is 57

num = 1

for i in range(10):

    for j in range(10):

        if num == 57:
            break

        print(num, end=" ")
        num += 1

    print()

    if num == 57:
        break