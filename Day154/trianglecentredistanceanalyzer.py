def trianglecentredistanceanalyzer():
    print("Triangle Centre Distance Analyzer :")

    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid triangle.")
        return

    x1 = float(input("Enter x-coordinate of A: "))
    y1 = float(input("Enter y-coordinate of A: "))

    x2 = float(input("Enter x-coordinate of B: "))
    y2 = float(input("Enter y-coordinate of B: "))

    x3 = float(input("Enter x-coordinate of C: "))
    y3 = float(input("Enter y-coordinate of C: "))

    perimeter = a + b + c

    gx = (x1 + x2 + x3) / 3
    gy = (y1 + y2 + y3) / 3

    ix = (a * x1 + b * x2 + c * x3) / perimeter
    iy = (a * y1 + b * y2 + c * y3) / perimeter

    distance = ((gx - ix) * (gx - ix) + (gy - iy) * (gy - iy)) ** 0.5

    print("\nTriangle Centre Distance :")
    print("Centroid: ({:.2f}, {:.2f})".format(gx, gy))
    print("Incentre: ({:.2f}, {:.2f})".format(ix, iy))
    print("Distance between Centroid and Incentre: {:.2f}".format(distance))

trianglecentredistanceanalyzer()