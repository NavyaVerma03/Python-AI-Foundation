# Take a number as input and check the  number is amrstrong or not using for loop

n = int(input("Enter number: "))
temp = n
sum = 0

for i in range(1, n + 1):
    if temp == 0:
        break
    digit = temp % 10
    sum += digit ** 3
    temp = temp // 10

if sum == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")