# Find largest digit in number n

n = int(input("Enter number: "))

if n < 0:
    n = -n

largest = 0

while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n = n // 10

print("Largest digit:", largest)