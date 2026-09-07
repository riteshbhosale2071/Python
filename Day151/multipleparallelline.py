def multipleparallelline():
    print("Multiple Parallel Line Analyzer :")

    n = int(input("Enter number of parallel lines: "))

    if n < 2:
        print("Enter at least 2 parallel lines.")
        return

    print("\nEnter the angle made by the transversal with the first line:")
    base_angle = float(input("Enter angle: "))

    if not (0 < base_angle < 180):
        print("Angle must be between 0 and 180 degrees.")
        return

    supplementary = 180 - base_angle

    print("\nParallel Line Analysis :")
    print("Number of Parallel Lines:", n)
    print("Base Angle:", base_angle, "degrees")
    print("Supplementary Angle:", supplementary, "degrees")

    print("\nAngle Pattern:")
    for i in range(1, n + 1):
        print(
            f"Line {i}: Equal angles = {base_angle}°, "
            f"Supplementary angles = {supplementary}°"
        )

    print("\nConclusion:")
    print("All corresponding and alternate angles have the same measure.")
    print("Co-interior angles are supplementary.")
    print("The angle relationships remain consistent across all parallel lines.")

multipleparallelline()