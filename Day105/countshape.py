def countshape():
    shape = input("Enter 3D shape: ").lower()

    if shape == "cube":
        print("Faces = 6")
        print("Edges = 12")
        print("Vertices = 8")
    elif shape == "cuboid":
        print("Faces = 6")
        print("Edges = 12")
        print("Vertices = 8")
    elif shape == "cylinder":
        print("Faces = 3")
        print("Edges = 2")
        print("Vertices = 0")
    elif shape == "sphere":
        print("Faces = 1")
        print("Edges = 0")
        print("Vertices = 0")
    else:
        print("Shape not found.")

countshape()