# Count Consonants
s=input("Enter a string: ")
count=0
for ch in s:
    if ch.isalpha() and ch not in "aeiouAEIOU":
           count+=1
print("Total Consonants: ",count)

