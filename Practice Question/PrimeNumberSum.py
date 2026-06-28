# Find the sum of all prime numbers between 1 and N.
n=int(input("Enter no: "))
sum=0
for i in range(2,n+1):
    count = 0
    for j in range(2,i):
        if i%j==0:
            count=count+1
    if count==0:
        sum=sum+i
print(sum)