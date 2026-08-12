def polygoninteriorangle():
    sides = int(input("Enter the number of sides: "))

    if sides < 3:
        print("A polygon must have at least 3 sides.")
        return

    total_angle = (sides - 2) * 180
    each_angle = total_angle / sides

    print("Sum of Interior Angles:", total_angle, "°")
    print("Each Interior Angle (regular polygon):", each_angle, "°")

polygoninteriorangle()