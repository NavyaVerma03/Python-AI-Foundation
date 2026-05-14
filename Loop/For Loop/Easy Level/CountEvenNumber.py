# Take a number as input and count how many even numbers exist between 1 and N
n=int(input("Enter the number: "))
count=0
for i in range(1,n+1):
    if(i%2==0):
        count += 1

print("Total even numbers: ",count)

