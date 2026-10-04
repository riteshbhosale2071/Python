def chordmidpointrelationship():
    print("Chord-Midpoint Relationship :")

    radius = float(input("Enter radius of the circle: "))
    x1 = float(input("Enter x-coordinate of first chord endpoint: "))
    y1 = float(input("Enter y-coordinate of first chord endpoint: "))
    x2 = float(input("Enter x-coordinate of second chord endpoint: "))
    y2 = float(input("Enter y-coordinate of second chord endpoint: "))

    if radius <= 0:
        print("Radius must be greater than zero.")
        return

    chord_length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    if chord_length == 0:
        print("The two endpoints cannot be the same.")
        return

    if chord_length > 2 * radius:
        print("The chord cannot exist inside this circle.")
        return

    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2

    midpoint_distance = (midpoint_x ** 2 + midpoint_y ** 2) ** 0.5

    print("\nChord Analysis :")
    print("Chord Length:", round(chord_length, 2))
    print("Midpoint:", "(", round(midpoint_x, 2), ",", round(midpoint_y, 2), ")")
    print("Distance of Midpoint from Center:", round(midpoint_distance, 2))

    if abs(midpoint_distance) < 0.000001:
        print("Relationship: The chord passes through the center.")
        print("The chord is a diameter.")
    else:
        print("Relationship: The chord does not pass through the center.")
        print("The perpendicular from the center to the chord bisects the chord.")

chordmidpointrelationship()