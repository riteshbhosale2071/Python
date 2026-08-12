def supplementaryangle():
    angle = float(input("Enter the angle in degrees: "))

    if 0 < angle < 180:
        supplementary = 180 - angle
        print("Supplementary Angle:", supplementary, "°")
    else:
        print("Enter an angle between 0 deg and 180 deg")

supplementaryangle()