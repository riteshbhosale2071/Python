def matchobject():
    shape = input("Enter 3D shape: ").lower()

    if shape == "cube":
        print("Net: 6 Squares")
    elif shape == "cuboid":
        print("Net: 6 Rectangles")
    elif shape == "cylinder":
        print("Net: 2 Circles and 1 Rectangle")
    elif shape == "cone":
        print("Net: 1 Circle and 1 Sector")
    else:
        print("Shape not found.")

matchobject()