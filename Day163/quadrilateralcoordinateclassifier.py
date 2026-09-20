def quadrilateralcoordinateclassifier():
    print("Quadrilateral Coordinate Classifier :")

    x1 = float(input("Enter x-coordinate of point 1: "))
    y1 = float(input("Enter y-coordinate of point 1: "))

    x2 = float(input("Enter x-coordinate of point 2: "))
    y2 = float(input("Enter y-coordinate of point 2: "))

    x3 = float(input("Enter x-coordinate of point 3: "))
    y3 = float(input("Enter y-coordinate of point 3: "))

    x4 = float(input("Enter x-coordinate of point 4: "))
    y4 = float(input("Enter y-coordinate of point 4: "))

    side1 = (x2 - x1) ** 2 + (y2 - y1) ** 2
    side2 = (x3 - x2) ** 2 + (y3 - y2) ** 2
    side3 = (x4 - x3) ** 2 + (y4 - y3) ** 2
    side4 = (x1 - x4) ** 2 + (y1 - y4) ** 2

    diagonal1 = (x3 - x1) ** 2 + (y3 - y1) ** 2
    diagonal2 = (x4 - x2) ** 2 + (y4 - y2) ** 2

    slope1 = None
    slope2 = None
    slope3 = None
    slope4 = None

    if x2 != x1:
        slope1 = (y2 - y1) / (x2 - x1)

    if x3 != x2:
        slope2 = (y3 - y2) / (x3 - x2)

    if x4 != x3:
        slope3 = (y4 - y3) / (x4 - x3)

    if x1 != x4:
        slope4 = (y1 - y4) / (x1 - x4)

    if side1 == side2 == side3 == side4:
        if diagonal1 == diagonal2:
            print("The quadrilateral is a square or a rhombus with equal diagonals.")
        else:
            print("The quadrilateral is a rhombus.")

    elif side1 == side3 and side2 == side4:
        if diagonal1 == diagonal2:
            print("The quadrilateral is a rectangle.")
        else:
            print("The quadrilateral is a parallelogram.")

    elif side1 == side2 and side3 == side4:
        print("The quadrilateral may be a kite.")

    elif slope1 == slope3 or slope2 == slope4:
        print("The quadrilateral may be a trapezium.")

    else:
        print("The quadrilateral is an irregular quadrilateral.")

    print("\nSide Lengths Squared:")
    print("Side 1:", side1)
    print("Side 2:", side2)
    print("Side 3:", side3)
    print("Side 4:", side4)

    print("\nDiagonal Lengths Squared:")
    print("Diagonal 1:", diagonal1)
    print("Diagonal 2:", diagonal2)

quadrilateralcoordinateclassifier()