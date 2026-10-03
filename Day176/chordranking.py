def chordranking():
    print("Chord Ranking Program :")

    radius = float(input("Enter radius of the circle: "))
    number_of_chords = int(input("Enter number of chords: "))

    if radius <= 0 or number_of_chords <= 0:
        print("Enter valid values.")
        return

    chords = []

    for i in range(number_of_chords):
        distance = float(input("Enter distance of chord " + str(i + 1) + " from center: "))

        if distance < 0 or distance > radius:
            print("Distance must be between 0 and the radius.")
            return

        chord_length = 2 * (radius ** 2 - distance ** 2) ** 0.5
        chords.append([i + 1, chord_length])

    chords.sort(key=lambda x: x[1], reverse=True)

    print("\nChord Ranking :")

    for i in range(len(chords)):
        print("Rank", i + 1, ": Chord", chords[i][0], "- Length:", round(chords[i][1], 2))

chordranking()