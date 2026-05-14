# Count the frequency of the digit in given number n

n = int(input("Enter number: "))

d = 0
while d <= 9:
    temp = n
    count = 0

    while temp > 0:
        digit = temp % 10
        if digit == d:
            count += 1
        temp = temp // 10

    if count > 0:
        print(d, "->", count)

    d += 1