# Predefined username and password
username = "dinesh"
password = "12345"

# Ask user for input
entered_user_name = input("Enter username: ")

if entered_user_name== username:
    entered_passworld = input("Enter password: ")
    if entered_passworld == password:
        print("Login Successful ")
    else:
        print("Incorrect Password ")
else:
    print("Incorrect Username ")
