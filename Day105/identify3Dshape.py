def identifyshape():
    shape = input("Enter 3D shape (cube/sphere/cylinder): ").lower()

    if shape == "cube":
        print("Cube has 6 square faces.")
    elif shape == "sphere":
        print("Sphere has no edges or vertices.")
    elif shape == "cylinder":
        print("Cylinder has 2 circular faces.")
    else:
        print("Shape not found.")

identifyshape()