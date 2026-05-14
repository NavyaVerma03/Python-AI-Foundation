# Take a number as input from user and check the number is palindrome or not using for loop
num = int(input("Enter number: "))
temp = num
rev = 0
count = len(str(num))

for i in range(count):
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if rev == num:
    print("Palindrome")
else:
    print("Not Palindrome")