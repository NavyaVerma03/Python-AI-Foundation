# Create nested loop login system

correct_password = "1234"

for attempt in range(3):

    password = input("Enter password: ")

    for i in password:

        pass

    if len(password) < 4:
        print("Password too short")
        continue

    if password == correct_password:
        print("Login successful")
        break

    else:
        print("Wrong password")