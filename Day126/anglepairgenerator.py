def anglepairgenerator():
    angle = float(input("Enter the first angle in degrees: "))

    if angle <= 0 or angle >= 180:
        print("Enter an angle between 0° and 180°.")
        return

    complementary = 90 - angle
    supplementary = 180 - angle

    print("Given Angle:", angle, "°")

    if complementary > 0:
        print("Complementary Pair:", angle, "° and", complementary, "°")
    else:
        print("No positive complementary angle.")

    print("Supplementary Pair:", angle, "° and", supplementary, "°")

anglepairgenerator()