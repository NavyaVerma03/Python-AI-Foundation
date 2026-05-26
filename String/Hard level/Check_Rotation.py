# Check if s2 is rotation of s1.

s1 = input("Enter First String: ")
s2 = input("Enter Second String: ")

temp = s1 + s1

if s2 in temp and len(s1) == len(s2):
    print("true")

else:
    print("false")