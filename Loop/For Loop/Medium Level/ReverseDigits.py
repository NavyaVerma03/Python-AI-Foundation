# Take a number as input and reverse the number using for loop
n = int(input("Enter a number: "))
print("Original Number = ",n)
rev=0
for i in range(n):
    if n == 0:
        break
    digit = n % 10
    rev = rev *10+digit
    n //= 10
print("Reverse Number = ",rev)