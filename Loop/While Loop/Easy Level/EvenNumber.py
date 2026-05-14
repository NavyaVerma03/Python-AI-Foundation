# Print all even number up to n
n = int(input("Enter a number: "))

i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1