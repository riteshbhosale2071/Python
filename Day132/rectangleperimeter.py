def rectangleperimeter():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    if length <= 0 or width <= 0:
        print("Length and width must be positive.")
        return

    perimeter = 2 * (length + width)

    print("Perimeter of the Rectangle:", perimeter)

rectangleperimeter()