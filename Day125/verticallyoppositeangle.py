def verticallyoppositeangle():
    angle = float(input("Enter one angle in degrees: "))

    if angle <= 0 or angle >= 180:
        print("Enter an angle between 0° and 180°.")
    else:
        opposite_angle = angle
        print("Vertically Opposite Angle:", opposite_angle, "°")
        print("Vertically opposite angles are always equal.")

verticallyoppositeangle()