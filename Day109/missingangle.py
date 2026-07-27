def missingangle():
    angle1 = float(input("Enter the first angle: "))
    angle2 = float(input("Enter the second angle: "))

    missing_angle = 180 - (angle1 + angle2)

    print("Missing Angle:", missing_angle)

missingangle()