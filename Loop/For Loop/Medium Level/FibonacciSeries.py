# Take a number as input and print fibonacci series up to nth term using for loop
n = int(input("Enter a number: "))
first=0
second=1
print("Fibonacci Series of",n, "terms:",end=" ")
for i in range(n):
    print(first,end=" ")
    third=first+second
    first=second
    second=third

