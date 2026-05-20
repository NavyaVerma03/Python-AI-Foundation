# Remove Duplicates
s = input("Enter a string: ")

result = ""

for i in s:
    if i not in result:
        result += i

print(result)