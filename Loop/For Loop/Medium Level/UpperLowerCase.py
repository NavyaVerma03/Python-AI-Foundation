# Take a string as input and count upper and lower case character using for loop
s = input("Enter a string: ")

upper = 0
lower = 0

for i in s:
    if i >= 'A' and i <= 'Z':
        upper += 1
    elif i >= 'a' and i <= 'z':
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)