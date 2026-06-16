def database():
    shapes = {
        "Triangle": 3,
        "Square": 4,
        "Rectangle": 4,
        "Pentagon": 5,
        "Hexagon": 6
    }

    for shape, sides in shapes.items():
        print(shape, "->", sides, "sides")

database()