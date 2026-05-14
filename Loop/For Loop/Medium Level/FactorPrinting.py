# Take a number as input and print the factor of this number using for loop

n=int(input("Enter a number: "))
print("Factors of",n,"are: ",end="")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")