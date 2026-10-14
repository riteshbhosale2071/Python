def radiuschorddistance():
    print("Radius-Chord Distance Solver :")
    print("1. Calculate chord length")
    print("2. Calculate distance from center to chord")
    print("3. Calculate radius")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        radius = float(input("Enter circle radius: "))
        distance = float(input("Enter distance from center to chord: "))

        if radius <= 0 or distance < 0:
            print("Radius must be positive and distance cannot be negative.")
            return

        if distance > radius:
            print("Invalid measurements: Distance cannot exceed radius.")
            return

        half_chord = (radius ** 2 - distance ** 2) ** 0.5
        chord = 2 * half_chord

        print("\nChord Half-Length:", round(half_chord, 4))
        print("Full Chord Length:", round(chord, 4))

    elif choice == "2":
        radius = float(input("Enter circle radius: "))
        chord = float(input("Enter full chord length: "))

        if radius <= 0 or chord < 0:
            print("Radius must be positive and chord length cannot be negative.")
            return

        if chord > 2 * radius:
            print("Invalid measurements: Chord cannot exceed the diameter.")
            return

        half_chord = chord / 2
        distance = (radius ** 2 - half_chord ** 2) ** 0.5

        print("\nDistance from Center to Chord:", round(distance, 4))

    elif choice == "3":
        chord = float(input("Enter full chord length: "))
        distance = float(input("Enter distance from center to chord: "))

        if chord <= 0 or distance < 0:
            print("Chord length must be positive and distance cannot be negative.")
            return

        half_chord = chord / 2
        radius = (half_chord ** 2 + distance ** 2) ** 0.5

        print("\nCalculated Radius:", round(radius, 4))
        print("Calculated Diameter:", round(2 * radius, 4))

    else:
        print("Invalid option. Choose 1, 2, or 3.")
        return

    print("Calculation completed successfully.")

radiuschorddistance()