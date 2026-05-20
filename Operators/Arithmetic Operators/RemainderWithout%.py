#  Take two numbers and print remainder without using %.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

remainder = a - (a // b) * b

print("Remainder =", remainder)