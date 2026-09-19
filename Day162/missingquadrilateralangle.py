def missingquadrilateralangle():
    print("Missing Quadrilateral Angle Solver :")

    angle1 = float(input("Enter angle 1: "))
    angle2 = float(input("Enter angle 2: "))
    angle3 = float(input("Enter angle 3: "))

    missing_angle = 360 - (angle1 + angle2 + angle3)

    print("Missing angle =", missing_angle, "degrees")

    if missing_angle > 0 and missing_angle < 360:
        print("The missing angle is valid.")
    else:
        print("The given angles cannot form a valid quadrilateral.")

missingquadrilateralangle()