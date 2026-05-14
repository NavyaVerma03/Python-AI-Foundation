# Check string palindrome or not
s = input("Enter String: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
