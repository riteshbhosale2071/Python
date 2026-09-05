def multipleparallelline():
    print("Multiple Parallel Line Analyzer :")

    n = int(input("Enter number of parallel lines: "))

    if n < 2:
        print("At least 2 lines are required.")
        return

    print("\nEnter the angle made by the transversal with the first line.")
    base_angle = float(input("Enter angle: "))

    if not (0 < base_angle < 180):
        print("Angle must be between 0 and 180 degrees.")
        return

    print("\nMultiple Parallel Line Analysis :")

    for i in range(1, n + 1):
        print(f"\nLine {i}:")
        print("Acute/Equal Angle:", base_angle, "degrees")
        print("Supplementary Angle:", 180 - base_angle, "degrees")

    print("\nConclusion:")
    print("For parallel lines cut by the same transversal,")
    print("corresponding and alternate angles are equal,")
    print("while co-interior angles are supplementary.")

multipleparallelline()