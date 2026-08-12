def complementaryangle():
    angle = float(input("Enter the angle in degrees: "))

    if 0 < angle < 90:
        complementary = 90 - angle
        print("Complementary Angle:", complementary, "°")
    else:
        print("A complementary angle must be between 0 deg and 90 deg.")

complementaryangle()