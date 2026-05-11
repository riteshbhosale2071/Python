def find():
    email = input("Enter email: ")

    username = email.split("@")[0]

    print("Username =", username)

find()