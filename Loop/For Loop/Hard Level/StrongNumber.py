# Take a number as input from user and check the number is strong or not using for loop
num = int(input("Enter number: "))
temp = num
sum = 0

for i in str(num):
    fact = 1
    for j in range(1, int(i)+1):
        fact *= j
    sum += fact

if sum == num:
    print("Strong Number")
else:
    print("Not Strong Number")