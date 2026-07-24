def surfacecount():
    shape = input("Enter 3D shape: ").lower()

    if shape == "cube":
        print("Surfaces = 6")
    elif shape == "cuboid":
        print("Surfaces = 6")
    elif shape == "cylinder":
        print("Surfaces = 3")
    elif shape == "cone":
        print("Surfaces = 2")
    elif shape == "sphere":
        print("Surfaces = 1")
    else:
        print("Shape not found.")

surfacecount()