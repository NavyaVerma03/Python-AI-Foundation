# Count Vowel
s=input("Enter String: ")
count =0
for ch in s:
    if ch in "aeiouAEIOU":
        count+=1
print("Total Vowel: ",count)