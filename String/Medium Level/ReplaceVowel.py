# Replace Vowels
s = input("Enter string: ")

vowels = "aeiouAEIOU"

result = ""

for i in s:
    if i in vowels:
        result += "*"
    else:
        result += i

print(result)