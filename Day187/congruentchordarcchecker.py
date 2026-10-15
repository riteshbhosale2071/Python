def congruentchordarcchecker():
    print("Congruent Chord-Arc Checker :")

    import math

    radius1 = float(input("Enter the radius of circle 1: "))
    chord1 = float(input("Enter chord length of circle 1: "))
    angle1 = float(input("Enter central angle of circle 1 in degrees: "))

    radius2 = float(input("\nEnter the radius of circle 2: "))
    chord2 = float(input("Enter chord length of circle 2: "))
    angle2 = float(input("Enter central angle of circle 2 in degrees: "))

    if radius1 <= 0 or radius2 <= 0:
        print("Both circle radii must be greater than zero.")
        return

    if chord1 < 0 or chord1 > 2 * radius1:
        print("Invalid chord length for circle 1.")
        return

    if chord2 < 0 or chord2 > 2 * radius2:
        print("Invalid chord length for circle 2.")
        return

    if not (0 <= angle1 <= 360 and 0 <= angle2 <= 360):
        print("Central angles must be between 0 and 360 degrees.")
        return

    expected_chord1 = 2 * radius1 * math.sin(math.radians(angle1 / 2))
    expected_chord2 = 2 * radius2 * math.sin(math.radians(angle2 / 2))

    chord1_valid = abs(chord1 - expected_chord1) < 0.0001
    chord2_valid = abs(chord2 - expected_chord2) < 0.0001

    print("\nCircle 1 Analysis :")
    print("Expected Chord Length:", round(expected_chord1, 4))
    print("Chord Validation:", "PASSED" if chord1_valid else "FAILED")

    print("\nCircle 2 Analysis :")
    print("Expected Chord Length:", round(expected_chord2, 4))
    print("Chord Validation:", "PASSED" if chord2_valid else "FAILED")

    chords_equal = abs(chord1 - chord2) < 0.0001
    arcs_equal = abs(angle1 - angle2) < 0.0001

    print("\nCongruence Results :")
    print("Chord Lengths Equal:", chords_equal)
    print("Central Angles Equal:", arcs_equal)

    if not chord1_valid or not chord2_valid:
        print("Result: At least one chord does not match its circle's central angle.")
    elif chords_equal and arcs_equal:
        print("Result: Chords and corresponding arcs are congruent.")
    elif chords_equal:
        print("Result: Chords are equal, but the central angles differ.")
    elif arcs_equal:
        print("Result: Central angles are equal, but chord lengths differ.")
    else:
        print("Result: Chords and corresponding arcs are not congruent.")

    if abs(radius1 - radius2) < 0.0001:
        print("Both circles have equal radii.")
    else:
        print("The circles have different radii.")

congruentchordarcchecker()