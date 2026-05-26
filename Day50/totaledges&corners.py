def find():
    shapes = {
        "cube": {"edges": 12, "corners": 8},
        "cuboid": {"edges": 12, "corners": 8},
        "triangle": {"edges": 3, "corners": 3},
        "square": {"edges": 4, "corners": 4}
    }

    shape = input("Enter shape name: ").lower()

    if shape in shapes:

        print("Edges =", shapes[shape]["edges"])
        print("Corners =", shapes[shape]["corners"])

    else:
        print("Shape not found")

find()