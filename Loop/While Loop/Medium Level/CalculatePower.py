# Calculate Power without using ** operator

base = int(input("Enter base: "))
power = int(input("Enter power: "))

result = 1
i = 1

while i <= power:
    result = result * base
    i += 1

print("Result:", result)
