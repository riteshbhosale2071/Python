def find():
    pattern = ["Circle", "Square", "Circle", "Square", "?"]

    if pattern[-2] == "Square":
        print("Missing Shape = Circle")

    elif pattern[-2] == "Circle":
        print("Missing Shape = Square")

find()