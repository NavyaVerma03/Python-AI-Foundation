# Print square pattern but stop entire process if user enters 0
n = int(input("Enter number: "))

if n == 0:
    print("Program Stopped")
else:
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()