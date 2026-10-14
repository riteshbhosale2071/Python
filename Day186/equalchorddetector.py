def equalchorddetector():
    print("Equal Chord Detector :")

    radius = float(input("Enter the common circle radius: "))

    if radius <= 0:
        print("Radius must be greater than zero.")
        return

    number = int(input("Enter the number of chords: "))

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

        distance = (radius ** 2 - (length / 2) ** 2) ** 0.5
        chords.append([i + 1, length, distance])

    print("\nChord Analysis :")

    equal_found = False

    for i in range(number):
        print(
            "Chord", chords[i][0],
            "- Length:", round(chords[i][1], 4),
            "- Distance from Center:", round(chords[i][2], 4)
        )

    for i in range(number):
        for j in range(i + 1, number):
            if abs(chords[i][1] - chords[j][1]) < 0.000001:
                print(
                    "Equal Chords Detected: Chord",
                    chords[i][0], "and Chord", chords[j][0]
                )
                equal_found = True

    if equal_found:
        print("\nResult: One or more pairs of equal chords were found.")
    else:
        print("\nResult: No equal chords were found.")

    print("Note: Equal chords in the same circle are equally distant from the center.")

equalchorddetector()