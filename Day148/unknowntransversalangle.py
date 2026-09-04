def unknowntransversalangle():
    print("Unknown Transversal Angle Solver :")
    print("1. Corresponding Angles")
    print("2. Alternate Interior Angles")
    print("3. Alternate Exterior Angles")
    print("4. Co-Interior Angles")

    choice = int(input("Enter relationship type: "))

    known_angle = float(input("Enter the known angle: "))

    if not (0 < known_angle < 180):
        print("Angle must be between 0 and 180 degrees.")
        return

    if choice in (1, 2, 3):
        unknown_angle = known_angle

        if choice == 1:
            relationship = "Corresponding Angles"
        elif choice == 2:
            relationship = "Alternate Interior Angles"
        else:
            relationship = "Alternate Exterior Angles"

    elif choice == 4:
        relationship = "Co-Interior Angles"
        unknown_angle = 180 - known_angle

    else:
        print("Invalid choice.")
        return

    print("\nTransversal Angle Solution :")
    print("Relationship:", relationship)
    print("Known Angle:", known_angle, "degrees")
    print("Unknown Angle:", unknown_angle, "degrees")

unknowntransversalangle()