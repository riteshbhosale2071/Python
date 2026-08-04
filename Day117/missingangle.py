def missingangle():
    angle1 = float(input("Enter the first angle: "))
    angle2 = float(input("Enter the second angle: "))

    angle3 = 180 - (angle1 + angle2)

    if angle3 > 0:
        print("The missing angle is:", angle3, "degrees")
    else:
        print("Invalid angles. A triangle cannot be formed.")

missingangle()