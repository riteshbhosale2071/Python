def shapearea():
    length = float(input("Enter rectangle length: "))
    width = float(input("Enter rectangle width: "))

    side = float(input("Enter square side: "))

    rectangle_area = length * width
    square_area = side * side

    print("Rectangle Area =", rectangle_area)
    print("Square Area =", square_area)

    if rectangle_area > square_area:
        print("Rectangle has a larger area")

    elif square_area > rectangle_area:
        print("Square has a larger area")

    else:
        print("Both have the same area")

shapearea()