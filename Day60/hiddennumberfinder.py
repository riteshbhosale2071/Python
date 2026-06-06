def find():
    numbers = [5, 8, 3, 12, 7]

    hidden = int(input("Enter number to find: "))

    if hidden in numbers:
        print("Number Found")

    else:
        print("Number Not Found")

find()