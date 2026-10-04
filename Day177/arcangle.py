def arcangle():
    print("Arc Angle Calculator :")

    radius = float(input("Enter radius of the circle: "))
    arc_length = float(input("Enter arc length: "))

    if radius <= 0 or arc_length <= 0:
        print("Radius and arc length must be greater than zero.")
        return

    circumference = 2 * 3.14159 * radius

    if arc_length > circumference:
        print("Arc length cannot be greater than the circumference.")
        return

    central_angle = (arc_length / circumference) * 360

    print("\nRadius:", round(radius, 2))
    print("Arc Length:", round(arc_length, 2))
    print("Central Angle:", round(central_angle, 2), "degrees")

    if central_angle < 180:
        print("Arc Type: Minor Arc")
    elif central_angle == 180:
        print("Arc Type: Semicircle")
    else:
        print("Arc Type: Major Arc")

arcangle()