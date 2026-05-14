# Take a number as input and find the largest digit  the number using for loop
n = input("Enter a number: ")

max = '0'

for i in n:
    if i > max:
        max_digit = i

print("Largest Digit in", n, "is", max)
