def trianglerectanglecompositearea():
    print("Triangle-and-Rectangle Composite Area :")

    length = float(input("Enter rectangle length: "))
    width = float(input("Enter rectangle width: "))
    base = float(input("Enter triangle base: "))
    height = float(input("Enter triangle height: "))

    if length <= 0 or width <= 0 or base <= 0 or height <= 0:
        print("All measurements must be greater than zero.")
        return

    rectangle_area = length * width
    triangle_area = 0.5 * base * height
    total_area = rectangle_area + triangle_area

    print("\nArea Calculation :")
    print("Rectangle Area:", round(rectangle_area, 2))
    print("Triangle Area:", round(triangle_area, 2))
    print("Combined Area:", round(total_area, 2))

    if rectangle_area > triangle_area:
        print("The rectangle has the larger area.")
    elif triangle_area > rectangle_area:
        print("The triangle has the larger area.")
    else:
        print("Both shapes have equal areas.")

trianglerectanglecompositearea()