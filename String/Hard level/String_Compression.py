# Compress string using character counts.

s=input("Enter String: ")
result =""
count =1
for i in range(len(s)):
    if i< len(s)-1 and s[i] == s[i+1]:
        count+=1
    else:
        result += s[i] + str(count)
        count=1
print("Compressed String: ",result)
