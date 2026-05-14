# Take a number as input from user and print all prime numbers from 1 to n using for loop
n = int(input("Enter n: "))
print("Prime numbers are: ",end=" ")

for num in range(2, n + 1):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num, end=" ")