def shape():
    shape = input("Enter shape (cube/cuboid): ").lower()

    if shape == "cube":
        print("Edges = 12")
        print("Corners = 8")

    elif shape == "cuboid":
        print("Edges = 12")
        print("Corners = 8")

    else:
        print("Shape not available")

shape()