# Take a number as input and print the sum of numbers from 1 to n it using a for loop.

n=int(input("Enter the number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i   
print("The sum of numbers from 1 to",n,"is",sum)