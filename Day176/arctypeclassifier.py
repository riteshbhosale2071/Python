def arctypeclassifier():
    print("Arc Type Classifier :")

    radius = float(input("Enter radius of the circle: "))
    central_angle = float(input("Enter central angle in degrees: "))

    if radius <= 0:
        print("Radius must be greater than zero.")
        return

    if central_angle <= 0 or central_angle >= 360:
        print("Central angle must be between 0 and 360 degrees.")
        return

    arc_length = (central_angle / 360) * 2 * 3.14159 * radius

    print("\nRadius:", radius)
    print("Central Angle:", central_angle, "degrees")
    print("Arc Length:", round(arc_length, 2))

    if central_angle < 180:
        print("Arc Type: Minor Arc")
    elif central_angle == 180:
        print("Arc Type: Semicircle")
    else:
        print("Arc Type: Major Arc")

arctypeclassifier()