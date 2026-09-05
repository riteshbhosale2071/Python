def anglepropagation():
    print("Angle Propagation Simulator :")
    print("This program propagates an angle through parallel lines")
    print("using standard transversal angle relationships.")

    lines = int(input("Enter number of parallel lines: "))

    if lines < 2:
        print("At least 2 parallel lines are required.")
        return

    base_angle = float(input("Enter the initial angle: "))

    if not (0 < base_angle < 180):
        print("Angle must be between 0 and 180 degrees.")
        return

    print("\nChoose propagation pattern:")
    print("1. Equal-angle propagation")
    print("2. Supplementary-angle propagation")
    print("3. Alternating propagation")

    choice = int(input("Enter your choice: "))

    if choice not in (1, 2, 3):
        print("Invalid choice.")
        return

    print("\nAngle Propagation :")

    current_angle = base_angle

    for i in range(1, lines + 1):
        print(f"Line {i}: {current_angle} degrees")

        if choice == 1:
            current_angle = base_angle

        elif choice == 2:
            current_angle = 180 - current_angle

        elif choice == 3:
            if i < lines:
                current_angle = 180 - current_angle

    print("\nPropagation completed.")

anglepropagation()