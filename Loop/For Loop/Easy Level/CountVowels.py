# Take# Take a string as input and count how many vowels its contains using for loop
s=input("Enter String:  ")
count=0
for i in s:
    if i in "aeiouAEIOU":
        count += 1
print("Total vowels in ", s,": ",count)