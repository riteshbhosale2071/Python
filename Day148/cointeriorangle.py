def cointeriorangle():
    print("Co-Interior Angle Checker :")

    angle1 = float(input("Enter first co-interior angle: "))
    angle2 = float(input("Enter second co-interior angle: "))

    if not (0 < angle1 < 180 and 0 < angle2 < 180):
        print("Angles must be between 0 and 180 degrees.")
        return

    angle_sum = angle1 + angle2

    print("\nCo-Interior Angle Check :")
    print("First Angle:", angle1, "degrees")
    print("Second Angle:", angle2, "degrees")
    print("Sum of Angles:", angle_sum, "degrees")

    if angle_sum == 180:
        print("The angles are supplementary.")
        print("The co-interior angle relationship is valid.")
        print("The two lines can be considered parallel.")
    else:
        print("The angles are not supplementary.")
        print("The co-interior angle relationship is not valid.")
        print("The two lines are not parallel based on these angles.")

cointeriorangle()