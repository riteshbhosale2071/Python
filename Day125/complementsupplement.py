def complementsupplement():
    angle = float(input("Enter the angle in degrees: "))

    if angle <= 0 or angle >= 180:
        print("Enter an angle between 0 deg and 180 deg :")
        return

    complement = 90 - angle
    supplement = 180 - angle

    if complement > 0:
        print("Complementary Angle:", complement, "degrees")
    else:
        print("No positive complementary angle.")

    if supplement > 0:
        print("Supplementary Angle:", supplement, "degrees")

complementsupplement()