def triangleangle():
    angle1 = float(input("Enter the first angle: "))
    angle2 = float(input("Enter the second angle: "))

    angle3 = 180 - (angle1 + angle2)

    if angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
        print("Invalid triangle angles.")
    else:
        print("Third Angle:", angle3, "°")

triangleangle()