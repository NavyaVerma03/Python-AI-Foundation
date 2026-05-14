# LCM using while loop

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

max_num = a if a > b else b
lcm = max_num

while True:

    if lcm % a == 0 and lcm % b == 0:
        print("LCM =", lcm)
        break

    lcm += 1