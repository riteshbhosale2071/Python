def chordreconstruction():
    print("Chord Reconstruction :")
    print("1. Reconstruct chord using radius and distance from center")
    print("2. Reconstruct chord using radius and central angle")
    print("3. Reconstruct chord using endpoints")

    choice = input("Choose a method (1-3): ")

    if choice == "1":
        radius = float(input("Enter circle radius: "))
        distance = float(input("Enter perpendicular distance from center to chord: "))

        if radius <= 0 or distance < 0:
            print("Radius must be positive and distance cannot be negative.")
            return

        if distance > radius:
            print("Invalid measurements: Distance cannot exceed radius.")
            return

        half_length = (radius ** 2 - distance ** 2) ** 0.5
        chord_length = 2 * half_length

    elif choice == "2":
        import math

        radius = float(input("Enter circle radius: "))
        angle = float(input("Enter central angle in degrees: "))

        if radius <= 0:
            print("Radius must be greater than zero.")
            return

        if angle < 0 or angle > 180:
            print("Central angle must be between 0 and 180 degrees.")
            return

        half_length = radius * math.sin(math.radians(angle / 2))
        chord_length = 2 * half_length

    elif choice == "3":
        import math

        x1 = float(input("Enter first endpoint x-coordinate: "))
        y1 = float(input("Enter first endpoint y-coordinate: "))
        x2 = float(input("Enter second endpoint x-coordinate: "))
        y2 = float(input("Enter second endpoint y-coordinate: "))

        chord_length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        if chord_length == 0:
            print("Endpoints must be different to form a chord.")
            return

        half_length = chord_length / 2

    else:
        print("Invalid choice. Select 1, 2, or 3.")
        return

    print("\nChord Reconstruction Results :")
    print("Chord Half-Length:", round(half_length, 4))
    print("Full Chord Length:", round(chord_length, 4))

    if choice in ["1", "2"]:
        distance_from_center = (radius ** 2 - half_length ** 2) ** 0.5
        print("Perpendicular Distance from Center:", round(distance_from_center, 4))

    print("Reconstruction Status: Successful")

chordreconstruction()