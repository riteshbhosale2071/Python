def chordrankingsystem():
    print("Chord Ranking System :")

    radius = float(input("Enter the common circle radius: "))

    if radius <= 0:
        print("Circle radius must be greater than zero.")
        return

    number = int(input("Enter the number of chords to compare: "))

    if number <= 0:
        print("Number of chords must be greater than zero.")
        return

    chords = []
    diameter = 2 * radius

    for i in range(number):
        print("\nChord", i + 1)
        length = float(input("Enter chord length: "))

        if length <= 0 or length > diameter:
            print("Invalid chord length. It must be positive and cannot exceed the diameter.")
            return

        half_length = length / 2
        distance = (radius ** 2 - half_length ** 2) ** 0.5

        chords.append([i + 1, length, distance])

    chords.sort(key=lambda chord: chord[1], reverse=True)

    print("\nChord Ranking Results :")

    for i in range(number):
        chord = chords[i]

        print("\nRank:", i + 1)
        print("Chord Number:", chord[0])
        print("Chord Length:", round(chord[1], 4))
        print("Distance from Center:", round(chord[2], 4))

    longest = chords[0]
    shortest = chords[-1]

    print("\nFinal Comparison :")
    print("Longest Chord: Chord", longest[0])
    print("Longest Length:", round(longest[1], 4))
    print("Shortest Chord: Chord", shortest[0])
    print("Shortest Length:", round(shortest[1], 4))
    print("Length Difference:", round(longest[1] - shortest[1], 4))

    print("\nRanking is based on chord length.")
    print("For a common circle, the longest chord is the diameter.")

chordrankingsystem()