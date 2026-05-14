# Print all factors of the number n

n = int(input("Enter number: "))

i = 1

print("Factors:", end="")
while i <= n:
    if n % i == 0:
        print(i, end=" ")
    i += 1