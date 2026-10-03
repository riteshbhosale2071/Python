def chordlength():
    print("Chord Length Comparison :")

    radius = float(input("Enter radius of the circle: "))
    number_of_chords = int(input("Enter number of chords: "))

    if radius <= 0 or number_of_chords <= 0:
        print("Enter valid values.")
        return

    chord_lengths = []

    for i in range(number_of_chords):
        print("\nChord", i + 1)
        distance = float(input("Enter perpendicular distance from center to chord: "))

        if distance < 0 or distance > radius:
            print("Distance must be between 0 and the radius.")
            return

        chord = 2 * (radius ** 2 - distance ** 2) ** 0.5
        chord_lengths.append(chord)

        print("Chord Length:", round(chord, 2))

    print("\nComparison :")

    longest = max(chord_lengths)
    shortest = min(chord_lengths)

    for i in range(number_of_chords):
        print("Chord", i + 1, "Length:", round(chord_lengths[i], 2))

    print("\nLongest Chord: Chord", chord_lengths.index(longest) + 1)
    print("Length:", round(longest, 2))

    print("\nShortest Chord: Chord", chord_lengths.index(shortest) + 1)
    print("Length:", round(shortest, 2))

chordlength()