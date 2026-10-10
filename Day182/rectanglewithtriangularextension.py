def rectanglewithtriangularextension():
    print("Rectangle with Triangular Extension :")

    length = float(input("Enter rectangle length: "))
    width = float(input("Enter rectangle width: "))
    triangle_base = float(input("Enter triangular extension base: "))
    triangle_height = float(input("Enter triangular extension height: "))

    if length <= 0 or width <= 0 or triangle_base <= 0 or triangle_height <= 0:
        print("All measurements must be greater than zero.")
        return

    rectangle_area = length * width
    triangle_area = 0.5 * triangle_base * triangle_height
    total_area = rectangle_area + triangle_area

    print("\nComposite Shape Result :")
    print("Rectangle Area:", round(rectangle_area, 2))
    print("Triangular Extension Area:", round(triangle_area, 2))
    print("Total Area:", round(total_area, 2))

    if triangle_base == length:
        print("The triangular base matches the rectangle length.")
    else:
        print("The triangular base differs from the rectangle length.")

rectanglewithtriangularextension()