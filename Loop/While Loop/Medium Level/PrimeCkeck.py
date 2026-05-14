# Check the number is prime or not

n = int(input("Enter number: "))

i = 2

while i < n:
    if n % i == 0:
        print("Not Prime")
        break
    i += 1
else:
    if n > 1:
        print("Prime")
    else:
        print("Not Prime")