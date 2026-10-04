def chordandarcrelationship():
    print("Chord-and-Arc Relationship Analyzer :")

    radius = float(input("Enter radius of the circle: "))
    angle = float(input("Enter central angle of the arc in degrees: "))

    if radius <= 0:
        print("Radius must be greater than zero.")
        return

    if angle <= 0 or angle > 360:
        print("Angle must be between 0 and 360 degrees.")
        return

    pi = 3.14159

    arc_length = (angle / 360) * 2 * pi * radius
    chord_length = 2 * (radius ** 2 - (radius * (1 - (angle / 180)) ** 2) / 4) ** 0.5

    if angle == 180:
        chord_length = 2 * radius
    elif angle < 180:
        half_angle = angle / 2
        chord_length = 2 * radius * (1 - (half_angle / 180)) ** 0.5
    else:
        minor_angle = 360 - angle
        half_angle = minor_angle / 2
        chord_length = 2 * radius * (1 - (half_angle / 180)) ** 0.5

    print("\nRelationship Analysis :")
    print("Radius:", round(radius, 2))
    print("Central Angle:", round(angle, 2), "degrees")
    print("Arc Length:", round(arc_length, 2))
    print("Chord Length:", round(chord_length, 2))

    if angle < 180:
        print("Arc Type: Minor Arc")
    elif angle == 180:
        print("Arc Type: Semicircle")
    else:
        print("Arc Type: Major Arc")

    if angle == 180:
        print("Chord Type: Diameter")
    else:
        print("Chord Type: Regular Chord")

    if arc_length > chord_length:
        print("Relationship: Arc length is greater than chord length.")
    elif abs(arc_length - chord_length) < 0.000001:
        print("Relationship: Arc length and chord length are equal.")
    else:
        print("Relationship: Chord length is greater than arc length.")

chordandarcrelationship()