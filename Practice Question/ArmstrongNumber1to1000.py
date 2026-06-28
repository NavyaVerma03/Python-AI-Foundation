# Print all Armstrong numbers between 1 to 1000
print("Print Artmstrong Number between 1 and 1000: ")


for num in range(1,1001):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3
        temp = temp // 10
    if num == sum:
        print(num)

