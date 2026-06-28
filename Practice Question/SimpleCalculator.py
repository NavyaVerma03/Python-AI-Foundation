# Simple Calculator
n1 = int(input("Enter no1: "))
n2 = int(input("Enter no2: "))

opt = input("Enter operator (+, -, *, /, %): ")

match opt:
    case '+':
        print("Addition:", n1 + n2)

    case '-':
        print("Subtraction:", n1 - n2)

    case '*':
        print("Multiplication:", n1 * n2)

    case '/':
        if n2 != 0:
            print("Division:", n1 / n2)
        else:
            print("Cannot divide by zero")

    case '%':
        if n2 != 0:
            print("Remainder:", n1 % n2)
        else:
            print("Cannot divide by zero")

    case _:
        print("Invalid operator")


