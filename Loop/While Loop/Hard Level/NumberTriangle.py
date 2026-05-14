# Number Triangle

n = int(input("Enter number: "))

i = 1

while i <= n:

    j = 1

    while j <= i:
        print(j, end="")
        j += 1

    print()
    i += 1