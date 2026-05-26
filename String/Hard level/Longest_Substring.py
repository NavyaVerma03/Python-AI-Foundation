# Find longest substring without repeating characters.
s=input("Enter string: ")
maxlength=0
for i in range(len(s)):
    visited=set()
    count=0
    for j in range(len(s)):
        if s[i] in visited:
            break
        if s[j] in visited:
            break

        visited.add(s[j])
        count+=1

        maxlength=max(maxlength,count)

print("Longest Length: ",maxlength)