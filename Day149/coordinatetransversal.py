def coordinatetransversal():
    print("Coordinate Transversal Analyzer :")

    print("\nEnter coordinates for Line 1:")
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    print("\nEnter coordinates for Line 2:")
    x3 = float(input("Enter x3: "))
    y3 = float(input("Enter y3: "))
    x4 = float(input("Enter x4: "))
    y4 = float(input("Enter y4: "))

    print("\nEnter coordinates for the Transversal:")
    x5 = float(input("Enter x1: "))
    y5 = float(input("Enter y1: "))
    x6 = float(input("Enter x2: "))
    y6 = float(input("Enter y2: "))

    if (x1 == x2 and y1 == y2) or (x3 == x4 and y3 == y4) or (x5 == x6 and y5 == y6):
        print("A line cannot be formed from two identical points.")
        return

    def get_slope(xa, ya, xb, yb):
        if xa == xb:
            return None
        return (yb - ya) / (xb - xa)

    slope1 = get_slope(x1, y1, x2, y2)
    slope2 = get_slope(x3, y3, x4, y4)
    transversal_slope = get_slope(x5, y5, x6, y6)

    print("\nCoordinate Transversal Analysis :")

    print("Line 1 Slope:", "Vertical" if slope1 is None else slope1)
    print("Line 2 Slope:", "Vertical" if slope2 is None else slope2)
    print("Transversal Slope:",
          "Vertical" if transversal_slope is None else transversal_slope)

    if slope1 is None and slope2 is None:
        parallel = True
    elif slope1 is None or slope2 is None:
        parallel = False
    else:
        parallel = slope1 == slope2

    if slope1 is None and transversal_slope is None:
        intersects = False
    elif slope1 is None or transversal_slope is None:
        intersects = True
    else:
        intersects = slope1 != transversal_slope

    print("\nParallel Lines:", "Yes" if parallel else "No")
    print("Transversal Intersects the Parallel Direction:",
          "Yes" if intersects else "No")

    if parallel and intersects:
        print("Result: The third line can act as a transversal.")
    else:
        print("Result: A valid parallel-line/transversal configuration is not established.")

coordinatetransversal()