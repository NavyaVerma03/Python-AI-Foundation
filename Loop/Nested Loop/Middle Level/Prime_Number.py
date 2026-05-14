# Print prime numbers from 1 to 20 using nested loops
for num in range(2, 21):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)