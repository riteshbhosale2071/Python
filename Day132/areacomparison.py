def areacomparison():
    shape1 = input("Enter first shape (rectangle/circle): ").lower()
    shape2 = input("Enter second shape (rectangle/circle): ").lower()

    def calculate_area(shape):
        if shape == "rectangle":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))

            if length <= 0 or width <= 0:
                return None

            return length * width

        elif shape == "circle":
            radius = float(input("Enter radius: "))

            if radius <= 0:
                return None

            return 3.14159 * radius * radius

        else:
            return None

    area1 = calculate_area(shape1)
    area2 = calculate_area(shape2)

    if area1 is None or area2 is None:
        print("Invalid shape or dimensions.")
        return

    print("Area of First Shape:", area1)
    print("Area of Second Shape:", area2)

    if area1 > area2:
        print("First shape has the larger area.")
    elif area1 < area2:
        print("Second shape has the larger area.")
    else:
        print("Both shapes have equal areas.")

areacomparison()