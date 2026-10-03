def equalchorddetector():
    print("Equal Chord Detector :")

    radius = float(input("Enter radius of the circle: "))
    number_of_chords = int(input("Enter number of chords: "))

    if radius <= 0 or number_of_chords <= 0:
        print("Enter valid values.")
        return

    chord_lengths = []

    for i in range(number_of_chords):
        distance = float(input("Enter distance of chord " + str(i + 1) + " from center: "))

        if distance < 0 or distance > radius:
            print("Distance must be between 0 and the radius.")
            return

        chord = 2 * (radius ** 2 - distance ** 2) ** 0.5
        chord_lengths.append(chord)

    print("\nChord Lengths :")

    for i in range(number_of_chords):
        print("Chord", i + 1, ":", round(chord_lengths[i], 2))

    equal_found = False

    for i in range(number_of_chords):
        for j in range(i + 1, number_of_chords):
            if abs(chord_lengths[i] - chord_lengths[j]) < 0.000001:
                print("Chord", i + 1, "and Chord", j + 1, "are equal.")
                equal_found = True

    if not equal_found:
        print("No equal chords found.")

equalchorddetector()