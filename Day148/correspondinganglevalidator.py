def correspondinganglevalidator():
    print("Corresponding Angle Validator :")

    angle1 = float(input("Enter first corresponding angle: "))
    angle2 = float(input("Enter second corresponding angle: "))

    if not (0 < angle1 < 180 and 0 < angle2 < 180):
        print("Angles must be between 0 and 180 degrees.")
        return

    print("\nCorresponding Angle Check :")
    print("First Angle:", angle1, "degrees")
    print("Second Angle:", angle2, "degrees")

    if angle1 == angle2:
        print("The angles are equal.")
        print("For parallel lines, the corresponding angle relationship is valid.")
    else:
        print("The angles are not equal.")
        print("The corresponding angle relationship is not valid for parallel lines.")

correspondinganglevalidator()