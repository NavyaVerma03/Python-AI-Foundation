# Calculate the electricity bill based on slab rates
units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 100 * 2 + (units - 100) * 3
elif units <= 300:
    bill = 100 * 2 + 100 * 3 + (units - 200) * 5
else:
    bill = 100 * 2 + 100 * 3 + 100 * 5 + (units - 300) * 7

print("Electricity Bill =", bill)