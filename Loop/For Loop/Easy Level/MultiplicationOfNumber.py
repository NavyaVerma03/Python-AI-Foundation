# Take a number as input and print its table up to 10 using a for loop.

n=int(input("Enter the number: "))
for i in range(1,11):
    print(n, " X ", i, " = ", n*i)
