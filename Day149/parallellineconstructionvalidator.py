def parallellineconstructionvalidator():
    print("Parallel-Line Construction Validator :")

    print("\nEnter coordinates for Line 1:")
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    print("\nEnter coordinates for the proposed Line 2:")
    x3 = float(input("Enter x3: "))
    y3 = float(input("Enter y3: "))
    x4 = float(input("Enter x4: "))
    y4 = float(input("Enter y4: "))

    if x1 == x2 and y1 == y2:
        print("Line 1 is invalid.")
        return

    if x3 == x4 and y3 == y4:
        print("Line 2 is invalid.")
        return

    def slope(xa, ya, xb, yb):
        if xa == xb:
            return None
        return (yb - ya) / (xb - xa)

    slope1 = slope(x1, y1, x2, y2)
    slope2 = slope(x3, y3, x4, y4)

    print("\nConstruction Validation :")
    print("Line 1 Slope:", "Vertical" if slope1 is None else slope1)
    print("Line 2 Slope:", "Vertical" if slope2 is None else slope2)

    if slope1 is None and slope2 is None:
        parallel = True
    elif slope1 is None or slope2 is None:
        parallel = False
    else:
        parallel = abs(slope1 - slope2) < 1e-9

    if parallel:
        print("\nResult: Valid Parallel-Line Construction.")
        print("Both lines have the same direction.")
    else:
        print("\nResult: Invalid Parallel-Line Construction.")
        print("The two lines have different slopes.")

parallellineconstructionvalidator()