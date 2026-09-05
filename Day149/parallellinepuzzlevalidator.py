def parallellinepuzzlevalidator():
    print("Parallel-Line Puzzle Validator :")

    known_angle = float(input("Enter the known angle: "))
    unknown_angle = float(input("Enter the unknown angle: "))

    if not (0 < known_angle < 180 and 0 < unknown_angle < 180):
        print("Angles must be between 0 and 180 degrees.")
        return

    print("\nChoose the angle relationship:")
    print("1. Corresponding Angles")
    print("2. Alternate Interior Angles")
    print("3. Alternate Exterior Angles")
    print("4. Co-Interior Angles")
    print("5. Vertically Opposite Angles")
    print("6. Linear Pair")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        relationship = "Corresponding Angles"
        expected_angle = known_angle

    elif choice == 2:
        relationship = "Alternate Interior Angles"
        expected_angle = known_angle

    elif choice == 3:
        relationship = "Alternate Exterior Angles"
        expected_angle = known_angle

    elif choice == 4:
        relationship = "Co-Interior Angles"
        expected_angle = 180 - known_angle

    elif choice == 5:
        relationship = "Vertically Opposite Angles"
        expected_angle = known_angle

    elif choice == 6:
        relationship = "Linear Pair"
        expected_angle = 180 - known_angle

    else:
        print("Invalid choice.")
        return

    print("\nPuzzle Validation :")
    print("Relationship:", relationship)
    print("Known Angle:", known_angle, "degrees")
    print("Given Unknown Angle:", unknown_angle, "degrees")
    print("Expected Angle:", expected_angle, "degrees")

    if abs(unknown_angle - expected_angle) < 0.000001:
        print("Result: Correct!")
        print("The angle satisfies the given relationship.")
    else:
        print("Result: Incorrect.")
        print("The angle does not satisfy the given relationship.")

parallellinepuzzlevalidator()