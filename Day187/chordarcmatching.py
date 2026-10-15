def chordarcmatching():
    print("Chord-Arc Matching :")

    import math

    radius = float(input("Enter the circle radius: "))
    chord_length = float(input("Enter the chord length: "))
    arc_angle = float(input("Enter the central angle of the arc in degrees: "))

    if radius <= 0:
        print("Radius must be greater than zero.")
        return

    if chord_length < 0 or chord_length > 2 * radius:
        print("Invalid chord length. It must be between 0 and the diameter.")
        return

    if arc_angle < 0 or arc_angle > 360:
        print("Arc angle must be between 0 and 360 degrees.")
        return

    expected_chord = 2 * radius * math.sin(math.radians(arc_angle / 2))
    arc_length = (arc_angle / 360) * 2 * math.pi * radius
    difference = abs(chord_length - expected_chord)

    print("\nMatching Results :")
    print("Circle Radius:", round(radius, 4))
    print("Given Chord Length:", round(chord_length, 4))
    print("Expected Chord Length:", round(expected_chord, 4))
    print("Central Angle:", round(arc_angle, 2), "degrees")
    print("Arc Length:", round(arc_length, 4))
    print("Chord Length Difference:", round(difference, 4))

    if difference < 0.0001:
        print("Result: MATCH — the chord corresponds to the given minor or semicircular arc.")
    else:
        print("Result: NO MATCH — the chord length does not correspond to the given central angle.")

    if arc_angle < 180:
        print("Arc Classification: Minor Arc")
    elif arc_angle == 180:
        print("Arc Classification: Semicircle")
    else:
        print("Arc Classification: Major Arc")

chordarcmatching()