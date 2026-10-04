def circlesymmetrythroughchords():
    print("Circle Symmetry Through Chords :")

    radius = float(input("Enter radius of the circle: "))
    number_of_chords = int(input("Enter number of chords: "))

    if radius <= 0 or number_of_chords <= 0:
        print("Enter valid values.")
        return

    distances = []

    for i in range(number_of_chords):
        distance = float(input("Enter distance of chord " + str(i + 1) + " from center: "))

        if distance < 0 or distance > radius:
            print("Distance must be between 0 and the radius.")
            return

        distances.append(distance)

    print("\nChord Symmetry Analysis :")

    symmetric_found = False

    for i in range(number_of_chords):
        for j in range(i + 1, number_of_chords):
            if abs(distances[i] - distances[j]) < 0.000001:
                print("Chord", i + 1, "and Chord", j + 1, "have equal distances from the center.")
                print("They have equal chord lengths and show symmetry.")
                symmetric_found = True

    if not symmetric_found:
        print("No symmetric chord pairs found.")

    print("\nChord Lengths :")

    for i in range(number_of_chords):
        chord_length = 2 * (radius ** 2 - distances[i] ** 2) ** 0.5
        print("Chord", i + 1, "Length:", round(chord_length, 2))

circlesymmetrythroughchords()