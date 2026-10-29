def angleclassification():
    print("Angle Classification Program")
    print("1. Acute Angle")
    print("2. Right Angle")
    print("3. Obtuse Angle")
    print("4. Straight Angle")
    print("5. Reflex Angle")

    angle = float(input("Enter the angle in degrees: "))

    if angle <= 0 or angle >= 360:
        if angle == 360:
            print("Complete Angle")
        else:
            print("Invalid angle.")
    elif angle < 90:
        print("Acute Angle")
    elif angle == 90:
        print("Right Angle")
    elif angle < 180:
        print("Obtuse Angle")
    elif angle == 180:
        print("Straight Angle")
    else:
        print("Reflex Angle")

angleclassification()