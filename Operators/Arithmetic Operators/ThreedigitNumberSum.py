#  Take a 3-digit number and find sum of digits using % and //.

num = int(input("Enter a 3-digit number: "))

digit1 = num % 10
digit2 = (num // 10) % 10
digit3 = num // 100

sum_digits = digit1 + digit2 + digit3

print("Sum of Digits =", sum_digits)