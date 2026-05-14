# Menu Driven Calculator

choice = 0

while choice != 4:

    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice >= 1 and choice <= 3:

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == 1:
            print("Result =", a + b)

        elif choice == 2:
            print("Result =", a - b)

        elif choice == 3:
            print("Result =", a * b)

    elif choice == 4:
        print("Calculator Closed")

    else:
        print("Invalid Choice")