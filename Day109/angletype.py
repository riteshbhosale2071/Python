def angletype():
    angle = float(input("Enter the angle: "))

    if angle == 0:
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
    elif angle == 360:
        print("Complete Angle")
    else:
        print("Invalid Angle")

angletype()