def orthocentrecoordinatefinder():
    print("Orthocentre Coordinate Finder :")

    print("\nEnter coordinates of Vertex A:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))

    print("\nEnter coordinates of Vertex B:")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    print("\nEnter coordinates of Vertex C:")
    x3 = float(input("x3: "))
    y3 = float(input("y3: "))

    if (x1 == x2 and y1 == y2) or (x2 == x3 and y2 == y3) or (x1 == x3 and y1 == y3):
        print("Invalid triangle.")
        return

    if x2 == x3:
        altitude_a_slope = 0
    elif y2 == y3:
        altitude_a_slope = None
    else:
        slope_bc = (y3 - y2) / (x3 - x2)
        altitude_a_slope = -1 / slope_bc

    if x1 == x3:
        altitude_b_slope = 0
    elif y1 == y3:
        altitude_b_slope = None
    else:
        slope_ac = (y3 - y1) / (x3 - x1)
        altitude_b_slope = -1 / slope_ac

    if altitude_a_slope is None:
        x = x1
        if altitude_b_slope is None:
            print("Unable to find a unique orthocentre.")
            return
        y = altitude_b_slope * (x - x2) + y2

    elif altitude_b_slope is None:
        x = x2
        y = altitude_a_slope * (x - x1) + y1

    else:
        b1 = y1 - altitude_a_slope * x1
        b2 = y2 - altitude_b_slope * x2

        x = (b2 - b1) / (altitude_a_slope - altitude_b_slope)
        y = altitude_a_slope * x + b1

    print("\nOrthocentre Coordinates :")
    print(f"Orthocentre: ({x:.2f}, {y:.2f})")

orthocentrecoordinatefinder()