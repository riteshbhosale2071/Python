def chordhalflengthcalculator():
    print("Chord Half-Length Calculator :")
    print("1. Calculate using radius and distance from center")
    print("2. Calculate using radius and central angle")

    choice = input("Choose calculation method (1-2): ")

    if choice == "1":
        radius = float(input("Enter circle radius: "))
        distance = float(input("Enter perpendicular distance from center to chord: "))

        if radius <= 0 or distance < 0:
            print("Radius must be positive and distance cannot be negative.")
            return

        if distance > radius:
            print("Invalid input: Distance cannot exceed the radius.")
            return

        half_length = (radius ** 2 - distance ** 2) ** 0.5

    elif choice == "2":
        radius = float(input("Enter circle radius: "))
        angle = float(input("Enter central angle in degrees: "))

        if radius <= 0:
            print("Radius must be greater than zero.")
            return

        if angle < 0 or angle > 180:
            print("Central angle must be between 0 and 180 degrees.")
            return

        import math
        half_length = radius * math.sin(math.radians(angle / 2))

    else:
        print("Invalid choice. Select 1 or 2.")
        return

    full_length = 2 * half_length

    print("\n Chord Calculation Results :")
    print("Chord Half-Length:", round(half_length, 4))
    print("Full Chord Length:", round(full_length, 4))

    if half_length == 0:
        print("The chord touches the circle at a single point.")
    else:
        print("The chord has a positive length.")

chordhalflengthcalculator()