def chordlengthfromradiusanddistance():
    print("Chord Length from Radius and Distance :")

    radius = float(input("Enter the circle radius: "))
    distance = float(input("Enter perpendicular distance from center to chord: "))

    if radius <= 0:
        print("Radius must be greater than zero.")
        return

    if distance < 0:
        print("Distance cannot be negative.")
        return

    if distance > radius:
        print("Invalid input: Distance cannot exceed the radius.")
        return

    half_chord = (radius ** 2 - distance ** 2) ** 0.5
    chord_length = 2 * half_chord

    print("\nChord Calculation Results :")
    print("Circle Radius:", round(radius, 2))
    print("Distance from Center:", round(distance, 2))
    print("Half Chord Length:", round(half_chord, 4))
    print("Full Chord Length:", round(chord_length, 4))

    if distance == 0:
        print("The chord is the diameter of the circle.")
    elif chord_length == 0:
        print("The chord touches the circle at exactly one point.")
    else:
        print("The chord lies inside the circle.")

chordlengthfromradiusanddistance()