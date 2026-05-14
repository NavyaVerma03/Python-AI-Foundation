# Password Validation Loop

password = ""

while password != "1234":

    password = input("Enter password: ")

    if password != "1234":
        print("Wrong password")

print("Login Successful")