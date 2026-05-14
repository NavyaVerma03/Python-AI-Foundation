# Take a number as input and calculate the all even number sum and all odd number sum up to 1 to n using for loop
n = int(input("Enter number: "))

even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)