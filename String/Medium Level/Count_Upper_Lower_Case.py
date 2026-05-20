# Count Uppercase & Lowercase
s = input("Enter String: ")

upper = 0
lower = 0

for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)