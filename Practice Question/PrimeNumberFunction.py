# Prime Number
def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("Enter a number: "))

if prime(n):
    print("Prime")
else:
    print("Not Prime")