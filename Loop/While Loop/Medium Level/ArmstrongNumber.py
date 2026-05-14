# Check the number is armstrong or not
n = int(input("Enter number: "))

temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit * digit * digit
    n = n // 10

if temp == sum:
    print("Armstrong")
else:
    print("Not Armstrong")