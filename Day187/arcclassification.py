def arcclassification():
    print("Arc Classification :")

    radius = float(input("Enter circle radius: "))
    angle = float(input("Enter central angle in degrees: "))

    if radius <= 0:
        print("Radius must be greater than zero.")
        return

    if angle < 0 or angle > 360:
        print("Central angle must be between 0 and 360 degrees.")
        return

    import math

    circumference = 2 * math.pi * radius
    arc_length = (angle / 360) * circumference

    print("\nArc Classification Results :")
    print("Circle Radius:", round(radius, 2))
    print("Central Angle:", round(angle, 2), "degrees")
    print("Arc Length:", round(arc_length, 4))

    if angle == 0:
        arc_type = "Zero-Length Arc"
        description = "No arc is formed."
    elif angle < 180:
        arc_type = "Minor Arc"
        description = "The arc is smaller than a semicircle."
    elif angle == 180:
        arc_type = "Semicircle"
        description = "The arc covers exactly half the circle."
    elif angle < 360:
        arc_type = "Major Arc"
        description = "The arc is larger than a semicircle."
    else:
        arc_type = "Full Circle"
        description = "The arc covers the entire circumference."

    print("Arc Classification:", arc_type)
    print("Description:", description)

    if angle > 0:
        print("Percentage of Circumference:", round(angle / 360 * 100, 2), "%")

    print("Classification completed successfully.")

arcclassification()