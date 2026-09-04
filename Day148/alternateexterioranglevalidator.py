def alternateexterioranglevalidator():
    print("Alternate Exterior Angle Validator :")

    angle1 = float(input("Enter first alternate exterior angle: "))
    angle2 = float(input("Enter second alternate exterior angle: "))

    if not (0 < angle1 < 180 and 0 < angle2 < 180):
        print("Angles must be between 0 and 180 degrees.")
        return

    print("\nAlternate Exterior Angle Check :")
    print("First Angle:", angle1, "degrees")
    print("Second Angle:", angle2, "degrees")

    if angle1 == angle2:
        print("The angles are equal.")
        print("The alternate exterior angle relationship is valid.")
        print("The two lines can be considered parallel.")
    else:
        print("The angles are not equal.")
        print("The alternate exterior angle relationship is not valid.")
        print("The two lines are not parallel based on these angles.")

alternateexterioranglevalidator()