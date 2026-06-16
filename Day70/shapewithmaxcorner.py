def corners():
    shapes = {
        "Triangle": 3,
        "Square": 4,
        "Rectangle": 4,
        "Pentagon": 5,
        "Hexagon": 6
    }

    max_shape = max(shapes, key=shapes.get)

    print("Shape with Maximum Corners =", max_shape)
    print("Number of Corners =", shapes[max_shape])

corners()