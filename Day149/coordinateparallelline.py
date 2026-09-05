def coordinateparallelline():
    print("Coordinate Parallel-Line Checker :")

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

    if x1 == x2 and y1 == y2:
        print("Line 1 is invalid: both points are identical.")
        return

    if x3 == x4 and y3 == y4:
        print("Line 2 is invalid: both points are identical.")
        return

    if x1 == x2 and x3 == x4:
        print("\nBoth lines are vertical.")
        print("The lines are Parallel.")
        return

    if x1 == x2 or x3 == x4:
        print("\nOne line is vertical and the other is not.")
        print("The lines are Not Parallel.")
        return

    slope1 = (y2 - y1) / (x2 - x1)
    slope2 = (y4 - y3) / (x4 - x3)

    print("\nParallel-Line Analysis :")
    print("Slope of Line 1:", slope1)
    print("Slope of Line 2:", slope2)

    if slope1 == slope2:
        print("The lines have equal slopes.")
        print("The lines are Parallel.")
    else:
        print("The lines have different slopes.")
        print("The lines are Not Parallel.")

coordinateparallelline()