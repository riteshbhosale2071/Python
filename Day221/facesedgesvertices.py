def facesedgesvertices():
    print("3D Shape: Faces, Edges and Vertices")
    print("1. Cube")
    print("2. Cuboid")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        print("\nCube:")
        print("Faces: 6")
        print("Edges: 12")
        print("Vertices: 8")
    elif choice == 2:
        print("\nCuboid:")
        print("Faces: 6")
        print("Edges: 12")
        print("Vertices: 8")
    else:
        print("Invalid choice!")

facesedgesvertices()