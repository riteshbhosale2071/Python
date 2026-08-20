def trianglearea():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    if base <= 0 or height <= 0:
        print("Base and height must be positive.")
        return

    area = 0.5 * base * height

    print("Area of the Triangle:", area)

trianglearea()