# Print numbers 1-25 in 5x5 grid with FizzBuzz

num = 1

for i in range(5):

    for j in range(5):

        if num % 3 == 0:
            print("Fizz", end=" ")
            num += 1
            continue

        if num % 5 == 0:
            print("Buzz", end=" ")
            num += 1
            continue

        print(num, end=" ")
        num += 1

    print()