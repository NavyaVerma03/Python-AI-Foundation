# Convert decimal to binary

n = int(input("Enter decimal number: "))
binary = 0
place = 1

while n > 0:
    rem = n % 2
    binary = binary + rem * place
    place = place * 10
    n = n // 2

print("Binary:", binary)

