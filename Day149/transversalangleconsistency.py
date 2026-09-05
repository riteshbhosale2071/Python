def transversalangleconsistency():
    print("Transversal Angle Consistency Checker :")
    print("Enter the angles formed by a transversal.")
    print("The program checks whether they are consistent with parallel lines.")

    n = int(input("Enter number of angles: "))

    if n < 2:
        print("Enter at least 2 angles.")
        return

    angles = []

    for i in range(n):
        angle = float(input(f"Enter angle {i + 1}: "))

        if not (0 < angle < 180):
            print("Angles must be between 0 and 180 degrees.")
            return

        angles.append(angle)

    acute_angles = [angle for angle in angles if angle < 90]
    right_angles = [angle for angle in angles if angle == 90]
    obtuse_angles = [angle for angle in angles if angle > 90]

    print("\nTransversal Angle Consistency :")
    print("Angles:", angles)

    if all(angle == 90 for angle in angles):
        print("All angles are 90 degrees.")
        print("The angle set is consistent with perpendicular lines.")

    elif len(right_angles) == 0:
        if acute_angles and obtuse_angles:
            acute = acute_angles[0]
            obtuse = obtuse_angles[0]

            if abs((acute + obtuse) - 180) < 0.000001:
                print("The angles are consistent with parallel lines.")
                print("Acute and obtuse angles are supplementary.")
            else:
                print("The angles are not consistent.")
        elif len(acute_angles) == n or len(obtuse_angles) == n:
            if all(abs(angle - angles[0]) < 0.000001 for angle in angles):
                print("All angles are equal.")
                print("The angle set is consistent with parallel lines.")
            else:
                print("The angles are not consistent.")
        else:
            print("The angle set does not provide consistent evidence.")

    else:
        print("The angle set contains 90-degree angles.")
        print("Further geometric information is required.")

transversalangleconsistency()