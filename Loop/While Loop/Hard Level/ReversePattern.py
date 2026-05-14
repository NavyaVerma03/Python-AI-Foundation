# Reverse Pattern

n = int(input("Enter number: "))

i = n

while i >= 1:
    j = 1

    while j <= i:
        print("*", end=" ")
        j += 1

    print()
    i -= 1