# Sum of first natural number using recursion
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

n = int(input("Enter N: "))

print("Sum =", sum_n(n))