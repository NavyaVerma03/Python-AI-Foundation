# Print all Prime Numbers between 1 and N
n = int(input("Enter the value of N: "))

for i in range(2, n + 1):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        print(i, end=" ")