def midpointoftwocoordinates():
    x1 = float(input("Enter the X-coordinate of the first point: "))
    y1 = float(input("Enter the Y-coordinate of the first point: "))

    x2 = float(input("Enter the X-coordinate of the second point: "))
    y2 = float(input("Enter the Y-coordinate of the second point: "))

    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2

    print(f"First Point: ({x1:.2f}, {y1:.2f})")
    print(f"Second Point: ({x2:.2f}, {y2:.2f})")
    print(f"Midpoint: ({midpoint_x:.2f}, {midpoint_y:.2f})")

midpointoftwocoordinates()