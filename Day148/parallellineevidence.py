def parallellineevidence():
    print("Parallel Line Evidence Checker :")
    print("Choose the angle relationship used as evidence:")
    print("1. Corresponding Angles")
    print("2. Alternate Interior Angles")
    print("3. Alternate Exterior Angles")
    print("4. Co-Interior Angles")

    choice = int(input("Enter your choice: "))

    angle1 = float(input("Enter first angle: "))
    angle2 = float(input("Enter second angle: "))

    if not (0 < angle1 < 180 and 0 < angle2 < 180):
        print("Angles must be between 0 and 180 degrees.")
        return

    valid = False
    relationship = ""

    if choice == 1:
        relationship = "Corresponding Angles"
        valid = angle1 == angle2

    elif choice == 2:
        relationship = "Alternate Interior Angles"
        valid = angle1 == angle2

    elif choice == 3:
        relationship = "Alternate Exterior Angles"
        valid = angle1 == angle2

    elif choice == 4:
        relationship = "Co-Interior Angles"
        valid = angle1 + angle2 == 180

    else:
        print("Invalid choice.")
        return

    print("\nParallel Line Evidence :")
    print("Relationship:", relationship)
    print("First Angle:", angle1, "degrees")
    print("Second Angle:", angle2, "degrees")

    if choice == 4:
        print("Angle Sum:", angle1 + angle2, "degrees")

    if valid:
        print("Valid evidence for parallel lines.")
        print("The given angle relationship supports that the lines are parallel.")
    else:
        print("Insufficient evidence for parallel lines.")
        print("The given angle relationship is not satisfied.")

parallellineevidence()