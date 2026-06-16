def symmetric():
    shape = input("Enter shape name: ").lower()

    symmetrical_shapes = ["circle", "square", "rectangle", "equilateral triangle"]

    if shape in symmetrical_shapes:
        print("Symmetrical Shape")

    else:
        print("Not a Symmetrical Shape")

symmetric()