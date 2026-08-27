def verticallyoppositepair():
    angle = float(input("Enter an angle: "))

    if angle <= 0 or angle >= 180:
        print("Angle must be between 0° and 180°.")
        return

    opposite_angle = angle

    print("Vertically Opposite Angles:")
    print("First Angle:", angle, "°")
    print("Opposite Angle:", opposite_angle, "°")
    print("Both angles are equal.")

verticallyoppositepair()