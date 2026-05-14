# Print fibonacci series of number n terms

n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 1
print("Fibonacci Series: ", end=" ")
while i <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    i += 1