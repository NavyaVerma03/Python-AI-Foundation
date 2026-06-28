# Print Pascal's Triangle for n row
n=int(input("Enter row:"))
for i in range(n):
    num = 1
    for j in range(i+1):
        print(num,end=" ")
        num = num * (i - j) // (j + 1)
    print()
