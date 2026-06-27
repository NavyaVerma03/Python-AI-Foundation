# Check whether a number is an Armstrong number.
num = int(input("Enter a number: "))

temp = num
digits = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
