database = {}

while True:

    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        username = input("Enter username: ")
        password = input("Enter password: ")

        database[username] = password

        print("Registration Successful")

    elif choice == 2:

        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in database and database[username] == password:
            print("Login Successful")

        else:
            print("Invalid Username or Password")

    elif choice == 3:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")