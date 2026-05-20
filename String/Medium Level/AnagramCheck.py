#  Anagram Check
s1 = input("Enter 1st Word: ")
s2 = input("Enter 2nd Word: ")
if sorted(s1) == sorted(s2):
    print(True)
else:
    print(False)