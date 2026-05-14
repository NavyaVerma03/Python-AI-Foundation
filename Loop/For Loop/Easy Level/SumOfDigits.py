# Take a number as input and calculate the sum of digits using a for loop.
n = input("Enter no:  ")
sum=0
for i in n:
   sum +=int(i)
print("Sum of all digits of ",n,": ",sum)
