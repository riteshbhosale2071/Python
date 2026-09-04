def multitransversalangle():
    print("Multi-Transversal Angle Solver :")
    print("This program solves unknown angles formed by multiple transversals")
    print("using standard parallel-line angle relationships.")

    n = int(input("Enter number of unknown angles: "))

    if n <= 0:
        print("Number of unknown angles must be positive.")
        return

    known_angle = float(input("Enter the known angle: "))

    if not (0 < known_angle < 180):
        print("Angle must be between 0 and 180 degrees.")
        return

    print("\nChoose relationship for each unknown angle:")
    print("1. Corresponding")
    print("2. Alternate Interior")
    print("3. Alternate Exterior")
    print("4. Co-Interior")
    print("5. Vertically Opposite")
    print("6. Linear Pair")

    angles = []

    for i in range(1, n + 1):
        choice = int(input(f"\nEnter relationship for unknown angle {i}: "))

        if choice in (1, 2, 3, 5):
            unknown = known_angle

        elif choice in (4, 6):
            unknown = 180 - known_angle

        else:
            print("Invalid relationship.")
            return

        angles.append(unknown)

    print("\nMulti-Transversal Angle Results :")

    for i, angle in enumerate(angles, start=1):
        print(f"Unknown Angle {i}: {angle} degrees")

multitransversalangle()