def circlepropertyrule():
    print("Circle Property Rule :")
    print("1. Check chord feasibility")
    print("2. Check equal chords")
    print("3. Check semicircle angle")
    print("4. Calculate arc length")
    print("5. Calculate sector area")
    print("6. Check inscribed angle theorem")

    choice = input("Select a rule (1-6): ")

    if choice == "1":
        radius = float(input("Enter circle radius: "))
        chord = float(input("Enter chord length: "))

        if radius <= 0 or chord < 0:
            print("Invalid measurements.")
            return

        if chord <= 2 * radius:
            print("Rule Result: Chord is geometrically possible.")
            distance = (radius ** 2 - (chord / 2) ** 2) ** 0.5
            print("Distance from center:", round(distance, 4))
        else:
            print("Rule Result: Chord exceeds the diameter.")

    elif choice == "2":
        chord1 = float(input("Enter first chord length: "))
        chord2 = float(input("Enter second chord length: "))

        if chord1 <= 0 or chord2 <= 0:
            print("Chord lengths must be positive.")
            return

        if abs(chord1 - chord2) < 0.000001:
            print("Rule Result: Chords are equal in length.")
        else:
            print("Rule Result: Chords have different lengths.")

    elif choice == "3":
        angle = float(input("Enter the angle subtended by a diameter: "))

        if angle < 0 or angle > 180:
            print("Angle must be between 0 and 180 degrees.")
            return

        if abs(angle - 90) < 0.000001:
            print("Rule Result: The angle in a semicircle is 90 degrees.")
        else:
            print("Rule Result: The angle does not satisfy the semicircle theorem.")

    elif choice == "4":
        radius = float(input("Enter circle radius: "))
        angle = float(input("Enter central angle in degrees: "))

        if radius <= 0 or angle < 0 or angle > 360:
            print("Invalid radius or central angle.")
            return

        arc_length = (angle / 360) * 2 * 3.14159 * radius

        print("Arc Length:", round(arc_length, 4))
        print("Rule Applied: Arc length is proportional to the central angle.")

    elif choice == "5":
        radius = float(input("Enter circle radius: "))
        angle = float(input("Enter central angle in degrees: "))

        if radius <= 0 or angle < 0 or angle > 360:
            print("Invalid radius or central angle.")
            return

        sector_area = (angle / 360) * 3.14159 * radius ** 2

        print("Sector Area:", round(sector_area, 4))
        print("Rule Applied: Sector area is proportional to the central angle.")

    elif choice == "6":
        central_angle = float(input("Enter central angle in degrees: "))
        inscribed_angle = float(input("Enter inscribed angle in degrees: "))

        if not (0 <= central_angle <= 360 and 0 <= inscribed_angle <= 180):
            print("Invalid angle measurements.")
            return

        expected_angle = central_angle / 2

        print("Expected Inscribed Angle:", round(expected_angle, 2), "degrees")

        if abs(inscribed_angle - expected_angle) < 0.000001:
            print("Rule Result: Inscribed angle theorem is satisfied.")
        else:
            print("Rule Result: Inscribed angle theorem is not satisfied.")

    else:
        print("Invalid selection. Choose a rule from 1 to 6.")

circlepropertyrule()