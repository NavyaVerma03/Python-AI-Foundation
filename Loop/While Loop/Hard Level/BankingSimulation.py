# Banking Simulation

balance = 5000

while balance > 0:

    print("Current Balance =", balance)

    withdraw = int(input("Enter withdraw amount: "))

    if withdraw > balance:
        print("Insufficient Balance")
        break

    balance -= withdraw

print("Final Balance =", balance)