def find():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if a < b:
        print(a, "comes first")

    elif b < a:
        print(b, "comes first")

    else:
        print("Both numbers are equal")

find()