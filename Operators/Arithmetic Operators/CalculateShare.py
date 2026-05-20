# Take total bill and number of people, calculate per person share.

bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))

share = bill / people

print("Per Person Share =", share)