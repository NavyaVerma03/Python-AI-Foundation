# Count digit in number n
n=int(input("Enter a number: "))
n = int(input("Enter number: "))
count = 0
if n == 0:
    count = 1
else:
    if n < 0:
        n = -n   # make positive

    while n > 0:
        n = n // 10
        count += 1

print("Total digits:", count)