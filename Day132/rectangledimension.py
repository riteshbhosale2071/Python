def rectangledimension():
    area = float(input("Enter the area of the rectangle: "))
    length = float(input("Enter the length of the rectangle: "))

    if area <= 0 or length <= 0:
        print("Area and length must be positive.")
        return

    width = area / length

    print("Width of the Rectangle:", width)

rectangledimension()