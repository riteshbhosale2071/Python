def angletype():
    angle = float(input("Enter the angle in degrees: "))

    if angle < 0 or angle > 360:
        print("Invalid angle. Enter an angle between 0° and 360°.")
    elif angle == 0:
        print("Zero Angle")
    elif angle < 90:
        print("Acute Angle")
    elif angle == 90:
        print("Right Angle")
    elif angle < 180:
        print("Obtuse Angle")
    elif angle == 180:
        print("Straight Angle")
    elif angle < 360:
        print("Reflex Angle")
    else:
        print("Complete Angle")

angletype()