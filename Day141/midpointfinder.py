def midpointfinder():
    x1 = float(input("Enter x-coordinate of first point: "))
    y1 = float(input("Enter y-coordinate of first point: "))

    x2 = float(input("Enter x-coordinate of second point: "))
    y2 = float(input("Enter y-coordinate of second point: "))

    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2

    print("Midpoint:", (midpoint_x, midpoint_y))

midpointfinder()