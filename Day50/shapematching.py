def create():
    shape1 = input("Enter first shape: ").lower()
    shape2 = input("Enter second shape: ").lower()

    if shape1 == shape2:
        print("Shapes Match")

    else:
        print("Shapes Do Not Match")

create()