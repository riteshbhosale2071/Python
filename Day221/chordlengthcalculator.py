import math

def chordlengthcalculator():
    print("Chord Length Calculator")
    print("1. Calculate Chord using Radius and Central Angle")
    print("2. Calculate Chord using Radius and Perpendicular Distance")
    print("3. Calculate Chord using Radius and Arc Length")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        radius = float(input("Enter radius: "))
        angle = float(input("Enter central angle in degrees: "))

        if radius <= 0 or angle <= 0 or angle > 180:
            print("Enter a positive radius and an angle between 0 and 180.")
            return

        chord = 2 * radius * math.sin(math.radians(angle / 2))

    elif choice == "2":
        radius = float(input("Enter radius: "))
        distance = float(input("Enter perpendicular distance from centre to chord: "))

        if radius <= 0 or distance < 0 or distance >= radius:
            print("Invalid values: distance must be non-negative and less than radius.")
            return

        chord = 2 * math.sqrt(radius ** 2 - distance ** 2)

    elif choice == "3":
        radius = float(input("Enter radius: "))
        arc_length = float(input("Enter minor arc length: "))

        if radius <= 0 or arc_length <= 0 or arc_length > math.pi * radius:
            print("Invalid radius or minor arc length.")
            return

        angle = arc_length / radius
        chord = 2 * radius * math.sin(angle / 2)

    else:
        print("Invalid choice.")
        return

    print("\nChord Length =", round(chord, 4))

chordlengthcalculator()