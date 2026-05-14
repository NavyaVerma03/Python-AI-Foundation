# Create simple ATM system using nested loop

while True:

    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance: 5000")

    elif choice == "2":
        print("Withdraw option")

    elif choice == "3":
        print("Thank you")
        break

    else:
        print("Invalid choice")
        continue