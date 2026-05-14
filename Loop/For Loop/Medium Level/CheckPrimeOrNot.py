# Take a number as input and check the  number is prime or not using for loop

n=int(input("Enter a number:"))
if n <= 1:
    print("Not a prime number")
else:
    for i in range(2,n):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")


