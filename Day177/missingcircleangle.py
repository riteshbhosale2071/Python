def missingcircleangle():
    print("Missing Circle Angle Solver :")

    known_angles = int(input("Enter number of known angles: "))

    if known_angles <= 0:
        print("Enter a valid number of angles.")
        return

    total_angle = 360
    angle_sum = 0

    for i in range(known_angles):
        angle = float(input("Enter angle " + str(i + 1) + " in degrees: "))

        if angle < 0 or angle > 360:
            print("Enter a valid angle between 0 and 360 degrees.")
            return

        angle_sum += angle

    missing_angle = total_angle - angle_sum

    print("\nResult :")
    print("Known Angle Sum:", round(angle_sum, 2), "degrees")

    if missing_angle < 0:
        print("The given angles exceed 360 degrees.")
    elif missing_angle == 0:
        print("No missing angle remains.")
    else:
        print("Missing Angle:", round(missing_angle, 2), "degrees")

missingcircleangle()