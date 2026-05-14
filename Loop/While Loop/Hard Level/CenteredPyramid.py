# Centered Pyramid

n = int(input("Enter Row: "))

i = 1

while i <= n:

    space = 1

    while space <= n - i:
        print(" ", end="")
        space += 1

    star = 1

    while star <= (2 * i - 1):
        print("*", end="")
        star += 1

    print()
    i += 1