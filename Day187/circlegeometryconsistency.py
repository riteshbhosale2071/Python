def circlegeometryconsistency():
    print("Circle Geometry Consistency :")
    print("1. Radius and diameter consistency")
    print("2. Radius and circumference consistency")
    print("3. Radius and area consistency")
    print("4. Chord and radius consistency")
    print("5. Central angle and inscribed angle consistency")
    print("6. Arc angle sum consistency")

    choice = input("Choose a consistency check (1-6): ")

    tolerance = 0.01

    if choice == "1":
        radius = float(input("Enter radius: "))
        diameter = float(input("Enter diameter: "))

        if radius <= 0 or diameter <= 0:
            print("Measurements must be greater than zero.")
            return

        expected = 2 * radius
        print("Expected Diameter:", round(expected, 4))

        if abs(diameter - expected) <= tolerance:
            print("Status: CONSISTENT")
        else:
            print("Status: INCONSISTENT")

    elif choice == "2":
        radius = float(input("Enter radius: "))
        circumference = float(input("Enter circumference: "))

        if radius <= 0 or circumference <= 0:
            print("Measurements must be greater than zero.")
            return

        expected = 2 * 3.14159 * radius
        print("Expected Circumference:", round(expected, 4))

        if abs(circumference - expected) <= tolerance:
            print("Status: CONSISTENT")
        else:
            print("Status: INCONSISTENT")

    elif choice == "3":
        radius = float(input("Enter radius: "))
        area = float(input("Enter circle area: "))

        if radius <= 0 or area <= 0:
            print("Measurements must be greater than zero.")
            return

        expected = 3.14159 * radius ** 2
        print("Expected Area:", round(expected, 4))

        if abs(area - expected) <= tolerance:
            print("Status: CONSISTENT")
        else:
            print("Status: INCONSISTENT")

    elif choice == "4":
        radius = float(input("Enter circle radius: "))
        chord = float(input("Enter chord length: "))

        if radius <= 0 or chord < 0:
            print("Radius must be positive and chord cannot be negative.")
            return

        if chord > 2 * radius:
            print("Status: INCONSISTENT — chord exceeds the diameter.")
        else:
            distance = (radius ** 2 - (chord / 2) ** 2) ** 0.5
            print("Status: CONSISTENT")
            print("Distance from Center to Chord:", round(distance, 4))

    elif choice == "5":
        central = float(input("Enter central angle in degrees: "))
        inscribed = float(input("Enter inscribed angle in degrees: "))

        if not (0 <= central <= 360 and 0 <= inscribed <= 180):
            print("Invalid angle measurements.")
            return

        expected = central / 2
        print("Expected Inscribed Angle:", round(expected, 4))

        if abs(inscribed - expected) <= tolerance:
            print("Status: CONSISTENT")
        else:
            print("Status: INCONSISTENT")

    elif choice == "6":
        number = int(input("Enter the number of arc angles: "))

        if number <= 0:
            print("Number of arcs must be greater than zero.")
            return

        total = 0

        for i in range(number):
            angle = float(input("Enter arc angle " + str(i + 1) + ": "))

            if angle < 0 or angle > 360:
                print("Each arc angle must be between 0 and 360 degrees.")
                return

            total += angle

        print("Total Arc Angle:", round(total, 4), "degrees")

        if abs(total - 360) <= tolerance:
            print("Status: CONSISTENT — arcs total one full circle.")
        else:
            print("Status: INCONSISTENT — arcs do not total 360 degrees.")

    else:
        print("Invalid selection. Choose a number from 1 to 6.")

circlegeometryconsistency()