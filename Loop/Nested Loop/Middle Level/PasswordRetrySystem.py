# Password retry system using nested loops
correct_password = "admin"
for i in range(3):
    password = input("Enter password: ")
    if password == correct_password:
        print("Login Successful")
        break
    else:
        print("Wrong password! Try again")